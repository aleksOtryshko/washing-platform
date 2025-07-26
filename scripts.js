// scripts.js

function getLanguage() {
  return localStorage.getItem('lang') ||
    (navigator.language.startsWith('ru') ? 'ru'
      : navigator.language.startsWith('en') ? 'en' : 'uk');
}

document.addEventListener('DOMContentLoaded', () => {
  const slides = document.querySelectorAll('.slide');
  if (slides.length) {
    slides.forEach(slide => slide.style.transition = 'opacity 0.6s');
    showSlide(0);
    startAutoSlide();
  }

  const slider = document.querySelector('#slider');
  if (slider) {
    slider.addEventListener('mouseover', stopAutoSlide);
    slider.addEventListener('mouseout', startAutoSlide);
  }
});

let currentSlideIndex = 0;
let autoSlideTimer = null;

function showSlide(index) {
  const slides = document.querySelectorAll('.slide');
  slides.forEach((slide, i) => {
    slide.style.display = i === index ? 'block' : 'none';
    slide.style.opacity = i === index ? '1' : '0';
  });
}

function nextSlide() {
  const slides = document.querySelectorAll('.slide');
  currentSlideIndex = (currentSlideIndex + 1) % slides.length;
  showSlide(currentSlideIndex);
}

function prevSlide() {
  const slides = document.querySelectorAll('.slide');
  currentSlideIndex = (currentSlideIndex - 1 + slides.length) % slides.length;
  showSlide(currentSlideIndex);
}

function startAutoSlide() {
  autoSlideTimer = setInterval(nextSlide, 5000);
}

function stopAutoSlide() {
  clearInterval(autoSlideTimer);
}

const form = document.getElementById('orderForm');
if (form) {
  const nameError = document.getElementById('nameError');
  const phoneError = document.getElementById('phoneError');

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

  const modal = document.createElement('div');
  modal.id = 'modal';
  modal.style.cssText = `
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 10000;
  `;
  const box = document.createElement('div');
  box.style.cssText = `
    background: #fff;
    padding: 30px 20px;
    border-radius: 8px;
    font-size: 1.1em;
    text-align: center;
    box-shadow: 0 0 10px rgba(0,0,0,0.3);
    max-width: 300px;
  `;
  box.innerHTML = '<div class="spinner"></div><p id="modalText">' + messages[lang].processing + '</p>';
  modal.appendChild(box);

  const spinner = document.createElement('style');
  spinner.innerHTML = `
    .spinner {
      border: 4px solid #f3f3f3;
      border-top: 4px solid #3498db;
      border-radius: 50%;
      width: 40px;
      height: 40px;
      animation: spin 1s linear infinite;
      margin: 0 auto 15px;
    }
    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
  `;
  document.head.appendChild(spinner);

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const name = form.querySelector('input[name="name"]').value.trim();
    const phone = form.querySelector('input[name="phone_number"]').value.trim();
    const desc = form.querySelector('textarea[name="problem_description"]').value.trim();

    nameError.textContent = '';
    phoneError.textContent = '';

    if (name.length > 50) {
      nameError.textContent = messages[lang].nameError;
      return;
    }

    if (!/^\d{10}$/.test(phone)) {
      phoneError.textContent = messages[lang].phoneError;
      return;
    }

    document.body.appendChild(modal);

    const data = {
      name,
      phone_number: '+38' + phone,
      problem_description: desc
    };

    try {
      const response = await fetch('https://washing-platform.onrender.com/api/orders', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      });

      const text = document.getElementById('modalText');
      if (response.ok) {
        form.reset();
        text.textContent = messages[lang].success;
        setTimeout(() => window.location.reload(), 3000);
      } else {
        throw new Error();
      }
    } catch {
      const text = document.getElementById('modalText');
      text.textContent = messages[lang].error;
      setTimeout(() => modal.remove(), 4000);
    }
  });
}
