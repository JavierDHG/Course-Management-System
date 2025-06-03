// Add smooth scrolling to comparison table
document.addEventListener("DOMContentLoaded", function () {
  // Highlight featured package
  const featuredCards = document.querySelectorAll(".border-primary");
  featuredCards.forEach((card) => {
    card.style.position = "relative";
    card.style.zIndex = "1";
  });

  // Add click tracking for analytics (if needed)
  const packageButtons = document.querySelectorAll(
    '[href*="pay_package_method"]'
  );
  packageButtons.forEach((button) => {
    button.addEventListener("click", function () {
      // Track package selection
      console.log(
        "Package selected:",
        this.closest(".card").querySelector(".card-title").textContent
      );
    });
  });
});
