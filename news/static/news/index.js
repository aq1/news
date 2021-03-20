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

    window.closeModal = (modalId) => {
        document.getElementById(modalId).classList.remove('is-active');
    };

    let activateModals = () => {
        const buttons = document.querySelectorAll('[data-modal-id]');
        const menu = document.getElementById('menu');
        const modals = document.querySelectorAll('div.modal');

        let clickHandler = (button, modal, menu) => {
            return function () {
                modals.forEach((e) => {
                    if(e !== modal) {
                        e.classList.remove('is-active');
                    }
                });
                button.classList.toggle('is-active');
                modal.classList.toggle('is-active');
                menu.classList.remove('is-active');
            };
        };
        for (let button of buttons) {
            let modal = document.getElementById(button.dataset.modalId);
            button.addEventListener('click', clickHandler(button, modal, menu));
        }
    };

    document.addEventListener('DOMContentLoaded', () => {
        activateMenu();
        activateModals();
    });
})();
