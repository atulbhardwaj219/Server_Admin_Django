/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 10.1.19-MariaDB : Database - cloudpanel
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`cloudpanel` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `cloudpanel`;

/*Table structure for table `galaxy_request` */

DROP TABLE IF EXISTS `galaxy_request`;

CREATE TABLE `galaxy_request` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Instancename` varchar(15) NOT NULL,
  `ip` char(39) NOT NULL,
  `status` varchar(10) NOT NULL,
  `request` varchar(10) NOT NULL,
  `requesttime` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `galaxy_request` */

/*Table structure for table `galaxy_servers` */

DROP TABLE IF EXISTS `galaxy_servers`;

CREATE TABLE `galaxy_servers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Instancename` varchar(15) NOT NULL,
  `ip` char(39) NOT NULL,
  `port` int(10) unsigned NOT NULL,
  `username` varchar(10) NOT NULL,
  `password` varchar(10) NOT NULL,
  `OsType` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Instancename` (`Instancename`),
  UNIQUE KEY `ip` (`ip`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `galaxy_servers` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
