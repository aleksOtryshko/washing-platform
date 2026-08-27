#!/usr/bin/env bash

set -e

cd "$HOME/washing-platform"

SRC="$HOME/washing-platform/tmp-washing-images"
DST="$HOME/washing-platform/assets/service"

mkdir -p "$DST"

mapfile -t FILES < <(find "$SRC" -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.webp" \) | sort)

COUNT="${#FILES[@]}"

echo "Найдено изображений: $COUNT"

if [ "$COUNT" -lt 19 ]; then
  echo "ОШИБКА: найдено меньше 19 изображений."
  find "$SRC" -type f | head -n 100
  exit 1
fi

convert_img() {
  local index="$1"
  local target_name="$2"
  local source_file="${FILES[$index]}"

  echo "$((index+1)) -> $target_name"
  echo "   из: $(basename "$source_file")"

  if command -v magick >/dev/null 2>&1; then
    magick "$source_file" -auto-orient -resize 1200x900^ -gravity center -extent 1200x900 -quality 82 "$DST/$target_name"
  else
    convert "$source_file" -auto-orient -resize 1200x900^ -gravity center -extent 1200x900 -quality 82 "$DST/$target_name"
  fi
}

convert_img 0  "hero-master.webp"
convert_img 1  "diagnostic.webp"
convert_img 2  "repair-process.webp"
convert_img 3  "washing-machine-open.webp"

convert_img 4  "problem-drain.webp"
convert_img 5  "problem-heating.webp"
convert_img 6  "problem-spin.webp"
convert_img 7  "problem-leak.webp"
convert_img 8  "problem-door.webp"
convert_img 9  "problem-noise.webp"

convert_img 10 "part-heater.webp"
convert_img 11 "part-pump.webp"
convert_img 12 "part-door-lock.webp"
convert_img 13 "part-rubber-seal.webp"
convert_img 14 "part-belt.webp"
convert_img 15 "part-bearings.webp"

convert_img 16 "brand-bosch.webp"
convert_img 17 "brand-samsung.webp"
convert_img 18 "brand-lg.webp"

if [ "$COUNT" -ge 20 ]; then
  convert_img 19 "brand-indesit.webp"
else
  cp "$DST/brand-lg.webp" "$DST/brand-indesit.webp"
  echo "20-го файла нет: brand-indesit.webp временно создан из brand-lg.webp"
fi

echo
echo "Готово:"
find "$DST" -maxdepth 1 -type f | sort
