document.addEventListener("DOMContentLoaded", function () {
  // Card number formatting
  const cardNumberInput = document.getElementById("cardNumber");
  if (cardNumberInput) {
    cardNumberInput.addEventListener("input", function (e) {
      let value = e.target.value.replace(/\D/g, "");
      if (value.length > 16) value = value.slice(0, 16);

      // Format with spaces
      let formattedValue = "";
      for (let i = 0; i < value.length; i++) {
        if (i > 0 && i % 4 === 0) {
          formattedValue += " ";
        }
        formattedValue += value[i];
      }

      e.target.value = formattedValue;
    });
  }

  // Expiry date formatting
  const expiryInput = document.getElementById("cardExpiry");
  if (expiryInput) {
    expiryInput.addEventListener("input", function (e) {
      let value = e.target.value.replace(/\D/g, "");
      if (value.length > 4) value = value.slice(0, 4);

      if (value.length > 2) {
        e.target.value = value.slice(0, 2) + "/" + value.slice(2);
      } else {
        e.target.value = value;
      }
    });
  }

  // CVC formatting
  const cvcInput = document.getElementById("cardCVC");
  if (cvcInput) {
    cvcInput.addEventListener("input", function (e) {
      let value = e.target.value.replace(/\D/g, "");
      if (value.length > 4) value = value.slice(0, 4);
      e.target.value = value;
    });
  }
});
