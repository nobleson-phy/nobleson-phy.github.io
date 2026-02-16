// Complete main.js file with all functionality

document.addEventListener('DOMContentLoaded', function() {
  // Mobile menu toggle
  const navTrigger = document.getElementById('nav-trigger');
  const menuIcon = document.querySelector('.menu-icon');
  
  if (navTrigger && menuIcon) {
    menuIcon.addEventListener('click', function() {
      navTrigger.checked = !navTrigger.checked;
    });
  }
  
  // Smooth scrolling for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      
      // Skip if it's just "#"
      if (targetId === '#' || targetId === '#!') return;
      
      // Check if it's an on-page anchor
      if (targetId.startsWith('#') && targetId.length > 1) {
        e.preventDefault();
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
          window.scrollTo({
            top: targetElement.offsetTop - 80,
            behavior: 'smooth'
          });
          
          // Update URL without jumping
          history.pushState(null, null, targetId);
        }
      }
    });
  });
  
  // Back to top button
  const backToTopButton = document.createElement('a');
  backToTopButton.href = '#';
  backToTopButton.className = 'back-to-top';
  backToTopButton.innerHTML = '<i class="fas fa-chevron-up"></i>';
  backToTopButton.setAttribute('aria-label', 'Back to top');
  document.body.appendChild(backToTopButton);
  
  // Show/hide back to top button
  window.addEventListener('scroll', function() {
    if (window.pageYOffset > 300) {
      backToTopButton.classList.add('visible');
    } else {
      backToTopButton.classList.remove('visible');
    }
  });
  
  // Back to top functionality
  backToTopButton.addEventListener('click', function(e) {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
  
  // Add current year to copyright (optional)
  const copyrightElements = document.querySelectorAll('.copyright');
  const currentYear = new Date().getFullYear();
  
  copyrightElements.forEach(el => {
    if (el.textContent.includes('{{ site.time | date: "%Y" }}')) {
      el.textContent = el.textContent.replace('{{ site.time | date: "%Y" }}', currentYear);
    } else if (el.textContent.includes('YEAR')) {
      el.textContent = el.textContent.replace('YEAR', currentYear);
    }
  });
  
  // External link indicator
  document.querySelectorAll('a').forEach(link => {
    if (link.hostname && link.hostname !== window.location.hostname) {
      link.setAttribute('target', '_blank');
      link.setAttribute('rel', 'noopener noreferrer');
      
      // Add external link icon
      if (!link.querySelector('i.fa-external-link-alt')) {
        link.innerHTML += ' <i class="fas fa-external-link-alt" style="font-size: 0.8em;"></i>';
      }
    }
  });
  
  // Initialize paper list functionality
  initPaperList();
});

// Paper list functionality
function initPaperList() {
  // Filter papers by type
  const filterButtons = document.querySelectorAll('.filter-btn');
  const paperItems = document.querySelectorAll('.paper-item');
  
  if (filterButtons.length > 0) {
    filterButtons.forEach(button => {
      button.addEventListener('click', function() {
        // Remove active class from all buttons
        filterButtons.forEach(btn => btn.classList.remove('active'));
        
        // Add active class to clicked button
        this.classList.add('active');
        
        const filter = this.dataset.filter;
        
        // Show/hide papers based on filter
        paperItems.forEach(item => {
          if (filter === 'all' || item.dataset.type === filter) {
            item.style.display = 'block';
            // Add slight delay for smooth transition
            setTimeout(() => {
              item.style.opacity = '1';
              item.style.transform = 'translateY(0)';
            }, 10);
          } else {
            item.style.opacity = '0';
            item.style.transform = 'translateY(10px)';
            setTimeout(() => {
              item.style.display = 'none';
            }, 300);
          }
        });
      });
    });
  }
  
  // Toggle abstract visibility
  const abstractToggles = document.querySelectorAll('.abstract-toggle');
  abstractToggles.forEach(toggle => {
    toggle.addEventListener('click', function() {
      const targetId = this.dataset.target;
      const target = document.getElementById(targetId);
      const icon = this.querySelector('i');
      
      if (target.classList.contains('show')) {
        target.classList.remove('show');
        this.classList.remove('expanded');
        this.innerHTML = 'Show Abstract <i class="fas fa-chevron-down"></i>';
      } else {
        target.classList.add('show');
        this.classList.add('expanded');
        this.innerHTML = 'Hide Abstract <i class="fas fa-chevron-up"></i>';
      }
    });
  });
  
  // Toggle BibTeX visibility
  const bibtexToggles = document.querySelectorAll('.bibtex-toggle');
  bibtexToggles.forEach(toggle => {
    toggle.addEventListener('click', function() {
      const targetId = this.dataset.target;
      const target = document.getElementById(targetId);
      
      if (target.classList.contains('show')) {
        target.classList.remove('show');
      } else {
        // Close other open BibTeX boxes
        document.querySelectorAll('.bibtex-content.show').forEach(el => {
          el.classList.remove('show');
        });
        target.classList.add('show');
      }
    });
  });
  
  // Toggle citation visibility
  const citationToggles = document.querySelectorAll('.citation-toggle');
  citationToggles.forEach(toggle => {
    toggle.addEventListener('click', function() {
      const targetId = this.dataset.target;
      const target = document.getElementById(targetId);
      
      if (target.classList.contains('show')) {
        target.classList.remove('show');
      } else {
        // Close other open citation boxes
        document.querySelectorAll('.citation-content.show').forEach(el => {
          el.classList.remove('show');
        });
        target.classList.add('show');
      }
    });
  });
  
  // Click outside to close BibTeX/citation boxes
  document.addEventListener('click', function(e) {
    if (!e.target.closest('.paper-link')) {
      document.querySelectorAll('.bibtex-content.show, .citation-content.show').forEach(el => {
        el.classList.remove('show');
      });
    }
  });
}