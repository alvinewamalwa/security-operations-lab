# Active Reconnaissance

In this lab, I performed active reconnaissance on a DMZ network (10.6.6.0/24) as part of a controlled environment provided for security analysis (Cisco/SMN lab setup). The objective was to identify active hosts, enumerate services, analyze network traffic, and detect potential security weaknesses on a suspicious machine (10.6.6.23).

---

## I) Nmap

I used Nmap to perform network discovery and detailed scanning of the DMZ network.

- I executed a discovery scan to identify active hosts on the 10.6.6.0/24 network.
- - I discovered multiple live hosts and isolated the suspicious host (10.6.6.23).
- I performed a default scan on the target and identified open ports and running services.
  ![Network Discovery](screenshots/nmap_I_network-discovery-and-default-scan.png)

- I used OS detection (`-O`) to determine the operating system of the target machine.
  ![OS Detection](screenshots/nmap_II_os-detection-scan.png)
  
- I performed service version detection to identify applications running on specific ports.
  ![Service Version Detection](screenshots/nmap_III_service-version-detection-port21.png)
  I discovered that the version of FTP running on the computer is vsftpd 3.0.3
  
- I ran an aggressive scan (`-A`) and discovered accessible resources on the FTP service.
  ![Aggressive Scan](screenshots/nmap_IV_aggressive-scan-ftp-enumeration.png)
  I found 4 files on the FTP server are accessible through this connection

**What I discovered:**
- Active hosts: 7
- Open ports: 21, 22, 53, 80, 139, 445
- Notable finding: I found that the FTP server is configured to permit anonymous logins, this weakness allowed me to log into the FTP server.

---

## II) Packet Inspection and Crafting (Scapy)

I used Scapy to analyze, capture, and manipulate network packets.

- I obtained root privileges and launched Scapy to begin packet-level analysis.
  ![Scapy Initialization and Root Access](screenshots/scapy_I_initialization-root-access.png)

- I verified connectivity by sending ICMP packets (ping) to external hosts.
  ![ICMP Connectivity Test](screenshots/scapy_II_icmp-connectivity-test.png)
  
- I sniffed network traffic and observed different protocols such as TCP, UDP, and ICMP.
- I filtered captured traffic to focus specifically on ICMP packets.
- I exported captured traffic into a `.pcap` file for further analysis.

I also performed packet crafting:

- I created and sent custom ICMP packets to the target host (10.6.6.23).
- I analyzed packet summaries and detailed packet structures.
- I compared multiple packets to observe differences in responses.

**What I discovered:**
- Types of packets observed: [your result]
- Packet counts: [your result]
- Notable behavior: [your result]

---

## III) Network Sniffing (Wireshark & Tcpdump)

I used tcpdump and Wireshark to capture and analyze live network traffic.

- I used `ifconfig` to identify the active network interface.
- I used `ip route` to determine the default gateway.
- I checked DNS configuration using `/etc/resolv.conf`.
- I captured network traffic using `tcpdump` on the `eth0` interface.
- I saved the captured traffic into a `.pcap` file.

I then analyzed the traffic using Wireshark:

- I opened the `.pcap` file and inspected packet-level details.
- I identified source and destination IP addresses.
- I observed DNS queries and browsing activity.
- I analyzed communication patterns between systems.

**What I discovered:**
- Interface used: [your result]
- Type of traffic captured: [your result]
- DNS / browsing insights: [your result]

---

## IV) Analysis of Network Behavior

During packet crafting and analysis:

- I observed that custom ICMP packets sent to the target did not return any response flags.
- I inferred that the target system or firewall is likely configured to silently drop packets rather than respond.

**Conclusion:**
This behavior suggests the presence of a firewall or filtering mechanism designed to reduce detectability and enhance security.

---

## Evidence

I have included screenshots of all commands, outputs, and analysis in the `screenshots/` directory.

---

## Disclaimer

This activity was conducted in a controlled lab environment for educational purposes only, with proper authorization.
