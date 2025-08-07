function getLanguage() {
  return window.pageLang || 'uk';
}

document.addEventListener('DOMContentLoaded', () => {
  const lang = getLanguage();
  const messages = {
    uk: {
      nameError: 'Ім’я не може перевищувати 50 символів.',
      phoneError: 'Введіть 10 цифр без +38.',
      processing: '⏳ Ваша заявка обробляється...',
      success: '✅ Заявку прийнято! Ми скоро зв’яжемося з вами.',
      error: '❌ Помилка. Повторіть спробу через кілька хвилин.'
    },
    ru: {
      nameError: 'Имя не может превышать 50 символов.',
      phoneError: 'Введите 10 цифр без +38.',
      processing: '⏳ Ваша заявка обрабатывается...',
      success: '✅ Заявка принята! Мы скоро свяжемся с вами.',
      error: '❌ Ошибка. Повторите попытку через пару минут.'
    },
    en: {
      nameError: 'Name must be under 50 characters.',
      phoneError: 'Enter 10 digits without +38.',
      processing: '⏳ Processing your request...',
      success: '✅ Request received! We’ll contact you soon.',
      error: '❌ Error. Please try again in a few minutes.'
    }
  };

  const form = document.getElementById('orderForm');
  if (!form) return;

  const nameError = document.getElementById('nameError');
  const phoneError = document.getElementById('phoneError');

  const notify = (text, type = 'info') => {
    const box = document.createElement('div');
    box.textContent = text;
    box.style.cssText = `
      position: fixed;
      top: 20px;
      right: 20px;
      background: ${type === 'error' ? '#ff4d4d' : type === 'success' ? '#4caf50' : '#2196f3'};
      color: white;
      padding: 12px 18px;
      font-size: 16px;
      border-radius: 6px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.2);
      z-index: 9999;
      animation: fadeout 0.3s ease-in-out 3s forwards;
    `;
    document.body.appendChild(box);
    setTimeout(() => box.remove(), 4000);
  };

  const style = document.createElement('style');
  style.innerHTML = `
    @keyframes fadeout {
      to {
        opacity: 0;
        transform: translateY(-10px);
      }
    }
  `;
  document.head.appendChild(style);

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const name = form.querySelector('input[name="name"]').value.trim();
    const phone = form.querySelector('input[name="phone_number"]').value.trim();
    const desc = form.querySelector('textarea[name="problem_description"]').value.trim();

    nameError.textContent = '';
    phoneError.textContent = '';

    if (name.length > 50) {
      nameError.textContent = messages[lang].nameError;
      notify(messages[lang].nameError, 'error');
      return;
    }

    if (!/^\d{10}$/.test(phone)) {
      phoneError.textContent = messages[lang].phoneError;
      notify(messages[lang].phoneError, 'error');
      return;
    }

    notify(messages[lang].processing, 'info');

    try {
      const response = await fetch('https://washing-platform.onrender.com/api/orders', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name,
          phone_number: '+38' + phone,
          problem_description: desc
        })
      });

      if (response.ok) {
        notify(messages[lang].success, 'success');
        form.reset();
      } else {
        const errText = await response.text();
        notify(messages[lang].error + `\n${errText}`, 'error');
        console.error('Ошибка сервера:', errText);
      }
    } catch (err) {
      notify(messages[lang].error + `\n${err.message}`, 'error');
      console.error('Ошибка отправки:', err);
    }
  });
});
