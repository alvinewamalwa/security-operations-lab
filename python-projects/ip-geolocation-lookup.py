# IP Geolocation Lookup Tool (Cybersecurity Recon Script)

import requests

def get_ip_info(ip):
    try:
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url)
        data = response.json()

        print("\n--- IP Geolocation Information ---")
        print("IP Address:", data.get("ip"))
        print("City:", data.get("city"))
        print("Region:", data.get("region"))
        print("Country:", data.get("country"))
        print("Location (Lat/Long):", data.get("loc"))
        print("Organization:", data.get("org"))
        print("----------------------------------\n")

    except Exception as e:
        print("Error retrieving IP information:", e)


ip = input("Enter IP address: ")
get_ip_info(ip)
