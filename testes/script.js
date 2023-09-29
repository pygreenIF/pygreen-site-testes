function showMenu() {
    let menuMobile = document.querySelector('.menu-mobile');
    if (menuMobile.classList.contains('open')) {
        menuMobile.classList.remove('open');
        // document.querySelector('.icon') = <i class="fa-solid fa-bars"></i>;
    } else {
        menuMobile.classList.add('open');
        // document.querySelector('.icon')= <i class="fa-solid fa-xmark"></i>;
    }
}

const modal = document.querySelector('#modal-login');
const openModal = document.querySelector('.login-button');
const closeModal = document.querySelector('.button-start');

openModal.addEventListener("click", () => {
    modal.showModal();
  });