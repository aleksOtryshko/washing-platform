const ORDER_API_URL = 'https://washing-platform.onrender.com/api/orders';
const ORDER_REQUEST_TIMEOUT_MS = 120000;

let modalCloseTimer = null;

function getLanguage() {
  const lang =
    window.pageLang ||
    document.documentElement.lang ||
    'ru';

  return String(lang)
    .toLowerCase()
    .split('-')[0];
}

function getMessages() {
  const lang = getLanguage();

  const messages = {
    ru: {
      nameError: 'Имя не может превышать 50 символов.',
      phoneError: 'Введите 10 цифр номера без +38, начиная с 0.',
      processing: '⏳ Ваша заявка обрабатывается...',
      success: '✅ Заявка принята! Мастер скоро свяжется с вами.',
      serverError: '❌ Сервер не принял заявку. Попробуйте ещё раз через пару минут.',
      networkError: '❌ Не удалось связаться с сервером. Проверьте интернет и попробуйте ещё раз.',
      timeoutError: '❌ Сервер отвечает слишком долго. Попробуйте ещё раз через пару минут.'
    },

    uk: {
      nameError: 'Ім’я не може перевищувати 50 символів.',
      phoneError: 'Введіть 10 цифр номера без +38, починаючи з 0.',
      processing: '⏳ Ваша заявка обробляється...',
      success: '✅ Заявку прийнято! Майстер скоро зв’яжеться з вами.',
      serverError: '❌ Сервер не прийняв заявку. Спробуйте ще раз через кілька хвилин.',
      networkError: '❌ Не вдалося зв’язатися із сервером. Перевірте інтернет і спробуйте ще раз.',
      timeoutError: '❌ Сервер відповідає надто довго. Спробуйте ще раз через кілька хвилин.'
    },

    en: {
      nameError: 'Name must be under 50 characters.',
      phoneError: 'Enter 10 phone digits without +38, starting with 0.',
      processing: '⏳ Processing your request...',
      success: '✅ Request received! We will contact you soon.',
      serverError: '❌ The server did not accept the request. Please try again in a few minutes.',
      networkError: '❌ Could not connect to the server. Check your internet connection and try again.',
      timeoutError: '❌ The server is taking too long to respond. Please try again in a few minutes.'
    }
  };

  return messages[lang] || messages.ru;
}

function addSpinnerStyles() {
  if (document.getElementById('spinnerStyles')) {
    return;
  }

  const style = document.createElement('style');

  style.id = 'spinnerStyles';

  style.textContent = `
    #modal {
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.55);
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 10000;
      padding: 20px;
    }

    #modal .order-modal-box {
      background: #ffffff;
      padding: 28px 22px;
      border-radius: 18px;
      font-size: 1.05rem;
      text-align: center;
      box-shadow: 0 20px 60px rgba(15, 23, 42, 0.25);
      max-width: 360px;
      width: 100%;
      color: #0f172a;
    }

    #modal .spinner {
      border: 4px solid #f1f5f9;
      border-top: 4px solid #0b75d1;
      border-radius: 50%;
      width: 42px;
      height: 42px;
      animation: orderSpin 1s linear infinite;
      margin: 0 auto 15px;
    }

    #modal .spinner.is-hidden {
      display: none;
    }

    @keyframes orderSpin {
      0% {
        transform: rotate(0deg);
      }

      100% {
        transform: rotate(360deg);
      }
    }
  `;

  document.head.appendChild(style);
}

function showModal(message, isLoading = false) {
  addSpinnerStyles();

  if (modalCloseTimer) {
    clearTimeout(modalCloseTimer);
    modalCloseTimer = null;
  }

  let modal = document.getElementById('modal');

  if (!modal) {
    modal = document.createElement('div');

    modal.id = 'modal';
    modal.setAttribute('role', 'status');
    modal.setAttribute('aria-live', 'polite');

    const box = document.createElement('div');
    box.className = 'order-modal-box';

    const spinner = document.createElement('div');
    spinner.className = 'spinner';
    spinner.setAttribute('aria-hidden', 'true');

    const text = document.createElement('div');
    text.id = 'modalText';

    box.appendChild(spinner);
    box.appendChild(text);
    modal.appendChild(box);
    document.body.appendChild(modal);
  }

  const spinner = modal.querySelector('.spinner');
  const text = modal.querySelector('#modalText');

  if (spinner) {
    spinner.classList.toggle('is-hidden', !isLoading);
  }

  if (text) {
    text.textContent = message;
  }
}

function closeModalLater(delay) {
  if (modalCloseTimer) {
    clearTimeout(modalCloseTimer);
  }

  modalCloseTimer = setTimeout(() => {
    const modal = document.getElementById('modal');

    if (modal) {
      modal.remove();
    }

    modalCloseTimer = null;
  }, delay);
}

function setFormSubmitting(form, isSubmitting) {
  const submitControls = form.querySelectorAll(
    'button[type="submit"], input[type="submit"]'
  );

  submitControls.forEach((control) => {
    control.disabled = isSubmitting;
  });
}

function normalizeLocalPhone(phoneRaw) {
  const digits = phoneRaw.replace(/\D/g, '');

  if (/^0\d{9}$/.test(digits)) {
    return digits;
  }

  if (/^380\d{9}$/.test(digits)) {
    return '0' + digits.slice(3);
  }

  return null;
}

async function readResponseBody(response) {
  const text = await response.text();

  if (!text) {
    return null;
  }

  try {
    return JSON.parse(text);
  } catch {
    return text;
  }
}

function createHttpError(response, responseBody) {
  const error = new Error(
    `Order request failed with HTTP ${response.status}`
  );

  error.name = 'OrderHttpError';
  error.status = response.status;
  error.statusText = response.statusText;
  error.responseBody = responseBody;

  return error;
}

function initOrderForms() {
  const forms = document.querySelectorAll('.orderForm');

  if (!forms.length) {
    return;
  }

  const messages = getMessages();

  forms.forEach((form) => {
    if (form.dataset.orderFormInitialized === 'true') {
      return;
    }

    form.dataset.orderFormInitialized = 'true';

    form.addEventListener('submit', async (event) => {
      event.preventDefault();

      const nameInput = form.querySelector(
        'input[name="name"]'
      );

      const phoneInput = form.querySelector(
        'input[name="phone_number"]'
      );

      const descInput = form.querySelector(
        'textarea[name="problem_description"]'
      );

      const nameError = form.querySelector('.nameError');
      const phoneError = form.querySelector('.phoneError');

      const name = nameInput
        ? nameInput.value.trim()
        : '';

      const phoneRaw = phoneInput
        ? phoneInput.value.trim()
        : '';

      const desc = descInput
        ? descInput.value.trim()
        : '';

      if (nameError) {
        nameError.textContent = '';
      }

      if (phoneError) {
        phoneError.textContent = '';
      }

      if (name.length > 50) {
        if (nameError) {
          nameError.textContent = messages.nameError;
        }

        if (nameInput) {
          nameInput.focus();
        }

        return;
      }

      const localPhone = normalizeLocalPhone(phoneRaw);

      if (!localPhone) {
        if (phoneError) {
          phoneError.textContent = messages.phoneError;
        }

        if (phoneInput) {
          phoneInput.focus();
        }

        return;
      }

      const data = {
        name: name,
        phone_number: `+38${localPhone}`,
        problem_description: desc
      };

      const controller = new AbortController();

      const timeoutId = setTimeout(() => {
        controller.abort();
      }, ORDER_REQUEST_TIMEOUT_MS);

      setFormSubmitting(form, true);

      showModal(
        messages.processing,
        true
      );

      try {
        const response = await fetch(
          ORDER_API_URL,
          {
            method: 'POST',

            headers: {
              'Content-Type': 'application/json',
              'Accept': 'application/json'
            },

            body: JSON.stringify(data),

            signal: controller.signal
          }
        );

        const responseBody =
          await readResponseBody(response);

        if (!response.ok) {
          throw createHttpError(
            response,
            responseBody
          );
        }

        console.info(
          'Order successfully sent:',
          {
            status: response.status,
            response: responseBody
          }
        );

        form.reset();

        showModal(
          messages.success,
          false
        );

        closeModalLater(3000);

      } catch (error) {

        if (
          error &&
          error.name === 'AbortError'
        ) {
          console.error(
            'Order form timeout:',
            error
          );

          showModal(
            messages.timeoutError,
            false
          );

        } else if (
          error &&
          error.name === 'OrderHttpError'
        ) {
          console.error(
            'Order form server error:',
            {
              status: error.status,
              statusText: error.statusText,
              response: error.responseBody
            }
          );

          showModal(
            messages.serverError,
            false
          );

        } else {
          console.error(
            'Order form network/fetch error:',
            error
          );

          showModal(
            messages.networkError,
            false
          );
        }

        closeModalLater(5000);

      } finally {
        clearTimeout(timeoutId);

        setFormSubmitting(
          form,
          false
        );
      }
    });
  });
}

if (document.readyState === 'loading') {
  document.addEventListener(
    'DOMContentLoaded',
    initOrderForms,
    {
      once: true
    }
  );

} else {
  initOrderForms();
}
