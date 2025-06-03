document.addEventListener("DOMContentLoaded", function () {
  // Filter functionality
  const filterButtons = document.querySelectorAll("[data-filter]");
  const courseItems = document.querySelectorAll(".course-item");

  filterButtons.forEach((button) => {
    button.addEventListener("click", function (e) {
      e.preventDefault();
      const filter = this.getAttribute("data-filter");

      courseItems.forEach((item) => {
        if (filter === "all" || item.getAttribute("data-status") === filter) {
          item.style.display = "block";
        } else {
          item.style.display = "none";
        }
      });
    });
  });

  // Favorite button functionality
  const favoriteButtons = document.querySelectorAll(".favorite-btn");
  favoriteButtons.forEach((button) => {
    button.addEventListener("click", function () {
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
  });

  // Smooth scroll for navigation
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
