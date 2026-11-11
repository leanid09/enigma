#!/usr/bin/env bash
# Download the original design assets from upakenigma.com into reference/assets/
# for local study. reference/ is git-ignored: these files belong to ODO «ENIGMA»
# and are not redistributed in this public repository.
#
# Fonts are deliberately not downloaded: Museo Sans Cyrl and Geometria are
# commercial typefaces that need their own licence.
#
# Usage: scripts/fetch-assets.sh [--with-video]   (the hero video is about 3 MB)
set -euo pipefail

BASE="https://upakenigma.com/design/default"
DEST="$(cd "$(dirname "$0")/.." && pwd)/reference/assets"
mkdir -p "$DEST"

FILES=(
  logo.png
  icon-benefit-1.png icon-benefit-2.png icon-benefit-3.png icon-benefit-4.png icon-benefit-5.png
  icons-steps1.png
  viber.svg whatsapp.svg telegram.svg instagram.svg
  icon-loupe.png icon-close.png images/icon_top.png
  bg-certificates.jpg bg-steps.jpg bg-consult.jpg img-banner-charity-bg.jpg
)
[[ "${1:-}" == "--with-video" ]] && FILES+=(vid.mp4)

failed=0
for f in "${FILES[@]}"; do
  if curl -fsSL -o "$DEST/$(basename "$f")" "$BASE/$f"; then
    echo "ok    $f"
  else
    echo "fail  $f" >&2
    failed=1
  fi
done
echo "saved to $DEST"
exit "$failed"
