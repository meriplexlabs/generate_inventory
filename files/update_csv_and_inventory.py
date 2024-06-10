import pandas as pd
import re
import yaml

def normalize_mac(mac):
    """Normalize MAC address to the format xx:xx:xx:xx:xx:xx and convert to lowercase."""
    mac = mac.lower()
    if '.' in mac:
        mac = mac.replace('.', '')
    if '-' in mac:
        mac = mac.replace('-', '')
    if ':' not in mac:
        mac = ':'.join(mac[i:i+2] for i in range(0, len(mac), 2))
    return mac

def increment_mac(mac):
    """Increment the MAC address by 1."""
    mac_int = int(mac.replace(':', ''), 16)
    mac_int += 1
    incremented_mac = '{:012x}'.format(mac_int)
    return ':'.join(incremented_mac[i:i+2] for i in range(0, 12, 2))

def parse_dhcp_data(dhcp_data):
    """Parse the DHCP lease list data into a dictionary with MAC as key and IP as value."""
    dhcp_entries = {}
    for line in dhcp_data.strip().split('\n'):
        match = re.search(r'(?P<ip>\d+\.\d+\.\d+\.\d+)\s+(?P<mac>[0-9a-fA-F:\-\.]+)', line)
        if match:
            ip = match.group('ip')
            mac = normalize_mac(match.group('mac'))
            dhcp_entries[mac] = ip
    return dhcp_entries

# Paths to the temporary files
dhcp_data_path = "/tmp/dhcp_data.txt"
csv_path = "/tmp/image.csv"
inventory_path = "/tmp/pre-inventory.yml"

# Read DHCP data
with open(dhcp_data_path, "r") as file:
    dhcp_data = file.read()

# Parse DHCP data
dhcp_entries = parse_dhcp_data(dhcp_data)

# Load the CSV file
df = pd.read_csv(csv_path)

# Normalize MAC addresses in the CSV
df['mac'] = df['mac'].apply(normalize_mac)

# Update the IP column based on normalized MAC addresses or their incremented versions
ips = []
for mac in df['mac']:
    incremented_mac = increment_mac(mac)
    ips.append(dhcp_entries.get(incremented_mac, ''))

df['ip'] = ips

# Save the updated CSV
df.to_csv(csv_path, index=False)

# Create inventory dictionary
inventory = {"pre_config": {"hosts": {}}}

for index, row in df.iterrows():
    if row['ip']:
        inventory["pre_config"]["hosts"][row['hostname']] = {"ansible_host": row['ip']}

# Save inventory to YAML file
with open(inventory_path, 'w') as file:
    yaml.dump(inventory, file, default_flow_style=False)

print("CSV and inventory YAML updated successfully")
