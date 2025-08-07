// 🔐 Obtener el token CSRF desde la cookie
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}


document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('comment-form');
  const commentList = document.getElementById('comment-list');

  if (!form || !commentList) return; // Evita errores si no existen

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    const contentInput = form.querySelector('textarea');
    const content = contentInput.value;

    if (!content.trim()) {
      alert("El comentario no puede estar vacío.");
      return;
    }

    const postId = form.dataset.postId;

    fetch(`/posts/comment/${postId}/create/`, {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrfToken,
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: `content=${encodeURIComponent(content)}`
    })
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      if (data.success) {
        commentList.insertAdjacentHTML('afterbegin', data.html);
        contentInput.value = '';
        const newComment = document.getElementById(`comment-${data.comment_id}`);
        if (newComment) {
          newComment.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      } else {
        alert(data.error);
      }
    })
    .catch(error => {
      console.error("Error al enviar el comentario:", error);
      alert("Hubo un problema al enviar el comentario.");
    });
  });
});