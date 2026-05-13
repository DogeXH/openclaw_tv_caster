# openclaw_tv_caster

SmartTV casting toolkit with DIAL/SSDP/mDNS discovery, protocol negotiation
drivers, and a built-in display server for pushing agent-rendered content to
smart TVs and large screens.

## Features

- **SSDP discovery** — find DIAL-capable devices on the local network
- **mDNS/Bonjour** — discover Chromecast and AirPlay devices
- **DIAL v3 driver** — capability negotiation for legacy Samsung/LG firmware
- **Cast Display server** — zero-dependency HTTP server that turns any smart
  TV or browser into a live agent-controlled display

## Quick start

### Install the library

```bash
pip install -e .
```

### Discover devices

```python
from src.protocols.ssdp import ssdp_discover
from src.protocols.mdns import mdns_discover

devices = ssdp_discover(timeout=4) + mdns_discover(timeout=4)
for d in devices:
    print(d)
```

### Start the display server

```bash
python3 cast-display/server.py --port 9876
```

Open `http://<your-ip>:9876` on the target display (smart TV browser,
Chromecast with browser, tablet, etc.).

### Push content to the display

```bash
curl -X POST http://localhost:9876/api/content \
  -H "Content-Type: application/json" \
  -d '{"html": "<h1>Hello from the agent</h1>"}'
```

The display page long-polls and auto-refreshes within one second.

## Project layout

```
src/
  protocols/
    ssdp.py           SSDP M-SEARCH discovery
    mdns.py           mDNS/Bonjour service browser
  drivers/
    dial_v3.py        DIAL v3 protocol negotiation driver
cast-display/
    server.py         Zero-dependency HTTP display server
    SKILL.md          OpenClaw skill definition
tests/
  test_discovery.py   Unit tests for discovery modules
```

## Cast Display API

| Method | Path             | Description                       |
|--------|------------------|-----------------------------------|
| GET    | `/`              | Main display page                 |
| POST   | `/api/content`   | Update HTML and optional CSS      |
| POST   | `/api/clear`     | Reset to default waiting screen   |
| GET    | `/api/status`    | Current state JSON                |
| GET    | `/api/poll?v=N`  | Long-poll — blocks until v > N    |

## Use cases

- **Dashboard kiosk** — push live metrics, charts, or status boards
- **Presentation remote** — advance slides from the agent
- **Notification display** — show alerts on a wall-mounted screen
- **Game scoreboard** — real-time score updates during events
- **Device discovery** — enumerate smart TVs and cast targets on the LAN

## License

MIT
