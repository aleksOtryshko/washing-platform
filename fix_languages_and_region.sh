#!/usr/bin/env bash

set -e

python3 <<'PY'
from pathlib import Path
import re

html_files = [
    Path("index.html"),
    Path("price/index.html"),
    Path("remont-bosch/index.html"),
    Path("remont-samsung/index.html"),
    Path("remont-lg/index.html"),
    Path("remont-indesit/index.html"),
    Path("uk/index.html"),
    Path("uk/price/index.html"),
    Path("uk/remont-bosch/index.html"),
    Path("uk/remont-samsung/index.html"),
    Path("uk/remont-lg/index.html"),
    Path("uk/remont-indesit/index.html"),
]

for path in html_files:
    if not path.exists():
        print(f"Нет файла: {path}")
        continue

    text = path.read_text(encoding="utf-8")

    # Удаляем видимые переключатели RU / UA из меню.
    # Украинские страницы раньше могли содержать ссылки вида <a href="../">RU</a>, <a href="../../price/">RU</a> и т.д.
    text = re.sub(r'\s*<a\s+href="[^"]*">RU</a>', '', text)
    text = re.sub(r'\s*<a\s+href="[^"]*">UA</a>', '', text)
    text = re.sub(r'\s*<a\s+href="[^"]*">UK</a>', '', text)

    # Русская география.
    text = text.replace("в Харькове и пригороде", "в Харькове и области")
    text = text.replace("по Харькову и пригороду", "по Харькову и области")
    text = text.replace("по Харькову", "по Харькову и области")
    text = text.replace("район Харькова", "район Харькова или область")
    text = text.replace("Харьков ·", "Харьков и область ·")
    text = text.replace("Харьков</title>", "Харьков и область</title>")
    text = text.replace("Харькове</title>", "Харькове и области</title>")
    text = text.replace("Харькове —", "Харькове и области —")
    text = text.replace("Харькове на дому", "Харькове и области на дому")
    text = text.replace("Харькове вдома", "Харькове и области на дому")
    text = text.replace("Харькове.", "Харькове и области.")
    text = text.replace("Харькове:", "Харькове и области:")
    text = text.replace("Харькове,", "Харькове и области,")
    text = text.replace("Харькове ", "Харькове и области ")
    text = text.replace("Харькова.", "Харькова и области.")
    text = text.replace("Харькова", "Харькова и области")

    # Чистим возможные повторы после замен.
    text = text.replace("Харькове и области и области", "Харькове и области")
    text = text.replace("Харькова и области и области", "Харькова и области")
    text = text.replace("Харькову и области и области", "Харькову и области")
    text = text.replace("Харьков и область и область", "Харьков и область")

    # Украинская география.
    text = text.replace("у Харкові та передмісті", "у Харкові та області")
    text = text.replace("по Харкову та передмістю", "по Харкову та області")
    text = text.replace("по Харкову", "по Харкову та області")
    text = text.replace("район Харкова", "район Харкова або область")
    text = text.replace("Харків ·", "Харків і область ·")
    text = text.replace("Харкові</title>", "Харкові та області</title>")
    text = text.replace("Харкові —", "Харкові та області —")
    text = text.replace("Харкові вдома", "Харкові та області вдома")
    text = text.replace("Харкові на дому", "Харкові та області вдома")
    text = text.replace("Харкові.", "Харкові та області.")
    text = text.replace("Харкові:", "Харкові та області:")
    text = text.replace("Харкові,", "Харкові та області,")
    text = text.replace("Харкові ", "Харкові та області ")
    text = text.replace("Харкова.", "Харкова та області.")
    text = text.replace("Харкова", "Харкова та області")

    # Чистим возможные повторы после замен.
    text = text.replace("Харкові та області та області", "Харкові та області")
    text = text.replace("Харкова та області та області", "Харкова та області")
    text = text.replace("Харкову та області та області", "Харкову та області")
    text = text.replace("Харків і область і область", "Харків і область")

    path.write_text(text, encoding="utf-8")
    print(f"Обновлено: {path}")

print("Готово: переключатели удалены, регион обновлён.")
PY

# Обновляем sitemap.xml без визуального переключения языков.
cat > sitemap.xml <<'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

  <url>
    <loc>https://aleksotryshko.github.io/washing-platform/</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>

  <url>
    <loc>https://aleksotryshko.github.io/washing-platform/price/</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>

  <url>
    <loc>https://aleksotryshko.github.io/washing-platform/remont-bosch/</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>

  <url>
    <loc>https://aleksotryshko.github.io/washing-platform/remont-samsung/</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>

  <url>
    <loc>https://aleksotryshko.github.io/washing-platform/remont-lg/</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>

  <url>
    <loc>https://aleksotryshko.github.io/washing-platform/remont-indesit/</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>

  <url>
    <loc>https://aleksotryshko.github.io/washing-platform/uk/</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>

  <url>
    <loc>https://aleksotryshko.github.io/washing-platform/uk/price/</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>

  <url>
    <loc>https://aleksotryshko.github.io/washing-platform/uk/remont-bosch/</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>

  <url>
    <loc>https://aleksotryshko.github.io/washing-platform/uk/remont-samsung/</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>

  <url>
    <loc>https://aleksotryshko.github.io/washing-platform/uk/remont-lg/</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>

  <url>
    <loc>https://aleksotryshko.github.io/washing-platform/uk/remont-indesit/</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>

</urlset>
EOF

echo "Исправления применены."
