document.addEventListener("DOMContentLoaded", function () {
  const avatarInput = document.getElementById("id_avatar");
  const preview = document.getElementById("avatar-preview");

  if (avatarInput && preview) {
    avatarInput.addEventListener("change", function () {
      const file = this.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
          preview.src = e.target.result;
          preview.classList.remove("hidden");
        };
        reader.readAsDataURL(file);
      } else {
        preview.src = "#";
        preview.classList.add("hidden");
      }
    });
  }
});