import { getCSRFToken, fadeOutAndRemove, showAlert, confirmAction } from './utils.js';

const csrfToken = getCSRFToken();

// 🗑️ Eliminar comentario
function deleteComment(id) {
  fetch('/posts/comment/delete/', {
    method: 'POST',
    headers: {
      'X-CSRFToken': csrfToken,
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: `id=${id}`
  })
  .then(response => {
    if (!response.ok) throw new Error(`HTTP error ${response.status}`);
    return response.json();
  })
  .then(data => {
    if (data.success) {
      const commentElement = document.getElementById(`comment-${id}`);
      fadeOutAndRemove(commentElement);
    } else {
      showAlert(data.error || 'No se pudo eliminar el comentario.');
    }
  })
  .catch(error => {
    console.error("Error al eliminar el comentario:", error);
    showAlert("Hubo un problema al eliminar el comentario.");
  });
}

document.addEventListener('DOMContentLoaded', () => {
  const commentList = document.getElementById('comment-list');
  if (!commentList) return;

  commentList.addEventListener('click', (e) => {
    const deleteBtn = e.target.closest('[id^="delete-"]');
    if (deleteBtn) {
      e.stopPropagation(); // ⛔ Detiene que el clic active otros handlers
      const id = deleteBtn.dataset.id;
      if (confirmAction("¿Estás seguro de que querés eliminar este comentario?")) {
        deleteComment(id);
      }
    }
  });
});