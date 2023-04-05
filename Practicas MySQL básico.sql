CREATE DATABASE PRACTICAS;
USE PRACTICAS;

-- creamos la tabla
CREATE TABLE program (
idProgram INT NOT NULL AUTO_INCREMENT,
faculty VARCHAR (50) NOT NULL,
yearDuration INT (10) NOT NULL,
numberCredits INT (10) NOT NULL,
valueSemester DECIMAL (5,2) NOT NULL,
PRIMARY KEY (idProgram)
);

desc program;

-- agregar nueva columna a la tabla
ALTER TABLE program
ADD university VARCHAR (50) NOT NULL;

-- para cambia rle orden de las columnas de la tabla
ALTER TABLE program MODIFY COLUMN university INT AFTER faculty;
-- acá modificamos el tipo de dato de queremos en university por Varhar y no nos genere un error
ALTER TABLE program MODIFY COLUMN university VARCHAR(50) NOT NULL;

SELECT * FROM program;

-- se ingresará los datos a la tabla de 2 formas difrentes
INSERT INTO program (idProgram,faculty,university,yearDuration,numberCredits,valueSemester)
VALUES (null, 'engineering','Universidad Nacional' , 5 , 170 , 866.73),
       (null, 'engineering', 'Unversidad Colombiana' , 4 , 150 , 700.23);

SELECT * FROM program;
       
-- segunda forma 
INSERT INTO program
VALUES (null, 'arts', 'Universidad de Artes', 4, 155, 685.50),
       (null, 'arts', 'Universidad de creatividad', 3, 130, 450.20);
       
SELECT * FROM program;

-- Si sólo quiero ver la facultad, universidad y precios
select faculty,university,valueSemester
from program;

-- Si sólo quiero ver la facultad de ingeniería, universidad y precios
select faculty, university, valueSemester
from program
where faculty = 'engineering'; 


-- cambiar le nombre de una columna 
ALTER TABLE program RENAME COLUMN yearDuration to NumberSemesters;

-- cambiar varios valores de una columna 
UPDATE program
SET NumberSemesters = 8
WHERE idProgram IN (2, 3);

UPDATE program
SET NumberSemesters = 10
WHERE idProgram = 1;

UPDATE program
SET NumberSemesters = 6
WHERE idProgram = 4;

SELECT * FROM program;

-- poniendo alias y haciendo operaciones directas para facultad de ingenieria
select faculty, university, NumberSemesters * ValueSemester as annual_value
from program;

-- Sólo para la facultad de ingenieria 
select faculty, university, NumberSemesters * ValueSemester as annual_value
from program
where faculty = 'engineering'; 

SELECT * FROM program;

 


