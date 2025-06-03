// Validación de formulario
(function () {
  "use strict";
  var forms = document.querySelectorAll(".needs-validation");
  Array.prototype.slice.call(forms).forEach(function (form) {
    form.addEventListener(
      "submit",
      function (event) {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add("was-validated");
      },
      false
    );
  });
})();

// Toggle para mostrar/ocultar contraseña
function togglePassword() {
  const passwordField = document.getElementById("password");
  const toggleIcon = document.getElementById("togglePasswordIcon");

  if (passwordField.type === "password") {
    passwordField.type = "text";
    toggleIcon.classList.remove("bi-eye");
    toggleIcon.classList.add("bi-eye-slash");
  } else {
    passwordField.type = "password";
    toggleIcon.classList.remove("bi-eye-slash");
    toggleIcon.classList.add("bi-eye");
  }
}

// Auto-focus en el primer campo
document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("email").focus();
});

// Animación de carga en el botón de envío
document.querySelector("form").addEventListener("submit", function () {
  const submitBtn = this.querySelector('button[type="submit"]');
  const originalText = submitBtn.innerHTML;
  submitBtn.innerHTML =
    '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>Iniciando sesión...';
  submitBtn.disabled = true;

  // Restaurar el botón si hay errores (esto se puede manejar mejor con AJAX)
  setTimeout(() => {
    submitBtn.innerHTML = originalText;
    submitBtn.disabled = false;
  }, 3000);
});
