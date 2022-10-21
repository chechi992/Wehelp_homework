-- MySQL dump 10.13  Distrib 8.0.31, for macos12 (x86_64)
--
-- Host: 127.0.0.1    Database: website
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.21-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '獨立編號',
  `name` varchar(255) NOT NULL COMMENT '姓名',
  `username` varchar(255) NOT NULL COMMENT '帳戶名稱',
  `password` varchar(255) NOT NULL COMMENT '帳戶密碼',
  `follower_count` int(10) unsigned NOT NULL DEFAULT 0 COMMENT '追蹤者數量',
  `time` datetime NOT NULL DEFAULT current_timestamp() COMMENT '註冊時間',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'kevin','test','test',600,'2022-10-20 17:23:12'),(2,'lorin','rin','poi',780,'2022-10-20 17:26:47'),(3,'erin','poi89','ury5677',3400,'2022-10-20 17:27:48'),(4,'yotty','tory','roi',830,'2022-10-20 17:28:25'),(5,'sally','daddy','mpmmy33',260,'2022-10-20 17:28:56');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;
