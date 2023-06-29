CREATE TABLE Band ( bandName varchar(50),
                    creation YEAR,
                    genre ENUM("rock", "rap", "pop", "classical", "jazz"),
                    PRIMARY KEY (bandName));

ALTER TABLE Singer RENAME TO Musician;
ALTER TABLE Musician RENAME COLUMN singerName TO musicianName;
ALTER TABLE Musician ADD COLUMN (role ENUM("vocals", "guitar", "bass", "percussion", "violin", "piano", "other"));
ALTER TABLE Musician ADD COLUMN (bandName varchar(50));
ALTER TABLE Musician ADD CONSTRAINT FK_M_bandName FOREIGN KEY (bandName) REFERENCES Band(bandName);

INSERT INTO Band VALUES ("Crazy Duo", 2015, "rock"), ("Luna", 2009, "classical"), ("Mysterio", 2019 ,"pop");
UPDATE Musician SET role = "vocals", bandName = "Crazy Duo" WHERE musicianName = "Alina";
UPDATE Musician SET role = "piano", bandName = "Luna" WHERE musicianName = "Luna";
UPDATE Musician SET role = "guitar", bandName = "Mysterio" WHERE musicianName = "Mysterio";
UPDATE Musician SET role = "percussion", bandName = "Crazy Duo" WHERE musicianName = "Rainbow";

ALTER TABLE Label DROP COLUMN genre;

ALTER TABLE Album RENAME COLUMN singerName TO bandName;
ALTER TABLE Album DROP CONSTRAINT FK_A_singerName;
ALTER TABLE Album ADD CONSTRAINT FK_A_bandName FOREIGN KEY (bandName) REFERENCES Band(bandName);

# CREATE TABLE Tour ( tourName varchar(50),
#                     bandName varchar(50),
#                     year YEAR,
#                     continent ENUM("North America", "South America", "Africa", "Europe", "Asia", "Oceania"),
#                     PRIMARY KEY (tourName, bandName),
#                     FOREIGN KEY (bandName) REFERENCES Band(bandName));
#
# ALTER TABLE Concert RENAME COLUMN singerName TO bandName;
# ALTER TABLE Concert DROP CONSTRAINT FK_C_singerName;
# ALTER TABLE Concert ADD FOREIGN KEY (bandName) REFERENCES Band(bandName);
# ALTER TABLE Concert ADD COLUMN (tourName varchar(50) DEFAULT NULL);
# ALTER TABLE Concert ADD FOREIGN KEY (tourName) REFERENCES Tour(tourName);