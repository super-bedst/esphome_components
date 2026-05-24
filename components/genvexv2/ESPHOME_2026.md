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

Then include the device package as usual, e.g. `components/genvexv2/optima250.yaml` via `packages:` or copy its contents.

## Changes (genvexv2)

- `set_supported_custom_fan_modes()` moved from `ClimateTraits` to `Climate::setup()` (ESPHome 2026.11 deprecation).
- Genvex select write uses direct `uint16_t` register write (removed deprecated `modbus_controller::float_to_payload`).
- Fan speed callback uses `float` (matches number component).
- Removed duplicate `CONF_FORCE_NEW_RANGE` in select schema.

Upstream base: [heinekmadsen/esphome_components](https://github.com/heinekmadsen/esphome_components) (branch `fix/genvexv2-compile-warnings` merged).
