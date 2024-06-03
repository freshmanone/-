SHOW GRANTS FOR 'root'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;

CREATE DATABASE MigrationDB;

USE MigrationDB;

CREATE VIEW PersonView AS
SELECT name, residence_planet
FROM Person;

CREATE TABLE Person (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(10) PRIMARY KEY NOT NULL,
    age INT NOT NULL,
    zodiac VARCHAR(20) NOT NULL,
    birth_planet VARCHAR(50) NOT NULL,
    residence_planet VARCHAR(50) NOT NULL,
    FOREIGN KEY (residence_planet) REFERENCES Planet(name),
    FOREIGN KEY (birth_planet) REFERENCES Planet(name)
)ENGINE=InnoDB;

CREATE TABLE Planet (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(10) UNIQUE PRIMARY KEY
)ENGINE=InnoDB;

DELIMITER //
CREATE TRIGGER before_person_insert
BEFORE INSERT ON Person
FOR EACH ROW
BEGIN
    IF NEW.age <= 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Age must be greater than 0';
    END IF;
END; //
DELIMITER ;


START TRANSACTION;
DELETE FROM Person WHERE residence_planet = 'Mars';
SELECT * FROM Person WHERE residence_planet = 'Mars';
COMMIT;

DELIMITER //

CREATE PROCEDURE UpdatePersonAge(
    IN personName VARCHAR(50),
    IN newAge INT
)
BEGIN
    -- 开始事务
    START TRANSACTION;
    
    -- 检查新的年龄值是否大于 0
    IF newAge <= 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Age must be greater than 0';
    ELSE
        -- 更新Person表中的年龄
        UPDATE Person
        SET age = newAge
        WHERE name = personName;
    END IF;
    
    -- 提交事务
    COMMIT;
END //

DELIMITER ;

