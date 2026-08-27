#!/usr/bin/env bash

set -e

echo "Добавляю изображения во фронт..."

python3 <<'PY'
from pathlib import Path
import re

def read(path):
    return Path(path).read_text(encoding="utf-8")

def write(path, text):
    Path(path).write_text(text, encoding="utf-8")
    print(f"Обновлён: {path}")

def file_exists(path):
    return Path(path).exists()

def add_css():
    path = Path("styles.css")
    css = read(path)

    block = """

/* Service images */
.hero-media {
  display: flex;
  align-items: stretch;
}

.hero-media img {
  width: 100%;
  height: 100%;
  min-height: 360px;
  object-fit: cover;
  border-radius: 28px;
  box-shadow: 0 22px 55px rgba(15, 23, 42, 0.16);
  border: 1px solid rgba(148, 163, 184, 0.22);
  background: #fff;
}

.card-image {
  width: 100%;
  height: 190px;
  object-fit: cover;
  border-radius: 20px;
  margin-bottom: 18px;
  display: block;
  background: #eef2f7;
}

.brand-link .card-image {
  height: 170px;
}

.parts-section {
  background: linear-gradient(180deg, #ffffff 0%, #f6f9fc 100%);
}

.notice-image-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
  margin-top: 24px;
}

.notice-image-row img {
  width: 100%;
  height: 260px;
  object-fit: cover;
  border-radius: 24px;
  box-shadow: 0 14px 35px rgba(15, 23, 42, 0.12);
}

@media (max-width: 900px) {
  .hero-media img {
    min-height: 260px;
    max-height: 360px;
  }

  .notice-image-row {
    grid-template-columns: 1fr;
  }

  .notice-image-row img {
    height: 220px;
  }
}

@media (max-width: 640px) {
  .card-image {
    height: 180px;
  }

  .hero-media img {
    border-radius: 22px;
  }
}
"""
    if "/* Service images */" not in css:
        css += block
        write(path, css)
    else:
        print("styles.css уже содержит Service images")

def insert_hero_image(text, img_src, alt):
    if 'class="hero-media"' in text:
        return text

    marker = '</div>\n\n      <div class="hero-card"'
    if marker in text:
        block = f'''</div>

      <div class="hero-media">
        <img src="{img_src}" alt="{alt}" loading="eager">
      </div>

      <div class="hero-card"'''
        return text.replace(marker, block, 1)

    marker = '</div>\n    </section>'
    if marker in text:
        block = f'''</div>

      <div class="hero-media">
        <img src="{img_src}" alt="{alt}" loading="eager">
      </div>
    </section>'''
        return text.replace(marker, block, 1)

    return text

def add_img_to_card(text, h3, img_src, alt):
    if img_src in text:
        return text

    old = f'<div class="card"><h3>{h3}</h3>'
    new = f'<div class="card"><img class="card-image" src="{img_src}" alt="{alt}" loading="lazy"><h3>{h3}</h3>'
    text = text.replace(old, new)

    old = f'<article class="card"><h3>{h3}</h3>'
    new = f'<article class="card"><img class="card-image" src="{img_src}" alt="{alt}" loading="lazy"><h3>{h3}</h3>'
    text = text.replace(old, new)

    return text

def add_brand_img(text, href_part, img_src, alt):
    if img_src in text:
        return text

    pattern = rf'(<a class="card brand-link" href="[^"]*{re.escape(href_part)}[^"]*">)(<h3>)'
    repl = rf'\1<img class="card-image" src="{img_src}" alt="{alt}" loading="lazy">\2'
    text = re.sub(pattern, repl, text, count=1)

    return text

def insert_parts_ru(text):
    if "Какие детали чаще всего меняем" in text:
        return text

    block = '''
  <section class="section parts-section">
    <h2 class="section-title">Какие детали чаще всего меняем</h2>
    <p class="section-lead">Мастер уточняет модель и симптомы поломки, чтобы взять на выезд инструмент и распространённые запчасти.</p>
    <div class="grid grid-3">
      <div class="card"><img class="card-image" src="assets/service/part-heater.webp" alt="Замена ТЭНа стиральной машины" loading="lazy"><h3>ТЭН</h3><p>Если машинка не греет воду, мастер проверяет нагреватель, датчик температуры и проводку.</p></div>
      <div class="card"><img class="card-image" src="assets/service/part-pump.webp" alt="Замена сливного насоса стиральной машины" loading="lazy"><h3>Сливной насос</h3><p>При проблемах со сливом проверяется фильтр, помпа, патрубки и сливной шланг.</p></div>
      <div class="card"><img class="card-image" src="assets/service/part-door-lock.webp" alt="Замена замка люка стиральной машины" loading="lazy"><h3>Замок люка / УБЛ</h3><p>Если люк не блокируется или не открывается, проверяется замок, ручка и петля люка.</p></div>
      <div class="card"><img class="card-image" src="assets/service/part-rubber-seal.webp" alt="Замена манжеты люка стиральной машины" loading="lazy"><h3>Манжета люка</h3><p>При течи возле дверцы мастер осматривает резиновую манжету и посадочное место.</p></div>
      <div class="card"><img class="card-image" src="assets/service/part-belt.webp" alt="Замена ремня стиральной машины" loading="lazy"><h3>Приводной ремень</h3><p>Если барабан не вращается или машинка не отжимает, проверяется ремень и привод.</p></div>
      <div class="card"><img class="card-image" src="assets/service/part-bearings.webp" alt="Замена подшипников стиральной машины" loading="lazy"><h3>Подшипники</h3><p>При сильном шуме, люфте барабана и вибрации может потребоваться замена подшипников.</p></div>
    </div>
  </section>

'''
    marker = '  <section class="section">\n    <h2 class="section-title">Ремонт стиральных машин за брендами</h2>'
    if marker in text:
        return text.replace(marker, block + marker, 1)

    marker = '  <section class="section">\n    <h2 class="section-title">Ремонт стиральных машин по брендам</h2>'
    if marker in text:
        return text.replace(marker, block + marker, 1)

    marker = '  <section class="section">\n    <h2 class="section-title">Как проходит ремонт</h2>'
    if marker in text:
        return text.replace(marker, block + marker, 1)

    return text

def insert_parts_uk(text):
    if "Які деталі найчастіше міняємо" in text:
        return text

    block = '''
  <section class="section parts-section">
    <h2 class="section-title">Які деталі найчастіше міняємо</h2>
    <p class="section-lead">Майстер уточнює модель і симптоми поломки, щоб взяти на виїзд інструмент і поширені запчастини.</p>
    <div class="grid grid-3">
      <div class="card"><img class="card-image" src="../assets/service/part-heater.webp" alt="Заміна ТЕНа пральної машини" loading="lazy"><h3>ТЕН</h3><p>Якщо машинка не гріє воду, майстер перевіряє нагрівач, датчик температури та проводку.</p></div>
      <div class="card"><img class="card-image" src="../assets/service/part-pump.webp" alt="Заміна зливного насоса пральної машини" loading="lazy"><h3>Зливний насос</h3><p>При проблемах зі зливом перевіряється фільтр, помпа, патрубки та зливний шланг.</p></div>
      <div class="card"><img class="card-image" src="../assets/service/part-door-lock.webp" alt="Заміна замка люка пральної машини" loading="lazy"><h3>Замок люка / УБЛ</h3><p>Якщо люк не блокується або не відкривається, перевіряється замок, ручка та петля люка.</p></div>
      <div class="card"><img class="card-image" src="../assets/service/part-rubber-seal.webp" alt="Заміна манжети люка пральної машини" loading="lazy"><h3>Манжета люка</h3><p>При протіканні біля дверцят майстер оглядає гумову манжету і місце посадки.</p></div>
      <div class="card"><img class="card-image" src="../assets/service/part-belt.webp" alt="Заміна ременя пральної машини" loading="lazy"><h3>Приводний ремінь</h3><p>Якщо барабан не обертається або машинка не віджимає, перевіряється ремінь і привід.</p></div>
      <div class="card"><img class="card-image" src="../assets/service/part-bearings.webp" alt="Заміна підшипників пральної машини" loading="lazy"><h3>Підшипники</h3><p>При сильному шумі, люфті барабана та вібрації може знадобитися заміна підшипників.</p></div>
    </div>
  </section>

'''
    marker = '  <section class="section">\n    <h2 class="section-title">Ремонт пральних машин за брендами</h2>'
    if marker in text:
        return text.replace(marker, block + marker, 1)

    marker = '  <section class="section">\n    <h2 class="section-title">Як проходить ремонт</h2>'
    if marker in text:
        return text.replace(marker, block + marker, 1)

    return text

add_css()

# Русская главная
if file_exists("index.html"):
    text = read("index.html")
    text = insert_hero_image(text, "assets/service/hero-master.webp", "Мастер по ремонту стиральных машин в Харькове и области")

    ru_cards = {
        "Не сливает воду": ("assets/service/problem-drain.webp", "Ремонт стиральной машины, которая не сливает воду"),
        "Не греет воду": ("assets/service/problem-heating.webp", "Проверка ТЭНа и нагрева стиральной машины"),
        "Не отжимает": ("assets/service/problem-spin.webp", "Ремонт стиральной машины, которая не отжимает"),
        "Течёт": ("assets/service/problem-leak.webp", "Устранение течи стиральной машины"),
        "Не открывается люк": ("assets/service/problem-door.webp", "Ремонт люка и замка стиральной машины"),
        "Шумит и прыгает": ("assets/service/problem-noise.webp", "Диагностика шума и вибрации стиральной машины"),
        "Шумит барабан": ("assets/service/problem-noise.webp", "Диагностика шума барабана стиральной машины"),
    }

    for h3, data in ru_cards.items():
        text = add_img_to_card(text, h3, data[0], data[1])

    text = add_brand_img(text, "remont-bosch/", "assets/service/brand-bosch.webp", "Ремонт стиральной машины Bosch")
    text = add_brand_img(text, "remont-samsung/", "assets/service/brand-samsung.webp", "Ремонт стиральной машины Samsung")
    text = add_brand_img(text, "remont-lg/", "assets/service/brand-lg.webp", "Ремонт стиральной машины LG")
    text = add_brand_img(text, "remont-indesit/", "assets/service/brand-indesit.webp", "Ремонт стиральной машины Indesit")

    text = insert_parts_ru(text)
    write("index.html", text)

# Украинская главная
if file_exists("uk/index.html"):
    text = read("uk/index.html")
    text = insert_hero_image(text, "../assets/service/hero-master.webp", "Майстер з ремонту пральних машин у Харкові та області")

    uk_cards = {
        "Не зливає воду": ("../assets/service/problem-drain.webp", "Ремонт пральної машини, яка не зливає воду"),
        "Не гріє воду": ("../assets/service/problem-heating.webp", "Перевірка ТЕНа і нагріву пральної машини"),
        "Не віджимає": ("../assets/service/problem-spin.webp", "Ремонт пральної машини, яка не віджимає"),
        "Тече": ("../assets/service/problem-leak.webp", "Усунення протікання пральної машини"),
        "Не відкривається люк": ("../assets/service/problem-door.webp", "Ремонт люка і замка пральної машини"),
        "Шумить і стрибає": ("../assets/service/problem-noise.webp", "Діагностика шуму і вібрації пральної машини"),
        "Шумить барабан": ("../assets/service/problem-noise.webp", "Діагностика шуму барабана пральної машини"),
    }

    for h3, data in uk_cards.items():
        text = add_img_to_card(text, h3, data[0], data[1])

    text = add_brand_img(text, "remont-bosch/", "../assets/service/brand-bosch.webp", "Ремонт пральної машини Bosch")
    text = add_brand_img(text, "remont-samsung/", "../assets/service/brand-samsung.webp", "Ремонт пральної машини Samsung")
    text = add_brand_img(text, "remont-lg/", "../assets/service/brand-lg.webp", "Ремонт пральної машини LG")
    text = add_brand_img(text, "remont-indesit/", "../assets/service/brand-indesit.webp", "Ремонт пральної машини Indesit")

    text = insert_parts_uk(text)
    write("uk/index.html", text)

# Русские брендовые страницы
brand_ru = {
    "remont-bosch/index.html": ("../assets/service/brand-bosch.webp", "Мастер ремонтирует стиральную машину Bosch"),
    "remont-samsung/index.html": ("../assets/service/brand-samsung.webp", "Мастер ремонтирует стиральную машину Samsung"),
    "remont-lg/index.html": ("../assets/service/brand-lg.webp", "Мастер ремонтирует стиральную машину LG"),
    "remont-indesit/index.html": ("../assets/service/brand-indesit.webp", "Мастер ремонтирует стиральную машину Indesit"),
}

for file, data in brand_ru.items():
    if not file_exists(file):
        continue

    text = read(file)
    text = insert_hero_image(text, data[0], data[1])

    ru_problem_cards = {
        "Не сливает воду": "../assets/service/problem-drain.webp",
        "Не греет воду": "../assets/service/problem-heating.webp",
        "Не отжимает": "../assets/service/problem-spin.webp",
        "Течёт": "../assets/service/problem-leak.webp",
        "Не открывается люк": "../assets/service/problem-door.webp",
        "Шумит при отжиме": "../assets/service/problem-noise.webp",
        "Шумит барабан": "../assets/service/problem-noise.webp",
        "Ошибка 5E / SE": "../assets/service/problem-drain.webp",
        "Ошибка OE": "../assets/service/problem-drain.webp",
        "Ошибка F05": "../assets/service/problem-drain.webp",
    }

    for h3, img in ru_problem_cards.items():
        text = add_img_to_card(text, h3, img, h3)

    write(file, text)

# Украинские брендовые страницы
brand_uk = {
    "uk/remont-bosch/index.html": ("../../assets/service/brand-bosch.webp", "Майстер ремонтує пральну машину Bosch"),
    "uk/remont-samsung/index.html": ("../../assets/service/brand-samsung.webp", "Майстер ремонтує пральну машину Samsung"),
    "uk/remont-lg/index.html": ("../../assets/service/brand-lg.webp", "Майстер ремонтує пральну машину LG"),
    "uk/remont-indesit/index.html": ("../../assets/service/brand-indesit.webp", "Майстер ремонтує пральну машину Indesit"),
}

for file, data in brand_uk.items():
    if not file_exists(file):
        continue

    text = read(file)
    text = insert_hero_image(text, data[0], data[1])

    uk_problem_cards = {
        "Не зливає воду": "../../assets/service/problem-drain.webp",
        "Не гріє воду": "../../assets/service/problem-heating.webp",
        "Не віджимає": "../../assets/service/problem-spin.webp",
        "Тече": "../../assets/service/problem-leak.webp",
        "Не відкривається люк": "../../assets/service/problem-door.webp",
        "Шумить при віджимі": "../../assets/service/problem-noise.webp",
        "Шумить барабан": "../../assets/service/problem-noise.webp",
        "Помилка 5E / SE": "../../assets/service/problem-drain.webp",
        "Помилка OE": "../../assets/service/problem-drain.webp",
        "Помилка F05": "../../assets/service/problem-drain.webp",
    }

    for h3, img in uk_problem_cards.items():
        text = add_img_to_card(text, h3, img, h3)

    write(file, text)

# Русский прайс
if file_exists("price/index.html"):
    text = read("price/index.html")
    if "Как выглядит диагностика и ремонт" not in text:
        block = '''
  <section class="section">
    <h2 class="section-title">Как выглядит диагностика и ремонт</h2>
    <p class="section-lead">Мастер проверяет узлы стиральной машины, объясняет причину поломки и согласует стоимость до начала ремонта.</p>
    <div class="notice-image-row">
      <img src="../assets/service/diagnostic.webp" alt="Диагностика стиральной машины на дому" loading="lazy">
      <img src="../assets/service/repair-process.webp" alt="Ремонт стиральной машины на дому" loading="lazy">
    </div>
  </section>

'''
        marker = '  <section class="section" id="order">'
        if marker in text:
            text = text.replace(marker, block + marker, 1)
        else:
            text = text.replace('</main>', block + '</main>', 1)
    write("price/index.html", text)

# Украинский прайс
if file_exists("uk/price/index.html"):
    text = read("uk/price/index.html")
    if "Як виглядає діагностика і ремонт" not in text:
        block = '''
  <section class="section">
    <h2 class="section-title">Як виглядає діагностика і ремонт</h2>
    <p class="section-lead">Майстер перевіряє вузли пральної машини, пояснює причину поломки та погоджує вартість до початку ремонту.</p>
    <div class="notice-image-row">
      <img src="../../assets/service/diagnostic.webp" alt="Діагностика пральної машини вдома" loading="lazy">
      <img src="../../assets/service/repair-process.webp" alt="Ремонт пральної машини вдома" loading="lazy">
    </div>
  </section>

'''
        marker = '  <section class="section" id="order">'
        if marker in text:
            text = text.replace(marker, block + marker, 1)
        else:
            text = text.replace('</main>', block + '</main>', 1)
    write("uk/price/index.html", text)

print("Готово: изображения добавлены во фронт.")
PY

echo "Готово."
