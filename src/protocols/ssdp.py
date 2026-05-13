"""SSDP M-SEARCH discovery for DIAL-capable devices."""

import socket

SSDP_ADDR = "239.255.255.250"
SSDP_PORT = 1900

SSDP_SEARCH = (
    "M-SEARCH * HTTP/1.1\r\n"
    "HOST: 239.255.255.250:1900\r\n"
    'MAN: "ssdp:discover"\r\n'
    "MX: 3\r\n"
    "ST: urn:dial-multiscreen-org:service:dial:1\r\n"
    "\r\n"
)


def ssdp_discover(timeout=4):
    """Send SSDP M-SEARCH and collect DIAL-capable device responses."""
    devices = []
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.settimeout(timeout)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        sock.sendto(SSDP_SEARCH.encode(), (SSDP_ADDR, SSDP_PORT))
        while True:
            try:
                data, addr = sock.recvfrom(4096)
                text = data.decode("utf-8", errors="ignore")
                location = None
                friendly = None
                for line in text.splitlines():
                    low = line.lower()
                    if low.startswith("location:"):
                        location = line.split(":", 1)[1].strip()
                    if low.startswith("server:"):
                        friendly = line.split(":", 1)[1].strip()
                devices.append({
                    "ip": addr[0],
                    "port": addr[1],
                    "location": location,
                    "server": friendly,
                    "protocol": "DIAL/SSDP",
                })
            except socket.timeout:
                break
    finally:
        sock.close()
    return devices


def main():
    print("Scanning for DIAL devices...")
    devs = ssdp_discover()
    if not devs:
        print("  No devices found.")
    for d in devs:
        print(f"  {d['ip']}:{d['port']}  {d.get('server', '?')}")


if __name__ == "__main__":
    main()
