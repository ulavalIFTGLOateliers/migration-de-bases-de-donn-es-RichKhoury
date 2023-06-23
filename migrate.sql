CREATE TABLE Band ( bandName varchar(50),
                    creation YEAR,
                    genre ENUM("rock", "rap", "pop", "classical", "jazz"),
                    PRIMARY KEY (bandName));

ALTER TABLE Singer RENAME TO Musician;
ALTER TABLE Musician RENAME COLUMN singerName TO musicianName;
ALTER TABLE Musician ADD COLUMN (role ENUM("vocals", "guitar", "bass", "percussion", "violin", "piano", "other"));
ALTER TABLE Musician ADD COLUMN (bandName varchar(50));
ALTER TABLE Musician ADD FOREIGN KEY (bandName) REFERENCES Band(bandName);

ALTER TABLE Label DROP COLUMN genre;

ALTER TABLE Album RENAME COLUMN singerName TO bandName;
ALTER TABLE Album DROP CONSTRAINT FK_A_singerName;
ALTER TABLE Album ADD FOREIGN KEY (bandName) REFERENCES Band(bandName);

CREATE TABLE Tour ( tourName varchar(50),
                    bandName varchar(50),
                    year YEAR,
                    continent ENUM("North America", "South America", "Africa", "Europe", "Asia", "Oceania"),
                    PRIMARY KEY (tourName, bandName),
                    FOREIGN KEY (bandName) REFERENCES Band(bandName));

ALTER TABLE Concert RENAME COLUMN singerName TO bandName;
ALTER TABLE Concert DROP CONSTRAINT FK_C_singerName;
ALTER TABLE Concert ADD FOREIGN KEY (bandName) REFERENCES Band(bandName);
ALTER TABLE Concert ADD COLUMN (tourName varchar(50) DEFAULT NULL);
ALTER TABLE Concert ADD FOREIGN KEY (tourName) REFERENCES Tour(tourName);