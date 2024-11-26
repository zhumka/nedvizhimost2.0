document.addEventListener('DOMContentLoaded', () => {
    const dropdowns = document.querySelectorAll('.dropdown');

    dropdowns.forEach(dropdown => {
        const menu = dropdown.querySelector('.dropdown-menu');
        if (!menu) return;

        // Показать меню
        dropdown.addEventListener('mouseenter', () => {
            menu.classList.add('show');
        });

        // Скрыть меню
        dropdown.addEventListener('mouseleave', () => {
            menu.classList.remove('show');
        });
    });
});
