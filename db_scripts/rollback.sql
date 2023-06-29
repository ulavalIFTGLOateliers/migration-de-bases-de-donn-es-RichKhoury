ALTER TABLE Musician DROP CONSTRAINT FK_M_bandName;
ALTER TABLE Musician DROP COLUMN role;
ALTER TABLE Musician DROP COLUMN bandName;
ALTER TABLE Musician RENAME COLUMN musicianName TO singerName;
ALTER TABLE Musician RENAME TO Singer;

ALTER TABLE Album DROP CONSTRAINT FK_A_bandName;
ALTER TABLE Album RENAME COLUMN bandName TO singerName;
ALTER TABLE Album ADD CONSTRAINT FK_A_singerName FOREIGN KEY (singerName) REFERENCES Singer(singerName);

ALTER TABLE Label ADD COLUMN genre ENUM("rock", "rap", "pop", "classical", "jazz");
UPDATE Label SET genre = "pop" WHERE labelName = "World Music";
UPDATE Label SET genre = "rock" WHERE labelName = "Dark Matter";
UPDATE Label SET genre = "classical" WHERE labelName = "Four Seasons";

DROP TABLE Band;