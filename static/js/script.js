// Auto-hide messages after 5 seconds
document.addEventListener("DOMContentLoaded", () => {
  const messages = document.querySelectorAll(".alert")
  if (messages) {
    messages.forEach((message) => {
      setTimeout(() => {
        message.style.transition = "opacity 0.5s"
        message.style.opacity = "0"
        setTimeout(() => {
          message.remove()
        }, 500)
      }, 5000)
    })
  }

  // Confirm before deleting
  const deleteButtons = document.querySelectorAll(".btn-delete")
  if (deleteButtons) {
    deleteButtons.forEach((button) => {
      button.addEventListener("click", (e) => {
        if (!confirm("Are you sure you want to delete this item?")) {
          e.preventDefault()
        }
      })
    })
  }

  // Form validation
  const forms = document.querySelectorAll("form")
  forms.forEach((form) => {
    form.addEventListener("submit", (e) => {
      const requiredFields = form.querySelectorAll("[required]")
      let isValid = true

      requiredFields.forEach((field) => {
        if (!field.value.trim()) {
          isValid = false
          field.style.borderColor = "red"
        } else {
          field.style.borderColor = "#ddd"
        }
      })

      if (!isValid) {
        e.preventDefault()
        alert("Please fill in all required fields")
      }
    })
  })

  // Smooth scroll for anchor links
  const anchorLinks = document.querySelectorAll('a[href^="#"]')
  anchorLinks.forEach((link) => {
    link.addEventListener("click", function (e) {
      const targetId = this.getAttribute("href")
      if (targetId !== "#") {
        const targetElement = document.querySelector(targetId)
        if (targetElement) {
          e.preventDefault()
          targetElement.scrollIntoView({
            behavior: "smooth",
            block: "start",
          })
        }
      }
    })
  })

  // Enhanced dropdown functionality for all navbar menus (Profile, Academics, Campus Life)
  const allDropdowns = document.querySelectorAll(".dropdown, .nav-profile-dropdown")

  allDropdowns.forEach((dropdown) => {
    // Target triggers: both generic .dropbtn and specific .nav-profile-trigger
    const trigger = dropdown.querySelector(".dropbtn, .nav-profile-trigger")
    if (!trigger) return

    trigger.addEventListener("click", (e) => {
      e.preventDefault()
      e.stopPropagation()

      const wasActive = dropdown.classList.contains("active")

      // Close all other dropdowns
      allDropdowns.forEach((other) => {
        if (other !== dropdown) other.classList.remove("active")
      })

      // Toggle current dropdown
      // If it's already active (perhaps from hover), we want to ensure it stays 
      // active or toggles properly without flickering.
      dropdown.classList.toggle("active")
    })

    // Mouseenter adds 'active' for smooth hover experience on desktop
    dropdown.addEventListener("mouseenter", () => {
      dropdown.classList.add("active")
    })

    // Mouseleave removes 'active'
    dropdown.addEventListener("mouseleave", () => {
      dropdown.classList.remove("active")
    })
  })

  // Close all open dropdowns when clicking anywhere outside
  document.addEventListener("click", () => {
    allDropdowns.forEach((dropdown) => {
      dropdown.classList.remove("active")
    })
  })
})
