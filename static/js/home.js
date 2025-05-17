function init(){
    console.log("home page")
}


let root = document.documentElement;

root.addEventListener("mousemove", e => {
  root.style.setProperty('--mouse-x', e.clientX + "deg");
  root.style.setProperty('--mouse-y', e.clientY + "deg");
});


document.addEventListener("DOMContentLoaded", () => {
  const blocks = document.querySelectorAll('.block');
  const io = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });
  
  blocks.forEach(el => io.observe(el));
});


document.addEventListener('DOMContentLoaded', () => {
  const navToggle = document.getElementById('nav-toggle');
  document
    .querySelectorAll('.nav-menu-mobile a')
    .forEach(link => {
      link.addEventListener('click', () => {
        navToggle.checked = false;
      });
    });
});


window.onload=init;