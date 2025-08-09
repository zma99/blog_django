import { getCSRFToken, showAlert } from './utils.js';

const csrfToken = getCSRFToken();

// 🔍 Obtener y validar los elementos del comentario
function getCommentElements(id) {
  const contentEl = document.getElementById(`content-${id}`);
  const editEl = document.getElementById(`edit-${id}`);
  const saveEl = document.getElementById(`save-${id}`);
  const editedSpan = document.getElementById(`edited-${id}`);

  if (!contentEl || !editEl || !saveEl || !editedSpan) {
    console.warn(`Elementos del comentario ${id} no encontrados. Puede que haya sido eliminado.`);
    return null;
  }

  return { contentEl, editEl, saveEl, editedSpan };
}

// ✏️ Mostrar el textarea de edición
function toggleEdit(id) {
  const elements = getCommentElements(id);
  if (!elements) return;

  const { contentEl, editEl, saveEl } = elements;

  contentEl.style.display = 'none';
  editEl.style.display = 'block';
  saveEl.style.display = 'inline';
}

// 💾 Guardar el comentario editado
function saveEdit(id) {
  const editInput = document.getElementById(`edit-${id}`);
  if (!editInput) {
    console.warn(`Textarea de edición para ${id} no encontrado.`);
    return;
  }

  const content = editInput.value;

  fetch(`/posts/comment/${id}/edit/`, {
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
      const elements = getCommentElements(id);
      if (!elements) return;

      const { contentEl, editEl, saveEl, editedSpan } = elements;

      contentEl.innerText = data.content;
      contentEl.style.display = 'block';
      editEl.style.display = 'none';
      saveEl.style.display = 'none';

      editedSpan.textContent = `Editado: ${data.edited_at}`;
      editedSpan.classList.remove('hidden');
    } else {
      showAlert(data.error);
    }
  })
  .catch(error => {
    console.error("Error al editar el comentario:", error);
    showAlert("Hubo un problema al guardar el comentario.");
  });
}

// 🧠 Delegación de eventos
document.addEventListener('DOMContentLoaded', () => {
  const commentList = document.getElementById('comment-list');
  if (!commentList) return;

  commentList.addEventListener('click', (e) => {
    const editBtn = e.target.closest('.edit-btn');
    const saveBtn = e.target.closest('.save-btn');

    if (editBtn) {
      const id = editBtn.dataset.id;
      toggleEdit(id);
    }

    if (saveBtn) {
      const id = saveBtn.dataset.id;
      saveEdit(id);
    }
  });
});