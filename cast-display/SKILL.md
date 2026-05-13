---
name: cast-display
description: >
  Start a lightweight HTTP server that renders agent-generated content on
  smart TVs and large displays over the local network.  The agent pushes
  HTML/CSS updates via a REST API and the TV auto-refreshes in real time.
metadata:
  openclaw:
    emoji: "\U0001F4FA"
    os: [darwin, linux]
    requires:
      bins: [python3]
    tags: [display, cast, tv, dashboard, kiosk]
---

# Cast Display

A zero-dependency Python HTTP server that turns any smart TV or browser
into a live display for agent-rendered content.  All web assets are
bundled inside the single `server.py` file — no `npm install`, no static
folder, no build step.

## Quick start

```bash
python3 server.py --port 9876
```

Then open `http://<your-ip>:9876` on the target display (smart TV
browser, Chromecast with browser, tablet, etc.).

## Updating content

Push new HTML to the display from the agent or any HTTP client:

```bash
curl -X POST http://localhost:9876/api/content \
  -H "Content-Type: application/json" \
  -d '{"html": "<h1>Hello from the agent</h1><p>Updated at $(date)</p>"}'
```

The display page long-polls the server and applies updates within one
second — no manual refresh needed.

### Pushing styled content

Include a `css` field to override the display stylesheet:

```bash
curl -X POST http://localhost:9876/api/content \
  -H "Content-Type: application/json" \
  -d '{
    "html": "<h1 class=\"big\">Score: 42</h1>",
    "css": ".big { font-size: 8rem; color: #58a6ff; }"
  }'
```

### Resetting the display

```bash
curl -X POST http://localhost:9876/api/clear
```

## API reference

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

## Notes

- The server binds to `0.0.0.0` by default so any device on the same
  network can reach it.  Use `--bind 127.0.0.1` to restrict to localhost.
- Content is stored in memory only — restarting the server resets the
  display.
- The bundled page uses a dark theme optimised for TV viewing at
  distance.  Override with the `css` field if you prefer a light theme.
