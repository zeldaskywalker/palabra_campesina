function revealImageWithText() {
    const img_desktop_container = document.querySelector('.img_desktop_container');
    img_desktop_container.style.backgroundImage = imgDesktopTextUrl;
    console.log('text reveal');
}

function defaultHomeImageNoText() {
    const img_desktop_container = document.querySelector('.img_desktop_container');
    img_desktop_container.style.backgroundImage = imgDesktopNoTextUrl;
    console.log('text hide');
}

const img_desktop_container = document.querySelector('.img_desktop_container');
img_desktop_container.addEventListener('mouseover', revealImageWithText);
img_desktop_container.addEventListener('mouseout', defaultHomeImageNoText);
