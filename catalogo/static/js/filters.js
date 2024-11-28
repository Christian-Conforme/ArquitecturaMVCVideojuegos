// static/js/filters.js

document.addEventListener('DOMContentLoaded', function() {
    applyFilters();
});

function applyFilters() {
    const plataforma = document.getElementById('plataforma').value;
    const genero = document.getElementById('género').value;
    const precioMin = document.getElementById('precio_min').value;
    const precioMax = document.getElementById('precio_max').value;
    const buscar = document.getElementById('buscar').value;

    fetch(`/filtrar/?plataforma=${plataforma}&género=${genero}&precio_min=${precioMin}&precio_max=${precioMax}&buscar=${buscar}`)
        .then(response => response.json())
        .then(data => {
            const videojuegosList = document.getElementById('videojuegos-list');
            videojuegosList.innerHTML = '';
            data.videojuegos.forEach(juego => {
                const div = document.createElement('div');
                div.className = 'grid-item';
                div.innerHTML = `
                    <img src="${juego.imagen}" alt="${juego.nombre}">
                    <h2><a href="/detalles/${juego.id}/">${juego.nombre}</a></h2>
                    <p>Género: ${juego.género}</p>
                    <p>Precio: ${juego.precio}</p>
                    <p>Plataforma: ${juego.plataforma}</p>
                `;
                videojuegosList.appendChild(div);
            });
        });
}