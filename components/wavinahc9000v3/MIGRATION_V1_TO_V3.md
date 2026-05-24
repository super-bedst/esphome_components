# Migrate Wavin v1 (`wavinAhc9000`) → v3 (`wavinahc9000v3`)

## What changes

| v1 (old) | v3 (new) |
|----------|----------|
| `modbus:` + custom function codes via modbus component | Direct UART protocol (no `modbus:` block) |
| `wavinAhc9000:` hub | `wavinahc9000v3:` hub |
| `platform: wavinAhc9000` climate | `platform: wavinahc9000v3` climate |
| Battery/temp under each climate | Optional `sensor` platform (`type: battery` / `temperature`) |
| `heinekmadsen` + martgras modbus fork | `super-bedst/esphome_components` only |

## Recommended path (ESP-01 / 16 zones)

### Option A — Full file (fastest)

Copy the complete config to Home Assistant:

**[configs/wavin.yaml](configs/wavin.yaml)** → `/config/esphome/wavin.yaml`

One file, ESPHome 2026.5 syntax (`esp8266:` block, no `platform:` under `esphome:`), single `external_components` entry.

Adjust secrets, `use_address`, and GPIO pins if your wiring differs.

### Option B — Discovery first (safest)

1. Flash a **minimal** config: `example.yaml` structure + your WiFi/UART/`tx_enable_pin`.
2. Wait 30–60 s, call service **`dump_wavin_yaml`** (or button).
3. Copy logged `climate:` / `sensor:` blocks into your YAML.
4. Remove the dump service if you no longer need it.

## Hardware notes (your ESP-01)

- **UART:** `GPIO3` (RX), `GPIO1` (TX) — same as `RX`/`TX` aliases on ESP-01.
- **RS-485 enable:** `tx_enable_pin: GPIO2` (your existing `tx_enable_pin`).
- v3 talks **directly on UART** — remove the entire `modbus:` section from v1.
- ESP8266 works; upstream docs prefer ESP32 for margin. If you see bus errors, try `module: ustepper` or lower `poll_channels_per_cycle`.

## Home Assistant entity names

Entity IDs will change (new platform). Update dashboards/automations after first successful flash.

## Standby drift

If zones turn back to heat after a few minutes in OFF/standby, enable:

```yaml
wavinahc9000v3:
  keep_standby_alive: true
  standby_keepalive_interval: 180s
```

## Grouped rooms (optional)

Replace two single climates with one group:

```yaml
  - platform: wavinahc9000v3
    wavinahc9000v3_id: wavin
    name: "Stue & Gang"
    members: [8, 10]
```

Remove or comment the individual channel climates for members in that group.
