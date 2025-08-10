document.addEventListener("DOMContentLoaded", () => {
  // Menú hamburguesa
  const mobileMenuButton = document.getElementById("mobile-menu-button");
  const mobileMenu = document.getElementById("mobile-menu");

  if (mobileMenuButton && mobileMenu) {
    mobileMenuButton.addEventListener("click", () => {
      console.log("Botón hamburguesa clickeado");
      mobileMenu.classList.toggle("hidden");
    });

    document.addEventListener("click", (e) => {
      if (!mobileMenu.contains(e.target) && !mobileMenuButton.contains(e.target)) {
        mobileMenu.classList.add("hidden");
      }
    });
  } else {
    console.warn("No se encontró el botón o el menú hamburguesa");
  }

  // Menú de usuario
  const userButton = document.getElementById("user-menu-button");
  const userMenu = document.getElementById("user-menu");
  const userContainer = document.getElementById("user-menu-container");

  if (userButton && userMenu && userContainer) {
    userButton.addEventListener("click", () => {
      userMenu.classList.toggle("hidden");
    });

    document.addEventListener("click", (e) => {
      if (!userContainer.contains(e.target)) {
        userMenu.classList.add("hidden");
      }
    });
  }

  // Menú de categorías
  const categoryButton = document.getElementById("category-menu-button");
  const categoryMenu = document.getElementById("category-menu");
  const categoryContainer = document.getElementById("category-menu-container");

  if (categoryButton && categoryMenu && categoryContainer) {
    categoryButton.addEventListener("click", () => {
      categoryMenu.classList.toggle("hidden");
    });

    document.addEventListener("click", (e) => {
      if (!categoryContainer.contains(e.target)) {
        categoryMenu.classList.add("hidden");
      }
    });
  }
});