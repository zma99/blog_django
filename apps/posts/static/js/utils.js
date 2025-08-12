// 🔐 Obtener el token CSRF desde la cookie
export function getCSRFToken() {
  const name = 'csrftoken';
  const cookies = document.cookie.split(';');
  for (let cookie of cookies) {
    cookie = cookie.trim();
    if (cookie.startsWith(name + '=')) {
      return decodeURIComponent(cookie.slice(name.length + 1));
    }
  }
  return null;
}

// 🧼 Fade out y remover elemento (usando Tailwind)
export function fadeOutAndRemove(element, duration = 300) {
  if (!element) return;
  element.classList.add('opacity-0', 'transition-opacity', `duration-${duration}`);
  setTimeout(() => element.remove(), duration);
}

// 📣 Mostrar alerta visual (puede integrarse con tu sistema de mensajes)
export function showAlert(message, type = 'error') {
  alert(message); // Podés reemplazar esto por un toast visual si tenés uno
}

// 🧠 Confirmación con fallback
export function confirmAction(message = "¿Estás seguro?") {
  return window.confirm(message);
}

// 🧪 Verificar si un elemento existe
export function exists(selector) {
  return document.querySelector(selector) !== null;
}