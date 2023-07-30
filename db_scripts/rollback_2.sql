ALTER TABLE Musician DROP CONSTRAINT FK_M_bandName;

ALTER TABLE Album DROP CONSTRAINT FK_A_bandName;
ALTER TABLE Album RENAME COLUMN bandName TO singerName;
ALTER TABLE Album ADD CONSTRAINT FK_A_singerName FOREIGN KEY (singerName) REFERENCES Musician(musicianName);

ALTER TABLE Label ADD COLUMN genre ENUM("rock", "rap", "pop", "classical", "jazz");
UPDATE Label SET genre = "pop" WHERE labelName = "World Music";
UPDATE Label SET genre = "rock" WHERE labelName = "Dark Matter";
UPDATE Label SET genre = "classical" WHERE labelName = "Four Seasons";
