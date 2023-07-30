ALTER TABLE Singer RENAME TO Musician;
ALTER TABLE Musician RENAME COLUMN singerName TO musicianName;
ALTER TABLE Musician ADD COLUMN (role ENUM("vocals", "guitar", "bass", "percussion", "violin", "piano", "other"));
ALTER TABLE Musician ADD COLUMN (bandName varchar(50));
UPDATE Musician SET role = "vocals", bandName = "Crazy Duo" WHERE musicianName = "Alina";
UPDATE Musician SET role = "piano", bandName = "Luna" WHERE musicianName = "Luna";
UPDATE Musician SET role = "guitar", bandName = "Mysterio" WHERE musicianName = "Mysterio";
UPDATE Musician SET role = "percussion", bandName = "Crazy Duo" WHERE musicianName = "Rainbow";

CREATE TABLE Band ( bandName varchar(50),
                    creation YEAR,
                    genre ENUM("rock", "rap", "pop", "classical", "jazz"),
                    PRIMARY KEY (bandName));

INSERT INTO Band VALUES ("Crazy Duo", 2015, "rock"), ("Luna", 2009, "classical"), ("Mysterio", 2019 ,"pop");