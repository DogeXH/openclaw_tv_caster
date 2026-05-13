"""mDNS/Bonjour service discovery for Chromecast and AirPlay devices."""

import subprocess


def mdns_discover(timeout=4):
    """Discover Chromecast and AirPlay devices via dns-sd (macOS)."""
    devices = []
    for svc in ("_googlecast._tcp", "_airplay._tcp", "_raop._tcp"):
        try:
            proc = subprocess.run(
                ["dns-sd", "-B", svc, "local."],
                capture_output=True, timeout=timeout, text=True,
            )
            for line in proc.stdout.splitlines():
                parts = line.split()
                if len(parts) >= 7 and parts[1] != "Timestamp":
                    devices.append({
                        "name": " ".join(parts[6:]),
                        "service": svc,
                        "protocol": "mDNS/Bonjour",
                    })
        except (subprocess.TimeoutExpired, FileNotFoundError):
            continue
    return devices


def main():
    print("Scanning for mDNS services...")
    devs = mdns_discover()
    if not devs:
        print("  No devices found.")
    for d in devs:
        print(f"  {d['name']}  ({d['service']})")


if __name__ == "__main__":
    main()
