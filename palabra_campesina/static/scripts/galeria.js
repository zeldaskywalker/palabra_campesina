const loading_container = document.getElementById('loading');
const gallery_items_container = document.getElementById('gallery_items');

setTimeout(() => {
    if (loading_container) { // Check if the element still exists before attempting to remove
        loading_container.style.display = 'none';
        gallery_items_container.style.display = 'block';
    }
}, 2000);

const solo_galeria_img = document.getElementById('solo_galeria_image');
// solo_galeria_img.src = solo_galeria_img.dataset.src;

solo_galeria_img.onload = function() {
    solo_galeria_img.style.visibility = 'visible';
};

if (!solo_galeria_img.complete) {
    solo_galeria_img.style.visibility = 'hidden';
}