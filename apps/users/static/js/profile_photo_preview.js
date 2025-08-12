document.addEventListener('DOMContentLoaded', () => {
  const avatarInput = document.getElementById('id_avatar');
  console.log(avatarInput)
  const avatarPreview = document.getElementById('avatar-preview');
  console.log(avatarPreview)
  const discardButton = document.getElementById('discard-avatar');
  console.log(discardButton)

  const originalSrc = avatarPreview?.src;

  if (avatarInput && avatarPreview && discardButton) {
    avatarInput.addEventListener('change', (event) => {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          avatarPreview.src = e.target.result;
          discardButton.classList.remove('hidden'); // mostrar botón
          console.log(discardButton)
        };
        reader.readAsDataURL(file);
      }
    });

    discardButton.addEventListener('click', () => {
      avatarInput.value = ''; // limpiar input
      avatarPreview.src = originalSrc; // restaurar imagen original
      discardButton.classList.add('hidden'); // ocultar botón
    });
  }
});