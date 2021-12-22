<div align="center"><h1>HCIA Cheatsheet<h1></div>

Take me to [pookie](#pookie)



# OTHER

MTU - Maximal transit unit (for interface)

Control plane: provides functions such as protocol processing, service processing, route calculation, forwarding control, service scheduling, traffic statistics collection, and system security. The control plane of a switch is used to control and manage the running of all network protocols. The control plane provides various network information and forwarding query entries required for data processing and forwarding on the data plane

forwarding equivalence class (FEC) is a term used in Multiprotocol Label Switching (MPLS) to describe a set of packets with similar or identical characteristics which may be forwarded the same way

In asynchronous transmission, data is transmitted byte by byte. Therefore, it is less efficient than synchronous transmission.

> IPv6 - OSPFv3
>
> IPv4 - OSPFv2

VRP - console, telnet, USB router conf (no FTP)

> simple switches doNOT isolate broadcast domains, but vlan or layer 3 can (usually routers do)

AAA - Authentication, Authorization, Accounting (Auth modes: hwtacacs | local (default) | radius)

FTP kinds: active, passive

Blackhole route / null route - key from routing loops

traceroute - ICMP 

> Routes: direct (link layer protos), static (handmade), dynamic (ospf, is-is, etc.)

**TYPE CODES**: TCP-6, UDP-17, ICMP-1

**Ports:**

> SNMP uses UDP/161, UDP/162
>
> TFTP uses UDP/69
>
> FTP uses TCP/21 (commands), TCP/20 (data)
>
> SFTP uses SSH+TCP/22

Message Age of STP root conf msg = 0

RSTP = STP after conf BDPU

> TODO: 4096 step where?,CAPWAP TOPOS + DHCP, ip classes, hybrid port, STP ports and ID, eth2+1q frames, wifi standarts and default channels, ospf cost formulas, ospf statuses
>
> 
>
> blackhole null route, SDN, OpenFlow

<a name="pookie">gg</a>

# OSI

![osi](./media/osi.PNG)

![osi_proto](./media/osi_proto.jpg)

# MAC 

IEEE - MAC 01-80-C2-xx-xx-xx (STP MULTICAST 8bit = 1, 7 - Local administrated addr)

? Terminal host - not multicast ?

# IPv4

32 bits (24 mask as default)

OSPFv2

![ipv4 multi](./media/ipv4_multicast.PNG)

# IPv6

Multicast addresses: https://support.huawei.com/enterprise/en/doc/EDOC1000177796/16e69f9c/multicast-addresses

128 bits

ospf v3

MULTICAST starts with FF

> ?Stages?
>
> - address configuration 
> - duplicate address detection (DAD)
> - address resolution

An IPv6 packet has three parts: an IPv6 basic header, one or more IPv6 extension headers, and an upper-layer protocol data unit (PDU). An upper-layer PDU is composed of the upper-layer protocol header and its payload, which maybe an ICMPv6 packet, a TCP packet, or a UDP packet.

> Parts:
>
> - IPv6 basic header
> - one or more IPv6 extension headers
> - upper-layer protocol data unit (PDU)

![ipv4 vs ipv6](./media/ipv4_ipv6.PNG)

![ipv6 multi](./media/ipv6_multicast.PNG)

# OSPF 

fields: priority, router ID[no 0?] (**HIGHER** is best)

> Netowrk types
>
> - Point-to-point
> - Point-to-multipoint
> - Broadcast Multiaccess (BMA)
> - Virtual links
> - Nonbroadcast Multiaccess (NBMA)

**LSDB is same on DR and BDR (not DRO)**

> display ospf lsdb 

**IPv6** - OSPFv3

**IPv4** - OSPFv2

>ospf 1
>
>area 0 | 0.0.0.0
>
>// ? no enable ?

Area 0 - backbone

> DR is elected by all routers in segment

adjaency(full) DR/BDR + all > neighbour (2way) DRO+DRO

> Statuses: 

types: broadcast, nbma, p2mp, p2p

packets: Hello, DD, LSR, LSU, LSAack (LSA - not packet - link state advertise)

![packets types ](./media/ospf_packets.PNG)

# DHCP

> addresses can be reused

> DHCPv6 devices are identified by DUIDs, and each DHCPv6 server or client can have only one DUID.

Packets (in time order): Discover-broadcast, offer-unicast, request-broadcast, ack-unicast 

![ ](./media/dhcp_phases.PNG)

# VLAN (802.q1)

**TPID** tag 0x8100 in TAG-ID .1q-frame (not Eth)

> PVID - port vlan id, Vlan_ID - frame vlan id

Kinds:

- Interface-based
- Mac-based

> // enable command?

canNOT contain STP, RSTP (stp dont understand virtual networks, so works badly)

can - OSPF, ARP

by default all ports in default VLAN (can be manually deleted)

> ACCESS:
>
> Eth2 (no Vlan_ID) -> Vlan_ID := PVID
>
> Vlan_ID == PVID -> Eth2 (no Vlan_ID)
>
> Vlan_id != PVID -> X_discard_X
>
> 
>
> TRUNK (inherits access):
>
> Eth2 -> Vlan_id -> check allow pass
>
> Vlan_id != PVID -> check allow pass
>
> Vlan_id == PVID -> Eth2

# STP + RSTP

doNOT work with vlan

Only 1 root port on non-root device

**LOWER** is best

> RSTP = STP after conf BDPU

> In RSTP, a backup port can replace a faulty root port

Default Forward delay = **15 sec**

![stp port states](./media/stp_port_states.PNG)

# WLAN

AP upgrade modes: AC, FTP, SFTP (no tftp)

**Authentication modes**: MAC, SN, no auth

DHCP + **option 43**

packet **Beacon** - AP **proactively** share SSID (**passive** STA scanning)

packet **Probe** - active STA scanning

![ap_requests](./media/wlan_ap_reqs.PNG)

> Config process
>
> 1 - AP obtains AC addr
>
> 2 - Establish CAPWAP
>
> 3 - AP access control

# ACL

Default increment = 5 , CAN be changed

![acl_types](./media/acl_types.jpg)

# Eth-Trunk, iStack+ CSS

Layer 2 and 3 both

> flow-based load balancing

LACP(DU) - link aggregation control protocol

LACP(DU): Device priority (default = **32768**), MAC, interface priority, port number

> LACP flags: synchronizing, collecting, distributing (111 - active, 000 - inactive)

Actor: **LOWER** system (device) priority, ? MAC ?

Interfaces: **LOWER** interfaces priorities of actor, port number

Same params on member interfaces: vlan, speed, duplex mode + load-balancing

___

iStack and CSS provide the same functions, despite their different names and implementation mechanisms.



# SDN

> Characterisitics:
>
> - centralized control
> - forwarding-control separation
> - open programmable interfaces
> - (distributed frowarding)

![sdn arch](./media/sdn_arch.PNG)
___
<div align="center">by t̶̹̊r̵̺̬̐i̶̡̲̋c̶̟̈̐k̷̩̓s̷̯̾t̴̞̏ḙ̷̽̈́ṛ̷̾</div>
<div align="center">all rights reserved (no)</div>