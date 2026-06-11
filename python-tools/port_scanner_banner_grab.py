In this project I accomplished the following objectives:
- Port scanning of common services
- Detection of open ports
- Banner grabbing for service identification
- Error handling for stable scanning



import socket

target = input("Enter target IP: ")

ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3389]

print("\nScanning target:", target)
print("-" * 50)

def grab_banner(sock):
    try:
        return sock.recv(1024).decode().strip()
    except:
        return "No banner available"

for port in ports:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")

            # Try banner grabbing
            try:
                s.send(b"Hello\r\n")
                banner = grab_banner(s)
                print(f"   Banner: {banner}")
            except:
                print("   Banner: Not available")

        s.close()

    except KeyboardInterrupt:
        print("\nScan stopped by user")
        break

    except socket.gaierror:
        print("Hostname could not be resolved")
        break

    except socket.error:
        print("Could not connect to server")
        break
