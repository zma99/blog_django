document.addEventListener("DOMContentLoaded", function () {
    function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  const likeButtons = document.querySelectorAll("#like-button");
  console.log("Likebtn:", likeButtons)

  likeButtons.forEach(likeBtn => {
    const postId = likeBtn.dataset.postId;
    if (!postId) return;

    const csrftoken = getCookie("csrftoken");

    likeBtn.addEventListener("click", function (e) {
      e.preventDefault();

      fetch(`/posts/${postId}/like/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrftoken
        },
        body: JSON.stringify({})
      })
      .then(response => {
        if (!response.ok) throw new Error("Error en la petición");
        return response.json();
      })
      .then(data => {
        if (data.liked) {
          likeBtn.classList.replace("bg-green-500", "bg-red-500");
          likeBtn.textContent = `👎 Quitar Me gusta (${data.likes_count})`;
        } else {
          likeBtn.classList.replace("bg-red-500", "bg-green-500");
          likeBtn.textContent = `👍 Me gusta (${data.likes_count})`;
        }
      })
      .catch(error => {
        console.error("Error en la petición:", error);
      });
    });
  });

  
});