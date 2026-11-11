#!/usr/bin/env python3
"""Generate tokens/tokens.css from tokens/tokens.json.

Every token becomes a CSS custom property named after its path, e.g.
color.green.base -> --enigma-color-green-base. Typography tokens also get a
`font` shorthand, so `font: var(--enigma-typography-display);` works.

Usage: python3 scripts/build_tokens.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tokens" / "tokens.json"
OUT = ROOT / "tokens" / "tokens.css"
PREFIX = "--enigma"
FONT_VAR = f"var({PREFIX}-font-family-sans)"


def kebab(name):
    return re.sub(r"(?<!^)(?=[A-Z])", "-", name).lower()


def shadow(v):
    inset = "inset " if v.get("inset") else ""
    return f"{inset}{v['offsetX']} {v['offsetY']} {v['blur']} {v['spread']} {v['color']}"


def font_family(names):
    generic = {"serif", "sans-serif", "monospace", "system-ui", "cursive", "fantasy"}
    return ", ".join(n if n in generic or " " not in n else f'"{n}"' for n in names)


def declarations(name, token):
    t, v = token.get("$type"), token["$value"]
    if t == "gradient":
        stops = ", ".join(f"{s['color']} {round(s['position'] * 100)}%" for s in v)
        return [(name, f"linear-gradient(180deg, {stops})")]
    if t == "shadow":
        return [(name, shadow(v))]
    if t == "fontFamily":
        return [(name, font_family(v))]
    if t == "typography":
        out = [(name, f"{v['fontWeight']} {v['fontSize']}/{v['lineHeight']} {FONT_VAR}")]
        for key, val in v.items():
            out.append((f"{name}-{kebab(key)}", str(val)))
        return out
    return [(name, str(v))]


def walk(node, path):
    for key, child in node.items():
        if key.startswith("$") or not isinstance(child, dict):
            continue
        child_path = path + [kebab(key)]
        if "$value" in child:
            yield child, f"{PREFIX}-" + "-".join(child_path)
        else:
            yield from walk(child, child_path)


def main():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    lines = [
        "/* GENERATED from tokens.json by scripts/build_tokens.py. Do not edit by hand. */",
        f"/* {data.get('$description', '')} */",
        ":root {",
    ]
    for token, name in walk(data, []):
        if token.get("$description"):
            lines.append(f"  /* {token['$description']} */")
        for prop, value in declarations(name, token):
            lines.append(f"  {prop}: {value};")
    lines.append("}")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
