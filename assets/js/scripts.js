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

/*
 * Reveal additional LinkedIn embeds on the news page (only present there)
 */
var showMoreLinkedinBtn = document.querySelector('#show-more-linkedin');
if (showMoreLinkedinBtn) {
    showMoreLinkedinBtn.onclick = function() {
        document.querySelector('#more-linkedin-posts').classList.remove('hidden');
        showMoreLinkedinBtn.classList.add('hidden');
    }
}
