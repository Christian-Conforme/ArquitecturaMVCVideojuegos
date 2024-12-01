
CREATE TABLE juegos (
    id INT PRIMARY KEY,
    nombre VARCHAR(255),
    plataforma VARCHAR(255),
    genero VARCHAR(255),
    precio DECIMAL(5,2),
    descripcion TEXT,
    imagen_url TEXT,
    fecha_lanzamiento DATE
);

INSERT INTO juegos (id, nombre, plataforma, genero, precio, descripcion, imagen_url, fecha_lanzamiento) VALUES
(1, 'The Legend of Zelda: Breath of the Wild', 'Nintendo Switch', 'Aventura', 59.99, 'Un juego de aventura en un mundo abierto.', 'https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/en_US/games/switch/t/the-legend-of-zelda-breath-of-the-wild-switch/hero', '2017-03-03'),
(2, 'God of War', 'PlayStation 4', 'Acción', 39.99, 'Un juego de acción y aventura basado en la mitología nórdica.', 'https://upload.wikimedia.org/wikipedia/en/a/a7/God_of_War_4_cover.jpg', '2018-04-20'),
(3, 'Halo Infinite', 'Xbox Series X', 'Disparos', 59.99, 'Un juego de disparos en primera persona.', 'https://twinfinite.net/wp-content/uploads/2020/07/Halo-Infinite-2.jpg', '2021-12-08'),
(4, 'The Legend of Zelda: Echoes of Wisdom', 'Nintendo Switch', 'Aventura y Accion', 59.99, 'Un juego de aventura en un mundo abierto.', 'https://www.lavozdelafrontera.com.mx/local/p74u8y-the-legend-of-zelda/ALTERNATES/LANDSCAPE_1140/The%20Legend%20Of%20Zelda', '2024-09-26'),
(5, 'God of War: Ragnarök', 'PC', 'Acción', 69.99, 'Un juego de acción y aventura basado en el Ragnarok de la mitología nórdica.', 'https://www.gameaccessibilitynexus.com/wp-content/uploads/2022/11/GOWR-LV-Header-01.jpg', '2022-11-09'),
(6, 'Grand Theft Auto V', 'PC , PlayStation 4 y PlayStation 5', 'Disparos y Aventura', 59.99, 'Un juego de acción-aventura de mundo abierto desarrollado por Rockstar North y distribuido por Rockstar Games', 'https://media-rockstargames-com.akamaized.net/rockstargames-newsite/img/global/games/fob/1280/V.jpg', '2021-12-08'),
(7, 'Red Dead Redemption 2', 'PlayStation 4', 'Aventura', 59.99, 'Un juego de aventura en el viejo oeste.', 'https://cdn1.epicgames.com/b30b6d1b4dfd4dcc93b5490be5e094e5/offer/RDR2476298253_Epic_Games_Wishlist_RDR2_2560x1440_V01-2560x1440-2a9ebe1f7ee202102555be202d5632ec.jpg', '2018-10-26'),
(8, 'Cyberpunk 2077', 'PC', 'RPG', 49.99, 'Un juego de rol en un mundo futurista.', 'https://cdn1.epicgames.com/offer/77f2b98e2cef40c8a7437518bf420e47/EGS_Cyberpunk2077_CDPROJEKTRED_S1_03_2560x1440-359e77d3cd0a40aebf3bbc130d14c5c7', '2020-12-10'),
(9, 'The Witcher 3: Wild Hunt', 'Xbox One', 'RPG', 39.99, 'Un juego de rol en un mundo de fantasía.', 'https://image.api.playstation.com/vulcan/ap/rnd/202211/0914/TvcIHkYqqln1RGbaFqBeuFp6.jpg', '2015-05-19');