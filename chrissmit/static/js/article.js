const postImage = document.querySelector('#article_image');
const article = document.querySelector('article')

const fullFadePosition = 150;
const finalOpacity = 0.04;

// header.setAttribute('style','padding-top: ' + imageBottom + 'px')

function imageControl(e) {
    // let windowPosition = window.scrollY;
    let windowPosition = window.pageYOffset
    if (windowPosition > fullFadePosition) {
        postImage.setAttribute('style','opacity: ' + finalOpacity);
    } else {
        let newOpacity = 1 - (windowPosition/fullFadePosition)*(1-finalOpacity);
        postImage.setAttribute('style','opacity: ' + newOpacity);
    }
}

window.addEventListener('scroll', imageControl);
