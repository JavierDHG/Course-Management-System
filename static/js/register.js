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
function togglePassword(fieldId, iconId) {
  const passwordField = document.getElementById(fieldId);
  const toggleIcon = document.getElementById(iconId);

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

// Verificación de coincidencia de contraseñas
document
  .getElementById("confirm_password")
  .addEventListener("input", function () {
    const password = document.getElementById("password").value;
    const passwordConfirm = this.value;

    if (password && password !== passwordConfirm) {
      this.setCustomValidity("Las contraseñas no coinciden");
    } else {
      this.setCustomValidity("");
    }
  });

// Medidor de fortaleza de contraseña
document.getElementById("password").addEventListener("input", function () {
  const password = this.value;
  const strengthBar = document.getElementById("password-strength");
  const strengthText = document.getElementById("password-strength-text");

  // Criterios de fortaleza
  const hasLowerCase = /[a-z]/.test(password);
  const hasUpperCase = /[A-Z]/.test(password);
  const hasNumber = /\d/.test(password);
  const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(password);
  const isLongEnough = password.length >= 8;

  // Calcular puntuación (0-100)
  let score = 0;
  if (hasLowerCase) score += 20;
  if (hasUpperCase) score += 20;
  if (hasNumber) score += 20;
  if (hasSpecialChar) score += 20;
  if (isLongEnough) score += 20;

  // Actualizar barra de progreso
  strengthBar.style.width = score + "%";

  // Actualizar clase de color
  if (score < 40) {
    strengthBar.className = "progress-bar bg-danger";
    strengthText.textContent = "Contraseña débil";
  } else if (score < 80) {
    strengthBar.className = "progress-bar bg-warning";
    strengthText.textContent = "Contraseña media";
  } else {
    strengthBar.className = "progress-bar bg-success";
    strengthText.textContent = "Contraseña fuerte";
  }
});

// Animación de carga en el botón de envío
document.querySelector("form").addEventListener("submit", function () {
  const submitBtn = this.querySelector('button[type="submit"]');
  const originalText = submitBtn.innerHTML;
  submitBtn.innerHTML =
    '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>Creando cuenta...';
  submitBtn.disabled = true;

  // Restaurar el botón si hay errores (esto se puede manejar mejor con AJAX)
  setTimeout(() => {
    submitBtn.innerHTML = originalText;
    submitBtn.disabled = false;
  }, 3000);
});
