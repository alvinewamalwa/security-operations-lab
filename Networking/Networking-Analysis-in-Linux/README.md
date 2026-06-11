# Networking Analysis in Linux

In this section, I performed network inspection and analysis using Linux commands to understand system connectivity, routing behavior, and DNS resolution in a simulated cybersecurity environment.

---

## I) Interface and IP Analysis

I used Linux commands to inspect active network interfaces and identify assigned IP addresses.

```bash
ip a
ifconfig
```
I observed:

Active network interfaces (e.g. eth0)
Assigned IPv4 addresses
MAC address information

This helped me understand how the system is positioned within the network.

## II) Routing Path Analysis

I examined the routing table to understand how traffic is directed within and outside the network.

ip route

I identified:

Default gateway
Network routes
Traffic flow direction to external networks

This information is useful in mapping network topology during reconnaissance.

## III) DNS Resolution Inspection

I reviewed DNS configuration to understand how domain name resolution is handled.

cat /etc/resolv.conf

I identified:

DNS server IP address
Name resolution settings used by the system

This helps in understanding how external domains are resolved in the network.

## IV) Connectivity and Network Behavior

I tested connectivity and network responsiveness using ICMP requests.

ping google.com

I observed:

Packet transmission and response behavior
Network latency
Stability of the connection

This helps assess whether a host is reachable and responsive.

## V) Security Relevance

Network inspection is critical in cybersecurity because it supports:

Identifying how systems communicate
Understanding routing paths used by traffic
Detecting misconfigurations in DNS or routing
Supporting both passive and active reconnaissance activities
Key Observation

The combination of interface inspection, routing analysis, and DNS resolution provides a clear understanding of how a system interacts within a network environment, which is essential during penetration testing and network analysis.
