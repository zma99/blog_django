// comment_edit.js

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

const csrfToken = getCookie('csrftoken');

// ✏️ Mostrar el textarea de edición
function toggleEdit(id) {
  document.getElementById(`content-${id}`).style.display = 'none';
  document.getElementById(`edit-${id}`).style.display = 'block';
  document.getElementById(`save-${id}`).style.display = 'inline';
}

// 💾 Guardar el comentario editado
function saveEdit(id) {
  const content = document.getElementById(`edit-${id}`).value;

  fetch(`/posts/comment/${id}/edit/`, {
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
      // Actualizar contenido
      document.getElementById(`content-${id}`).innerText = data.content;
      document.getElementById(`content-${id}`).style.display = 'block';
      document.getElementById(`edit-${id}`).style.display = 'none';
      document.getElementById(`save-${id}`).style.display = 'none';

      // Mostrar y actualizar el mensaje de "Editado"
      const editedSpan = document.getElementById(`edited-${id}`);
      editedSpan.textContent = `Editado: ${data.edited_at}`;  // 👈 actualiza la fecha
      editedSpan.classList.remove('hidden');                  // 👈 lo muestra
    } else {
      alert(data.error);
    }
  })
  .catch(error => {
    console.error("Error al editar el comentario:", error);
    alert("Hubo un problema al guardar el comentario.");
  });
}

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