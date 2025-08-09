import { getCSRFToken, showAlert } from './utils.js';

const csrfToken = getCSRFToken();

document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('comment-form');
  const commentList = document.getElementById('comment-list');

  if (!form || !commentList) return;

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    const contentInput = form.querySelector('textarea');
    const content = contentInput.value;

    if (!content.trim()) {
      showAlert("El comentario no puede estar vacío.");
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
      if (!response.ok) throw new Error(`HTTP error ${response.status}`);
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
        showAlert(data.error);
      }
    })
    .catch(error => {
      console.error("Error al enviar el comentario:", error);
      showAlert("Hubo un problema al enviar el comentario.");
    });
  });
});