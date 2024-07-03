
CREATE TABLE IF NOT EXISTS Usuario (
    id  INTEGER PRIMARY KEY,
    nome    VARCHAR(36),
    cpf     VARCHAR(18) UNIQUE NOT NULL,
    email   VARCHAR(36) UNIQUE NOT NULL,
    senha   VARCHAR(36) NOT NULL
);


INSERT INTO Usuario (nome , cpf , email , senha) VALUES ('Robson' , '973.877.100-85' , 'rob2son3@gmail.com' , '5493127');
INSERT INTO Usuario (nome , cpf , email , senha) VALUES ('Julia' , '111.527.400-00' , 'julia.sobrenome@gmail.com' , '182A##A172');
INSERT INTO Usuario (nome , cpf , email , senha) VALUES ('Samira' , '999.999.999-99' , 'sim@gmail.com' , '0000');

SELECT * FROM Usuario;

SELECT nome, cpf, email FROM Usuario;


UPDATE Usuario SET nome = 'Roberto' WHERE id = 1;

DELETE FROM Usuario WHERE id = 5;

SELECT * FROM Usuario WHERE email = 'julia.sobrenome@gmail.com' ORDER BY id ASC;