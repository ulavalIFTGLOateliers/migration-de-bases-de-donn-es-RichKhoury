ALTER TABLE musician DROP CONSTRAINT FK_M_bandName;

ALTER TABLE album DROP CONSTRAINT FK_A_bandName;
ALTER TABLE album RENAME COLUMN bandName TO singerName;
ALTER TABLE album ADD CONSTRAINT FK_A_singerName FOREIGN KEY (singerName) REFERENCES musician(musicianName);

ALTER TABLE label ADD COLUMN genre ENUM("rock", "rap", "pop", "classical", "jazz");
UPDATE label SET genre = "pop" WHERE labelName = "World Music";
UPDATE label SET genre = "rock" WHERE labelName = "Dark Matter";
UPDATE label SET genre = "classical" WHERE labelName = "Four Seasons";
