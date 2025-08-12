import { showAlert } from './utils.js';

document.addEventListener("DOMContentLoaded", () => {
  const loadMoreBtn = document.getElementById("load-more");
  if (!loadMoreBtn) return;

  loadMoreBtn.addEventListener("click", () => {
    const nextPage = loadMoreBtn.dataset.next;

    fetch(`?page=${nextPage}`)
      .then(response => {
        if (!response.ok) throw new Error(`HTTP error ${response.status}`);
        return response.text();
      })
      .then(html => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, "text/html");
        const newComments = doc.querySelectorAll("#comment-list li");
        const commentList = document.getElementById("comment-list");

        newComments.forEach(comment => commentList.appendChild(comment));

        const nextButton = doc.getElementById("load-more");
        if (nextButton) {
          loadMoreBtn.dataset.next = nextButton.dataset.next;
        } else {
          loadMoreBtn.remove(); // Ya no hay más comentarios
        }
      })
      .catch(error => {
        console.error("Error al cargar más comentarios:", error);
        showAlert("No se pudieron cargar más comentarios.");
      });
  });
});