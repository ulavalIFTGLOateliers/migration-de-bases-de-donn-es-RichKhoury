DROP TABLE Band;

ALTER TABLE Musician DROP COLUMN role;
ALTER TABLE Musician DROP COLUMN bandName;
ALTER TABLE Musician RENAME COLUMN musicianName TO singerName;
ALTER TABLE Musician RENAME TO Singer;