/*
 * Control mobile menu display
 */
var body = document.querySelector('body')
var menuTrigger = document.querySelector('#toggle-main-menu-mobile');
var menuContainer = document.querySelector('#main-menu-mobile');

menuTrigger.onclick = function() {
    menuContainer.classList.toggle('collapse');
    body.classList.toggle('overflow-hidden');
}
