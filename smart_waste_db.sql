Enter password: ***********
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 18
Server version: 8.0.46 MySQL Community Server - GPL

Copyright (c) 2000, 2026, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> CREATE DATABASE smart_waste_db;
Query OK, 1 row affected (0.06 sec)

mysql> USE smart_waste_db;
Database changed
mysql> CREATE TABLE users (
    -> user_id INT AUTO_INCREMENT PRIMARY KEY,
    -> name VARCHAR(100)
    -> name VARCHAR(100)NOT NULL,
    -> email VARCHAR(100) UNIQUE NOT NULL,
    -> password VARCHAR(100)NOT NULL,
    -> phone VARCHAR(15),
    -> role VARCHAR(20)
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'name VARCHAR(100)NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
password VARCHAR(' at line 4
mysql> CREATE TABLE users (
    -> user_id INT AUTO_INCREMENT PRIMARY KEY,
    -> name VARCHAR(100)NOT NULL,
    -> email VARCHAR(100) UNIQUE NOT NULL,
    -> password VARCHAR(100)NOT NULL,
    -> phone VARCHAR(15),
    -> role VARCHAR(20)
    -> );
Query OK, 0 rows affected (0.11 sec)

mysql> SHOW TABLES;
+--------------------------+
| Tables_in_smart_waste_db |
+--------------------------+
| users                    |
+--------------------------+
1 row in set (0.04 sec)

mysql> CREATE TABLE bins (
    -> bin_id INT AUTO_INCREMENT PRIMARY KEY,
    -> location VARCHAR(200) NOT NULL,
    -> bin_type VARCHAR(50),
    -> capacity INT,
    -> fill_level INT,
    -> status VARCHAR(20)
    -> );
Query OK, 0 rows affected (0.07 sec)

mysql> CREATE TABLE workers (
    -> worker_id INT AUTO_INCREMENT PRIMARY KEY,
    -> worker_name VARCHAR(100) NOT NULL,
    -> phone VARCHAR(15),
    -> address VRCHR(200),
    -> shift_time VARCHAR(50)
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'VRCHR(200),
shift_time VARCHAR(50)
)' at line 5
mysql> CREATE TABLE workers (
    -> worker_id INT AUTO_INCREMENT PRIMARY KEY,
    -> worker_name VARCHAR(100) NOT NULL,
    -> phone VARCHAR(15),
    -> address VARCHR(200),
    -> shift_time VARCHAR(50)
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'VARCHR(200),
shift_time VARCHAR(50)
)' at line 5
mysql> CREATE TABLE workers (
    -> worker_id INT AUTO_INCREMENT PRIMARY KEY,
    -> worker_name VARCHAR(100) NOT NULL,
    -> phone VARCHAR(15),
    -> address VARCHAR(200),
    -> shift_time VARCHAR(50)
    -> );
Query OK, 0 rows affected (0.11 sec)

mysql> CREATE TABLE vehicles (
    -> vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    -> vehicle_number VARCHAR(20) UNIQUE,
    -> vehicle_type VARCHR(50),
    -> driver_name VARCHAR(100),
    -> capacity INT
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'VARCHR(50),
driver_name VARCHAR(100),
capacity INT
)' at line 4
mysql> CREATE TABLE vehicles (
    -> vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    -> vehicle_number VARCHAR(20) UNIQUE,
    -> vehicle_type VARCHAR(50),
    -> driver_name VARCHAR(100),
    -> capacity INT
    -> );
Query OK, 0 rows affected (0.18 sec)

mysql> SHOW TABLES;
+--------------------------+
| Tables_in_smart_waste_db |
+--------------------------+
| bins                     |
| users                    |
| vehicles                 |
| workers                  |
+--------------------------+
4 rows in set (0.05 sec)

mysql>