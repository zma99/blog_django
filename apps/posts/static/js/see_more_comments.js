document.addEventListener("DOMContentLoaded", () => {
  const loadMoreBtn = document.getElementById("load-more");
  if (!loadMoreBtn) return;

  loadMoreBtn.addEventListener("click", () => {
    const nextPage = loadMoreBtn.dataset.next;
    fetch(`?page=${nextPage}`)
      .then(response => response.text())
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
      });
  });
});
