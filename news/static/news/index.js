(function main() {
    'use strict';

    let activateMenu = function () {
        const button = document.getElementById('menu-button');
        button.addEventListener('click', () => {
            const menu = document.getElementById('menu');
            button.classList.toggle('is-active');
            menu.classList.toggle('is-active');
        });
    };

    let activateModal = function () {
        const menuButton = document.getElementById('menu-button');
        const menu = document.getElementById('menu');
        const button = document.getElementById('message-us');
        const closeButton = document.getElementById('close-modal');
        const modal = document.getElementById('write-us-modal');
        button.addEventListener('click', () => {
            modal.classList.toggle('is-active');
            menu.classList.toggle('is-active');
            menuButton.classList.toggle('is-active');
        });
        closeButton.addEventListener('click', () => {
            modal.classList.toggle('is-active');
        });
    };

    document.addEventListener('DOMContentLoaded', () => {
        activateMenu();
        activateModal();
    });
})();
