from pathlib import Path
from textwrap import dedent


ROOT = Path.cwd()

DOMAIN = (
    "https://remontstiralok.kh.ua"
)

PHONE_E164 = (
    "+380671371673"
)

PHONE_DISPLAY = (
    "+38 (067) 137-16-73"
)

ADS_ID = (
    "AW-17465538794"
)


GOOGLE_TAG = f'''
<!-- Google tag (gtag.js) - Google Ads -->
<script async
        src="https://www.googletagmanager.com/gtag/js?id={ADS_ID}">
</script>

<script>
  window.dataLayer =
    window.dataLayer || [];

  function gtag(){{
    dataLayer.push(arguments);
  }}

  gtag(
    'js',
    new Date()
  );

  gtag(
    'config',
    '{ADS_ID}'
  );
</script>
'''


BRANDS = [

    (
        "bosch",
        "Bosch",
        "brand-bosch.webp",
    ),

    (
        "samsung",
        "Samsung",
        "brand-samsung.webp",
    ),

    (
        "lg",
        "LG",
        "brand-lg.webp",
    ),

    (
        "indesit",
        "Indesit",
        "brand-indesit.webp",
    ),

    (
        "electrolux",
        "Electrolux",
        "washing-machine-open.webp",
    ),

    (
        "zanussi",
        "Zanussi",
        "washing-machine-open.webp",
    ),
]


PRICE_ROWS_RU = [

    (
        "Вызов мастера на дом",
        "700 грн",
    ),

    (
        "Диагностика стиральной машины",
        "600 грн",
    ),

    (
        "Подключение стиральной машины",
        "1500 грн",
    ),

    (
        "Чистка фильтра стиральной машины",
        "1000 грн",
    ),

    (
        "Устранение засора в стиральной машине",
        "900–1400 грн",
    ),

    (
        "Извлечение постороннего предмета без разбора",
        "1100 грн",
    ),

    (
        "Извлечение постороннего предмета с разбором",
        "1400 грн",
    ),

    (
        "Замена сливного шланга",
        "1200 грн",
    ),

    (
        "Замена заливного шланга",
        "900 грн",
    ),

    (
        "Замена сетевого шнура",
        "1100 грн",
    ),

    (
        "Замена кнопки включения",
        "1400 грн",
    ),

    (
        "Замена ручки люка",
        "1500 грн",
    ),

    (
        "Замена петли люка",
        "1500 грн",
    ),

    (
        "Замена стекла люка",
        "цена договорная",
    ),

    (
        "Замена замка люка / УБЛ",
        "1900 грн",
    ),

    (
        "Замена манжеты люка",
        "1300–2300 грн",
    ),

    (
        "Устранение течи",
        "1000–1600 грн",
    ),

    (
        "Замена ТЭНа",
        "1900–2200 грн",
    ),

    (
        "Замена датчика температуры",
        "1400 грн",
    ),

    (
        "Замена сливного насоса / помпы",
        "1800–2300 грн",
    ),

    (
        "Замена заливного клапана",
        "1900–2200 грн",
    ),

    (
        "Замена прессостата / датчика уровня воды",
        "1700 грн",
    ),

    (
        "Замена приводного ремня",
        "1700 грн",
    ),

    (
        "Замена щёток двигателя",
        "1800 грн",
    ),

    (
        "Ремонт двигателя",
        "уточняется",
    ),

    (
        "Замена амортизаторов",
        "1800–2200 грн",
    ),

    (
        "Замена пружин бака",
        "1700 грн",
    ),

    (
        "Ремонт платы управления",
        "1900–3000 грн",
    ),

    (
        "Замена платы управления",
        "2000 грн",
    ),

    (
        "Ремонт модуля управления",
        "цена договорная",
    ),

    (
        "Замена селектора программ",
        "1800 грн",
    ),

    (
        "Замена подшипников в разборном баке",
        "4500 грн",
    ),

    (
        "Замена подшипников в неразборном баке",
        "5400 грн",
    ),

    (
        "Замена крестовины барабана при снятом барабане",
        "800 грн",
    ),

    (
        "Замена шкива барабана",
        "1800 грн",
    ),

    (
        "Замена бака",
        "3000 грн",
    ),

    (
        "Замена барабана",
        "3000 грн",
    ),
]


PRICE_ROWS_UK = [

    (
        "Виклик майстра додому",
        "700 грн",
    ),

    (
        "Діагностика пральної машини",
        "600 грн",
    ),

    (
        "Підключення пральної машини",
        "1500 грн",
    ),

    (
        "Чищення фільтра пральної машини",
        "1000 грн",
    ),

    (
        "Усунення засмічення у пральній машині",
        "900–1400 грн",
    ),

    (
        "Вилучення стороннього предмета без розбирання",
        "1100 грн",
    ),

    (
        "Вилучення стороннього предмета з розбиранням",
        "1400 грн",
    ),

    (
        "Заміна зливного шланга",
        "1200 грн",
    ),

    (
        "Заміна заливного шланга",
        "900 грн",
    ),

    (
        "Заміна мережевого шнура",
        "1100 грн",
    ),

    (
        "Заміна кнопки увімкнення",
        "1400 грн",
    ),

    (
        "Заміна ручки люка",
        "1500 грн",
    ),

    (
        "Заміна петлі люка",
        "1500 грн",
    ),

    (
        "Заміна скла люка",
        "ціна договірна",
    ),

    (
        "Заміна замка люка / УБЛ",
        "1900 грн",
    ),

    (
        "Заміна манжети люка",
        "1300–2300 грн",
    ),

    (
        "Усунення протікання",
        "1000–1600 грн",
    ),

    (
        "Заміна ТЕНа",
        "1900–2200 грн",
    ),

    (
        "Заміна датчика температури",
        "1400 грн",
    ),

    (
        "Заміна зливного насоса / помпи",
        "1800–2300 грн",
    ),

    (
        "Заміна заливного клапана",
        "1900–2200 грн",
    ),

    (
        "Заміна пресостату / датчика рівня води",
        "1700 грн",
    ),

    (
        "Заміна приводного ременя",
        "1700 грн",
    ),

    (
        "Заміна щіток двигуна",
        "1800 грн",
    ),

    (
        "Ремонт двигуна",
        "уточнюється",
    ),

    (
        "Заміна амортизаторів",
        "1800–2200 грн",
    ),

    (
        "Заміна пружин бака",
        "1700 грн",
    ),

    (
        "Ремонт плати керування",
        "1900–3000 грн",
    ),

    (
        "Заміна плати керування",
        "2000 грн",
    ),

    (
        "Ремонт модуля керування",
        "ціна договірна",
    ),

    (
        "Заміна селектора програм",
        "1800 грн",
    ),

    (
        "Заміна підшипників у розбірному баку",
        "4500 грн",
    ),

    (
        "Заміна підшипників у нерозбірному баку",
        "5400 грн",
    ),

    (
        "Заміна хрестовини барабана при знятому барабані",
        "800 грн",
    ),

    (
        "Заміна шківа барабана",
        "1800 грн",
    ),

    (
        "Заміна бака",
        "3000 грн",
    ),

    (
        "Заміна барабана",
        "3000 грн",
    ),
]


T = {

    "ru": {

        "home":
            "Главная",

        "prices":
            "Цены",

        "brands":
            "Бренды",

        "how":
            "Как работаем",

        "call":
            "Позвонить мастеру",

        "order":
            "Вызвать мастера",

        "phone_hint":
            "Можно сразу позвонить",

        "area":
            "Харьков и область · ремонт на дому",

        "price_agree":
            "Стоимость согласуем до ремонта",

        "diagnosis":
            "Диагностика на дому",

        "all_brands":
            "Популярные бренды и другие модели",

        "modal_title":
            "Вызвать мастера",

        "modal_text":
            (
                "Оставьте номер. "
                "Имя и описание проблемы — "
                "по желанию."
            ),

        "name":
            "Ваше имя (необязательно)",

        "phone":
            "Телефон",

        "problem":
            "Что случилось? (необязательно)",

        "submit":
            "Отправить заявку",

        "privacy":
            (
                "Нажимая кнопку, "
                "вы отправляете заявку "
                "для связи с мастером."
            ),

        "menu":
            "Меню",

        "close":
            "Закрыть",

        "footer":
            (
                "Ремонт стиральных машин "
                "в Харькове и области на дому."
            ),

        "choose_problem":
            "Выбрать эту проблему",

        "search_price":
            "Найти услугу в прайсе…",
    },


    "uk": {

        "home":
            "Головна",

        "prices":
            "Ціни",

        "brands":
            "Бренди",

        "how":
            "Як працюємо",

        "call":
            "Подзвонити майстру",

        "order":
            "Викликати майстра",

        "phone_hint":
            "Можна одразу подзвонити",

        "area":
            "Харків і область · ремонт вдома",

        "price_agree":
            "Вартість узгоджуємо до ремонту",

        "diagnosis":
            "Діагностика вдома",

        "all_brands":
            "Популярні бренди та інші моделі",

        "modal_title":
            "Викликати майстра",

        "modal_text":
            (
                "Залиште номер. "
                "Ім’я та опис проблеми — "
                "за бажанням."
            ),

        "name":
            "Ваше ім’я (необов’язково)",

        "phone":
            "Телефон",

        "problem":
            "Що сталося? (необов’язково)",

        "submit":
            "Надіслати заявку",

        "privacy":
            (
                "Натискаючи кнопку, "
                "ви надсилаєте заявку "
                "для зв’язку з майстром."
            ),

        "menu":
            "Меню",

        "close":
            "Закрити",

        "footer":
            (
                "Ремонт пральних машин "
                "у Харкові та області вдома."
            ),

        "choose_problem":
            "Обрати цю проблему",

        "search_price":
            "Знайти послугу в прайсі…",
    },
}


def icon(name):

    paths = {

        "phone": (
            '<path d="M6.6 10.8c1.7 3.3 '
            '4.3 5.9 7.6 7.6l2.5-2.5'
            'c.4-.4 1-.5 1.5-.2 '
            '1 .5 2 .8 3.1.9.6.1 '
            '1 .5 1 1.1V21c0 .6-.4 '
            '1-1 1C10.7 22 2 13.3 '
            '2 2.7c0-.6.4-1 1-1h3.3'
            'c.6 0 1 .4 1.1 1 '
            '.1 1.1.4 2.1.9 3.1 '
            '.3.5.2 1.1-.2 1.5z"/>'
        ),

        "home": (
            '<path d="M3 11.5 12 4l9 7.5V21'
            'a1 1 0 0 1-1 1h-5v-7H9v7H4'
            'a1 1 0 0 1-1-1z"/>'
        ),

        "wallet": (
            '<path d="M3 6a2 2 0 0 1 2-2h14v4'
            'H6a2 2 0 0 0 0 4h15v8H5a2 2 '
            '0 0 1-2-2zm14 7h4v4h-4a2 2 '
            '0 1 1 0-4z"/>'
        ),

        "tool": (
            '<path d="M14.7 6.3a5 5 0 0 0-6.4 '
            '6.4L3 18l3 3 5.3-5.3a5 5 0 '
            '0 0 6.4-6.4l-3 3-3-3z"/>'
        ),

        "check": (
            '<path d="m5 12 4 4L19 6" '
            'fill="none" '
            'stroke="currentColor" '
            'stroke-width="2.4" '
            'stroke-linecap="round" '
            'stroke-linejoin="round"/>'
        ),

        "menu": (
            '<path d="M4 7h16M4 12h16M4 17h16" '
            'fill="none" '
            'stroke="currentColor" '
            'stroke-width="2" '
            'stroke-linecap="round"/>'
        ),

        "close": (
            '<path d="m6 6 12 12M18 6 6 18" '
            'fill="none" '
            'stroke="currentColor" '
            'stroke-width="2" '
            'stroke-linecap="round"/>'
        ),

        "spark": (
            '<path d="m12 2 1.8 5.2L19 9'
            'l-5.2 1.8L12 16l-1.8-5.2'
            'L5 9l5.2-1.8zM19 15l.8 2.2'
            'L22 18l-2.2.8L19 21'
            'l-.8-2.2L16 18l2.2-.8z"/>'
        ),
    }

    return (
        '<svg class="icon" '
        'viewBox="0 0 24 24" '
        'aria-hidden="true">'
        f'{paths[name]}'
        '</svg>'
    )


def route_url(
    lang,
    route,
):

    prefix = (
        "uk/"
        if lang == "uk"
        else ""
    )

    return (
        f"{DOMAIN}/"
        f"{prefix}"
        f"{route}"
    )


def head(
    lang,
    route,
    title,
    description,
    asset_prefix,
):

    canonical = route_url(
        lang,
        route,
    )

    alt_ru = route_url(
        "ru",
        route,
    )

    alt_uk = route_url(
        "uk",
        route,
    )

    return dedent(
        f'''
        <!doctype html>

        <html lang="{lang}">

        <head>

          <meta charset="utf-8">

          <meta
            name="viewport"
            content="width=device-width, initial-scale=1, viewport-fit=cover"
          >

          <title>
            {title}
          </title>

          <meta
            name="description"
            content="{description}"
          >

          <meta
            name="theme-color"
            content="#ffffff"
          >

          <link
            rel="canonical"
            href="{canonical}"
          >

          <link
            rel="alternate"
            hreflang="ru"
            href="{alt_ru}"
          >

          <link
            rel="alternate"
            hreflang="uk"
            href="{alt_uk}"
          >

          <link
            rel="alternate"
            hreflang="x-default"
            href="{alt_ru}"
          >

          <link
            rel="stylesheet"
            href="{asset_prefix}styles.css?v=20261006"
          >

          <script>
            window.pageLang =
              '{lang}';
          </script>


          <script type="application/ld+json">
          {{
            "@context":
              "https://schema.org",

            "@type":
              "LocalBusiness",

            "name":
              "remontstiralok.kh.ua",

            "url":
              "{canonical}",

            "telephone":
              "{PHONE_E164}",

            "areaServed":
              "Kharkiv",

            "priceRange":
              "₴₴"
          }}
          </script>

          {GOOGLE_TAG}

        </head>

        <body>
        '''
    )


def header(
    lang,
    local_root,
):

    t = T[lang]

    return dedent(
        f'''
        <header
          class="site-header"
          data-header
        >

          <div class="top-line">

            <div
              class="
                shell
                top-line__inner
              "
            >

              <span>
                {t["area"]}
              </span>

              <a
                href="tel:{PHONE_E164}"
                class="
                  top-phone
                  js-phone
                "
              >
                {icon("phone")}

                <strong>
                  {PHONE_DISPLAY}
                </strong>
              </a>

            </div>

          </div>


          <div
            class="
              shell
              header-main
            "
          >

            <a
              class="brand"
              href="{local_root}"
              aria-label="remontstiralok.kh.ua"
            >

              <span class="brand-mark">
                R
              </span>

              <span class="brand-text">
                remontstiralok
                <span>.kh.ua</span>
              </span>

            </a>


            <button
              class="menu-toggle"
              type="button"
              aria-expanded="false"
              aria-controls="main-nav"
              data-menu-toggle
            >
              {icon("menu")}

              <span>
                {t["menu"]}
              </span>
            </button>


            <nav
              class="main-nav"
              id="main-nav"
              data-menu
            >

              <a href="{local_root}">
                {t["home"]}
              </a>

              <a href="{local_root}price/">
                {t["prices"]}
              </a>

              <a href="{local_root}#brands">
                {t["brands"]}
              </a>

              <a href="{local_root}#how">
                {t["how"]}
              </a>

            </nav>


            <a
              class="
                header-call
                js-phone
              "
              href="tel:{PHONE_E164}"
            >

              {icon("phone")}

              <span>

                <small>
                  {t["phone_hint"]}
                </small>

                <strong>
                  {PHONE_DISPLAY}
                </strong>

              </span>

            </a>


            <button
              class="
                btn
                btn-primary
                header-order
                js-open-order
              "
              type="button"
            >
              {t["order"]}
            </button>

          </div>

        </header>
        '''
    )


def modal(
    lang,
):

    t = T[lang]

    or_text = (
        "или"
        if lang == "ru"
        else "або"
    )

    return dedent(
        f'''
        <div
          class="order-modal"
          id="order-modal"
          aria-hidden="true"
          data-order-modal
        >

          <div
            class="order-modal__backdrop"
            data-modal-close
          ></div>


          <section
            class="order-modal__panel"
            role="dialog"
            aria-modal="true"
            aria-labelledby="order-modal-title"
          >

            <button
              class="modal-close"
              type="button"
              aria-label="{t["close"]}"
              data-modal-close
            >
              {icon("close")}
            </button>


            <div class="modal-icon">
              {icon("tool")}
            </div>


            <h2 id="order-modal-title">
              {t["modal_title"]}
            </h2>


            <p>
              {t["modal_text"]}
            </p>


            <form
              class="
                form
                orderForm
              "
            >

              <label>

                {t["name"]}

                <input
                  type="text"
                  name="name"
                  maxlength="50"
                  autocomplete="name"
                >

              </label>


              <div
                class="
                  error
                  nameError
                "
              ></div>


              <label>
                {t["phone"]}
              </label>


              <div class="phone-row">

                <span>
                  +38
                </span>

                <input
                  type="tel"
                  name="phone_number"
                  placeholder="0671371673"
                  inputmode="numeric"
                  maxlength="10"
                  autocomplete="tel-national"
                  required
                >

              </div>


              <div
                class="
                  error
                  phoneError
                "
              ></div>


              <label>

                {t["problem"]}

                <textarea
                  name="problem_description"
                  rows="3"
                ></textarea>

              </label>


              <button
                class="
                  btn
                  btn-primary
                  btn-full
                "
                type="submit"
              >
                {t["submit"]}
              </button>


              <div class="form-note">
                {t["privacy"]}
              </div>

            </form>


            <div class="modal-or">

              <span>
                {or_text}
              </span>

            </div>


            <a
              class="
                btn
                btn-call
                btn-full
                js-phone
              "
              href="tel:{PHONE_E164}"
            >
              {icon("phone")}

              {PHONE_DISPLAY}
            </a>

          </section>

        </div>
        '''
    )


def footer(
    lang,
    asset_prefix,
):

    t = T[lang]

    return dedent(
        f'''
        <footer class="footer">

          <div
            class="
              shell
              footer-grid
            "
          >

            <div>

              <strong>
                remontstiralok.kh.ua
              </strong>

              <p>
                {t["footer"]}
              </p>

            </div>


            <a
              class="
                footer-phone
                js-phone
              "
              href="tel:{PHONE_E164}"
            >
              {icon("phone")}

              {PHONE_DISPLAY}
            </a>

          </div>

        </footer>


        <div
          class="mobile-actions"
          aria-label="Контакты"
        >

          <a
            class="
              mobile-actions__call
              js-phone
            "
            href="tel:{PHONE_E164}"
          >
            {icon("phone")}

            <span>
              {t["call"]}
            </span>
          </a>


          <button
            class="
              mobile-actions__order
              js-open-order
            "
            type="button"
          >
            {icon("tool")}

            <span>
              {t["order"]}
            </span>
          </button>

        </div>


        {modal(lang)}


        <script
          src="{asset_prefix}scripts.js?v=20261006"
          defer
        ></script>

        <script
          src="{asset_prefix}site-ui.js?v=20261006"
          defer
        ></script>

        </body>

        </html>
        '''
    )


def trust_items(
    lang,
):

    t = T[lang]

    if lang == "ru":

        home_text = (
            "Большинство типовых работ "
            "без вывоза техники"
        )

        agree_text = (
            "Сначала диагностика "
            "и согласование"
        )

    else:

        home_text = (
            "Більшість типових робіт "
            "без вивезення техніки"
        )

        agree_text = (
            "Спочатку діагностика "
            "та узгодження"
        )


    return f'''

    <div
      class="
        trust-grid
        reveal
      "
    >

      <div class="trust-item">

        <span class="icon-box">
          {icon("home")}
        </span>

        <div>

          <strong>
            {t["diagnosis"]}
          </strong>

          <small>
            {home_text}
          </small>

        </div>

      </div>


      <div class="trust-item">

        <span class="icon-box">
          {icon("wallet")}
        </span>

        <div>

          <strong>
            {t["price_agree"]}
          </strong>

          <small>
            {agree_text}
          </small>

        </div>

      </div>


      <div class="trust-item">

        <span class="icon-box">
          {icon("phone")}
        </span>

        <div>

          <strong>
            {t["call"]}
          </strong>

          <small>
            {PHONE_DISPLAY}
          </small>

        </div>

      </div>


      <div class="trust-item">

        <span class="icon-box">
          {icon("check")}
        </span>

        <div>

          <strong>
            {t["all_brands"]}
          </strong>

          <small>
            Bosch, Samsung, LG,
            Indesit, Electrolux, Zanussi
          </small>

        </div>

      </div>

    </div>
    '''


def problem_cards(
    lang,
    asset_prefix,
    brand="",
):

    if lang == "ru":

        items = [

            (
                "problem-drain.webp",
                "Не сливает воду",
                (
                    "Проверим фильтр, насос, "
                    "шланг и систему слива."
                ),
            ),

            (
                "problem-heating.webp",
                "Не греет воду",
                (
                    "Проверим ТЭН, "
                    "датчик температуры, "
                    "проводку и управление."
                ),
            ),

            (
                "problem-spin.webp",
                "Не отжимает",
                (
                    "Проверим ремень, двигатель, "
                    "щётки, датчики и амортизаторы."
                ),
            ),

            (
                "problem-leak.webp",
                "Протекает",
                (
                    "Найдём место течи: "
                    "манжета, патрубки, "
                    "фильтр, бак или шланги."
                ),
            ),

            (
                "problem-door.webp",
                "Не открывается люк",
                (
                    "Проверим ручку, петлю, "
                    "замок и устройство "
                    "блокировки люка."
                ),
            ),

            (
                "problem-noise.webp",
                "Шумит и вибрирует",
                (
                    "Проверим подшипники, "
                    "амортизаторы, барабан "
                    "и противовесы."
                ),
            ),
        ]

    else:

        items = [

            (
                "problem-drain.webp",
                "Не зливає воду",
                (
                    "Перевіримо фільтр, насос, "
                    "шланг і систему зливу."
                ),
            ),

            (
                "problem-heating.webp",
                "Не гріє воду",
                (
                    "Перевіримо ТЕН, "
                    "датчик температури, "
                    "проводку та керування."
                ),
            ),

            (
                "problem-spin.webp",
                "Не віджимає",
                (
                    "Перевіримо ремінь, двигун, "
                    "щітки, датчики "
                    "та амортизатори."
                ),
            ),

            (
                "problem-leak.webp",
                "Протікає",
                (
                    "Знайдемо місце протікання: "
                    "манжета, патрубки, "
                    "фільтр, бак або шланги."
                ),
            ),

            (
                "problem-door.webp",
                "Не відкривається люк",
                (
                    "Перевіримо ручку, петлю, "
                    "замок і пристрій "
                    "блокування люка."
                ),
            ),

            (
                "problem-noise.webp",
                "Шумить і вібрує",
                (
                    "Перевіримо підшипники, "
                    "амортизатори, барабан "
                    "і противаги."
                ),
            ),
        ]


    cards = []


    for (
        image_name,
        title,
        text,
    ) in items:

        problem = (
            f"{brand}: {title}"
            if brand
            else title
        )

        alt = (
            f"{title} {brand}"
            if brand
            else title
        )

        cards.append(
            f'''
            <article
              class="
                problem-card
                reveal
              "
            >

              <img
                src="{asset_prefix}assets/service/{image_name}"
                alt="{alt}"
                loading="lazy"
              >

              <div class="problem-card__body">

                <h3>
                  {title}
                </h3>

                <p>
                  {text}
                </p>

                <button
                  class="
                    text-action
                    js-open-order
                  "
                  type="button"
                  data-problem="{problem}"
                >
                  {T[lang]["choose_problem"]}
                  →
                </button>

              </div>

            </article>
            '''
        )


    return "\n".join(
        cards
    )


def quick_prices(
    lang,
):

    if lang == "ru":

        items = [

            (
                "Диагностика",
                "600 грн",
            ),

            (
                "Замена ТЭНа",
                "1900–2200 грн",
            ),

            (
                "Замена насоса",
                "1800–2300 грн",
            ),

            (
                "Замена УБЛ",
                "1900 грн",
            ),
        ]

    else:

        items = [

            (
                "Діагностика",
                "600 грн",
            ),

            (
                "Заміна ТЕНа",
                "1900–2200 грн",
            ),

            (
                "Заміна насоса",
                "1800–2300 грн",
            ),

            (
                "Заміна УБЛ",
                "1900 грн",
            ),
        ]


    return "".join(

        f'''
        <div
          class="
            price-chip
            reveal
          "
        >

          <span>
            {name}
          </span>

          <strong>
            {price}
          </strong>

        </div>
        '''

        for (
            name,
            price,
        ) in items
    )


def home_body(
    lang,
    asset_prefix,
    local_root,
):

    if lang == "ru":

        h1 = (
            "Ремонт стиральных машин "
            "в Харькове и области"
        )

        lead = (
            "Не нужно разбираться "
            "в кодах ошибок. "
            "Опишите симптом или просто "
            "оставьте номер — мастер "
            "уточнит детали и согласует "
            "стоимость до ремонта."
        )

        problems_h = (
            "Что случилось "
            "со стиральной машиной?"
        )

        problems_p = (
            "Нажмите на свою проблему — "
            "она автоматически попадёт "
            "в форму вызова мастера."
        )

        price_h = (
            "Понятные цены "
            "на популярные работы"
        )

        price_p = (
            "Точная стоимость зависит "
            "от модели и состояния техники. "
            "Перед ремонтом стоимость "
            "согласуется."
        )

        comfort_h = (
            "Сервис без лишних сложностей"
        )

        comfort = [

            (
                "home",
                "Ремонт на дому",
                (
                    "Большинство типовых "
                    "неисправностей устраняется "
                    "без вывоза техники."
                ),
            ),

            (
                "wallet",
                "Сначала стоимость",
                (
                    "Диагностика → согласование → "
                    "только потом ремонт."
                ),
            ),

            (
                "phone",
                "Можно позвонить",
                (
                    "Номер всегда виден "
                    "в шапке и внизу "
                    "экрана телефона."
                ),
            ),

            (
                "spark",
                "Короткая форма",
                (
                    "Обязателен только номер "
                    "телефона. Остальное можно "
                    "уточнить в разговоре."
                ),
            ),
        ]

        brands_h = (
            "Ремонтируем популярные марки"
        )

        how_h = (
            "Как проходит обращение"
        )

        steps = [

            (
                "1",
                "Вы связываетесь",
                (
                    "Звоните или нажимаете "
                    "«Вызвать мастера» "
                    "и оставляете номер."
                ),
            ),

            (
                "2",
                "Уточняем проблему",
                (
                    "Мастер уточняет модель, "
                    "симптомы и район."
                ),
            ),

            (
                "3",
                "Диагностика",
                (
                    "На месте проверяет технику "
                    "и называет стоимость."
                ),
            ),

            (
                "4",
                "Ремонт после согласования",
                (
                    "Работа начинается только "
                    "после того, как стоимость "
                    "вам понятна."
                ),
            ),
        ]

        faq = [

            (
                "Сколько стоит диагностика?",
                (
                    "Диагностика стиральной "
                    "машины — 600 грн. "
                    "Полный прайс доступен "
                    "на отдельной странице."
                ),
            ),

            (
                (
                    "Можно ли сначала узнать "
                    "ориентировочную цену?"
                ),
                (
                    "Да. Опишите симптом "
                    "в форме или позвоните. "
                    "Точная стоимость определяется "
                    "после диагностики и "
                    "согласуется до ремонта."
                ),
            ),

            (
                "Какие бренды ремонтируете?",
                (
                    "Bosch, Samsung, LG, Indesit, "
                    "Electrolux, Zanussi и другие "
                    "распространённые марки."
                ),
            ),

            (
                "Можно не заполнять форму?",
                (
                    "Да. Нажмите на номер "
                    f"{PHONE_DISPLAY} — "
                    "откроется звонок мастеру."
                ),
            ),
        ]

    else:

        h1 = (
            "Ремонт пральних машин "
            "у Харкові та області"
        )

        lead = (
            "Не потрібно розбиратися "
            "в кодах помилок. "
            "Опишіть симптом або просто "
            "залиште номер — майстер "
            "уточнить деталі та узгодить "
            "вартість до ремонту."
        )

        problems_h = (
            "Що сталося "
            "з пральною машиною?"
        )

        problems_p = (
            "Натисніть на свою проблему — "
            "вона автоматично потрапить "
            "у форму виклику майстра."
        )

        price_h = (
            "Зрозумілі ціни "
            "на популярні роботи"
        )

        price_p = (
            "Точна вартість залежить "
            "від моделі та стану техніки. "
            "Перед ремонтом вартість "
            "узгоджується."
        )

        comfort_h = (
            "Сервіс без зайвих складнощів"
        )

        comfort = [

            (
                "home",
                "Ремонт вдома",
                (
                    "Більшість типових "
                    "несправностей усувається "
                    "без вивезення техніки."
                ),
            ),

            (
                "wallet",
                "Спочатку вартість",
                (
                    "Діагностика → узгодження → "
                    "лише потім ремонт."
                ),
            ),

            (
                "phone",
                "Можна подзвонити",
                (
                    "Номер завжди видно "
                    "в шапці та внизу "
                    "екрана телефона."
                ),
            ),

            (
                "spark",
                "Коротка форма",
                (
                    "Обов’язковий лише номер "
                    "телефона. Решту можна "
                    "уточнити в розмові."
                ),
            ),
        ]

        brands_h = (
            "Ремонтуємо популярні марки"
        )

        how_h = (
            "Як проходить звернення"
        )

        steps = [

            (
                "1",
                "Ви зв’язуєтесь",
                (
                    "Телефонуєте або натискаєте "
                    "«Викликати майстра» "
                    "та залишаєте номер."
                ),
            ),

            (
                "2",
                "Уточнюємо проблему",
                (
                    "Майстер уточнює модель, "
                    "симптоми та район."
                ),
            ),

            (
                "3",
                "Діагностика",
                (
                    "На місці перевіряє техніку "
                    "та називає вартість."
                ),
            ),

            (
                "4",
                "Ремонт після узгодження",
                (
                    "Робота починається лише "
                    "після того, як вартість "
                    "вам зрозуміла."
                ),
            ),
        ]

        faq = [

            (
                "Скільки коштує діагностика?",
                (
                    "Діагностика пральної "
                    "машини — 600 грн. "
                    "Повний прайс доступний "
                    "на окремій сторінці."
                ),
            ),

            (
                (
                    "Чи можна спочатку дізнатися "
                    "орієнтовну ціну?"
                ),
                (
                    "Так. Опишіть симптом "
                    "у формі або зателефонуйте. "
                    "Точна вартість визначається "
                    "після діагностики та "
                    "узгоджується до ремонту."
                ),
            ),

            (
                "Які бренди ремонтуєте?",
                (
                    "Bosch, Samsung, LG, Indesit, "
                    "Electrolux, Zanussi та інші "
                    "поширені марки."
                ),
            ),

            (
                "Можна не заповнювати форму?",
                (
                    "Так. Натисніть на номер "
                    f"{PHONE_DISPLAY} — "
                    "відкриється дзвінок майстру."
                ),
            ),
        ]


    comfort_html = "".join(

        f'''
        <article
          class="
            benefit-card
            reveal
          "
        >

          <span class="icon-box">
            {icon(icon_name)}
          </span>

          <h3>
            {title}
          </h3>

          <p>
            {text}
          </p>

        </article>
        '''

        for (
            icon_name,
            title,
            text,
        ) in comfort
    )


    brand_cards = "".join(

        f'''
        <a
          class="
            brand-card
            reveal
          "
          href="{local_root}remont-{slug}/"
        >

          <span>
            {brand}
          </span>

          <small>
            {
                "Ремонт и диагностика"
                if lang == "ru"
                else "Ремонт і діагностика"
            }
          </small>

        </a>
        '''

        for (
            slug,
            brand,
            _,
        ) in BRANDS
    )


    steps_html = "".join(

        f'''
        <article
          class="
            step-card
            reveal
          "
        >

          <span>
            {num}
          </span>

          <h3>
            {title}
          </h3>

          <p>
            {text}
          </p>

        </article>
        '''

        for (
            num,
            title,
            text,
        ) in steps
    )


    faq_html = "".join(

        f'''
        <details>

          <summary>
            {question}
          </summary>

          <p>
            {answer}
          </p>

        </details>
        '''

        for (
            question,
            answer,
        ) in faq
    )


    faq_title = (
        "Частые вопросы"
        if lang == "ru"
        else "Поширені запитання"
    )


    return dedent(
        f'''
        <main>


          <section class="hero">

            <div
              class="
                shell
                hero-grid
              "
            >

              <div
                class="
                  hero-copy
                  reveal
                "
              >

                <div class="eyebrow">
                  {T[lang]["area"]}
                </div>


                <h1>
                  {h1}
                </h1>


                <p class="hero-lead">
                  {lead}
                </p>


                <div class="hero-phone-card">

                  <span
                    class="hero-phone-card__icon"
                  >
                    {icon("phone")}
                  </span>

                  <div>

                    <small>
                      {T[lang]["phone_hint"]}
                    </small>

                    <a
                      class="js-phone"
                      href="tel:{PHONE_E164}"
                    >
                      {PHONE_DISPLAY}
                    </a>

                  </div>

                </div>


                <div class="hero-actions">

                  <a
                    class="
                      btn
                      btn-call
                      js-phone
                    "
                    href="tel:{PHONE_E164}"
                  >
                    {icon("phone")}
                    {T[lang]["call"]}
                  </a>


                  <button
                    class="
                      btn
                      btn-primary
                      js-open-order
                    "
                    type="button"
                  >
                    {T[lang]["order"]}
                  </button>

                </div>

              </div>


              <div
                class="
                  hero-visual
                  reveal
                "
              >

                <img
                  src="{asset_prefix}assets/service/hero-master.webp"
                  alt="{h1}"
                  loading="eager"
                >


                <div class="hero-visual__note">

                  {icon("wallet")}

                  <span>
                    {T[lang]["price_agree"]}
                  </span>

                </div>

              </div>

            </div>


            <div class="shell">
              {trust_items(lang)}
            </div>

          </section>


          <section
            class="
              section
              shell
            "
          >

            <div class="section-head">

              <span class="section-kicker">
                01
              </span>

              <div>

                <h2>
                  {problems_h}
                </h2>

                <p>
                  {problems_p}
                </p>

              </div>

            </div>


            <div class="problem-grid">
              {
                  problem_cards(
                      lang,
                      asset_prefix,
                  )
              }
            </div>

          </section>


          <section
            class="
              section
              section-soft
            "
          >

            <div class="shell">

              <div class="section-head">

                <span class="section-kicker">
                  02
                </span>

                <div>

                  <h2>
                    {price_h}
                  </h2>

                  <p>
                    {price_p}
                  </p>

                </div>

              </div>


              <div class="quick-prices">
                {quick_prices(lang)}
              </div>


              <a
                class="inline-link"
                href="{local_root}price/"
              >
                {T[lang]["prices"]}
                →
              </a>

            </div>

          </section>


          <section
            class="
              section
              shell
            "
          >

            <div class="section-head">

              <span class="section-kicker">
                03
              </span>

              <div>

                <h2>
                  {comfort_h}
                </h2>

              </div>

            </div>


            <div class="benefit-grid">
              {comfort_html}
            </div>

          </section>


          <section
            class="
              section
              section-soft
            "
            id="brands"
          >

            <div class="shell">

              <div class="section-head">

                <span class="section-kicker">
                  04
                </span>

                <div>

                  <h2>
                    {brands_h}
                  </h2>

                </div>

              </div>


              <div class="brand-grid">
                {brand_cards}
              </div>

            </div>

          </section>


          <section
            class="
              section
              shell
            "
            id="how"
          >

            <div class="section-head">

              <span class="section-kicker">
                05
              </span>

              <div>

                <h2>
                  {how_h}
                </h2>

              </div>

            </div>


            <div class="steps-grid">
              {steps_html}
            </div>

          </section>


          <section
            class="
              section
              shell
            "
          >

            <div
              class="
                conversion-card
                reveal
              "
            >

              <div>

                <span class="eyebrow">
                  {T[lang]["area"]}
                </span>

                <h2>
                  {T[lang]["order"]}
                </h2>

                <p>
                  {T[lang]["modal_text"]}
                </p>

              </div>


              <div
                class="
                  conversion-card__actions
                "
              >

                <a
                  class="
                    btn
                    btn-call
                    js-phone
                  "
                  href="tel:{PHONE_E164}"
                >
                  {icon("phone")}

                  {PHONE_DISPLAY}
                </a>


                <button
                  class="
                    btn
                    btn-primary
                    js-open-order
                  "
                  type="button"
                >
                  {T[lang]["order"]}
                </button>

              </div>

            </div>

          </section>


          <section
            class="
              section
              shell
              faq-section
            "
          >

            <div class="section-head">

              <span class="section-kicker">
                FAQ
              </span>

              <div>

                <h2>
                  {faq_title}
                </h2>

              </div>

            </div>


            {faq_html}

          </section>


        </main>
        '''
    )


def price_body(
    lang,
):

    rows = (
        PRICE_ROWS_RU
        if lang == "ru"
        else PRICE_ROWS_UK
    )


    if lang == "ru":

        title = (
            "Цены на ремонт "
            "стиральных машин"
        )

        lead = (
            "Понятный прайс на основные "
            "работы по ремонту стиральных "
            "машин в Харькове и области."
        )

        note = (
            "Цены указаны за работу. "
            "Стоимость запчастей зависит "
            "от бренда и модели. "
            "Окончательная стоимость "
            "согласуется после диагностики "
            "до начала ремонта."
        )

        table_h = (
            "Полный прайс-лист"
        )

        name_header = (
            "Название операции"
        )

        price_header = (
            "Цена"
        )

        cta_title = (
            "Хотите уточнить стоимость?"
        )

    else:

        title = (
            "Ціни на ремонт "
            "пральних машин"
        )

        lead = (
            "Зрозумілий прайс на основні "
            "роботи з ремонту пральних "
            "машин у Харкові та області."
        )

        note = (
            "Ціни вказані за роботу. "
            "Вартість запчастин залежить "
            "від бренду та моделі. "
            "Остаточна вартість узгоджується "
            "після діагностики "
            "до початку ремонту."
        )

        table_h = (
            "Повний прайс-лист"
        )

        name_header = (
            "Назва роботи"
        )

        price_header = (
            "Ціна"
        )

        cta_title = (
            "Хочете уточнити вартість?"
        )


    rows_html = "\n".join(

        (
            "<tr>"
            f"<td>{name}</td>"
            f"<td>{price}</td>"
            "</tr>"
        )

        for (
            name,
            price,
        ) in rows
    )


    return dedent(
        f'''
        <main>


          <section class="page-hero">

            <div
              class="
                shell
                page-hero__grid
              "
            >

              <div>

                <div class="eyebrow">
                  {T[lang]["area"]}
                </div>


                <h1>
                  {title}
                </h1>


                <p>
                  {lead}
                </p>


                <div class="hero-actions">

                  <a
                    class="
                      btn
                      btn-call
                      js-phone
                    "
                    href="tel:{PHONE_E164}"
                  >
                    {icon("phone")}

                    {T[lang]["call"]}
                  </a>


                  <button
                    class="
                      btn
                      btn-primary
                      js-open-order
                    "
                    type="button"
                  >
                    {T[lang]["order"]}
                  </button>

                </div>

              </div>


              <div class="page-contact-card">

                <span>
                  {icon("phone")}
                </span>

                <small>
                  {T[lang]["phone_hint"]}
                </small>

                <a
                  class="js-phone"
                  href="tel:{PHONE_E164}"
                >
                  {PHONE_DISPLAY}
                </a>

              </div>

            </div>

          </section>


          <section
            class="
              section
              shell
            "
          >

            <div class="section-head">

              <span class="section-kicker">
                ₴
              </span>

              <div>

                <h2>
                  {table_h}
                </h2>

                <p>
                  {note}
                </p>

              </div>

            </div>


            <div class="price-tools">

              <label class="price-search">

                {icon("spark")}

                <input
                  id="price-search"
                  type="search"
                  placeholder="{T[lang]["search_price"]}"
                  autocomplete="off"
                >

              </label>

            </div>


            <div class="price-table-wrap">

              <table
                class="price-table"
                data-price-table
              >

                <thead>

                  <tr>

                    <th>
                      {name_header}
                    </th>

                    <th>
                      {price_header}
                    </th>

                  </tr>

                </thead>

                <tbody>
                  {rows_html}
                </tbody>

              </table>

            </div>


            <p class="notice">
              {note}
            </p>

          </section>


          <section
            class="
              section
              shell
            "
          >

            <div
              class="
                conversion-card
                reveal
              "
            >

              <div>

                <h2>
                  {cta_title}
                </h2>

                <p>
                  {T[lang]["modal_text"]}
                </p>

              </div>


              <div
                class="
                  conversion-card__actions
                "
              >

                <a
                  class="
                    btn
                    btn-call
                    js-phone
                  "
                  href="tel:{PHONE_E164}"
                >
                  {PHONE_DISPLAY}
                </a>


                <button
                  class="
                    btn
                    btn-primary
                    js-open-order
                  "
                  type="button"
                >
                  {T[lang]["order"]}
                </button>

              </div>

            </div>

          </section>


        </main>
        '''
    )


def brand_body(
    lang,
    asset_prefix,
    local_root,
    brand,
    hero_image,
):

    if lang == "ru":

        title = (
            f"Ремонт стиральных машин "
            f"{brand} в Харькове и области"
        )

        lead = (
            f"Ремонт {brand} на дому: "
            "слив, нагрев, отжим, течь, "
            "люк, шум и электроника. "
            "Можно позвонить сразу или "
            "открыть короткую форму "
            "поверх страницы."
        )

        issues_h = (
            f"Частые проблемы "
            f"стиральных машин {brand}"
        )

        issue_note = (
            "Выберите симптом — "
            "он автоматически подставится "
            "в форму вызова мастера."
        )

        prices_h = (
            "Ориентиры по стоимости работ"
        )

        price_note = (
            "Цена зависит от модели "
            "и конкретной неисправности. "
            "Перед ремонтом стоимость "
            "согласуется."
        )

        faq_title = (
            "Частые вопросы"
        )

        faq_q1 = (
            f"Вы ремонтируете {brand} "
            "на дому?"
        )

        faq_a1 = (
            "Да, большинство типовых "
            "неисправностей диагностируется "
            "и устраняется на дому."
        )

        faq_q2 = (
            "Можно сначала узнать цену?"
        )

        faq_a2 = (
            "Можно описать симптом "
            "в форме или позвонить. "
            "Точная стоимость определяется "
            "после диагностики и "
            "согласуется до ремонта."
        )

    else:

        title = (
            f"Ремонт пральних машин "
            f"{brand} у Харкові та області"
        )

        lead = (
            f"Ремонт {brand} вдома: "
            "злив, нагрів, віджим, "
            "протікання, люк, шум "
            "та електроніка. "
            "Можна одразу зателефонувати "
            "або відкрити коротку форму "
            "поверх сторінки."
        )

        issues_h = (
            f"Поширені проблеми "
            f"пральних машин {brand}"
        )

        issue_note = (
            "Оберіть симптом — "
            "він автоматично підставиться "
            "у форму виклику майстра."
        )

        prices_h = (
            "Орієнтири щодо вартості робіт"
        )

        price_note = (
            "Ціна залежить від моделі "
            "та конкретної несправності. "
            "Перед ремонтом вартість "
            "узгоджується."
        )

        faq_title = (
            "Поширені запитання"
        )

        faq_q1 = (
            f"Ви ремонтуєте {brand} "
            "вдома?"
        )

        faq_a1 = (
            "Так, більшість типових "
            "несправностей діагностується "
            "та усувається вдома."
        )

        faq_q2 = (
            "Можна спочатку дізнатися ціну?"
        )

        faq_a2 = (
            "Можна описати симптом "
            "у формі або зателефонувати. "
            "Точна вартість визначається "
            "після діагностики та "
            "узгоджується до ремонту."
        )


    return dedent(
        f'''
        <main>


          <section
            class="
              hero
              brand-hero
            "
          >

            <div
              class="
                shell
                hero-grid
              "
            >

              <div
                class="
                  hero-copy
                  reveal
                "
              >

                <div class="eyebrow">
                  {T[lang]["area"]}
                </div>


                <h1>
                  {title}
                </h1>


                <p class="hero-lead">
                  {lead}
                </p>


                <div class="hero-phone-card">

                  <span
                    class="hero-phone-card__icon"
                  >
                    {icon("phone")}
                  </span>

                  <div>

                    <small>
                      {T[lang]["phone_hint"]}
                    </small>

                    <a
                      class="js-phone"
                      href="tel:{PHONE_E164}"
                    >
                      {PHONE_DISPLAY}
                    </a>

                  </div>

                </div>


                <div class="hero-actions">

                  <a
                    class="
                      btn
                      btn-call
                      js-phone
                    "
                    href="tel:{PHONE_E164}"
                  >
                    {icon("phone")}

                    {T[lang]["call"]}
                  </a>


                  <button
                    class="
                      btn
                      btn-primary
                      js-open-order
                    "
                    type="button"
                    data-problem="{brand}"
                  >
                    {T[lang]["order"]}
                  </button>

                </div>

              </div>


              <div
                class="
                  hero-visual
                  reveal
                "
              >

                <img
                  src="{asset_prefix}assets/service/{hero_image}"
                  alt="{title}"
                  loading="eager"
                >


                <div class="hero-visual__note">

                  {icon("wallet")}

                  <span>
                    {T[lang]["price_agree"]}
                  </span>

                </div>

              </div>

            </div>


            <div class="shell">
              {trust_items(lang)}
            </div>

          </section>


          <section
            class="
              section
              shell
            "
          >

            <div class="section-head">

              <span class="section-kicker">
                01
              </span>

              <div>

                <h2>
                  {issues_h}
                </h2>

                <p>
                  {issue_note}
                </p>

              </div>

            </div>


            <div class="problem-grid">

              {
                  problem_cards(
                      lang,
                      asset_prefix,
                      brand,
                  )
              }

            </div>

          </section>


          <section
            class="
              section
              section-soft
            "
          >

            <div class="shell">

              <div class="section-head">

                <span class="section-kicker">
                  02
                </span>

                <div>

                  <h2>
                    {prices_h}
                  </h2>

                  <p>
                    {price_note}
                  </p>

                </div>

              </div>


              <div class="quick-prices">
                {quick_prices(lang)}
              </div>


              <a
                class="inline-link"
                href="{local_root}price/"
              >
                {T[lang]["prices"]}
                →
              </a>

            </div>

          </section>


          <section
            class="
              section
              shell
            "
          >

            <div
              class="
                conversion-card
                reveal
              "
            >

              <div>

                <h2>
                  {T[lang]["order"]}
                  {brand}
                </h2>

                <p>
                  {T[lang]["modal_text"]}
                </p>

              </div>


              <div
                class="
                  conversion-card__actions
                "
              >

                <a
                  class="
                    btn
                    btn-call
                    js-phone
                  "
                  href="tel:{PHONE_E164}"
                >
                  {PHONE_DISPLAY}
                </a>


                <button
                  class="
                    btn
                    btn-primary
                    js-open-order
                  "
                  type="button"
                  data-problem="{brand}"
                >
                  {T[lang]["order"]}
                </button>

              </div>

            </div>

          </section>


          <section
            class="
              section
              shell
              faq-section
            "
          >

            <div class="section-head">

              <span class="section-kicker">
                FAQ
              </span>

              <div>

                <h2>
                  {faq_title}
                </h2>

              </div>

            </div>


            <details>

              <summary>
                {faq_q1}
              </summary>

              <p>
                {faq_a1}
              </p>

            </details>


            <details>

              <summary>
                {faq_q2}
              </summary>

              <p>
                {faq_a2}
              </p>

            </details>

          </section>


        </main>
        '''
    )


def write_page(
    path,
    lang,
    route,
    title,
    description,
    body,
    asset_prefix,
    local_root,
):

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    html = (

        head(
            lang,
            route,
            title,
            description,
            asset_prefix,
        )

        +

        header(
            lang,
            local_root,
        )

        +

        body

        +

        footer(
            lang,
            asset_prefix,
        )
    )


    path.write_text(
        html,
        encoding="utf-8",
    )


    print(
        "[OK]",
        path.relative_to(ROOT),
    )


def build():

    #
    # RUSSIAN MAIN
    #

    write_page(

        ROOT
        / "index.html",

        "ru",

        "",

        (
            "Ремонт стиральных машин "
            "в Харькове и области — "
            "вызвать мастера"
        ),

        (
            "Ремонт стиральных машин "
            "в Харькове и области на дому. "
            "Звонок мастеру или короткая "
            "заявка, понятный прайс, "
            "ремонт Bosch, Samsung, LG, "
            "Indesit, Electrolux и Zanussi."
        ),

        home_body(
            "ru",
            "",
            "./",
        ),

        "",

        "./",
    )


    #
    # RUSSIAN PRICE
    #

    write_page(

        ROOT
        / "price"
        / "index.html",

        "ru",

        "price/",

        (
            "Цены на ремонт стиральных машин "
            "в Харькове — прайс-лист"
        ),

        (
            "Прайс-лист на ремонт "
            "стиральных машин "
            "в Харькове и области. "
            "Диагностика, ТЭН, насос, "
            "УБЛ, манжета, подшипники "
            "и другие работы."
        ),

        price_body(
            "ru",
        ),

        "../",

        "../",
    )


    #
    # RUSSIAN BRANDS
    #

    for (
        slug,
        brand,
        image_name,
    ) in BRANDS:

        write_page(

            ROOT
            / f"remont-{slug}"
            / "index.html",

            "ru",

            f"remont-{slug}/",

            (
                f"Ремонт стиральных машин "
                f"{brand} в Харькове "
                f"и области — мастер на дом"
            ),

            (
                f"Ремонт стиральных машин "
                f"{brand} в Харькове "
                f"и области на дому. "
                f"Диагностика, слив, нагрев, "
                f"отжим, люк, течь, шум "
                f"и электроника."
            ),

            brand_body(
                "ru",
                "../",
                "../",
                brand,
                image_name,
            ),

            "../",

            "../",
        )


    #
    # UKRAINIAN MAIN
    #

    write_page(

        ROOT
        / "uk"
        / "index.html",

        "uk",

        "",

        (
            "Ремонт пральних машин "
            "у Харкові та області — "
            "викликати майстра"
        ),

        (
            "Ремонт пральних машин "
            "у Харкові та області вдома. "
            "Дзвінок майстру або коротка "
            "заявка, зрозумілий прайс, "
            "ремонт Bosch, Samsung, LG, "
            "Indesit, Electrolux і Zanussi."
        ),

        home_body(
            "uk",
            "../",
            "./",
        ),

        "../",

        "./",
    )


    #
    # UKRAINIAN PRICE
    #

    write_page(

        ROOT
        / "uk"
        / "price"
        / "index.html",

        "uk",

        "price/",

        (
            "Ціни на ремонт пральних машин "
            "у Харкові — прайс-лист"
        ),

        (
            "Прайс-лист на ремонт "
            "пральних машин "
            "у Харкові та області. "
            "Діагностика, ТЕН, насос, "
            "УБЛ, манжета, підшипники "
            "та інші роботи."
        ),

        price_body(
            "uk",
        ),

        "../../",

        "../",
    )


    #
    # UKRAINIAN BRANDS
    #

    for (
        slug,
        brand,
        image_name,
    ) in BRANDS:

        write_page(

            ROOT
            / "uk"
            / f"remont-{slug}"
            / "index.html",

            "uk",

            f"remont-{slug}/",

            (
                f"Ремонт пральних машин "
                f"{brand} у Харкові "
                f"та області — майстер додому"
            ),

            (
                f"Ремонт пральних машин "
                f"{brand} у Харкові "
                f"та області вдома. "
                f"Діагностика, злив, нагрів, "
                f"віджим, люк, протікання, "
                f"шум та електроніка."
            ),

            brand_body(
                "uk",
                "../../",
                "../",
                brand,
                image_name,
            ),

            "../../",

            "../",
        )


    #
    # SITEMAP
    #

    routes = [

        "",

        "price/",

        *[
            f"remont-{slug}/"
            for (
                slug,
                _,
                _,
            )
            in BRANDS
        ],
    ]


    urls = []


    for route in routes:

        urls.append(

            "  <url>"
            f"<loc>{route_url('ru', route)}</loc>"
            "</url>"
        )

        urls.append(

            "  <url>"
            f"<loc>{route_url('uk', route)}</loc>"
            "</url>"
        )


    sitemap = (

        '<?xml version="1.0" '
        'encoding="UTF-8"?>\n'

        '<urlset '
        'xmlns="http://www.sitemaps.org/'
        'schemas/sitemap/0.9">\n'

        +

        "\n".join(
            urls
        )

        +

        '\n</urlset>\n'
    )


    (
        ROOT
        / "sitemap.xml"
    ).write_text(

        sitemap,

        encoding="utf-8",
    )


    print(
        "[OK] sitemap.xml"
    )


if __name__ == "__main__":

    if not (
        ROOT
        / "scripts.js"
    ).exists():

        raise SystemExit(

            "ОШИБКА: "
            "запустите файл "
            "из корня washing-platform — "
            "scripts.js не найден."
        )


    build()
