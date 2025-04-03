
DROP DATABASE IF EXISTS record;


CREATE DATABASE record;


USE record;


CREATE TABLE student (
    rollNo INT NOT NULL PRIMARY KEY,
    name VARCHAR(100),
    sub VARCHAR(100),
    marks VARCHAR(10)
);

SHOW TABLES;


DESCRIBE student;
