function getLanguage() {
  return window.pageLang || document.documentElement.lang || 'ru';
}

function getMessages() {
  const lang = getLanguage();

  const messages = {
    ru: {
      nameError: 'Имя не может превышать 50 символов.',
      phoneError: 'Введите 10 цифр без +38.',
      processing: '⏳ Ваша заявка обрабатывается...',
      success: '✅ Заявка принята! Мастер скоро свяжется с вами.',
      error: '❌ Ошибка. Повторите попытку через пару минут.'
    },
    uk: {
      nameError: 'Ім’я не може перевищувати 50 символів.',
      phoneError: 'Введіть 10 цифр без +38.',
      processing: '⏳ Ваша заявка обробляється...',
      success: '✅ Заявку прийнято! Майстер скоро зв’яжеться з вами.',
      error: '❌ Помилка. Повторіть спробу через кілька хвилин.'
    },
    en: {
      nameError: 'Name must be under 50 characters.',
      phoneError: 'Enter 10 digits without +38.',
      processing: '⏳ Processing your request...',
      success: '✅ Request received! We will contact you soon.',
      error: '❌ Error. Please try again in a few minutes.'
    }
  };

  return messages[lang] || messages.ru;
}

function showModal(message) {
  let modal = document.getElementById('modal');

  if (!modal) {
    modal = document.createElement('div');
    modal.id = 'modal';
    modal.style.cssText = `
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.55);
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 10000;
      padding: 20px;
    `;

    const box = document.createElement('div');
    box.style.cssText = `
      background: #fff;
      padding: 28px 22px;
      border-radius: 18px;
      font-size: 1.05rem;
      text-align: center;
      box-shadow: 0 20px 60px rgba(15, 23, 42, 0.25);
      max-width: 360px;
      width: 100%;
    `;

    box.innerHTML = `
      <div class="spinner"></div>
      <div id="modalText"></div>
    `;

    modal.appendChild(box);
    document.body.appendChild(modal);
  }

  const text = document.getElementById('modalText');
  if (text) {
    text.textContent = message;
  }
}

function closeModalLater(delay) {
  setTimeout(() => {
    const modal = document.getElementById('modal');
    if (modal) {
      modal.remove();
    }
  }, delay);
}

function addSpinnerStyles() {
  if (document.getElementById('spinnerStyles')) {
    return;
  }

  const spinner = document.createElement('style');
  spinner.id = 'spinnerStyles';
  spinner.innerHTML = `
    .spinner {
      border: 4px solid #f1f5f9;
      border-top: 4px solid #0b75d1;
      border-radius: 50%;
      width: 42px;
      height: 42px;
      animation: spin 1s linear infinite;
      margin: 0 auto 15px;
    }

    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
  `;
  document.head.appendChild(spinner);
}

function initOrderForms() {
  const forms = document.querySelectorAll('.orderForm');

  if (!forms.length) {
    return;
  }

  const messages = getMessages();
  addSpinnerStyles();

  forms.forEach((form) => {
    form.addEventListener('submit', async (event) => {
      event.preventDefault();

      const nameInput = form.querySelector('input[name="name"]');
      const phoneInput = form.querySelector('input[name="phone_number"]');
      const descInput = form.querySelector('textarea[name="problem_description"]');

      const nameError = form.querySelector('.nameError');
      const phoneError = form.querySelector('.phoneError');

      const name = nameInput ? nameInput.value.trim() : '';
      const phone = phoneInput ? phoneInput.value.trim() : '';
      const desc = descInput ? descInput.value.trim() : '';

      if (nameError) nameError.textContent = '';
      if (phoneError) phoneError.textContent = '';

      if (name.length > 50) {
        if (nameError) nameError.textContent = messages.nameError;
        return;
      }

      if (!/^\\d{10}$/.test(phone)) {
        if (phoneError) phoneError.textContent = messages.phoneError;
        return;
      }

      showModal(messages.processing);

      const data = {
        name: name,
        phone_number: '+38' + phone,
        problem_description: desc
      };

      try {
        const response = await fetch('https://washing-platform.onrender.com/api/orders', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
        });

        if (!response.ok) {
          throw new Error('Request failed');
        }

        form.reset();
        showModal(messages.success);
        closeModalLater(3000);
      } catch (error) {
        showModal(messages.error);
        closeModalLater(4000);
      }
    });
  });
}

document.addEventListener('DOMContentLoaded', initOrderForms);
