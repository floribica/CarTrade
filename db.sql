-- MySQL dump 10.13  Distrib 8.3.0, for macos14.2 (arm64)
--
-- Host: localhost    Database: AlbaniaCar
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;

/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;

/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;

/*!50503 SET NAMES utf8mb4 */;

/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;

/*!40103 SET TIME_ZONE='+00:00' */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;

/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `AlbaniaCar`
--

/*!40000 DROP DATABASE IF EXISTS `AlbaniaCar`*/;

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `ALBANIACAR` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `ALBANIACAR`;

--
-- Table structure for table `car_images`
--

DROP TABLE IF EXISTS `CAR_IMAGES`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!50503 SET character_set_client = utf8mb4 */;

CREATE TABLE `CAR_IMAGES` (
  `IMAGE_ID` INT NOT NULL AUTO_INCREMENT,
  `CAR_ID` INT NOT NULL,
  `IMAGE_URL` VARCHAR(255) NOT NULL,
  `CREATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `UPDATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`IMAGE_ID`),
  KEY `CAR_ID` (`CAR_ID`),
  CONSTRAINT `CAR_IMAGES_IBFK_1` FOREIGN KEY (`CAR_ID`) REFERENCES `CARS` (`CAR_ID`) ON DELETE CASCADE
) ENGINE=INNODB AUTO_INCREMENT=16 DEFAULT CHARSET=UTF8MB4 COLLATE=UTF8MB4_0900_AI_CI;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car_images`
--

LOCK TABLES `CAR_IMAGES` WRITE;

/*!40000 ALTER TABLE `car_images` DISABLE KEYS */;

INSERT INTO `CAR_IMAGES` VALUES (
  10,
  32,
  '1725388288.631991img1.jpeg',
  '2024-09-03 20:31:28',
  '2024-09-03 20:31:28'
),
(
  11,
  32,
  '1725388288.636156img2.jpeg',
  '2024-09-03 20:31:28',
  '2024-09-03 20:31:28'
),
(
  12,
  32,
  '1725388288.640406img3.jpeg',
  '2024-09-03 20:31:28',
  '2024-09-03 20:31:28'
);

/*!40000 ALTER TABLE `car_images` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `cars`
--

DROP TABLE IF EXISTS `CARS`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!50503 SET character_set_client = utf8mb4 */;

CREATE TABLE `CARS` (
  `CAR_ID` INT NOT NULL AUTO_INCREMENT,
  `YEAR` INT NOT NULL,
  `BRAND` VARCHAR(225) NOT NULL,
  `MODEL` VARCHAR(225) NOT NULL,
  `STYLE` VARCHAR(225) NOT NULL,
  `CONDITION` VARCHAR(225) NOT NULL,
  `PRICE` INT NOT NULL,
  `KM` INT NOT NULL,
  `CREATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `UPDATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `IMAGE` VARCHAR(255) DEFAULT NULL,
  `DESCRIPTION` TEXT,
  PRIMARY KEY (`CAR_ID`)
) ENGINE=INNODB AUTO_INCREMENT=51 DEFAULT CHARSET=UTF8MB4 COLLATE=UTF8MB4_0900_AI_CI;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cars`
--

LOCK TABLES `CARS` WRITE;

/*!40000 ALTER TABLE `cars` DISABLE KEYS */;

INSERT INTO `CARS` VALUES (
  2,
  2021,
  'BMW',
  '3 Series',
  'Sedan',
  'New',
  42000,
  1000,
  'nkfsdlsdf.jpg',
  'A sleek and modern sedan with advanced features.',
  200,
  1
),
(
  3,
  2019,
  'Audi',
  'A4',
  'Sedan',
  'Used',
  35000,
  15000,
  'maxresdefault.jpg',
  'A stylish and reliable sedan with premium features.',
  300,
  1
),
(
  4,
  2022,
  'Mercedes-Benz',
  'C-Class',
  'Coupe',
  'New',
  50000,
  500,
  'mb2019cclasscoupe77181934_600.jpg',
  'A luxury coupe with cutting-edge technology.',
  250,
  1
),
(
  5,
  2020,
  'Porsche',
  '911',
  'Convertible',
  'Used',
  90000,
  8000,
  'Used-2021-PORS8526.jpg',
  'A high-performance convertible sports car.',
  300,
  1
),
(
  6,
  2021,
  'Lamborghini',
  'Huracan',
  'Coupe',
  'New',
  220000,
  200,
  'Used-2021Huracan-70100.jpg',
  'A stunning supercar with incredible speed.',
  250,
  1
),
(
  7,
  2018,
  'Ferrari',
  '488',
  'Coupe',
  'Used',
  250000,
  12000,
  '488-1.jpg',
  'A legendary supercar with unmatched performance.',
  300,
  1
),
(
  8,
  2023,
  'Audi',
  'Q7',
  'SUV',
  'New',
  75000,
  100,
  'maxresdefault-2.jpg',
  'A luxurious and spacious SUV for the whole family.',
  200,
  1
),
(
  9,
  2022,
  'Mercedes-Benz',
  'G-Class',
  'SUV',
  'New',
  130000,
  500,
  'Used-2022-Mercedes-Benz-G-Class-AMG-G-63.jpg',
  'An iconic and powerful off-road SUV.',
  250,
  1
),
(
  10,
  2021,
  'BMW',
  'X5',
  'SUV',
  'Used',
  60000,
  8000,
  '2021-bmw-x5-phev-2.jpg',
  'A versatile and luxurious mid-size SUV.',
  200,
  1
),
(
  11,
  2020,
  'Porsche',
  'Cayenne',
  'SUV',
  'Used',
  70000,
  15000,
  '2020-porsche-cayenne-turbo-s-e-hybrid.jpeg',
  'A sporty and luxurious SUV with excellent handling.',
  250,
  1
),
(
  12,
  2019,
  'Lamborghini',
  'Urus',
  'SUV',
  'Used',
  180000,
  10000,
  '37gb6jep-Wq7xC-JXFU-(edit).jpg',
  'A super SUV that combines luxury and performance.',
  300,
  1
),
(
  13,
  2023,
  'Ferrari',
  'SF90',
  'Coupe',
  'New',
  500000,
  50,
  'Used-2023-Ferrari-SF90-Stradale-1701737930.jpg',
  'A hybrid supercar with unmatched power and speed.',
  250,
  1
),
(
  14,
  2022,
  'BMW',
  'M4',
  'Coupe',
  'New',
  75000,
  1000,
  '2-tiny-1200x0.png',
  'A high-performance coupe with thrilling driving dynamics.',
  400,
  1
),
(
  15,
  2020,
  'Audi',
  'RS7',
  'Sedan',
  'Used',
  90000,
  12000,
  '889ccb3cbbbd485293b8a9c8fc405ea9.jpg',
  'A powerful and luxurious performance sedan.',
  300,
  1
),
(
  16,
  2019,
  'Porsche',
  'Panamera',
  'Sedan',
  'Used',
  95000,
  18000,
  'IMG_3251-tiny-2048x0-0.5x0.jpg',
  'A luxurious and sporty sedan with dynamic performance.',
  250,
  1
),
(
  17,
  2023,
  'Lamborghini',
  'Aventador',
  'Coupe',
  'New',
  400000,
  100,
  '2023_Lamborghini_Aventador_Ultimae.jpg',
  'An iconic supercar with breathtaking design and speed.',
  300,
  1
),
(
  18,
  2021,
  'Ferrari',
  'Roma',
  'Coupe',
  'New',
  220000,
  3000,
  'i3rksb1b0x3q09xkyryzrym9qju4ew.jpg',
  'A sleek and elegant GT with impressive performance.',
  250,
  1
),
(
  19,
  2018,
  'BMW',
  'i8',
  'Coupe',
  'Used',
  80000,
  25000,
  'Grey-Blue-i8-8.jpg',
  'A futuristic hybrid sports car with striking design.',
  200,
  1
),
(
  20,
  2022,
  'Audi',
  'R8',
  'Coupe',
  'New',
  170000,
  500,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  '2022_audi_r8-performance.jpeg.webp',
  'A high-performance supercar with a V10 engine.'
),
(
  21,
  2020,
  'Mercedes-Benz',
  'E-Class',
  'Convertible',
  'Used',
  60000,
  10000,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  'mb2019eclasscabriolet75380928_600.jpg',
  'A luxurious convertible with a smooth ride.'
),
(
  22,
  2021,
  'Porsche',
  'Taycan',
  'Sedan',
  'New',
  130000,
  2000,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  'hi4a6704.jpg.webp',
  'An all-electric sports sedan with incredible acceleration.'
),
(
  23,
  2022,
  'BMW',
  'X7',
  'SUV',
  'New',
  90000,
  500,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  'The-BMW-X7.jpg',
  'A large luxury SUV with seating for seven.'
),
(
  24,
  2019,
  'Audi',
  'A8',
  'Sedan',
  'Used',
  75000,
  12000,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  '2019-audi-a8-first-drive.jpg',
  'A flagship luxury sedan with advanced technology.'
),
(
  25,
  2023,
  'Mercedes-Benz',
  'AMG GT',
  'Coupe',
  'New',
  160000,
  100,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  '2023-mercedes-amg-gt-coupe-renderings.jpg',
  'A high-performance coupe with aggressive styling.'
),
(
  26,
  2020,
  'Lamborghini',
  'Huracan Evo',
  'Coupe',
  'Used',
  210000,
  8000,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  '2020-lamborghini-huracan-evo-spyder-review-7.jpg',
  'Updated version with improved aerodynamics.'
),
(
  27,
  2021,
  'Ferrari',
  '812 Superfast',
  'Coupe',
  'New',
  350000,
  1500,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  '7d90eef6356146c4bf0c02a05a5c7099.jpg',
  'A front-engine supercar with a powerful V12 engine.'
),
(
  28,
  2022,
  'BMW',
  'Z4',
  'Convertible',
  'New',
  65000,
  500,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  '1356_main_l.jpg',
  'A sporty and stylish convertible with agile handling.'
),
(
  29,
  2019,
  'Audi',
  'TT',
  'Coupe',
  'Used',
  40000,
  15000,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  '2018-paris-motor-show-images-2019-audi-tt-roadster-e389.jpg',
  'A sports coupe with a turbocharged engine.'
),
(
  30,
  2023,
  'Porsche',
  'Boxster',
  'Convertible',
  'New',
  80000,
  100,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  '2022-porsche-7.jpg',
  'A mid-engine convertible with precise handling.'
),
(
  31,
  2022,
  'Mercedes-Benz',
  'SL',
  'Convertible',
  'New',
  110000,
  1000,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  '-1x-1.jpg',
  'A luxurious roadster with a retractable hardtop.'
),
(
  32,
  2013,
  'Lamborghini',
  'Gallardo',
  'Coupe',
  'Used',
  160000,
  12000,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  'lamborghini-gallardo-522017-1-1.jpg',
  'A classic supercar with a powerful V10 engine.'
),
(
  33,
  2022,
  'BMW',
  'M8',
  'Coupe',
  'New',
  140000,
  500,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  'maxresdefault-3.jpg',
  'A high-performance luxury coupe with a twin-turbo V8.'
),
(
  34,
  2019,
  'Audi',
  'Q5',
  'SUV',
  'Used',
  40000,
  20000,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  'IMG_2486.jpg',
  'A compact luxury SUV with quattro all-wheel drive.'
),
(
  35,
  2023,
  'Mercedes-Benz',
  'GLE',
  'SUV',
  'New',
  85000,
  300,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  '2023_Mercedes-Benz_GLE-Class_review_summary.jpeg',
  'A midsize luxury SUV with advanced features.'
),
(
  36,
  2020,
  'Porsche',
  'Macan',
  'SUV',
  'Used',
  60000,
  15000,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  '2020-porsche-macan-turbo-1.jpg.webp',
  'A compact SUV with sporty handling and luxury amenities.'
),
(
  37,
  2021,
  'Lamborghini',
  'Aventador SVJ',
  'Coupe',
  'New',
  450000,
  200,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  '11f98cf5d67c3b2f468ec0b783d9acd2.jpg',
  'A supercar with extreme performance.'
),
(
  38,
  2022,
  'Ferrari',
  'F8 Tributo',
  'Coupe',
  'New',
  330000,
  800,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  'Ferrari_F8_Tributo_4b.jpg',
  'A mid-engine supercar with breathtaking speed.'
),
(
  39,
  2018,
  'BMW',
  '7 Series',
  'Sedan',
  'Used',
  60000,
  30000,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  'BMW.jpg',
  'A full-size luxury sedan with a smooth and powerful ride.'
),
(
  40,
  2023,
  'Audi',
  'RS Q8',
  'SUV',
  'New',
  130000,
  100,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  'hi4a2076.jpg.webp',
  'A high-performance SUV with aggressive styling.'
),
(
  41,
  2022,
  'Mercedes-Benz',
  'GLS',
  'SUV',
  'New',
  100000,
  400,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  'obsidian-black-metallic.png',
  'A full-size luxury SUV with three rows of seating.'
),
(
  42,
  2021,
  'Porsche',
  '718 Cayman',
  'Coupe',
  'New',
  70000,
  1000,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  '2022-porsche-718-c.jpg',
  'A mid-engine sports coupe with sharp handling.'
),
(
  43,
  2004,
  'Lamborghini',
  'Murcielago',
  'Coupe',
  'Used',
  300000,
  15000,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  'lamborghini-murcielago-lp640-c665930072019063300_2.jpg',
  'A supercar with a V12 engine.'
),
(
  44,
  2020,
  'Ferrari',
  'GTC4Lusso',
  'Hatchback',
  'Used',
  280000,
  10000,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  '160491-car_ferrari-gtc4lusso.jpg',
  'A four-seater grand tourer with all-wheel drive.'
),
(
  45,
  2022,
  'BMW',
  'X6',
  'SUV',
  'New',
  90000,
  500,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  '4ddb8523ea6c602d22a924e85e6b04b7.jpg',
  'A coupe-style SUV with sporty handling and luxury features.'
),
(
  46,
  2021,
  'Audi',
  'e-tron GT',
  'Sedan',
  'New',
  100000,
  2000,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  'Audi_RS_e-tron_GT.jpg',
  'An all-electric performance sedan with stunning design.'
),
(
  47,
  2020,
  'Mercedes-Benz',
  'Maybach S-Class',
  'Sedan',
  'Used',
  180000,
  12000,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  'mercedes-maybach-s-class-sindelfingen-2020-09.jpg',
  'A luxurious car with VIP features.'
),
(
  48,
  2023,
  'Porsche',
  '911 Turbo S',
  'Coupe',
  'New',
  220000,
  100,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  '2021-porsche-911-turbo-s-td-03-di.jpg',
  'A high-performance version of the iconic 911.'
),
(
  49,
  2022,
  'Lamborghini',
  'Sian',
  'Coupe',
  'New',
  3500000,
  50,
  '2024-08-29 21:20:53',
  '2024-08-29 21:20:53',
  'Lamborghini-SIAN-FKP-37-.jpg',
  'A hybrid supercar with futuristic design and extreme power.'
),
(
  50,
  2024,
  'Rolls-Royce',
  'EWB - MANSORY Diamond Edition',
  'Phantom',
  'used',
  4300000,
  100,
  '2024-09-01 13:49:18',
  '2024-09-01 14:58:33',
  '1725191340.001969Phantom_black.webp',
  'Carbon fiber exterior, customized sporty interior.'
);

/*!40000 ALTER TABLE `cars` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `COMMENTS`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!50503 SET character_set_client = utf8mb4 */;

CREATE TABLE `COMMENTS` (
  `COMMENT_ID` INT NOT NULL AUTO_INCREMENT,
  `CONTENT` VARCHAR(225) NOT NULL,
  `CREATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `UPDATED_AT` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `USER_ID` INT NOT NULL,
  PRIMARY KEY (`COMMENT_ID`),
  KEY `USER_ID` (`USER_ID`),
  CONSTRAINT `COMMENTS_IBFK_1` FOREIGN KEY (`USER_ID`) REFERENCES `USERS` (`USER_ID`)
) ENGINE=INNODB AUTO_INCREMENT=8 DEFAULT CHARSET=UTF8MB4 COLLATE=UTF8MB4_0900_AI_CI;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `COMMENTS` WRITE;

/*!40000 ALTER TABLE `comments` DISABLE KEYS */;

INSERT INTO `COMMENTS` VALUES (
  5,
  'The Audi that i bought was in great condition for a used car. Defenitely recommend',
  '2024-09-03 14:09:17',
  '2024-09-03 14:09:17',
  5
),
(
  6,
  'The car was great and on top condition and the staff were very helpful',
  '2024-09-03 14:15:05',
  '2024-09-03 14:15:05',
  6
),
(
  7,
  'Great all around environment, very professional and helpful  ',
  '2024-09-03 14:17:48',
  '2024-09-03 14:17:48',
  7
);

/*!40000 ALTER TABLE `comments` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `ROLES`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!50503 SET character_set_client = utf8mb4 */;

CREATE TABLE `ROLES` (
  `ROLE_ID` INT NOT NULL AUTO_INCREMENT,
  `TYPE` VARCHAR(225) NOT NULL,
  `CREATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `UPDATED_AT()` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ROLE_ID`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4 COLLATE=UTF8MB4_0900_AI_CI;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `ROLES` WRITE;

/*!40000 ALTER TABLE `roles` DISABLE KEYS */;

/*!40000 ALTER TABLE `roles` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `USERS`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!50503 SET character_set_client = utf8mb4 */;

CREATE TABLE `USERS` (
  `USER_ID` INT NOT NULL AUTO_INCREMENT,
  `FIRST_NAME` VARCHAR(225) NOT NULL,
  `LAST_NAME` VARCHAR(225) NOT NULL,
  `EMAIL` VARCHAR(225) NOT NULL,
  `PASSWORD` VARCHAR(225) NOT NULL,
  `CREATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `UPDATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ROLE_ID` INT DEFAULT NULL,
  PRIMARY KEY (`USER_ID`),
  UNIQUE KEY `EMAIL_UNIQUE` (`EMAIL`),
  KEY `FK_USER_ROLE` (`ROLE_ID`),
  CONSTRAINT `FK_USER_ROLE` FOREIGN KEY (`ROLE_ID`) REFERENCES `ROLES` (`ROLE_ID`)
) ENGINE=INNODB AUTO_INCREMENT=8 DEFAULT CHARSET=UTF8MB4 COLLATE=UTF8MB4_0900_AI_CI;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `USERS` WRITE;

/*!40000 ALTER TABLE `users` DISABLE KEYS */;

INSERT INTO `USERS` VALUES (
  1,
  'Flori',
  'Bica',
  'bicaflori135@gmail.com',
  '$2b$12$fwCCt1V60SYI0o8CVrIujeitT4RTnGEgsaNLpp.c45i4lg6WHtAuu',
  '2024-08-29 18:19:39',
  '2024-08-29 18:41:34',
  NULL
),
(
  2,
  'test',
  'test',
  'test@test.com',
  '$2b$12$fwCCt1V60SYI0o8CVrIujeitT4RTnGEgsaNLpp.c45i4lg6WHtAuu',
  '2024-08-25 10:07:24',
  '2024-08-29 18:41:47',
  NULL
),
(
  5,
  'toni',
  'xhukellari',
  'abc@gmail.com',
  '$2b$12$IJp/VkmTFmBRz8cSJ.c2OOwXP6IPSrogglHfCQZAzSooqT2eA4LwO',
  '2024-09-03 14:04:07',
  '2024-09-03 14:04:07',
  NULL
),
(
  6,
  'John',
  'William',
  'abcd@gmail.com',
  '$2b$12$skCXfN4X0yOf1p5TUsls5uSpAxpNeuYFirUWKKbozU.PZWfE7F8.K',
  '2024-09-03 14:14:12',
  '2024-09-03 14:14:12',
  NULL
),
(
  7,
  'Giulio',
  'Agalliu',
  'abcde@gmail.com',
  '$2b$12$vg9oxq.f4eK4vuLB.AqE3e9sNNgAu0d3s3gf/CKvpW/IBUveNgK2O',
  '2024-09-03 14:16:04',
  '2024-09-03 14:16:04',
  NULL
);

/*!40000 ALTER TABLE `users` ENABLE KEYS */;

UNLOCK TABLES;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;

/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;

/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;

/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;

/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-12 10:23:57