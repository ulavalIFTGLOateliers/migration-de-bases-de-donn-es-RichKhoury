ALTER TABLE Musician RENAME COLUMN musicianName to singerName;
ALTER TABLE Musician RENAME TO Singer;





CREATE TABLE Tour ( tourName varchar(50),
                    bandName varchar(50),
                    year YEAR,
                    continent ENUM("North America", "South America", "Africa", "Europe", "Asia", "Oceania"),
                    PRIMARY KEY (tourName, singerName),
                    FOREIGN KEY);