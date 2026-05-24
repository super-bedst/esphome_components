# Genvex v2 — ESPHome 2026.5+

This fork fixes compile warnings/errors with **ESPHome 2026.5.0** (climate custom fan modes API, modbus select writes).

## Use in your YAML

Replace `custom_components` / old git refs with:

```yaml
external_components:
  - source:
      type: git
      url: https://github.com/super-bedst/esphome_components
      ref: main
    refresh: 0s
    components: [genvexv2]
```

Load the device config from the **same fork** (do not use `heinekmadsen/esphome_components`):

```yaml
packages:
  remote_package:
    url: https://github.com/super-bedst/esphome_components
    ref: main
    files:
      - components/genvexv2/optima250.yaml
    refresh: 0s
```

Put `external_components` **only** in your main `genvex.yaml` (not in the package file), so ESPHome fetches the git repo once.

### Silence other ESPHome 2026.5 warnings

**`custom_components` folder deprecated** — Remove or empty the old local folder if you migrated to git `external_components`, for example:

- Home Assistant: `/config/esphome/custom_components/` (delete `genvexv2` or the whole folder if unused)
- ESPHome Dashboard: check the device config directory for a `custom_components` subfolder

**WiFi `min_auth_mode`** — Add under `wifi:` in `genvex.yaml` (use `WPA2` if your router supports it):

```yaml
wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  min_auth_mode: WPA2
```

## Changes (genvexv2)

- `set_supported_custom_fan_modes()` moved from `ClimateTraits` to `Climate::setup()` (ESPHome 2026.11 deprecation).
- Genvex select write uses direct `uint16_t` register write (removed deprecated `modbus_controller::float_to_payload`).
- Fan speed callback uses `float` (matches number component).
- Removed duplicate `CONF_FORCE_NEW_RANGE` in select schema.

Upstream base: [heinekmadsen/esphome_components](https://github.com/heinekmadsen/esphome_components) (branch `fix/genvexv2-compile-warnings` merged).
