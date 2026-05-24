#!/usr/bin/env python3
import pathlib

lines = ["climate:"]
for i in range(1, 17):
    lines += [
        "  - platform: wavinahc9000v3",
        "    wavinahc9000v3_id: wavin",
        f'    name: "${{friendly_name}} Climate ${{channel_{i}}}"',
        f"    channel: {i}",
    ]
lines.append("sensor:")
for i in range(1, 17):
    lines += [
        "  - platform: wavinahc9000v3",
        "    wavinahc9000v3_id: wavin",
        f'    name: "${{friendly_name}} Battery ${{channel_{i}}}"',
        f"    channel: {i}",
        "    type: battery",
        "  - platform: wavinahc9000v3",
        "    wavinahc9000v3_id: wavin",
        f'    name: "${{friendly_name}} Temp ${{channel_{i}}}"',
        f"    channel: {i}",
        "    type: temperature",
    ]

root = pathlib.Path(__file__).parent
entities = "\n".join(lines) + "\n"
header = (root / "wavin_header.yaml").read_text(encoding="utf-8")
(root / "wavin.yaml").write_text(header + "\n" + entities, encoding="utf-8")
(root / "entities_substitutions.yaml").write_text(entities, encoding="utf-8")
print("wrote", root / "wavin.yaml")
