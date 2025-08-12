// session-timeout.js

(() => {
  const isAuthenticated = document.body.dataset.authenticated === 'true';
  if (!isAuthenticated) return;

  const TIMEOUT_MINUTES = 15;
  const WARNING_MINUTES = 2;
  const TIMEOUT_MS = TIMEOUT_MINUTES * 60 * 1000;
  const WARNING_MS = WARNING_MINUTES * 60 * 1000;

  let timeoutId, warningId;
  const warningEl = document.getElementById('session-warning');

  const logoutUser = async () => {
    try {
      await fetch('auth/logout/', {
        method: 'POST',
        headers: {
          'X-CSRFToken': getCookie('csrftoken'),
          'Content-Type': 'application/json',
        },
        credentials: 'include',
      });
      window.location.reload(); // O redirigir a login si preferís
    } catch (error) {
      console.error('Error al cerrar sesión:', error);
    }
  };

  const getCookie = name => {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    return parts.length === 2 ? parts.pop().split(';').shift() : '';
  };

  const showWarning = () => {
    if (warningEl) warningEl.classList.remove('hidden');
  };

  const hideWarning = () => {
    if (warningEl) warningEl.classList.add('hidden');
  };

  const resetTimers = () => {
    clearTimeout(timeoutId);
    clearTimeout(warningId);
    hideWarning();

    warningId = setTimeout(showWarning, TIMEOUT_MS - WARNING_MS);
    timeoutId = setTimeout(logoutUser, TIMEOUT_MS);
  };

  ['click', 'mousemove', 'keydown', 'scroll'].forEach(event => {
    document.addEventListener(event, resetTimers);
  });

  resetTimers();
})();