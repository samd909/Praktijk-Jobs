const menuToggle = document.getElementById('menu-toggle');
const sidebar = document.getElementById('sidebar');
const mainContent = document.getElementById('main-content');

// Toggle sidebar visibility
menuToggle.addEventListener('click', () => {
    sidebar.classList.toggle('-translate-x-full'); // Hide sidebar
    mainContent.classList.toggle('ml-0'); // Remove margin when sidebar is hidden
    mainContent.classList.toggle('ml-64'); // Add margin when sidebar is shown
});