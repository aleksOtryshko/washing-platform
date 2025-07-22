// scripts.js

function getLanguage() { return localStorage.getItem('lang') || (navigator.language.startsWith('ru') ? 'ru' : navigator.language.startsWith('en') ? 'en' : 'uk'); }

document.addEventListener('DOMContentLoaded', () => { const slides = document.querySelectorAll('.slide'); if (slides.length) { slides.forEach(slide => slide.style.transition = 'opacity 0.6s'); showSlide(0); startAutoSlide(); }

const slider = document.querySelector('#slider'); if (slider) { slider.addEventListener('mouseover', stopAutoSlide); slider.addEventListener('mouseout', startAutoSlide); } });

let currentSlideIndex = 0; let autoSlideTimer = null;

function showSlide(index) { const slides = document.querySelectorAll('.slide'); slides.forEach((slide, i) => { slide.style.display = i === index ? 'block' : 'none'; slide.style.opacity = i === index ? '1' : '0'; }); }

function nextSlide() { const slides = document.querySelectorAll('.slide'); currentSlideIndex = (currentSlideIndex + 1) % slides.length; showSlide(currentSlideIndex); }

function prevSlide() { const slides = document.querySelectorAll('.slide'); currentSlideIndex = (currentSlideIndex - 1 + slides.length) % slides.length; showSlide(currentSlideIndex); }

function startAutoSlide() { autoSlideTimer = setInterval(nextSlide, 5000); }

function stopAutoSlide() { clearInterval(autoSlideTimer); }

const form = document.getElementById('orderForm'); if (form) { const status = document.getElementById('status'); const loading = document.getElementById('loading'); const nameError = document.getElementById('nameError'); const phoneError = document.getElementById('phoneError');

form.addEventListener('submit', async (e) => { e.preventDefault();

const name = form.querySelector('input[name="name"]').value.trim();
const phone = form.querySelector('input[name="phone_number"]').value.trim();
const desc = form.querySelector('textarea[name="problem_description"]').value.trim();

nameError.textContent = '';
phoneError.textContent = '';
status.style.display = 'none';
status.className = '';
loading.style.display = 'block';

const lang = getLanguage();
const messages = {
  uk: {
    nameError: 'Ім’я не може перевищувати 50 символів.',
    phoneError: 'Введіть 10 цифр без +38.',
    loading: '⏳ Ваша заявка обробляється...',
    success: '✅ Заявка прийнята! Ми зателефонуємо найближчим часом.',
    error: '❌ Помилка надсилання. Спробуйте пізніше.'
  },
  ru: {
    nameError: 'Имя не может превышать 50 символов.',
    phoneError: 'Введите 10 цифр без +38.',
    loading: '⏳ Ваша заявка обрабатывается...',
    success: '✅ Заявка принята! Мы скоро свяжемся с вами.',
    error: '❌ Ошибка отправки. Повторите позже.'
  },
  en: {
    nameError: 'Name must be under 50 characters.',
    phoneError: 'Enter 10 digits without +38.',
    loading: '⏳ Your request is being processed...',
    success: '✅ Your request has been received!',
    error: '❌ Submission error. Please try again later.'
  }
};

const t = messages[lang];

if (name.length > 50) {
  nameError.textContent = t.nameError;
  loading.style.display = 'none';
  return;
}

if (!/^\d{10}$/.test(phone)) {
  phoneError.textContent = t.phoneError;
  loading.style.display = 'none';
  return;
}

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

  if (response.ok) {
    form.reset();
    status.textContent = t.success;
    status.className = 'success';
  } else {
    throw new Error();
  }
} catch {
  status.textContent = t.error;
  status.className = 'error-status';
} finally {
  loading.style.display = 'none';
  status.style.display = 'block';
}

}); }

