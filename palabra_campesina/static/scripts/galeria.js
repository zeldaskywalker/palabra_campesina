const loading_container = document.getElementById('loading');
const gallery_items_container = document.getElementById('gallery_items');

setTimeout(() => {
    if (loading_container) { // Check if the element still exists before attempting to remove
        loading_container.remove();
        gallery_items_container.style.display = 'block';
    }
}, 2000);
