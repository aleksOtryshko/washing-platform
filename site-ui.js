(() => {
  'use strict';

  const PHONE =
    '+380671371673';

  /*
   * СЮДА ПОЗЖЕ ВСТАВИМ
   * ОТДЕЛЬНЫЙ Google Ads label
   * для конверсии "Клик по телефону".
   *
   * Например:
   *
   * AW-17465538794/AbCdEf123456
   *
   * Не вставляй сюда label формы.
   */
  const CALL_CONVERSION_SEND_TO =
    '';

  let lastFocusedElement =
    null;

  const modal =
    document.querySelector(
      '[data-order-modal]'
    );

  const modalPhone =
    modal?.querySelector(
      'input[name="phone_number"]'
    );

  const modalProblem =
    modal?.querySelector(
      'textarea[name="problem_description"]'
    );


  function sendEvent(
    name,
    params = {}
  ) {

    if (
      typeof window.gtag !==
      'function'
    ) {
      return;
    }

    window.gtag(
      'event',
      name,
      params
    );
  }


  function openOrderModal(
    trigger
  ) {

    if (!modal) {
      return;
    }

    lastFocusedElement =
      trigger ||
      document.activeElement;

    const problem =
      trigger?.dataset?.problem;

    if (
      problem &&
      modalProblem
    ) {
      modalProblem.value =
        problem;
    }

    modal.classList.add(
      'is-open'
    );

    modal.setAttribute(
      'aria-hidden',
      'false'
    );

    document.body.classList.add(
      'modal-open'
    );

    sendEvent(
      'order_modal_open',
      {
        page_path:
          window.location.pathname,

        selected_problem:
          problem || ''
      }
    );

    window.setTimeout(
      () => {
        modalPhone?.focus();
      },
      80
    );
  }


  function closeOrderModal() {

    if (!modal) {
      return;
    }

    modal.classList.remove(
      'is-open'
    );

    modal.setAttribute(
      'aria-hidden',
      'true'
    );

    document.body.classList.remove(
      'modal-open'
    );

    if (
      lastFocusedElement &&
      typeof lastFocusedElement.focus ===
      'function'
    ) {
      lastFocusedElement.focus();
    }
  }


  /*
   * Вызвать мастера
   */

  document.addEventListener(
    'click',
    (event) => {

      const trigger =
        event.target.closest(
          '.js-open-order'
        );

      if (trigger) {

        event.preventDefault();

        openOrderModal(
          trigger
        );

        return;
      }


      if (
        event.target.closest(
          '[data-modal-close]'
        )
      ) {

        event.preventDefault();

        closeOrderModal();
      }
    }
  );


  /*
   * Escape закрывает форму.
   */

  document.addEventListener(
    'keydown',
    (event) => {

      if (
        event.key ===
        'Escape'
      ) {

        closeOrderModal();
      }
    }
  );


  /*
   * Мобильное меню.
   */

  const menuButton =
    document.querySelector(
      '[data-menu-toggle]'
    );

  const menu =
    document.querySelector(
      '[data-menu]'
    );

  if (
    menuButton &&
    menu
  ) {

    menuButton.addEventListener(
      'click',
      () => {

        const open =
          menu.classList.toggle(
            'is-open'
          );

        menuButton.setAttribute(
          'aria-expanded',
          String(open)
        );
      }
    );


    menu.addEventListener(
      'click',
      (event) => {

        if (
          event.target.closest(
            'a'
          )
        ) {

          menu.classList.remove(
            'is-open'
          );

          menuButton.setAttribute(
            'aria-expanded',
            'false'
          );
        }
      }
    );
  }


  /*
   * Тень шапки после начала прокрутки.
   */

  const header =
    document.querySelector(
      '[data-header]'
    );

  function updateHeader() {

    if (!header) {
      return;
    }

    header.classList.toggle(
      'is-scrolled',
      window.scrollY > 8
    );
  }

  updateHeader();

  window.addEventListener(
    'scroll',
    updateHeader,
    {
      passive: true
    }
  );


  /*
   * Мягкое появление карточек.
   */

  const revealElements =
    document.querySelectorAll(
      '.reveal'
    );

  if (
    'IntersectionObserver'
    in window
  ) {

    const observer =
      new IntersectionObserver(
        (entries) => {

          entries.forEach(
            (entry) => {

              if (
                entry.isIntersecting
              ) {

                entry.target.classList.add(
                  'is-visible'
                );

                observer.unobserve(
                  entry.target
                );
              }
            }
          );
        },
        {
          threshold: 0.08
        }
      );

    revealElements.forEach(
      (element) => {
        observer.observe(
          element
        );
      }
    );

  } else {

    revealElements.forEach(
      (element) => {

        element.classList.add(
          'is-visible'
        );
      }
    );
  }


  /*
   * Поиск по прайс-листу.
   */

  const priceSearch =
    document.getElementById(
      'price-search'
    );

  const priceTable =
    document.querySelector(
      '[data-price-table]'
    );

  if (
    priceSearch &&
    priceTable
  ) {

    const rows =
      Array.from(
        priceTable.querySelectorAll(
          'tbody tr'
        )
      );

    priceSearch.addEventListener(
      'input',
      () => {

        const query =
          priceSearch.value
            .trim()
            .toLocaleLowerCase();

        rows.forEach(
          (row) => {

            const text =
              row.textContent
                .toLocaleLowerCase();

            row.classList.toggle(
              'is-hidden',
              query &&
              !text.includes(
                query
              )
            );
          }
        );
      }
    );
  }


  /*
   * Клики по номеру телефона.
   *
   * Всегда отправляем служебное
   * событие phone_click.
   *
   * Когда появится отдельный
   * Google Ads conversion label,
   * также отправляем conversion.
   */

  function continueCall(
    href
  ) {

    window.location.href =
      href;
  }


  document.addEventListener(
    'click',
    (event) => {

      const phoneLink =
        event.target.closest(
          'a[href^="tel:"]'
        );

      if (!phoneLink) {
        return;
      }

      const href =
        phoneLink.getAttribute(
          'href'
        ) ||
        `tel:${PHONE}`;

      sendEvent(
        'phone_click',
        {
          phone_number:
            PHONE,

          page_path:
            window.location.pathname
        }
      );


      /*
       * Если отдельная конверсия
       * Google Ads ещё не создана,
       * звонилка открывается сразу.
       */

      if (
        !CALL_CONVERSION_SEND_TO
      ) {
        return;
      }


      /*
       * После настройки label
       * на мгновение ждём отправки
       * конверсии и открываем телефон.
       */

      event.preventDefault();

      let opened =
        false;

      const openPhone =
        () => {

          if (opened) {
            return;
          }

          opened = true;

          continueCall(
            href
          );
        };


      if (
        typeof window.gtag ===
        'function'
      ) {

        window.gtag(
          'event',
          'conversion',
          {
            send_to:
              CALL_CONVERSION_SEND_TO,

            event_callback:
              openPhone
          }
        );

        window.setTimeout(
          openPhone,
          350
        );

      } else {

        openPhone();
      }
    },
    true
  );

})();
