document.addEventListener("DOMContentLoaded", () => {
  const coverInput = document.getElementById("id_cover");
  const previewImage = document.getElementById("cover-preview");
  const previewContainer = document.getElementById("cover-preview-container");

  if (!coverInput || !previewImage || !previewContainer) return;

  coverInput.addEventListener("change", () => {
    const file = coverInput.files[0];
    if (file && file.type.startsWith("image/")) {
      const reader = new FileReader();
      reader.onload = (e) => {
        previewImage.src = e.target.result;
        previewContainer.classList.remove("hidden");
      };
      reader.readAsDataURL(file);
    } else {
      previewImage.src = "";
      previewContainer.classList.add("hidden");
    }
  });
});