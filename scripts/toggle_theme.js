document.addEventListener("DOMContentLoaded", function () {
  const toggleButton = document.getElementById("theme-toggle");
  const themeIcon = document.getElementById("theme-icon");
  const body = document.body;

  toggleButton.addEventListener("click", () => {
    body.classList.toggle("dark-theme");
    // Cambiar el ícono según el tema actual
    if (body.classList.contains("dark-theme")) {
      themeIcon.src = "./icons/moon-face.svg"; // Cambia a ícono de luna
      themeIcon.alt = "Icono de luna";
    } else {
      themeIcon.src = "./icons/sun-face.svg"; // Cambia a ícono de sol
      themeIcon.alt = "Icono de sol";
    }
  });
});
