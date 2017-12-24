-- --------------------------------------------------------
-- Host:                         localhost
-- Server version:               10.3.2-MariaDB-log - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping structure for table python_tutorial.public_toilets
CREATE TABLE IF NOT EXISTS `public_toilets` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `city_id` int(10) unsigned DEFAULT NULL,
  `latitude` float(10,8) DEFAULT NULL,
  `longitude` float(10,8) DEFAULT NULL,
  `category` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `picture` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  KEY `primary_index` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=498 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table python_tutorial.public_toilets: ~0 rows (approximately)
DELETE FROM `public_toilets`;
/*!40000 ALTER TABLE `public_toilets` DISABLE KEYS */;
/*!40000 ALTER TABLE `public_toilets` ENABLE KEYS */;

-- Dumping structure for table python_tutorial.public_toilets_timings
CREATE TABLE IF NOT EXISTS `public_toilets_timings` (
  `public_toilet_id` int(11) DEFAULT NULL,
  `locale` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT 'en',
  `day` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `from_time` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `to_time` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table python_tutorial.public_toilets_timings: ~348 rows (approximately)
DELETE FROM `public_toilets_timings`;
/*!40000 ALTER TABLE `public_toilets_timings` DISABLE KEYS */;
/*!40000 ALTER TABLE `public_toilets_timings` ENABLE KEYS */;

-- Dumping structure for table python_tutorial.public_toilet_translations
CREATE TABLE IF NOT EXISTS `public_toilet_translations` (
  `public_toilet_id` int(10) unsigned NOT NULL,
  `locale` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'en',
  `title` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `address` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `timings` mediumtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  KEY `public_toilet_translations_public_toilet_id` (`public_toilet_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table python_tutorial.public_toilet_translations: ~0 rows (approximately)
DELETE FROM `public_toilet_translations`;
/*!40000 ALTER TABLE `public_toilet_translations` DISABLE KEYS */;
/*!40000 ALTER TABLE `public_toilet_translations` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
