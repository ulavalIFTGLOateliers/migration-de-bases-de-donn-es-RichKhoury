ALTER TABLE singer RENAME TO musician;
ALTER TABLE musician RENAME COLUMN singerName TO musicianName;
ALTER TABLE musician ADD COLUMN (role ENUM("vocals", "guitar", "bass", "percussion", "violin", "piano", "other"));
ALTER TABLE musician ADD COLUMN (bandName varchar(50));
UPDATE musician SET role = "vocals", bandName = "Crazy Duo" WHERE musicianName = "Alina";
UPDATE musician SET role = "piano", bandName = "Luna" WHERE musicianName = "Luna";
UPDATE musician SET role = "guitar", bandName = "Mysterio" WHERE musicianName = "Mysterio";
UPDATE musician SET role = "percussion", bandName = "Crazy Duo" WHERE musicianName = "Rainbow";

CREATE TABLE band ( bandName varchar(50),
                    creation YEAR,
                    genre ENUM("rock", "rap", "pop", "classical", "jazz"),
                    PRIMARY KEY (bandName));

INSERT INTO band VALUES ("Crazy Duo", 2015, "rock"), ("Luna", 2009, "classical"), ("Mysterio", 2019 ,"pop");