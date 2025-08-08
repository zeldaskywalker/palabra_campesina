// if screen width a certain size, show nav bar menu dropdown instead

function openOrCloseNav() {
    const navbar_items = document.getElementById("nav-items");

    if (navbar_items.style.display === 'none') {
        navbar_items.style.display = "flex";
        navbar_items.style['flex-direction'] = 'column';
    } else {
        navbar_items.style.display = 'none';
    }
}

const navbar_dropdown_button = document.getElementById('nav-button');
navbar_dropdown_button.addEventListener('click', openOrCloseNav);

function handleMobileOrResize() {
  const navbar_items = document.getElementById("nav-items");
  const navbar_dropdown_button = document.getElementById("nav-button");

  if (window.innerWidth < 680) {
    // if the screen IS NOT wide enough

    // show the navbar dropdown button
    navbar_dropdown_button.style.display = 'flex';

    // hide the navbar items
    navbar_items.style.display = 'none';

  } else if (window.innerWidth >= 680) {
    // if the screen IS wide enough

    // don't show navbar dropdown button
    navbar_dropdown_button.style.display = 'none';

    // show navbar items horizontally
    navbar_items.style.display = 'flex';
    navbar_items.style['flex-direction'] = 'row';
  }
}

handleMobileOrResize();

window.onresize = handleMobileOrResize;