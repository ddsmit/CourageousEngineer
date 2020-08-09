const header = document.querySelector('#header');
const menu = document.querySelector('.menu');
const postImage = document.querySelector('#article_image');
const article = document.querySelector('article')

const fullFadePosition = 150;
const finalOpacity = 0.04;

function imageControl(e) {
    let topOfHeader = header.offsetTop;
    let windowPosition = window.scrollY;
    if (windowPosition > fullFadePosition) {
        postImage.setAttribute('style','opacity: ' + finalOpacity)
    } else {
        let newOpacity = 1 - (windowPosition/fullFadePosition)*(1-finalOpacity);
        postImage.setAttribute('style','opacity: ' + newOpacity)
    }
}

function calculatePositions(e) {
    const menuBottom = menu.offsetHeight;
    const imageBottom = postImage.offsetHeight;
    header.setAttribute('style','padding-top: ' + imageBottom + 'px')
}

window.addEventListener('scroll', imageControl);
window.addEventListener('resize', calculatePositions);
window.addEventListener('load', calculatePositions);
