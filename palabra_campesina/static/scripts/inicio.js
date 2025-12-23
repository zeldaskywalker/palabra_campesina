function revealImageWithText() {
    const img_desktop_container = document.querySelector('.img_desktop_container');
    img_desktop_container.style.backgroundImage = imgDesktopTextUrl;
    
}

function defaultHomeImageNoText() {
    const img_desktop_container = document.querySelector('.img_desktop_container');
    img_desktop_container.style.backgroundImage = imgDesktopNoTextUrl;
}

const img_desktop_container = document.querySelector('.img_desktop_container');
img_desktop_container.addEventListener('mouseover', revealImageWithText);
img_desktop_container.addEventListener('mouseout', defaultHomeImageNoText);
