const solo_galeria_img = document.getElementById('solo_galeria_image');

solo_galeria_img.onload = function() {
    solo_galeria_img.style.visibility = 'visible';
};

if (!solo_galeria_img.complete) {
    solo_galeria_img.style.visibility = 'hidden';
}