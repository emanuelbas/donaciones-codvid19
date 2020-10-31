-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 31-10-2020 a las 02:18:05
-- Versión del servidor: 10.4.14-MariaDB
-- Versión de PHP: 7.2.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `grupo22`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `centro_de_ayuda`
--

CREATE TABLE `centro_de_ayuda` (
  `id` int(35) NOT NULL,
  `nombre` varchar(35) NOT NULL,
  `direccion` varchar(35) NOT NULL,
  `telefono` varchar(35) NOT NULL,
  `hora_de_apertura` time(6) NOT NULL,
  `hora_de_cierre` time(6) NOT NULL,
  `sitio_web` varchar(35) NOT NULL,
  `email` varchar(35) NOT NULL,
  `estado_id` int(11) NOT NULL DEFAULT 1,
  `protocolo_de_vista` varchar(35) NOT NULL DEFAULT 'PDF',
  `coordenada_x` int(35) NOT NULL,
  `coordenada_y` int(35) NOT NULL,
  `historico` tinyint(1) NOT NULL DEFAULT 0,
  `municipio_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `centro_de_ayuda`
--

INSERT INTO `centro_de_ayuda` (`id`, `nombre`, `direccion`, `telefono`, `hora_de_apertura`, `hora_de_cierre`, `sitio_web`, `email`, `estado_id`, `protocolo_de_vista`, `coordenada_x`, `coordenada_y`, `historico`, `municipio_id`) VALUES
(1, 'Centro de prueba', 'Calle 23, numero 35', '9111233255', '09:00:00.000000', '16:00:00.000000', 'http://www.centrodeprueba.gov', 'contacto@centrodeprueba.gov', 1, 'PDF', 300, 54234, 0, 2),
(2, 'Centro de prueba 2', 'Calle 2, numero 33', '9111233353', '09:00:00.000000', '16:00:00.000000', 'http://www.centrodeprueba2.gov', 'contacto@centrodeprueba2.gov', 2, 'PDF', 44, 54234, 0, 2),
(3, 'Donaciones Pepito', 'Calle 32, numero 12', '9111224525', '09:00:00.000000', '16:00:00.000000', 'http://www.centrodeprueba.gov', 'contacto@centrodeprueba.gov', 3, 'PDF', 300, 54234, 0, 2),
(4, 'Hospital Nacional', 'Calle 15, numero 3443', '9111233255', '09:00:00.000000', '16:00:00.000000', 'http://www.centrodeprueba.gov', 'contacto@centrodeprueba.gov', 2, 'PDF', 300, 54234, 0, 1),
(5, 'Hospital Enrique', 'Calle 53, numero 35', '9111233255', '09:00:00.000000', '16:00:00.000000', 'http://www.centrodeprueba.gov', 'contacto@centrodeprueba.gov', 1, 'PDF', 300, 54234, 0, 1),
(6, 'Centro la esperanza', 'Calle 23234, numero 35', '9111233255', '09:00:00.000000', '16:00:00.000000', 'http://www.centrodeprueba.gov', 'contacto@centrodeprueba.gov', 3, 'PDF', 300, 54234, 0, 1),
(7, 'Centro la poca imaginacion', 'Calle 123, numero 35', '9111233255', '09:00:00.000000', '16:00:00.000000', 'http://www.centrodeprueba.gov', 'contacto@centrodeprueba.gov', 1, 'PDF', 300, 54234, 0, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `centro_tiene_tipo`
--

CREATE TABLE `centro_tiene_tipo` (
  `centro_id` int(20) NOT NULL,
  `tipo_de_centro_id` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `centro_tiene_tipo`
--

INSERT INTO `centro_tiene_tipo` (`centro_id`, `tipo_de_centro_id`) VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 3),
(3, 1),
(4, 2),
(5, 2),
(5, 3),
(6, 1),
(6, 4),
(7, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `configuracion`
--

CREATE TABLE `configuracion` (
  `id` int(10) NOT NULL,
  `titulo` varchar(50) NOT NULL,
  `descripcion` text NOT NULL,
  `mail` varchar(50) NOT NULL,
  `activo` int(10) NOT NULL,
  `cantPagina` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `configuracion`
--

INSERT INTO `configuracion` (`id`, `titulo`, `descripcion`, `mail`, `activo`, `cantPagina`) VALUES
(1, 'Covid-19', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat. Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. ', 'centro@gmail.com', 1, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado_centro`
--

CREATE TABLE `estado_centro` (
  `id` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estado_centro`
--

INSERT INTO `estado_centro` (`id`, `nombre`) VALUES
(2, 'aceptado'),
(1, 'pendiente'),
(3, 'rechazado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `municipio`
--

CREATE TABLE `municipio` (
  `id` int(10) NOT NULL,
  `nombre` varchar(35) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `municipio`
--

INSERT INTO `municipio` (`id`, `nombre`) VALUES
(2, 'Ensenada'),
(1, 'La Plata');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permiso`
--

CREATE TABLE `permiso` (
  `id` int(10) NOT NULL,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `permiso`
--

INSERT INTO `permiso` (`id`, `nombre`) VALUES
(3, 'centro_destroy'),
(1, 'centro_index'),
(2, 'centro_new'),
(5, 'centro_show'),
(4, 'centro_update'),
(11, 'site_config'),
(8, 'user_create'),
(9, 'user_delete'),
(10, 'user_edit'),
(7, 'user_show');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE `rol` (
  `id` int(10) NOT NULL,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `rol`
--

INSERT INTO `rol` (`id`, `nombre`) VALUES
(1, 'admin'),
(2, 'operador');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol_tiene_permiso`
--

CREATE TABLE `rol_tiene_permiso` (
  `rol_id` int(10) NOT NULL,
  `permiso_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `rol_tiene_permiso`
--

INSERT INTO `rol_tiene_permiso` (`rol_id`, `permiso_id`) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(1, 7),
(1, 8),
(1, 9),
(1, 10),
(1, 11);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_de_centro`
--

CREATE TABLE `tipo_de_centro` (
  `id` int(20) NOT NULL,
  `nombre` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tipo_de_centro`
--

INSERT INTO `tipo_de_centro` (`id`, `nombre`) VALUES
(2, 'Alimentos'),
(4, 'Plasma'),
(1, 'Ropa'),
(3, 'Sangre');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `turnos_para_centro`
--

CREATE TABLE `turnos_para_centro` (
  `id` int(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `bloque_turno` varchar(50) NOT NULL,
  `dia` date NOT NULL,
  `activo` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `turnos_para_centro`
--

INSERT INTO `turnos_para_centro` (`id`, `email`, `bloque_turno`, `dia`, `activo`) VALUES
(1, 'dario@gmail.com', '9 a 9:30', '2020-10-30', 0),
(2, 'ema@gmail.com', '10 a 10:30', '2020-10-30', 0),
(3, 'maxi@gmail.com', '10:30 a 11', '2020-10-30', 1),
(4, 'may@gmail.com', '00:00', '2020-10-30', 1),
(5, 'juanp@gmail.com', '12:30', '2020-10-30', 1),
(6, 'hugo@gmail.com', '19:00', '2020-10-30', 1),
(9, 'nuevo@gmail.com', '14:00 a 14:30', '2020-10-30', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(10) NOT NULL,
  `usuario` varchar(255) NOT NULL,
  `clave` varchar(255) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `apellido` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `fecha_creacion` date NOT NULL,
  `fecha_actualizacion` date NOT NULL,
  `historico` tinyint(4) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `usuario`, `clave`, `nombre`, `apellido`, `email`, `activo`, `fecha_creacion`, `fecha_actualizacion`, `historico`) VALUES
(8, 'admin', '1234', 'Homero', 'Simpson', 'hsimpson@gmail.com', 1, '2020-10-18', '2020-10-18', 0),
(11, 'usuario', '1234', 'Ned', 'Flanders', 'flanders15@gmail.com', 1, '2020-10-18', '2020-10-18', 0),
(13, 'nuevo', '1234', 'new', 'new', 'new@gmail.com', 1, '2020-10-24', '2020-10-24', 1),
(19, 'sarasa', '1234', 'sara', 'sars', 'sara@gmail.commm', 0, '2020-10-30', '2020-10-30', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_tiene_rol`
--

CREATE TABLE `usuario_tiene_rol` (
  `usuario_id` int(10) NOT NULL,
  `rol_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `usuario_tiene_rol`
--

INSERT INTO `usuario_tiene_rol` (`usuario_id`, `rol_id`) VALUES
(8, 1),
(11, 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `centro_de_ayuda`
--
ALTER TABLE `centro_de_ayuda`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `centro_tiene_tipo`
--
ALTER TABLE `centro_tiene_tipo`
  ADD PRIMARY KEY (`centro_id`,`tipo_de_centro_id`);

--
-- Indices de la tabla `configuracion`
--
ALTER TABLE `configuracion`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `estado_centro`
--
ALTER TABLE `estado_centro`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `municipio`
--
ALTER TABLE `municipio`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `permiso`
--
ALTER TABLE `permiso`
  ADD PRIMARY KEY (`id`) USING BTREE,
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `rol_tiene_permiso`
--
ALTER TABLE `rol_tiene_permiso`
  ADD PRIMARY KEY (`rol_id`,`permiso_id`),
  ADD KEY `FK_permiso_id` (`permiso_id`);

--
-- Indices de la tabla `tipo_de_centro`
--
ALTER TABLE `tipo_de_centro`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `turnos_para_centro`
--
ALTER TABLE `turnos_para_centro`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuario` (`usuario`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `usuario_tiene_rol`
--
ALTER TABLE `usuario_tiene_rol`
  ADD PRIMARY KEY (`usuario_id`,`rol_id`),
  ADD KEY `FK_rol_utp_id` (`rol_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `centro_de_ayuda`
--
ALTER TABLE `centro_de_ayuda`
  MODIFY `id` int(35) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `configuracion`
--
ALTER TABLE `configuracion`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `estado_centro`
--
ALTER TABLE `estado_centro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `municipio`
--
ALTER TABLE `municipio`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `permiso`
--
ALTER TABLE `permiso`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `rol`
--
ALTER TABLE `rol`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tipo_de_centro`
--
ALTER TABLE `tipo_de_centro`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `turnos_para_centro`
--
ALTER TABLE `turnos_para_centro`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
