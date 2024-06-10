# generate_inventory
Pulls DHCP leases from Fortigate and matches them with MAC addresses in a CSV to generate an inventory.  Only confirmed to work on AOS-CX switches (due to the MAC address on the MGMT interface vs the barcode on the box)

#### Example playbook:

```yaml
---
- name: Update IP addresses in CSV based on Fortigate ARP table
  hosts: fortigates
  gather_facts: false
  roles:
    - generate_inventory
```

#### Example CSV
```csv 
location,hostname,model,mac,serial,ip
MDF,AOS-MDF-STK,r8q69a,ec:67:94:c4:ff:80,vn38lb91bw,10.144.10.21
MDF,,r8q70a,9c:37:08:98:7a:80,vn42lbb10h,
MDF,,r8q70a,9c:37:08:98:9b:00,vn42lbb10w,
MDF,,r8q70a,9c:37:08:98:73:40,vn42lbb0y7,
MDF,,r8q70a,9c:37:08:98:7b:40,vn42lbb12l,
GYM,AOS-GYM-STK,r8q68a,9c:37:08:9a:be:c0,vn43lb81mk,10.144.10.30
GYM,,r8q69a,ec:67:94:c4:db:40,vn38lb911v,
IDF3,AOS-IDF3-STK,r8q69a,ec:67:94:c4:ff:40,vn38lb91bt,10.144.10.25
IDF3,,r8q68a,9c:37:08:9a:1d:40,vn43lb81ms,
MS-IT,AOS-MS-IT,r8q68a,9c:37:08:9a:5f:00,vn43lb81lb,10.144.10.31
MS-FL1,AOS-MS-FL1-STK,r8q70a,9c:37:08:98:fb:00,vn42lbb11l,10.144.10.29
MS-FL1,,r8q70a,9c:37:08:98:7c:80,vn42lbb13d,
MS-FL2,AOS-MS-FL2-STK,r8q70a,9c:37:08:98:9a:80,vn42lbb107,10.144.10.28
MS-FL2,,r8q69a,ec:67:94:c4:cf:40,vn38lb91b1,10.144.10.22
MS-FL3,AOS-MS-FL3-STK,r8q70a,9c:37:08:98:4c:40,vn42lbb12z,10.144.10.27
MS-FL3,,r8q69a,ec:67:94:c4:db:c0,vn38lb911s,
DAYCARE,AOS-DAYCARE,r8q70a,9c:37:08:98:8b:80,vn42lbb10s,10.144.10.23
BASEMENT,AOS-BASEMENT-STK,r8q69a,ec:67:94:c4:df:c0,vn38lb91b6,10.144.10.32
BASEMENT,,r8q68a,9c:37:08:9a:3b:c0,vn43lb81br,
```