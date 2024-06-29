document.addEventListener('DOMContentLoaded', (event) => {
    const menuItems = document.querySelectorAll('.menu-item');
    const clickSound = document.getElementById('clickSound');
    const themeSwitch = document.getElementById('theme-switch');
    const body = document.body;

    // Función para reproducir el sonido de clic
    function playSound() {
        clickSound.currentTime = 0;
        clickSound.volume = 0.2;
        
        const playPromise = clickSound.play();
        if (playPromise !== undefined) {
            playPromise.then(_ => {
                // La reproducción se inició con éxito
            }).catch(error => {
                console.log("Reproducción automática impedida por el navegador:", error);
            });
        }
    }

    // Añadir el sonido a todos los elementos interactivos
    const interactiveElements = document.querySelectorAll('a, button, .menu-item');
    interactiveElements.forEach(element => {
        element.addEventListener('click', (e) => {
            playSound();
        });
    });

    // Función para cambiar el tema
    function toggleTheme() {
        body.classList.toggle('light-theme');
        playSound();
        
        if (body.classList.contains('light-theme')) {
            themeSwitch.textContent = 'Tema Oscuro';
            localStorage.setItem('theme', 'light');
        } else {
            themeSwitch.textContent = 'Tema Claro';
            localStorage.setItem('theme', 'dark');
        }
    }

    // Configuración inicial del tema según el valor almacenado en localStorage
    if (localStorage.getItem('theme') === 'light') {
        body.classList.add('light-theme');
        themeSwitch.textContent = 'Tema Oscuro';
    } else {
        themeSwitch.textContent = 'Tema Claro';
    }

    // Event listener para cambiar el tema
    themeSwitch.addEventListener('click', toggleTheme);

    // Solución para dispositivos móviles
    document.body.addEventListener('touchstart', function() {
        clickSound.play();
        clickSound.pause();
        clickSound.currentTime = 0;
    }, { once: true });
});