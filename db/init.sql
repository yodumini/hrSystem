CREATE DATABASE employee;
use employee;


-- employee.e_class_mode definition

CREATE TABLE employee.`c_class_mode` (
  `calss` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `on_time` time NOT NULL,
  `off_time` time NOT NULL,
  PRIMARY KEY (`calss`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- employee.e_class definition

CREATE TABLE employee.`e_class` (
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `class` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- employee.e_staff definition

CREATE TABLE employee.`e_staff` (
  `id` int NOT NULL,
  `chinese_name` varchar(20) DEFAULT NULL,
  `name` varchar(20) NOT NULL,
  `employment` varchar(20) DEFAULT NULL,
  `title` varchar(20) DEFAULT NULL,
  `department` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- employee.e_attend definition

CREATE TABLE employee.`e_attend` (
  `name` varchar(20) NOT NULL,
  `clock_date` date NOT NULL,
  `clock_in_time` datetime DEFAULT NULL,
  `clock_out_time` datetime DEFAULT NULL,
  `working_hours` time DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`name`,`clock_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- employee.c_schedule definition

CREATE TABLE employee.`c_schedule` (
  `schedule_date` date NOT NULL,
  `weekday` int DEFAULT NULL,
  `is_workday` int NOT NULL,
  `holiday` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`schedule_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;