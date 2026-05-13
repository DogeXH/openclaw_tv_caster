# openclaw_tv_caster

SmartTV casting toolkit with DIAL/SSDP/mDNS discovery, protocol negotiation
drivers, and cast session management.

## Features

- **SSDP discovery** — find DIAL-capable devices on the local network
- **mDNS/Bonjour** — discover Chromecast and AirPlay devices
- **DIAL v3 driver** — capability negotiation for legacy Samsung/LG firmware
- **Cast sessions** — push HTML/image content to discovered devices

## Quick start

```bash
pip install -e .
```

```python
from src.protocols.ssdp import ssdp_discover
from src.protocols.mdns import mdns_discover

devices = ssdp_discover(timeout=4) + mdns_discover(timeout=4)
for d in devices:
    print(d)
```

## Project layout

```
src/
  protocols/
    ssdp.py       SSDP M-SEARCH discovery
    mdns.py       mDNS/Bonjour service browser
  drivers/
    dial_v3.py    DIAL v3 protocol negotiation driver
tests/
  test_discovery.py
```

## License

MIT
