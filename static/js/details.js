document.addEventListener("DOMContentLoaded", function () {
  // Favorite button functionality
  const favoriteBtn = document.querySelector(".favorite-btn");
  if (favoriteBtn) {
    favoriteBtn.addEventListener("click", function () {
      this.classList.toggle("active");
      const icon = this.querySelector("i");
      if (this.classList.contains("active")) {
        icon.classList.remove("bi-heart");
        icon.classList.add("bi-heart-fill");
      } else {
        icon.classList.remove("bi-heart-fill");
        icon.classList.add("bi-heart");
      }
    });
  }

  // Share functionality
  const shareButtons = document.querySelectorAll('[class*="btn-outline-"] i');
  shareButtons.forEach((button) => {
    button.parentElement.addEventListener("click", function () {
      const platform = this.querySelector("i").className;
      console.log("Sharing on:", platform);
      // Implement actual sharing logic here
    });
  });

  // Smooth scroll for internal links
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute("href"));
      if (target) {
        target.scrollIntoView({
          behavior: "smooth",
        });
      }
    });
  });
});
