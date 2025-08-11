function revealImageWithText() {
    const img_desktop_container = document.querySelector('.img_desktop_container');
    img_desktop_container.style.backgroundImage = "url(/static/images/peering_through_with_text.png)";
}

function defaultHomeImageNoText() {
    const img_desktop_container = document.querySelector('.img_desktop_container');
    img_desktop_container.style.backgroundImage = "url(/static/images/peering_through_homepage_wide.jpg)";
}

const img_desktop_container = document.querySelector('.img_desktop_container');
img_desktop_container.addEventListener('mouseover', revealImageWithText);
img_desktop_container.addEventListener('mouseout', defaultHomeImageNoText);
