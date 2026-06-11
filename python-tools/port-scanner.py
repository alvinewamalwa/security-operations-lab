# Basic Port Scanner (For Educational / Lab Use Only)

import socket

target = "127.0.0.1"  # localhost ONLY

print(f"Scanning target: {target}")

open_ports = []

for port in range(20, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")
        open_ports.append(port)

    s.close()

print("\nScan complete.")
print("Open ports found:", open_ports)
