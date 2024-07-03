
CREATE TABLE IF NOT EXISTS Produto (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(36) NOT NULL,
    preco FLOAT NOT NULL,
    quantidade INTEGER NOT NULL
);

INSERT INTO Produto ( nome,preco,quantidade ) VALUES ( 'Fita Adesiva Durex' , 3.99 , 412 );
INSERT INTO Produto ( nome,preco,quantidade ) VALUES ( 'Martelo Sony' , 149.99 , 92 );
INSERT INTO Produto ( nome,preco,quantidade ) VALUES ( 'Serrote Panasonic' , 99.99 , 151 );
INSERT INTO Produto ( nome,preco,quantidade ) VALUES ( 'Trena Brastemp' , 29.99 , 65 );
INSERT INTO Produto ( nome,preco,quantidade ) VALUES ( 'Cx Pregos 100x' , 9.99 , 632 );

SELECT * FROM Produto;

UPDATE Produto SET preco = 89.99 WHERE id = 3;


DELETE FROM Produto WHERE id = 2;

INSERT INTO Produto ( id,nome,preco,quantidade ) VALUES ( 2,'Martelo Sony' , 149.99 , 92 );