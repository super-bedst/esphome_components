# Wavin AHC-9000 v1 (legacy) — ESPHome 2026.5+

The original `wavinAhc9000` component matches your 16-channel YAML layout. It is **deprecated** but updated for ESPHome 2026.5 in this fork. For new installs, consider [wavinahc9000v3](../wavinahc9000v3/README.md).

## Minimal changes to your existing YAML

1. Use modern ESPHome device blocks (no `platform:` under `esphome:`).
2. Point `external_components` at this fork only — **remove** the old `martgras/esphome` modbus fork.
3. Add `min_auth_mode: WPA2` under `wifi:`.
4. Use numeric `temperature_step` without `°C` in `visual:`.

### Header (replace down to `wavinAhc9000:`)

```yaml
substitutions:
  device_name: wavin
  friendly_name: Wavin
  # ... your channel names and pins unchanged ...

esphome:
  name: ${device_name}
  project:
    name: home.wavin_gulvvarme
    version: "1.0.0"

esp8266:
  board: esp01_1m

logger:
  baud_rate: 0
  level: ${log_level}

api:

ota:
  - platform: esphome
    password: !secret ota_pass

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  min_auth_mode: WPA2
  use_address: 192.168.10.8
  domain: .local
  ap:
    ssid: "Wavin Fallback Hotspot"
    password: !secret ap_pass

captive_portal:

uart:
  rx_pin: ${rx_pin}
  tx_pin: ${tx_pin}
  baud_rate: 38400
  id: uart_modbus
  stop_bits: 1

external_components:
  - source:
      type: git
      url: https://github.com/super-bedst/esphome_components
      ref: main
    refresh: 0s
    components: [wavinAhc9000]

modbus:
  uart_id: uart_modbus

wavinAhc9000:
  update_interval: ${update_interval}
  rw_pin: ${tx_enable_pin}
```

### Climate `visual:` (each channel)

```yaml
    visual:
      temperature_step: ${temp_step}
      min_temperature: ${climate_min_temp}
      max_temperature: ${climate_max_temp}
```

Set substitutions without units, e.g. `temp_step: "0.5"`.

## Remove

- `github://heinekmadsen/esphome_components`
- `martgras/esphome` modbus override (built into ESPHome 2026.5)
- Local `/config/esphome/custom_components/` copy if present
