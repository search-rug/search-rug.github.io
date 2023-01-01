/*
 * Control mobile menu display
 */
var body = document.querySelector('body')
var menuTrigger = document.querySelector('#toggle-main-menu-mobile');
var menuContainer = document.querySelector('#main-menu-mobile');

menuTrigger.onclick = function() {
    menuContainer.classList.toggle('open');
    menuTrigger.classList.toggle('is-active')
    body.classList.toggle('lock-scroll')
}

/*
 * Control desktop navbar display
 */
var navbarAutohide = document.querySelector('.header-autohide');
var navbarStartHidden = document.querySelector('.start-hidden');
var lastScrollTop = 0;

function updateNavbarOnScroll() {
    let scrollTop = window.scrollY;
    if(scrollTop < 300) {
        navbarAutohide.classList.remove('scrolled-down');
        navbarAutohide.classList.add('scrolled-up');
    }
    else {
        navbarAutohide.classList.remove('scrolled-up');
        navbarAutohide.classList.add('scrolled-down');
    }
    lastScrollTop = scrollTop;
}

document.addEventListener("DOMContentLoaded", function(){
    if(navbarAutohide){
      window.addEventListener('scroll', updateNavbarOnScroll);
    }

    if(navbarStartHidden){
        navbarStartHidden.classList.add('scrolled-up');
        navbarStartHidden.classList.remove('start-hidden');
    }
}); 
