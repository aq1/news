(function main() {
    'use strict';
    document.addEventListener('DOMContentLoaded', () => {

        const button = document.getElementById('menu-button');
        button.addEventListener('click', () => {
            const target = document.getElementById('menu');
            button.classList.toggle('is-active');
            target.classList.toggle('is-active');
        });
    });
})();
