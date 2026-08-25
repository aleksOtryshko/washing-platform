#!/usr/bin/env bash

set -e

mkdir -p uk/price uk/remont-bosch uk/remont-samsung uk/remont-lg uk/remont-indesit

cat > uk/index.html <<'EOF'
<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>Ремонт пральних машин у Харкові вдома — викликати майстра</title>
  <meta name="description" content="Ремонт пральних машин у Харкові вдома. Терміновий виїзд майстра, діагностика, ремонт Bosch, Samsung, LG, Indesit. Залиште заявку — майстер зв’яжеться з вами.">
  <link rel="canonical" href="https://aleksotryshko.github.io/washing-platform/uk/">
  <link rel="stylesheet" href="../styles.css">
  <script>
    window.pageLang = 'uk';
  </script>
</head>
<body>
<header class="site-header">
  <div class="header-inner">
    <a class="logo" href="./">Stiralka<span>.site</span></a>
    <nav class="main-nav" aria-label="Головна навігація">
      <a href="./">Головна</a>
      <a href="price/">Ціни</a>
      <a href="remont-bosch/">Bosch</a>
      <a href="remont-samsung/">Samsung</a>
      <a href="remont-lg/">LG</a>
      <a href="remont-indesit/">Indesit</a>
      <a href="#faq">FAQ</a>
      <a href="#order">Викликати майстра</a>
      <a href="../">RU</a>
    </nav>
    <a class="header-phone" href="#order">Залишити заявку</a>
  </div>
</header>

<main>
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-text">
        <div class="badge">Харків · ремонт вдома</div>
        <h1>Ремонт пральних машин у Харкові вдома</h1>
        <p>Викликайте майстра з ремонту пральних машин у Харкові. Діагностика, терміновий ремонт, заміна ТЕНа, насоса, замка люка, манжети, ременя, підшипників і модуля керування.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="#order">Викликати майстра</a>
          <a class="btn btn-secondary" href="price/">Переглянути ціни</a>
        </div>
        <ul class="trust-list">
          <li>✓ Ремонт пральних машин вдома</li>
          <li>✓ Терміновий виїзд по Харкову</li>
          <li>✓ Ціна погоджується до ремонту</li>
          <li>✓ Bosch, Samsung, LG, Indesit та інші</li>
        </ul>
      </div>

      <div class="hero-card" id="order">
        <h2>Залишити заявку</h2>
        <p>Введіть телефон — майстер зв’яжеться з вами та уточнить проблему.</p>
        <form class="form orderForm">
          <label>Ваше ім’я
            <input type="text" name="name" placeholder="Наприклад, Олександр" maxlength="50">
          </label>
          <div class="error nameError"></div>

          <label>Телефон</label>
          <div class="phone-row">
            <span>+38</span>
            <input type="tel" name="phone_number" placeholder="0501234567" inputmode="numeric" maxlength="10" required>
          </div>
          <div class="error phoneError"></div>

          <label>Що сталося з пральною машиною?
            <textarea name="problem_description" placeholder="Наприклад: не зливає воду, не віджимає, тече, шумить, не вмикається"></textarea>
          </label>

          <button class="btn btn-primary" type="submit">Викликати майстра</button>
          <div class="form-note">Натискаючи кнопку, ви надсилаєте заявку для зв’язку з майстром.</div>
        </form>
      </div>
    </div>
  </section>

  <section class="section">
    <h2 class="section-title">Які несправності усуваємо</h2>
    <p class="section-lead">Майстер може виконати діагностику пральної машини вдома та назвати вартість ремонту до початку робіт.</p>
    <div class="grid grid-3">
      <div class="card"><h3>Не зливає воду</h3><p>Перевірка фільтра, зливного насоса, шланга, засмічення та системи зливу.</p></div>
      <div class="card"><h3>Не гріє воду</h3><p>Діагностика ТЕНа, датчика температури, проводки та плати керування.</p></div>
      <div class="card"><h3>Не віджимає</h3><p>Перевірка ременя, двигуна, щіток, амортизаторів, датчиків і завантаження.</p></div>
      <div class="card"><h3>Тече</h3><p>Усунення протікання з люка, манжети, патрубків, бака, фільтра або шлангів.</p></div>
      <div class="card"><h3>Не відкривається люк</h3><p>Заміна ручки, петлі, замка люка або пристрою блокування люка.</p></div>
      <div class="card"><h3>Шумить і стрибає</h3><p>Перевірка підшипників, амортизаторів, барабана та противаг.</p></div>
    </div>
  </section>

  <section class="section">
    <h2 class="section-title">Популярні ціни на ремонт</h2>
    <p class="section-lead">Точна вартість залежить від моделі, доступу до деталі та стану пральної машини.</p>
    <div class="grid grid-4">
      <div class="card"><h3>Виклик майстра</h3><p><strong>700 грн</strong></p></div>
      <div class="card"><h3>Заміна ТЕНа</h3><p><strong>1400–1900 грн</strong></p></div>
      <div class="card"><h3>Заміна насоса</h3><p><strong>1500 грн</strong></p></div>
      <div class="card"><h3>Заміна УБЛ</h3><p><strong>1700 грн</strong></p></div>
    </div>
    <p style="margin-top:20px;">
      <a class="btn btn-blue" href="price/">Відкрити повний прайс-лист</a>
    </p>
  </section>

  <section class="section">
    <h2 class="section-title">Ремонт пральних машин за брендами</h2>
    <p class="section-lead">Окремі сторінки під популярні бренди допомагають швидше знайти потрібну послугу.</p>
    <div class="grid grid-4">
      <a class="card brand-link" href="remont-bosch/"><h3>Bosch / Бош</h3><p>Ремонт замка, ТЕНа, насоса, модуля, підшипників.</p></a>
      <a class="card brand-link" href="remont-samsung/"><h3>Samsung / Самсунг</h3><p>Помилки 5E, 4E, UE, LE, злив, віджим, люк, модуль.</p></a>
      <a class="card brand-link" href="remont-lg/"><h3>LG</h3><p>Ремонт зливу, двигуна, віджиму, нагріву та електроніки.</p></a>
      <a class="card brand-link" href="remont-indesit/"><h3>Indesit / Індезіт</h3><p>F05, F08, люк, насос, ТЕН, підшипники та модуль.</p></a>
    </div>
  </section>

  <section class="section">
    <h2 class="section-title">Як проходить ремонт</h2>
    <div class="grid grid-3 steps">
      <div class="card step"><h3>Залишаєте заявку</h3><p>Вказуєте телефон і коротко описуєте проблему.</p></div>
      <div class="card step"><h3>Майстер зв’язується</h3><p>Уточнює модель, симптоми поломки та район Харкова.</p></div>
      <div class="card step"><h3>Діагностика вдома</h3><p>Майстер перевіряє техніку та погоджує вартість ремонту.</p></div>
      <div class="card step"><h3>Ремонт</h3><p>Після погодження виконується ремонт або заміна деталі.</p></div>
      <div class="card step"><h3>Перевірка</h3><p>Пральна машина запускається та перевіряється після ремонту.</p></div>
      <div class="card step"><h3>Рекомендації</h3><p>Майстер пояснює, як уникнути повторної поломки.</p></div>
    </div>
  </section>

  <section class="section">
    <div class="cta-section">
      <div>
        <h2>Потрібно терміново викликати майстра?</h2>
        <p>Залиште заявку — майстер зв’яжеться з вами та підкаже можливу причину поломки.</p>
      </div>
      <div class="form-card">
        <h2>Швидка заявка</h2>
        <form class="form orderForm">
          <label>Ваше ім’я
            <input type="text" name="name" placeholder="Ваше ім’я" maxlength="50">
          </label>
          <div class="error nameError"></div>
          <label>Телефон</label>
          <div class="phone-row">
            <span>+38</span>
            <input type="tel" name="phone_number" placeholder="0501234567" inputmode="numeric" maxlength="10" required>
          </div>
          <div class="error phoneError"></div>
          <label>Опис проблеми
            <textarea name="problem_description" placeholder="Наприклад: пральна машина не зливає воду"></textarea>
          </label>
          <button class="btn btn-primary" type="submit">Надіслати заявку</button>
        </form>
      </div>
    </div>
  </section>

  <section class="section faq section-narrow" id="faq">
    <h2 class="section-title">Часті питання</h2>
    <details>
      <summary>Скільки коштує ремонт пральної машини у Харкові?</summary>
      <p>Ціна залежить від несправності. Наприклад, заміна ТЕНа коштує 1400–1900 грн, заміна зливного насоса — 1500 грн, заміна УБЛ — 1700 грн.</p>
    </details>
    <details>
      <summary>Чи можна відремонтувати пральну машину вдома?</summary>
      <p>Так, більшість несправностей усувається вдома без вивезення техніки в майстерню.</p>
    </details>
    <details>
      <summary>Які бренди ремонтуєте?</summary>
      <p>Bosch, Samsung, LG, Indesit, Electrolux, Zanussi, Whirlpool, Ariston та інші популярні бренди.</p>
    </details>
    <details>
      <summary>Що робити, якщо машина не зливає воду?</summary>
      <p>Не запускайте віджим багато разів поспіль. Залиште заявку, майстер перевірить фільтр, насос, шланг і систему зливу.</p>
    </details>
  </section>
</main>

<footer class="footer">
  <div class="footer-inner">
    <strong>Stiralka.site</strong>
    <span>Ремонт пральних машин у Харкові вдома.</span>
    <span>© 2026 Stiralka.site</span>
  </div>
</footer>

<div class="mobile-sticky">
  <a class="btn btn-primary" href="#order">Викликати майстра</a>
  <a class="btn btn-secondary" href="price/">Ціни</a>
</div>

<script src="../scripts.js"></script>
</body>
</html>
EOF

cat > uk/price/index.html <<'EOF'
<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>Ціни на ремонт пральних машин у Харкові — прайс-лист</title>
  <meta name="description" content="Прайс-лист на ремонт пральних машин у Харкові: виклик майстра, діагностика, заміна ТЕНа, насоса, УБЛ, манжети, підшипників та інших деталей.">
  <link rel="canonical" href="https://aleksotryshko.github.io/washing-platform/uk/price/">
  <link rel="stylesheet" href="../../styles.css">
  <script>window.pageLang = 'uk';</script>
</head>
<body>
<header class="site-header">
  <div class="header-inner">
    <a class="logo" href="../">Stiralka<span>.site</span></a>
    <nav class="main-nav">
      <a href="../">Головна</a>
      <a href="../price/">Ціни</a>
      <a href="../remont-bosch/">Bosch</a>
      <a href="../remont-samsung/">Samsung</a>
      <a href="../remont-lg/">LG</a>
      <a href="../remont-indesit/">Indesit</a>
      <a href="#order">Викликати майстра</a>
      <a href="../../price/">RU</a>
    </nav>
    <a class="header-phone" href="#order">Залишити заявку</a>
  </div>
</header>

<main>
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-text">
        <div class="breadcrumbs"><a href="../">Головна</a> / Прайс-лист</div>
        <div class="badge">Ціни · Харків</div>
        <h1>Прайс-лист на ремонт пральних машин у Харкові</h1>
        <p>Вартість ремонту залежить від моделі пральної машини, складності доступу до деталі та характеру несправності. Перед початком робіт майстер проводить діагностику та погоджує ціну.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="#order">Викликати майстра</a>
          <a class="btn btn-secondary" href="#prices">Дивитися таблицю</a>
        </div>
      </div>

      <div class="hero-card">
        <h2>Популярні роботи</h2>
        <ul>
          <li>Виклик майстра — 700 грн</li>
          <li>Заміна ТЕНа — 1400–1900 грн</li>
          <li>Заміна зливного насоса — 1500 грн</li>
          <li>Заміна УБЛ — 1700 грн</li>
          <li>Заміна підшипників — від 4000 грн</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section" id="prices">
    <h2 class="section-title">Повна таблиця цін</h2>
    <p class="section-lead">Ціни вказані за роботу. Вартість запчастин залежить від бренду та моделі пральної машини.</p>

    <div class="price-table-wrap">
      <table class="price-table">
        <thead>
          <tr>
            <th>Назва операції</th>
            <th>Ціна</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>Виклик майстра додому</td><td>700 грн</td></tr>
          <tr><td>Діагностика пральної машини</td><td>уточнюється</td></tr>
          <tr><td>Підключення пральної машини</td><td>1200 грн</td></tr>
          <tr><td>Чистка фільтра пральної машини</td><td>1000 грн</td></tr>
          <tr><td>Усунення засмічення в пральній машині</td><td>900–1400 грн</td></tr>
          <tr><td>Витяг стороннього предмета без розбору</td><td>900 грн</td></tr>
          <tr><td>Витяг стороннього предмета з розбором</td><td>1400 грн</td></tr>
          <tr><td>Заміна зливного шланга</td><td>900 грн</td></tr>
          <tr><td>Заміна заливного шланга</td><td>800 грн</td></tr>
          <tr><td>Заміна мережевого шнура</td><td>1000 грн</td></tr>
          <tr><td>Заміна кнопки увімкнення</td><td>1400 грн</td></tr>
          <tr><td>Заміна ручки люка</td><td>1300 грн</td></tr>
          <tr><td>Заміна петлі люка</td><td>1200 грн</td></tr>
          <tr><td>Заміна скла люка</td><td>ціна договірна</td></tr>
          <tr><td>Заміна замка люка / УБЛ</td><td>1700 грн</td></tr>
          <tr><td>Заміна манжети люка</td><td>1300–2300 грн</td></tr>
          <tr><td>Усунення протікання</td><td>1000–1600 грн</td></tr>
          <tr><td>Заміна ТЕНа</td><td>1400–1900 грн</td></tr>
          <tr><td>Заміна датчика температури</td><td>1000 грн</td></tr>
          <tr><td>Заміна зливного насоса / помпи</td><td>1500 грн</td></tr>
          <tr><td>Заміна заливного клапана</td><td>1400 грн</td></tr>
          <tr><td>Заміна пресостата / датчика рівня води</td><td>1200 грн</td></tr>
          <tr><td>Заміна приводного ременя</td><td>1200 грн</td></tr>
          <tr><td>Заміна щіток двигуна</td><td>1500 грн</td></tr>
          <tr><td>Ремонт двигуна</td><td>уточнюється</td></tr>
          <tr><td>Заміна амортизаторів</td><td>1600 грн</td></tr>
          <tr><td>Заміна пружин бака</td><td>1600 грн</td></tr>
          <tr><td>Ремонт плати керування</td><td>ціна договірна</td></tr>
          <tr><td>Заміна плати керування</td><td>1800 грн</td></tr>
          <tr><td>Ремонт модуля керування</td><td>ціна договірна</td></tr>
          <tr><td>Заміна селектора програм</td><td>1400 грн</td></tr>
          <tr><td>Заміна підшипників у розбірному баку</td><td>4000 грн</td></tr>
          <tr><td>Заміна підшипників у нерозбірному баку</td><td>4500 грн</td></tr>
          <tr><td>Заміна хрестовини барабана при знятому барабані</td><td>800 грн</td></tr>
          <tr><td>Заміна шківа барабана</td><td>1200 грн</td></tr>
          <tr><td>Заміна бака</td><td>3000 грн</td></tr>
          <tr><td>Заміна барабана</td><td>4000 грн</td></tr>
        </tbody>
      </table>
    </div>

    <p class="notice" style="margin-top:20px;">Остаточна ціна погоджується після діагностики. Якщо ремонт складний або потрібна рідкісна запчастина, вартість може відрізнятися.</p>
  </section>

  <section class="section" id="order">
    <div class="cta-section">
      <div>
        <h2>Хочете уточнити вартість?</h2>
        <p>Залиште заявку та опишіть проблему. Майстер підкаже можливу причину і приблизну ціну.</p>
      </div>
      <div class="form-card">
        <h2>Заявка на ремонт</h2>
        <form class="form orderForm">
          <label>Ваше ім’я
            <input type="text" name="name" placeholder="Ваше ім’я" maxlength="50">
          </label>
          <div class="error nameError"></div>
          <label>Телефон</label>
          <div class="phone-row">
            <span>+38</span>
            <input type="tel" name="phone_number" placeholder="0501234567" inputmode="numeric" maxlength="10" required>
          </div>
          <div class="error phoneError"></div>
          <label>Опис проблеми
            <textarea name="problem_description" placeholder="Наприклад: потрібна заміна ТЕНа або машина не зливає воду"></textarea>
          </label>
          <button class="btn btn-primary" type="submit">Надіслати заявку</button>
        </form>
      </div>
    </div>
  </section>
</main>

<footer class="footer">
  <div class="footer-inner">
    <strong>Stiralka.site</strong>
    <span>Прайс-лист на ремонт пральних машин у Харкові.</span>
    <span>© 2026 Stiralka.site</span>
  </div>
</footer>

<div class="mobile-sticky">
  <a class="btn btn-primary" href="#order">Викликати майстра</a>
  <a class="btn btn-secondary" href="../">Головна</a>
</div>

<script src="../../scripts.js"></script>
</body>
</html>
EOF

create_brand_page() {
  local file="$1"
  local canonical="$2"
  local ru_link="$3"
  local title="$4"
  local description="$5"
  local badge="$6"
  local h1="$7"
  local intro="$8"
  local button="$9"
  local problem1="${10}"
  local problem1_text="${11}"
  local problem2="${12}"
  local problem2_text="${13}"
  local problem3="${14}"
  local problem3_text="${15}"
  local problem4="${16}"
  local problem4_text="${17}"
  local problem5="${18}"
  local problem5_text="${19}"
  local problem6="${20}"
  local problem6_text="${21}"

  cat > "$file" <<EOF
<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>$title</title>
  <meta name="description" content="$description">
  <link rel="canonical" href="$canonical">
  <link rel="stylesheet" href="../../styles.css">
  <script>window.pageLang = 'uk';</script>
</head>
<body>
<header class="site-header">
  <div class="header-inner">
    <a class="logo" href="../">Stiralka<span>.site</span></a>
    <nav class="main-nav">
      <a href="../">Головна</a>
      <a href="../price/">Ціни</a>
      <a href="../remont-bosch/">Bosch</a>
      <a href="../remont-samsung/">Samsung</a>
      <a href="../remont-lg/">LG</a>
      <a href="../remont-indesit/">Indesit</a>
      <a href="#order">Викликати майстра</a>
      <a href="$ru_link">RU</a>
    </nav>
    <a class="header-phone" href="#order">Залишити заявку</a>
  </div>
</header>

<main>
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-text">
        <div class="breadcrumbs"><a href="../">Головна</a> / $badge</div>
        <div class="badge">$badge · Харків</div>
        <h1>$h1</h1>
        <p>$intro</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="#order">$button</a>
          <a class="btn btn-secondary" href="../price/">Переглянути ціни</a>
        </div>
        <ul class="trust-list">
          <li>✓ Ремонт вдома</li>
          <li>✓ Діагностика несправності</li>
          <li>✓ Узгодження ціни до ремонту</li>
          <li>✓ Виїзд по Харкову</li>
        </ul>
      </div>

      <div class="hero-card" id="order">
        <h2>Заявка на ремонт</h2>
        <p>Залиште телефон — майстер уточнить модель, симптоми поломки та район Харкова.</p>
        <form class="form orderForm">
          <label>Ваше ім’я
            <input type="text" name="name" placeholder="Ваше ім’я" maxlength="50">
          </label>
          <div class="error nameError"></div>
          <label>Телефон</label>
          <div class="phone-row">
            <span>+38</span>
            <input type="tel" name="phone_number" placeholder="0501234567" inputmode="numeric" maxlength="10" required>
          </div>
          <div class="error phoneError"></div>
          <label>Опис проблеми
            <textarea name="problem_description" placeholder="Наприклад: не зливає воду, не гріє, шумить або показує помилку"></textarea>
          </label>
          <button class="btn btn-primary" type="submit">$button</button>
        </form>
      </div>
    </div>
  </section>

  <section class="section">
    <h2 class="section-title">Часті несправності</h2>
    <div class="grid grid-3">
      <div class="card"><h3>$problem1</h3><p>$problem1_text</p></div>
      <div class="card"><h3>$problem2</h3><p>$problem2_text</p></div>
      <div class="card"><h3>$problem3</h3><p>$problem3_text</p></div>
      <div class="card"><h3>$problem4</h3><p>$problem4_text</p></div>
      <div class="card"><h3>$problem5</h3><p>$problem5_text</p></div>
      <div class="card"><h3>$problem6</h3><p>$problem6_text</p></div>
    </div>
  </section>

  <section class="section">
    <h2 class="section-title">Популярні ціни</h2>
    <div class="grid grid-4">
      <div class="card"><h3>Заміна насоса</h3><p><strong>1500 грн</strong></p></div>
      <div class="card"><h3>Заміна ТЕНа</h3><p><strong>1400–1900 грн</strong></p></div>
      <div class="card"><h3>Заміна УБЛ</h3><p><strong>1700 грн</strong></p></div>
      <div class="card"><h3>Ремонт модуля</h3><p><strong>ціна договірна</strong></p></div>
    </div>
    <p style="margin-top:20px;">
      <a class="btn btn-blue" href="../price/">Відкрити повний прайс-лист</a>
    </p>
  </section>

  <section class="section faq section-narrow">
    <h2 class="section-title">Часті питання</h2>
    <details>
      <summary>Чи можна виконати ремонт вдома?</summary>
      <p>Так, більшість робіт виконується вдома без вивезення пральної машини в майстерню.</p>
    </details>
    <details>
      <summary>Скільки коштує ремонт?</summary>
      <p>Ціна залежить від несправності. Наприклад, заміна насоса — 1500 грн, заміна ТЕНа — 1400–1900 грн, заміна УБЛ — 1700 грн.</p>
    </details>
    <details>
      <summary>Що робити, якщо машина не зливає воду?</summary>
      <p>Не запускайте машинку багато разів поспіль. Залиште заявку, майстер перевірить фільтр, насос, шланг і систему зливу.</p>
    </details>
  </section>
</main>

<footer class="footer">
  <div class="footer-inner">
    <strong>Stiralka.site</strong>
    <span>$h1.</span>
    <span>© 2026 Stiralka.site</span>
  </div>
</footer>

<div class="mobile-sticky">
  <a class="btn btn-primary" href="#order">Викликати майстра</a>
  <a class="btn btn-secondary" href="../price/">Ціни</a>
</div>

<script src="../../scripts.js"></script>
</body>
</html>
EOF
}

create_brand_page \
  "uk/remont-bosch/index.html" \
  "https://aleksotryshko.github.io/washing-platform/uk/remont-bosch/" \
  "../../remont-bosch/" \
  "Ремонт пральних машин Bosch у Харкові вдома — майстер Бош" \
  "Ремонт пральних машин Bosch і Бош у Харкові вдома. Викликати майстра Bosch: заміна ТЕНа, насоса, замка люка, ремонт модуля та усунення помилок." \
  "Bosch / Бош" \
  "Ремонт пральних машин Bosch у Харкові" \
  "Викликайте майстра з ремонту пральних машин Bosch вдома. Ремонтуємо машинки Бош при проблемах зі зливом, нагрівом, люком, барабаном, підшипниками та модулем керування." \
  "Викликати майстра Bosch" \
  "Не зливає воду" "Перевірка зливного насоса, фільтра, патрубків і шлангів." \
  "Не гріє воду" "Діагностика ТЕНа, датчика температури та ланцюга нагріву." \
  "Не блокується люк" "Заміна замка люка, ручки, петлі або УБЛ." \
  "Шумить при віджимі" "Перевірка підшипників, амортизаторів, барабана та бака." \
  "Не вмикається" "Перевірка мережевого шнура, кнопки увімкнення та плати керування." \
  "Помилка на дисплеї" "Діагностика датчиків, модуля керування та виконавчих вузлів."

create_brand_page \
  "uk/remont-samsung/index.html" \
  "https://aleksotryshko.github.io/washing-platform/uk/remont-samsung/" \
  "../../remont-samsung/" \
  "Ремонт пральних машин Samsung у Харкові вдома — майстер Самсунг" \
  "Ремонт пральних машин Samsung і Самсунг у Харкові вдома. Викликати майстра Samsung: злив, віджим, ТЕН, насос, люк, помилки 5E, 4E, UE, LE." \
  "Samsung / Самсунг" \
  "Ремонт пральних машин Samsung у Харкові" \
  "Майстер з ремонту пральних машин Samsung приїде додому, проведе діагностику та погодить ціну. Ремонтуємо злив, нагрів, віджим, люк, двигун і модуль керування." \
  "Викликати майстра Samsung" \
  "Помилка 5E / SE" "Часто пов’язана зі зливом води, фільтром, насосом або засміченням." \
  "Помилка 4E" "Проблема з набором води, заливним клапаном, тиском або шлангом." \
  "Помилка UE" "Дисбаланс, перевантаження, амортизатори або проблеми з віджимом." \
  "Не гріє воду" "Перевірка ТЕНа, датчика температури та плати керування." \
  "Не відкривається люк" "Заміна замка люка, ручки, петлі або УБЛ." \
  "Не крутить барабан" "Перевірка ременя, двигуна, щіток та електроніки керування."

create_brand_page \
  "uk/remont-lg/index.html" \
  "https://aleksotryshko.github.io/washing-platform/uk/remont-lg/" \
  "../../remont-lg/" \
  "Ремонт пральних машин LG у Харкові вдома — викликати майстра" \
  "Ремонт пральних машин LG у Харкові вдома. Викликати майстра LG: не зливає воду, не віджимає, помилка OE, UE, LE, заміна ТЕНа, насоса, модуля." \
  "LG" \
  "Ремонт пральних машин LG у Харкові" \
  "Викликайте майстра з ремонту пральних машин LG вдома. Усуваємо проблеми зі зливом, віджимом, нагрівом, люком, двигуном, барабаном і модулем керування." \
  "Викликати майстра LG" \
  "Помилка OE" "Проблеми зі зливом води, насосом, фільтром або засміченням." \
  "Помилка UE" "Дисбаланс, амортизатори, перевантаження або проблеми з віджимом." \
  "Помилка LE" "Проблеми з двигуном, датчиком, приводом або керуванням." \
  "Не гріє воду" "Заміна ТЕНа, датчика температури або ремонт ланцюга нагріву." \
  "Сильно шумить" "Перевірка підшипників, амортизаторів, барабана та бака." \
  "Тече" "Перевірка манжети, патрубків, шлангів, фільтра та бака."

create_brand_page \
  "uk/remont-indesit/index.html" \
  "https://aleksotryshko.github.io/washing-platform/uk/remont-indesit/" \
  "../../remont-indesit/" \
  "Ремонт пральних машин Indesit у Харкові вдома — майстер Індезіт" \
  "Ремонт пральних машин Indesit і Індезіт у Харкові вдома. Викликати майстра Indesit: злив, нагрів, люк, насос, ТЕН, підшипники, модуль." \
  "Indesit / Індезіт" \
  "Ремонт пральних машин Indesit у Харкові" \
  "Майстер з ремонту пральних машин Indesit приїде додому, проведе діагностику та погодить ціну. Ремонтуємо злив, нагрів, замок люка, насос, барабан, підшипники та модуль." \
  "Викликати майстра Indesit" \
  "Помилка F05" "Часто пов’язана зі зливом води, насосом, фільтром або засміченням." \
  "Помилка F08" "Проблема з нагрівом води, ТЕНом, датчиком або платою." \
  "Не відкривається люк" "Заміна ручки, петлі, замка люка або УБЛ." \
  "Не віджимає" "Перевірка ременя, двигуна, щіток, амортизаторів і датчиків." \
  "Тече" "Усунення протікання з манжети, патрубків, фільтра або шлангів." \
  "Шумить барабан" "Перевірка підшипників, бака, барабана, амортизаторів і пружин."


cat > sitemap.xml <<'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

  <url><loc>https://aleksotryshko.github.io/washing-platform/</loc><lastmod>2026-08-25</lastmod><changefreq>weekly</changefreq><priority>1.0</priority></url>
  <url><loc>https://aleksotryshko.github.io/washing-platform/price/</loc><lastmod>2026-08-25</lastmod><changefreq>weekly</changefreq><priority>0.9</priority></url>
  <url><loc>https://aleksotryshko.github.io/washing-platform/remont-bosch/</loc><lastmod>2026-08-25</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>
  <url><loc>https://aleksotryshko.github.io/washing-platform/remont-samsung/</loc><lastmod>2026-08-25</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>
  <url><loc>https://aleksotryshko.github.io/washing-platform/remont-lg/</loc><lastmod>2026-08-25</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>
  <url><loc>https://aleksotryshko.github.io/washing-platform/remont-indesit/</loc><lastmod>2026-08-25</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>

  <url><loc>https://aleksotryshko.github.io/washing-platform/uk/</loc><lastmod>2026-08-25</lastmod><changefreq>weekly</changefreq><priority>1.0</priority></url>
  <url><loc>https://aleksotryshko.github.io/washing-platform/uk/price/</loc><lastmod>2026-08-25</lastmod><changefreq>weekly</changefreq><priority>0.9</priority></url>
  <url><loc>https://aleksotryshko.github.io/washing-platform/uk/remont-bosch/</loc><lastmod>2026-08-25</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>
  <url><loc>https://aleksotryshko.github.io/washing-platform/uk/remont-samsung/</loc><lastmod>2026-08-25</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>
  <url><loc>https://aleksotryshko.github.io/washing-platform/uk/remont-lg/</loc><lastmod>2026-08-25</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>
  <url><loc>https://aleksotryshko.github.io/washing-platform/uk/remont-indesit/</loc><lastmod>2026-08-25</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>

</urlset>
EOF

echo "Украинская версия фронта создана."
