USE EINSTEIN;

DROP TABLE IF EXISTS USERS;

CREATE TABLE USERS (
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    USERNAME VARCHAR(255) NOT NULL,
    PWRD_SHA256 VARCHAR(255) NOT NULL,
    FIRST_NAME VARCHAR(255) NOT NULL,
    LAST_NAME VARCHAR(255) NOT NULL,
    EMAIL VARCHAR(255) NOT NULL,
    PHONE_NUMBER VARCHAR(255) NOT NULL
);

INSERT INTO 
    USERS (USERNAME, PWRD_SHA256, FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER)
VALUES
    ('brunomurino', "b7e94be513e96e8c45cd23d162275e5a12ebde9100a425c4ebcdd7fa4dcd897c", "Bruno", "Murino", "bfsmurino@gmail.com", "+44 78989 76564"),
    ('taymaradias', "b7e94be513e96e8c45cd23d162275e5a12ebde9100a425c4ebcdd7fa4dcd897c", "Taymara", "Dias", "taymaradias@gmail.com", "+44 78989 76564"),
    ('biancarodrigues', "b7e94be513e96e8c45cd23d162275e5a12ebde9100a425c4ebcdd7fa4dcd897c", "Bianca", "Rodrigues", "taymaradias@gmail.com", "+44 78989 76564")
;