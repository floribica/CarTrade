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
-- Table structure for table `car_images`
--

DROP TABLE IF EXISTS `car_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car_images` (
  `image_id` int NOT NULL AUTO_INCREMENT,
  `car_id` int NOT NULL,
  `image_url` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`image_id`),
  KEY `car_id` (`car_id`),
  CONSTRAINT `car_images_ibfk_1` FOREIGN KEY (`car_id`) REFERENCES `cars` (`car_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car_images`
--

LOCK TABLES `car_images` WRITE;
/*!40000 ALTER TABLE `car_images` DISABLE KEYS */;
/*!40000 ALTER TABLE `car_images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cars`
--

DROP TABLE IF EXISTS `cars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cars` (
  `car_id` int NOT NULL AUTO_INCREMENT,
  `year` int NOT NULL,
  `brand` varchar(225) NOT NULL,
  `model` varchar(225) NOT NULL,
  `style` varchar(225) NOT NULL,
  `condition` varchar(225) NOT NULL,
  `price` int NOT NULL,
  `km` int NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `image` varchar(255) DEFAULT NULL,
  `DESCRIPTION` text,
  PRIMARY KEY (`car_id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cars`
--

LOCK TABLES `cars` WRITE;
/*!40000 ALTER TABLE `cars` DISABLE KEYS */;
INSERT INTO `cars` VALUES (2,2021,'BMW','3 Series','Sedan','New',42000,1000,'2024-08-29 21:20:53','2024-08-29 21:20:53','nkfsdlsdf.jpg','A sleek and modern sedan with advanced features.'),(3,2019,'Audi','A4','Sedan','Used',35000,15000,'2024-08-29 21:20:53','2024-08-31 16:30:02','maxresdefault.jpg','A stylish and reliable sedan with premium features.'),(4,2022,'Mercedes-Benz','C-Class','Coupe','New',50000,500,'2024-08-29 21:20:53','2024-08-29 21:20:53','mb2019cclasscoupe77181934_600.jpg','A luxury coupe with cutting-edge technology.'),(5,2020,'Porsche','911','Convertible','Used',90000,8000,'2024-08-29 21:20:53','2024-08-29 21:20:53','Used-2021-PORS8526.jpg','A high-performance convertible sports car.'),(6,2021,'Lamborghini','Huracan','Coupe','New',220000,200,'2024-08-29 21:20:53','2024-08-29 21:20:53','Used-2021Huracan-70100.jpg','A stunning supercar with incredible speed.'),(7,2018,'Ferrari','488','Coupe','Used',250000,12000,'2024-08-29 21:20:53','2024-08-29 21:20:53','488-1.jpg','A legendary supercar with unmatched performance.'),(8,2023,'Audi','Q7','SUV','New',75000,100,'2024-08-29 21:20:53','2024-08-29 21:20:53','maxresdefault-2.jpg','A luxurious and spacious SUV for the whole family.'),(9,2022,'Mercedes-Benz','G-Class','SUV','New',130000,500,'2024-08-29 21:20:53','2024-08-29 21:20:53','Used-2022-Mercedes-Benz-G-Class-AMG-G-63.jpg','An iconic and powerful off-road SUV.'),(10,2021,'BMW','X5','SUV','Used',60000,8000,'2024-08-29 21:20:53','2024-08-29 21:20:53','2021-bmw-x5-phev-2.jpg','A versatile and luxurious mid-size SUV.'),(11,2020,'Porsche','Cayenne','SUV','Used',70000,15000,'2024-08-29 21:20:53','2024-08-29 21:20:53','2020-porsche-cayenne-turbo-s-e-hybrid.jpeg','A sporty and luxurious SUV with excellent handling.'),(12,2019,'Lamborghini','Urus','SUV','Used',180000,10000,'2024-08-29 21:20:53','2024-08-29 21:20:53','37gb6jep-Wq7xC-JXFU-(edit).jpg','A super SUV that combines luxury and performance.'),(13,2023,'Ferrari','SF90','Coupe','New',500000,50,'2024-08-29 21:20:53','2024-08-29 21:20:53','Used-2023-Ferrari-SF90-Stradale-1701737930.jpg','A hybrid supercar with unmatched power and speed.'),(14,2022,'BMW','M4','Coupe','New',75000,1000,'2024-08-29 21:20:53','2024-08-29 21:20:53','2-tiny-1200x0.png','A high-performance coupe with thrilling driving dynamics.'),(15,2020,'Audi','RS7','Sedan','Used',90000,12000,'2024-08-29 21:20:53','2024-08-29 21:20:53','889ccb3cbbbd485293b8a9c8fc405ea9.jpg','A powerful and luxurious performance sedan.'),(16,2019,'Porsche','Panamera','Sedan','Used',95000,18000,'2024-08-29 21:20:53','2024-08-29 21:20:53','IMG_3251-tiny-2048x0-0.5x0.jpg','A luxurious and sporty sedan with dynamic performance.'),(17,2023,'Lamborghini','Aventador','Coupe','New',400000,100,'2024-08-29 21:20:53','2024-08-29 21:20:53','2023_Lamborghini_Aventador_Ultimae.jpg','An iconic supercar with breathtaking design and speed.'),(18,2021,'Ferrari','Roma','Coupe','New',220000,3000,'2024-08-29 21:20:53','2024-08-29 21:20:53','i3rksb1b0x3q09xkyryzrym9qju4ew.jpg','A sleek and elegant GT with impressive performance.'),(19,2018,'BMW','i8','Coupe','Used',80000,25000,'2024-08-29 21:20:53','2024-08-29 21:20:53','Grey-Blue-i8-8.jpg','A futuristic hybrid sports car with striking design.'),(20,2022,'Audi','R8','Coupe','New',170000,500,'2024-08-29 21:20:53','2024-08-29 21:20:53','2022_audi_r8-performance.jpeg.webp','A high-performance supercar with a V10 engine.'),(21,2020,'Mercedes-Benz','E-Class','Convertible','Used',60000,10000,'2024-08-29 21:20:53','2024-08-29 21:20:53','mb2019eclasscabriolet75380928_600.jpg','A luxurious convertible with a smooth ride.'),(22,2021,'Porsche','Taycan','Sedan','New',130000,2000,'2024-08-29 21:20:53','2024-08-29 21:20:53','hi4a6704.jpg.webp','An all-electric sports sedan with incredible acceleration.'),(23,2022,'BMW','X7','SUV','New',90000,500,'2024-08-29 21:20:53','2024-08-29 21:20:53','The-BMW-X7.jpg','A large luxury SUV with seating for seven.'),(24,2019,'Audi','A8','Sedan','Used',75000,12000,'2024-08-29 21:20:53','2024-08-29 21:20:53','2019-audi-a8-first-drive.jpg','A flagship luxury sedan with advanced technology.'),(25,2023,'Mercedes-Benz','AMG GT','Coupe','New',160000,100,'2024-08-29 21:20:53','2024-08-29 21:20:53','2023-mercedes-amg-gt-coupe-renderings.jpg','A high-performance coupe with aggressive styling.'),(26,2020,'Lamborghini','Huracan Evo','Coupe','Used',210000,8000,'2024-08-29 21:20:53','2024-08-29 21:20:53','2020-lamborghini-huracan-evo-spyder-review-7.jpg','Updated version with improved aerodynamics.'),(27,2021,'Ferrari','812 Superfast','Coupe','New',350000,1500,'2024-08-29 21:20:53','2024-08-29 21:20:53','7d90eef6356146c4bf0c02a05a5c7099.jpg','A front-engine supercar with a powerful V12 engine.'),(28,2022,'BMW','Z4','Convertible','New',65000,500,'2024-08-29 21:20:53','2024-08-29 21:20:53','1356_main_l.jpg','A sporty and stylish convertible with agile handling.'),(29,2019,'Audi','TT','Coupe','Used',40000,15000,'2024-08-29 21:20:53','2024-08-29 21:20:53','2018-paris-motor-show-images-2019-audi-tt-roadster-e389.jpg','A sports coupe with a turbocharged engine.'),(30,2023,'Porsche','Boxster','Convertible','New',80000,100,'2024-08-29 21:20:53','2024-08-29 21:20:53','2022-porsche-7.jpg','A mid-engine convertible with precise handling.'),(31,2022,'Mercedes-Benz','SL','Convertible','New',110000,1000,'2024-08-29 21:20:53','2024-08-29 21:20:53','-1x-1.jpg','A luxurious roadster with a retractable hardtop.'),(32,2013,'Lamborghini','Gallardo','Coupe','Used',160000,12000,'2024-08-29 21:20:53','2024-08-29 21:20:53','lamborghini-gallardo-522017-1-1.jpg','A classic supercar with a powerful V10 engine.'),(33,2022,'BMW','M8','Coupe','New',140000,500,'2024-08-29 21:20:53','2024-08-29 21:20:53','maxresdefault-3.jpg','A high-performance luxury coupe with a twin-turbo V8.'),(34,2019,'Audi','Q5','SUV','Used',40000,20000,'2024-08-29 21:20:53','2024-08-29 21:20:53','IMG_2486.jpg','A compact luxury SUV with quattro all-wheel drive.'),(35,2023,'Mercedes-Benz','GLE','SUV','New',85000,300,'2024-08-29 21:20:53','2024-08-29 21:20:53','2023_Mercedes-Benz_GLE-Class_review_summary.jpeg','A midsize luxury SUV with advanced features.'),(36,2020,'Porsche','Macan','SUV','Used',60000,15000,'2024-08-29 21:20:53','2024-08-29 21:20:53','2020-porsche-macan-turbo-1.jpg.webp','A compact SUV with sporty handling and luxury amenities.'),(37,2021,'Lamborghini','Aventador SVJ','Coupe','New',450000,200,'2024-08-29 21:20:53','2024-08-29 21:20:53','11f98cf5d67c3b2f468ec0b783d9acd2.jpg','A supercar with extreme performance.'),(38,2022,'Ferrari','F8 Tributo','Coupe','New',330000,800,'2024-08-29 21:20:53','2024-08-29 21:20:53','Ferrari_F8_Tributo_4b.jpg','A mid-engine supercar with breathtaking speed.'),(39,2018,'BMW','7 Series','Sedan','Used',60000,30000,'2024-08-29 21:20:53','2024-08-29 21:20:53','BMW.jpg','A full-size luxury sedan with a smooth and powerful ride.'),(40,2023,'Audi','RS Q8','SUV','New',130000,100,'2024-08-29 21:20:53','2024-08-29 21:20:53','hi4a2076.jpg.webp','A high-performance SUV with aggressive styling.'),(41,2022,'Mercedes-Benz','GLS','SUV','New',100000,400,'2024-08-29 21:20:53','2024-08-29 21:20:53','obsidian-black-metallic.png','A full-size luxury SUV with three rows of seating.'),(42,2021,'Porsche','718 Cayman','Coupe','New',70000,1000,'2024-08-29 21:20:53','2024-08-29 21:20:53','2022-porsche-718-c.jpg','A mid-engine sports coupe with sharp handling.'),(43,2004,'Lamborghini','Murcielago','Coupe','Used',300000,15000,'2024-08-29 21:20:53','2024-08-29 21:20:53','lamborghini-murcielago-lp640-c665930072019063300_2.jpg','A supercar with a V12 engine.'),(44,2020,'Ferrari','GTC4Lusso','Hatchback','Used',280000,10000,'2024-08-29 21:20:53','2024-08-29 21:20:53','160491-car_ferrari-gtc4lusso.jpg','A four-seater grand tourer with all-wheel drive.'),(45,2022,'BMW','X6','SUV','New',90000,500,'2024-08-29 21:20:53','2024-08-29 21:20:53','4ddb8523ea6c602d22a924e85e6b04b7.jpg','A coupe-style SUV with sporty handling and luxury features.'),(46,2021,'Audi','e-tron GT','Sedan','New',100000,2000,'2024-08-29 21:20:53','2024-08-29 21:20:53','Audi_RS_e-tron_GT.jpg','An all-electric performance sedan with stunning design.'),(47,2020,'Mercedes-Benz','Maybach S-Class','Sedan','Used',180000,12000,'2024-08-29 21:20:53','2024-08-29 21:20:53','mercedes-maybach-s-class-sindelfingen-2020-09.jpg','A luxurious car with VIP features.'),(48,2023,'Porsche','911 Turbo S','Coupe','New',220000,100,'2024-08-29 21:20:53','2024-08-29 21:20:53','2021-porsche-911-turbo-s-td-03-di.jpg','A high-performance version of the iconic 911.'),(49,2022,'Lamborghini','Sian','Coupe','New',3500000,50,'2024-08-29 21:20:53','2024-08-29 21:20:53','Lamborghini-SIAN-FKP-37-.jpg','A hybrid supercar with futuristic design and extreme power.'),(50,2024,'Rolls-Royce','EWB - MANSORY Diamond Edition','Phantom','used',4300000,100,'2024-09-01 13:49:18','2024-09-01 14:58:33','1725191340.001969Phantom_black.webp','Carbon fiber exterior, customized sporty interior.');
/*!40000 ALTER TABLE `cars` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comments` (
  `comment_id` int NOT NULL AUTO_INCREMENT,
  `content` varchar(225) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` int NOT NULL,
  PRIMARY KEY (`comment_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (5,'The Audi that i bought was in great condition for a used car. Defenitely recommend','2024-09-03 14:09:17','2024-09-03 14:09:17',5),(6,'The car was great and on top condition and the staff were very helpful','2024-09-03 14:15:05','2024-09-03 14:15:05',6),(7,'Great all around environment, very professional and helpful  ','2024-09-03 14:17:48','2024-09-03 14:17:48',7);
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `role_id` int NOT NULL AUTO_INCREMENT,
  `type` varchar(225) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at()` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(225) NOT NULL,
  `last_name` varchar(225) NOT NULL,
  `email` varchar(225) NOT NULL,
  `password` varchar(225) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `role_id` int DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  KEY `fk_user_role` (`role_id`),
  CONSTRAINT `fk_user_role` FOREIGN KEY (`role_id`) REFERENCES `roles` (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Flori','Bica','bicaflori135@gmail.com','$2b$12$fwCCt1V60SYI0o8CVrIujeitT4RTnGEgsaNLpp.c45i4lg6WHtAuu','2024-08-29 18:19:39','2024-08-29 18:41:34',NULL),(2,'test','test','test@test.com','$2b$12$fwCCt1V60SYI0o8CVrIujeitT4RTnGEgsaNLpp.c45i4lg6WHtAuu','2024-08-25 10:07:24','2024-08-29 18:41:47',NULL),(5,'toni','xhukellari','abc@gmail.com','$2b$12$IJp/VkmTFmBRz8cSJ.c2OOwXP6IPSrogglHfCQZAzSooqT2eA4LwO','2024-09-03 14:04:07','2024-09-03 14:04:07',NULL),(6,'John','William','abcd@gmail.com','$2b$12$skCXfN4X0yOf1p5TUsls5uSpAxpNeuYFirUWKKbozU.PZWfE7F8.K','2024-09-03 14:14:12','2024-09-03 14:14:12',NULL),(7,'Giulio','Agalliu','abcde@gmail.com','$2b$12$vg9oxq.f4eK4vuLB.AqE3e9sNNgAu0d3s3gf/CKvpW/IBUveNgK2O','2024-09-03 14:16:04','2024-09-03 14:16:04',NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'AlbaniaCar'
--

--
-- Dumping routines for database 'AlbaniaCar'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-03 19:58:47
