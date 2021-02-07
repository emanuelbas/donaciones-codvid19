-- phpMyAdmin SQL Dump
-- version 4.6.6deb5ubuntu0.5
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 04-01-2021 a las 18:19:51
-- Versión del servidor: 10.1.47-MariaDB-0ubuntu0.18.04.1
-- Versión de PHP: 7.2.24-0ubuntu0.18.04.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
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
  `estado_id` int(11) NOT NULL DEFAULT '1',
  `publicado` tinyint(1) NOT NULL DEFAULT '0',
  `protocolo_de_vista` varchar(35) NOT NULL DEFAULT 'PDF',
  `coordenada_x` text NOT NULL,
  `coordenada_y` text NOT NULL,
  `historico` tinyint(1) NOT NULL DEFAULT '0',
  `municipio_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `centro_de_ayuda`
--

INSERT INTO `centro_de_ayuda` (`id`, `nombre`, `direccion`, `telefono`, `hora_de_apertura`, `hora_de_cierre`, `sitio_web`, `email`, `estado_id`, `publicado`, `protocolo_de_vista`, `coordenada_x`, `coordenada_y`, `historico`, `municipio_id`) VALUES
(1, 'Centro de prueba pepito', 'Calle 23, numero 35', '9111233255', '08:00:00.000000', '09:00:00.000000', 'http://www.centrodeprueba.gov', 'contacto@centrodeprueba.gov', 3, 1, 'PDF', '-37.40798255240778', '-59.49829123914243', 0, 19),
(2, 'Centro de prueba 2', 'Calle 2, numero 33', '9111233353', '09:00:00.000000', '16:00:00.000000', 'http://www.centrodeprueba2.gov', 'contacto@centrodeprueba2.gov', 2, 1, 'PDF', '44', '54234', 0, 7),
(3, 'Donaciones Pepito', 'Calle 32, numero 10', '9111224525', '09:00:00.000000', '16:00:00.000000', 'http://www.centrodeprueba.gov', 'contacto@centrodeprueba.gov', 2, 1, 'PDF', '-36.01059851114428', '-57.56469748914243', 0, 4),
(4, 'Hospital Nacional', 'Calle 15, numero 3443', '9111233255', '09:00:00.000000', '16:00:00.000000', 'http://www.centrodeprueba.gov', 'contacto@centrodeprueba.gov', 2, 1, 'PDF', '300', '54234', 0, 19),
(5, 'Hospital Enrique', 'Calle 53, numero 35', '9111233255', '09:00:00.000000', '16:00:00.000000', 'http://www.centrodeprueba.gov', 'contacto@centrodeprueba.gov', 2, 1, 'PDF', '300', '54234', 0, 4),
(6, 'Centro la esperanza', 'Calle 23234, numero 35', '9111233255', '09:00:00.000000', '16:00:00.000000', 'http://www.centrodeprueba.gov', 'contacto@centrodeprueba.gov', 3, 1, 'PDF', '300', '54234', 0, 7),
(7, 'Centro la poca imaginacion', 'Calle 123, numero 35', '9111233255', '09:00:00.000000', '16:00:00.000000', 'http://www.centrodeprueba.gov', 'contacto@centrodeprueba.gov', 2, 1, 'PDF', '300', '54234', 0, 19),
(8, 'Otro centro', 'wedswdq', '12123123', '22:22:00.000000', '22:22:00.000000', 'asdasddas', 'weqqwew@asdsda', 1, 1, 'PDF', '2', '3', 0, 5),
(9, 'Hola centros22', 'sadasdasdasd', '31231123', '22:22:00.000000', '22:22:00.000000', 'asdasddas', 'e@b', 1, 1, 'PDF', '2', '2', 1, 1),
(10, 'Centro sangres berisso', 'sadasdasdasd', '12312323', '02:22:00.000000', '02:22:00.000000', 'sdaasd', 'e@b', 1, 0, '10_Actividad_5_2.pdf', '2', '1', 0, 4),
(11, 'Centro morenito', 'La Plata, Plaza Moreno', '123123123', '07:00:00.000000', '23:00:00.000000', 'morenito.com', 'e@b', 2, 1, 'PDF', '-34.921478773656624', '-57.95273557308065', 0, 19),
(12, 'Hola centrowsas', 'sadasd@asda', '12312', '11:11:00.000000', '21:22:00.000000', 'asdasasd', 'e@b', 1, 0, '12_Actividad_5_2.pdf', '-35.499436784979984', '-57.74047873914242', 0, 3),
(13, 'nuevo centro', 'calle 40', '000000', '09:00:00.000000', '16:00:00.000000', 'www.nuevo.com', 'nuvo@gmail.com', 1, 1, '13_Dias_y_horarios_finales_V2.pdf', '35', '35', 0, 3),
(14, 'Centro en San Cañuelas', 'Cañuelas, 123 1223', '31231123', '10:00:00.000000', '20:30:00.000000', 'asdasasd', 'asasd@wawe', 1, 0, 'PDF', '-35.05431345777287', '-58.760501146534814', 0, 5),
(15, 'Centro de Lobos', 'Caba, 123 1223', '123123123', '10:00:00.000000', '18:00:00.000000', 'asdasasd', 'asasd@wawe', 1, 0, '15_', '-35.185219956195965', '-59.0952301165089', 0, 65),
(16, 'Centro de Chacabuco', 'Caba, 123 1223', '123123123', '10:00:00.000000', '18:00:00.000000', 'asdasasd', 'asasd@wawe', 1, 0, 'PDF', '-35.185219956195965', '-59.0952301165089', 0, 52),
(17, 'centro 17', 'calle 2 ', '123123123', '12:16:00.000000', '20:16:00.000000', 'asasdasd', 'e@b', 2, 1, 'PDF', '-35.082550843761055', '-57.504994869232185', 0, 28),
(18, 'Caritas', 'calle 5 y 48', '221784596', '09:00:00.000000', '17:00:00.000000', '', 'sadaf@dac.com', 1, 1, 'PDF', '-34.91197712606667', '-57.94905066490174', 0, 19),
(19, 'cruz roja', 'calle 2 ', '225366654', '10:00:00.000000', '16:00:00.000000', 'www.dadaf.com', 'op1@sfasfa.com', 1, 1, 'PDF', '-34.94448806230625', '-57.93262481689454', 0, 1),
(20, 'Centro post demo', 'ewqweqwe', '1123123', '14:24:00.000000', '14:25:00.000000', 'sdaasd', 'asasd@wawe', 1, 1, 'PDF', '-36.140832002520156', '-58.48754905164243', 0, 4),
(21, 'otro centro post demo', 'wqeqweqwe', '123412323', '00:00:00.000000', '03:01:00.000000', 'qweqweqwe', 'wqeweqwe@qwqw', 1, 0, '21_Protocolo_de_visita.pdf', '-36.91476428895593', '-60.79833984375001', 0, 12),
(22, 'Nombre de Centro', 'La Plata, Calle 23 numero 123', '9111233255', '09:00:00.000000', '18:00:00.000000', 'http://www.centrodeprueba.gov', 'contacto@centrodeprueba.gov', 1, 0, 'PDF', '-38', '-58', 0, 1),
(23, 'Nombre de Centro', 'La Plata, Calle 23 numero 123', '9111233255', '09:00:00.000000', '18:00:00.000000', 'http://www.centrodeprueba.gov', 'contacto@centrodeprueba.gov', 1, 0, 'PDF', '-38', '-58', 0, 1),
(24, 'Nombre de Centro', 'La Plata, Calle 23 numero 123', '9111233255', '09:00:00.000000', '18:00:00.000000', 'http://www.centrodeprueba.gov', 'contacto@centrodeprueba.gov', 1, 0, 'PDF', '-38', '-58', 0, 1),
(25, 'Nombre de Centro', 'La Plata, Calle 23 numero 123', '9111233255', '09:00:00.000000', '18:00:00.000000', 'http://www.centrodeprueba.gov', 'contacto@centrodeprueba.gov', 1, 0, 'PDF', '-38', '-58', 0, 1),
(26, 'Nombre de Centro', 'La Plata, Calle 23 numero 123', '9111233255', '09:00:00.000000', '18:00:00.000000', 'http://www.centrodeprueba.gov', 'contacto@centrodeprueba.gov', 1, 0, 'PDF', '-38', '-58', 0, 1),
(27, 'Nombre de Centro', 'La Plata, Calle 23 numero 123', '9111233255', '09:00:00.000000', '18:00:00.000000', 'http://www.centrodeprueba.gov', 'contacto@centrodeprueba.gov', 1, 0, 'PDF', '-38', '-58', 0, 1),
(28, 'Nombre de Centro', 'La Plata, Calle 23 numero 123', '9111233255', '09:00:00.000000', '18:00:00.000000', 'http://www.centrodeprueba.gov', 'contacto@centrodeprueba.gov', 1, 0, 'PDF', '-38', '-58', 0, 1),
(29, 'prueba', 'dsasd', '31123123', '00:13:00.000000', '00:17:00.000000', 'dasasd', 'daasd@ddasasd', 1, 0, '29_Protocolo_de_visita.pdf', '-36.686041276581925', '-58.20556640625001', 0, 47),
(30, 'dasds', 'dadads', '1123123123', '22:22:00.000000', '23:22:00.000000', 'asddasdas', 'asdaasd@asdsd', 1, 0, 'PDF', '-35.79999392988527', '-58.64501953125001', 0, 5),
(31, 'Comedor San Carlos', 'Sacn carlos calle 134 Numero 8500', '131212', '10:00:00.000000', '18:00:00.000000', 'asdadsads.com', 'asdasd@asdasd', 2, 1, '31_Actividad_6.pdf', '-34.92907864007865', '-57.995367050170906', 0, 19),
(32, 'Cnetro de prueba 17-12', 'La Plata , 1232442', '122131221', '10:00:00.000000', '14:00:00.000000', 'sdsdaasdasd', 'cprueba@gmail.com', 2, 1, '32_Actividad_6.pdf', '-34.953106225295436', '-57.96356678009033', 0, 19),
(33, 'Probando nombre largo', 'Casalins, Calle principal Numero 15', '21124412124', '10:00:00.000000', '15:00:00.000000', 'asdasdasds', 'asas@wqedqw', 1, 0, '33_Protocolo_de_visita_con_nombre_l', '-36.314580510868204', '-58.55156064033509', 0, 1);

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
(1, 4),
(2, 1),
(2, 3),
(3, 1),
(3, 2),
(4, 2),
(5, 2),
(5, 3),
(6, 1),
(6, 4),
(7, 1),
(8, 2),
(8, 4),
(9, 2),
(10, 3),
(10, 4),
(11, 2),
(12, 2),
(13, 1),
(13, 2),
(14, 2),
(14, 4),
(15, 2),
(16, 2),
(17, 1),
(17, 3),
(18, 1),
(19, 1),
(20, 4),
(21, 2),
(29, 2),
(30, 2),
(31, 2),
(32, 2),
(33, 2);

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
(1, 'Covid-19', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat. Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. ', 'centro@gmail.com', 1, 5);

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
  `nombre` varchar(35) NOT NULL,
  `fase_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `municipio`
--

INSERT INTO `municipio` (`id`, `nombre`, `fase_id`) VALUES
(1, 'Almirante Brown', 3),
(2, 'Avellaneda', 3),
(3, 'Berazategui', 3),
(4, 'Berisso', 3),
(5, 'Cañuelas', 3),
(6, 'Coronel Pringles', 3),
(7, 'Ensenada', 3),
(8, 'Escobar', 3),
(9, 'Esteban Echeverría', 3),
(10, 'Ezeiza', 3),
(11, 'Florencio Varela', 3),
(12, 'General Las Heras', 3),
(13, 'General Rodríguez', 3),
(14, 'General San Martín', 3),
(15, 'Hurlingham', 3),
(16, 'Ituzaingó', 3),
(17, 'José C. Paz', 3),
(18, 'La Matanza', 3),
(19, 'La Plata', 3),
(20, 'Lanús', 3),
(21, 'Lomas de Zamora', 3),
(22, 'Luján', 3),
(23, 'Malvinas Argentinas', 3),
(24, 'Marcos Paz', 3),
(25, 'Merlo', 3),
(26, 'Moreno', 3),
(27, 'Morón', 3),
(28, 'Pilar', 3),
(29, 'Presidente Perón', 3),
(30, 'Quilmes', 3),
(31, 'San Fernando', 3),
(32, 'San Isidro', 3),
(33, 'San Miguel', 3),
(34, 'San Vicente', 3),
(35, 'Tigre', 3),
(36, 'Tres de Febrero', 3),
(37, 'Vicente López', 3),
(38, '25 de Mayo', 4),
(39, 'Arrecifes', 4),
(40, 'Ayacucho', 4),
(41, 'Azul', 4),
(42, 'Bahía Blanca', 4),
(43, 'Balcarce', 4),
(44, 'Baradero', 4),
(45, 'Bolívar', 4),
(46, 'Bragado', 4),
(47, 'Brandsen', 4),
(48, 'Campana', 4),
(49, 'Capitán Sarmiento', 4),
(50, 'Carmen de Areco', 4),
(51, 'Castelli', 4),
(52, 'Chacabuco', 4),
(53, 'Chascomús', 4),
(54, 'Chivilcoy', 4),
(55, 'Coronel de Marina L. Rosales', 4),
(56, 'Coronel Dorrego', 4),
(57, 'Dolores', 4),
(58, 'Exaltación de la Cruz', 4),
(59, 'General Belgrano', 4),
(60, 'General Juan Madariaga', 4),
(61, 'General Paz', 4),
(62, 'General Pueyrredon', 4),
(63, 'HIpólito Yrigoyen', 4),
(64, 'Laprida', 4),
(65, 'Lobos', 4),
(66, 'Magdalena', 4),
(67, 'Mercedes', 4),
(68, 'Monte', 4),
(69, 'Navarro', 4),
(70, 'Pellegrini', 4),
(71, 'Pergamino', 4),
(72, 'Pila', 4),
(73, 'Pinamar', 4),
(74, 'Punta Indio', 4),
(75, 'Ramallo', 4),
(76, 'Roque Pérez', 4),
(77, 'Saladillo', 4),
(78, 'Salto', 4),
(79, 'San Andrés de Giles', 4),
(80, 'San Antonio de Areco', 4),
(81, 'San Pedro', 4),
(82, 'Suipacha', 4),
(83, 'Tordillo', 4),
(84, 'Tornquist', 4),
(85, 'Zárate', 4),
(86, '9 de Julio', 5),
(87, 'Adolfo Alsina', 5),
(88, 'Adolfo Gonzales Chaves', 5),
(89, 'Alberti', 5),
(90, 'Benito Juárez', 5),
(91, 'Carlos Casares', 5),
(92, 'Carlos Tejedor', 5),
(93, 'Colón', 5),
(94, 'Coronel Suárez', 5),
(95, 'Daireaux', 5),
(96, 'Florentino Ameghino', 5),
(97, 'General Alvarado', 5),
(98, 'General Alvear', 5),
(99, 'General Arenales', 5),
(100, 'General Guido', 5),
(101, 'General La Madrid', 5),
(102, 'General Lavalle', 5),
(103, 'General Pinto', 5),
(104, 'General Viamonte', 5),
(105, 'General Villegas', 5),
(106, 'Guarrini', 5),
(107, 'Junín', 5),
(108, 'La Costa', 5),
(109, 'Las Flores', 5),
(110, 'Leandra N. Alem', 5),
(111, 'Lezama', 5),
(112, 'Lincoln', 5),
(113, 'Lobería', 5),
(114, 'Maipú', 5),
(115, 'Mar Chiquita', 5),
(116, 'Monte Hermoso', 5),
(117, 'Necochea', 5),
(118, 'Olavarría', 5),
(119, 'Patagones', 5),
(120, 'Pehuajó', 5),
(121, 'Puán', 5),
(122, 'Rauch', 5),
(123, 'Rivadavia', 5),
(124, 'Rojas', 5),
(125, 'Saavedra', 5),
(126, 'Salliqueló', 5),
(127, 'San Cayetano', 5),
(128, 'San Nicolás', 5),
(129, 'Tandil', 5),
(130, 'Tapalque', 5),
(131, 'Trenque Lauquen', 5),
(132, 'Tres Arroyos', 5),
(133, 'Tres Lomas', 5),
(134, 'Villa Gesell', 5),
(135, 'Villarino', 5);

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
(2, 'centro_create'),
(3, 'centro_delete'),
(4, 'centro_edit'),
(1, 'centro_index'),
(5, 'centro_show'),
(11, 'site_config'),
(15, 'turno_create'),
(14, 'turno_delete'),
(16, 'turno_edit'),
(13, 'turno_index'),
(17, 'turno_show'),
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
(1, 11),
(1, 13),
(1, 14),
(1, 15),
(1, 16),
(1, 17),
(2, 1),
(2, 2),
(2, 4),
(2, 5),
(2, 13),
(2, 14),
(2, 15),
(2, 16),
(2, 17);

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
-- Estructura de tabla para la tabla `turnos_para_cada_centro`
--

CREATE TABLE `turnos_para_cada_centro` (
  `id` int(10) NOT NULL,
  `turno_id` int(10) NOT NULL,
  `centro_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `turnos_para_centro`
--

CREATE TABLE `turnos_para_centro` (
  `id` int(10) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `telefono` varchar(50) DEFAULT NULL,
  `hora_ini` time NOT NULL,
  `hora_fin` time NOT NULL,
  `dia` date NOT NULL,
  `borrado` int(10) NOT NULL,
  `centro_id` int(10) NOT NULL,
  `disponible` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `turnos_para_centro`
--

INSERT INTO `turnos_para_centro` (`id`, `nombre`, `apellido`, `email`, `telefono`, `hora_ini`, `hora_fin`, `dia`, `borrado`, `centro_id`, `disponible`) VALUES
(892, NULL, NULL, '', '', '09:00:00', '09:30:00', '2020-11-15', 1, 13, 1),
(893, NULL, NULL, 'probando.post@gmail.com', '2215930941', '09:30:00', '10:00:00', '2020-11-15', 1, 13, 0),
(894, NULL, NULL, 'probando.post@gmail.com', '2215930941', '10:00:00', '10:30:00', '2020-11-15', 1, 13, 0),
(895, NULL, NULL, 'admin@gmail.com', '33', '10:30:00', '11:00:00', '2020-11-15', 1, 13, 0),
(896, NULL, NULL, '', '', '11:00:00', '11:30:00', '2020-11-15', 1, 13, 1),
(897, NULL, NULL, 'probando.post@gmail.com', '2215930941', '11:30:00', '12:00:00', '2020-11-15', 1, 13, 0),
(898, NULL, NULL, '', '', '12:00:00', '12:30:00', '2020-11-15', 1, 13, 1),
(899, NULL, NULL, '', '', '12:30:00', '13:00:00', '2020-11-15', 1, 13, 1),
(900, NULL, NULL, '', '', '13:00:00', '13:30:00', '2020-11-15', 1, 13, 1),
(901, NULL, NULL, '', '', '13:30:00', '14:00:00', '2020-11-15', 1, 13, 1),
(902, NULL, NULL, '', '', '14:00:00', '14:30:00', '2020-11-15', 1, 13, 1),
(903, NULL, NULL, '', '', '14:30:00', '15:00:00', '2020-11-15', 1, 13, 1),
(904, NULL, NULL, '', '', '15:00:00', '15:30:00', '2020-11-15', 1, 13, 1),
(905, NULL, NULL, '', '', '15:30:00', '16:00:00', '2020-11-15', 1, 13, 1),
(906, NULL, NULL, '', '', '10:00:00', '10:30:00', '2020-11-19', 1, 1, 1),
(907, NULL, NULL, '', '', '10:30:00', '11:00:00', '2020-11-19', 1, 1, 1),
(908, NULL, NULL, '', '', '11:00:00', '11:30:00', '2020-11-19', 1, 1, 1),
(909, NULL, NULL, '', '', '11:30:00', '12:00:00', '2020-11-19', 1, 1, 1),
(910, NULL, NULL, '', '', '12:00:00', '12:30:00', '2020-11-19', 1, 1, 1),
(911, NULL, NULL, '', '', '12:30:00', '13:00:00', '2020-11-19', 1, 1, 1),
(912, NULL, NULL, '', '', '13:00:00', '13:30:00', '2020-11-19', 1, 1, 1),
(913, NULL, NULL, '', '', '13:30:00', '14:00:00', '2020-11-19', 1, 1, 1),
(914, NULL, NULL, '', '', '14:00:00', '14:30:00', '2020-11-19', 1, 1, 1),
(915, NULL, NULL, '', '', '14:30:00', '15:00:00', '2020-12-20', 1, 1, 1),
(916, NULL, NULL, '', '', '15:00:00', '15:30:00', '2020-12-20', 1, 1, 1),
(917, NULL, NULL, '', '', '15:30:00', '16:00:00', '2020-11-19', 1, 1, 1),
(918, NULL, NULL, '', '', '16:00:00', '16:30:00', '2020-11-19', 1, 1, 1),
(919, NULL, NULL, '', '', '16:30:00', '17:00:00', '2020-11-19', 1, 1, 1),
(920, NULL, NULL, '', '', '10:00:00', '10:30:00', '2020-12-26', 1, 4, 1),
(921, NULL, NULL, '', '', '09:00:00', '09:30:00', '2020-12-09', 1, 4, 1),
(922, NULL, NULL, '', '', '09:30:00', '10:00:00', '2020-12-09', 1, 4, 1),
(923, NULL, NULL, '', '', '10:00:00', '10:30:00', '2020-12-09', 1, 4, 1),
(924, NULL, NULL, '', '', '10:30:00', '11:00:00', '2020-12-09', 1, 4, 1),
(925, NULL, NULL, '', '', '11:00:00', '11:30:00', '2020-12-09', 1, 4, 1),
(926, NULL, NULL, '', '', '11:30:00', '12:00:00', '2020-12-09', 1, 4, 1),
(927, NULL, NULL, '', '', '12:00:00', '12:30:00', '2020-12-09', 1, 4, 1),
(928, NULL, NULL, '', '', '12:30:00', '13:00:00', '2020-12-09', 1, 4, 1),
(929, '', '', 'JUAN@GMAIL.COM', '2213334332', '08:00:00', '08:30:00', '2020-12-24', 1, 19, 0),
(930, NULL, NULL, 'post_funcionando@gmail.com', '2221100033312', '08:30:00', '09:00:00', '2020-12-24', 1, 19, 0),
(931, NULL, NULL, '', '222223324324234', '09:00:00', '09:30:00', '2020-12-24', 1, 19, 0),
(932, NULL, NULL, 'dario@gmail.com', '22123432212', '09:30:00', '10:00:00', '2020-12-24', 1, 19, 0),
(933, NULL, NULL, '', '', '10:00:00', '10:30:00', '2020-12-17', 1, 5, 1),
(934, NULL, NULL, '', '', '10:30:00', '11:00:00', '2020-12-17', 1, 5, 1),
(935, NULL, NULL, '', '', '11:00:00', '11:30:00', '2020-12-17', 1, 5, 1),
(936, NULL, NULL, '', '', '11:30:00', '12:00:00', '2020-12-17', 1, 5, 1),
(937, NULL, NULL, '', '', '12:00:00', '12:30:00', '2020-12-17', 1, 5, 1),
(938, NULL, NULL, '', '', '12:30:00', '13:00:00', '2020-12-17', 1, 5, 1),
(939, NULL, NULL, '', '', '13:00:00', '13:30:00', '2020-12-17', 1, 5, 1),
(940, NULL, NULL, 'hugo@gmail.com', '2216265422', '13:30:00', '14:00:00', '2020-12-17', 1, 5, 0),
(941, NULL, NULL, '', '', '09:00:00', '09:30:00', '2020-12-18', 1, 32, 1),
(942, NULL, NULL, '', '', '09:30:00', '10:00:00', '2020-12-18', 1, 32, 1),
(943, NULL, NULL, '', '', '10:00:00', '10:30:00', '2020-12-18', 1, 32, 1),
(944, NULL, NULL, '', '', '10:30:00', '11:00:00', '2020-12-18', 1, 32, 1),
(945, NULL, NULL, '', '', '11:00:00', '11:30:00', '2020-12-18', 1, 32, 1),
(946, NULL, NULL, '', '', '11:30:00', '12:00:00', '2020-12-18', 1, 32, 1),
(947, NULL, NULL, '', '', '12:00:00', '12:30:00', '2020-12-18', 1, 32, 1),
(948, NULL, NULL, '', '', '12:30:00', '13:00:00', '2020-12-18', 1, 32, 1),
(949, NULL, NULL, '', '', '13:00:00', '13:30:00', '2020-12-18', 1, 32, 1),
(950, NULL, NULL, '', '', '13:30:00', '14:00:00', '2020-12-18', 1, 32, 1),
(951, NULL, NULL, '', '', '14:00:00', '14:30:00', '2020-12-18', 1, 32, 1),
(952, NULL, NULL, '', '', '14:30:00', '15:00:00', '2020-12-18', 1, 32, 1),
(953, NULL, NULL, '', '', '15:00:00', '15:30:00', '2020-12-18', 1, 32, 1),
(954, NULL, NULL, '', '', '15:30:00', '16:00:00', '2020-12-18', 1, 32, 1),
(955, NULL, NULL, '', '', '08:00:00', '08:30:00', '2021-01-04', 1, 19, 1),
(956, NULL, NULL, '', '', '08:30:00', '09:00:00', '2021-01-04', 1, 19, 1),
(957, NULL, NULL, '', '', '09:00:00', '09:30:00', '2021-01-04', 1, 19, 1),
(958, NULL, NULL, '', '', '09:30:00', '10:00:00', '2021-01-04', 1, 19, 1),
(959, NULL, NULL, '', '', '10:00:00', '10:30:00', '2021-01-04', 1, 19, 1),
(960, NULL, NULL, '', '', '10:30:00', '11:00:00', '2021-01-04', 1, 19, 1),
(961, NULL, NULL, '', '', '11:00:00', '11:30:00', '2021-01-04', 1, 19, 1),
(962, NULL, NULL, '', '', '11:30:00', '12:00:00', '2021-01-04', 1, 19, 1),
(963, NULL, NULL, '', '', '12:00:00', '12:30:00', '2021-01-04', 1, 19, 1),
(964, NULL, NULL, '', '', '12:30:00', '13:00:00', '2021-01-04', 1, 19, 1);

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
  `historico` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `usuario`, `clave`, `nombre`, `apellido`, `email`, `activo`, `fecha_creacion`, `fecha_actualizacion`, `historico`) VALUES
(8, 'admin', '1234', 'Homero', 'Simpson', 'hsimpson@gmail.com', 1, '2020-10-18', '2020-10-18', 0),
(11, 'usuario', '1234', 'Ned', 'Flanders', 'flanders15@gmail.com', 1, '2020-10-18', '2020-10-18', 0),
(13, 'nuevo', '1234', 'new', 'new', 'new@gmail.com', 1, '2020-10-24', '2020-10-24', 1),
(19, 'Pantera', '1234', 'sara', 'sars', 'sara@gmail.commm', 1, '2020-10-30', '2020-10-30', 0),
(20, 'Operador', '1234', 'Julio', 'Domingo', 'julio@gmail.com', 0, '2020-11-14', '2020-11-14', 0),
(21, 'UsuarioNuevo', '1234', 'Us', 'Nue', 'us@nu', 1, '2020-12-17', '2020-12-17', 0),
(22, 'Nuevo User', '1234', 'Nuevo', 'User', 'nuevo@user', 1, '2020-12-26', '2020-12-26', 0);

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
(11, 1),
(19, 1),
(20, 2);

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
-- Indices de la tabla `turnos_para_cada_centro`
--
ALTER TABLE `turnos_para_cada_centro`
  ADD PRIMARY KEY (`id`);

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
  MODIFY `id` int(35) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;
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
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=136;
--
-- AUTO_INCREMENT de la tabla `permiso`
--
ALTER TABLE `permiso`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
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
-- AUTO_INCREMENT de la tabla `turnos_para_cada_centro`
--
ALTER TABLE `turnos_para_cada_centro`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `turnos_para_centro`
--
ALTER TABLE `turnos_para_centro`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=965;
--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
