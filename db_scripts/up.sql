CREATE TABLE IF NOT EXISTS Singer (     singerName varchar(50),
                                        firstName varchar(50),
                                        lastName varchar(50),
                                        age int,
                                        PRIMARY KEY(singerName));
CREATE TABLE IF NOT EXISTS Label (      labelName varchar(50),
                                        creation YEAR,
                                        genre ENUM("rock", "rap", "pop", "classical", "jazz"),
                                        PRIMARY KEY (labelName));
CREATE TABLE IF NOT EXISTS Album (      albumName varchar(50),
                                        singerName varchar(50),
                                        year YEAR,
                                        labelName varchar(50),
                                        PRIMARY KEY (albumName),
                                        CONSTRAINT FK_A_singerName FOREIGN KEY (singerName) REFERENCES Singer (singerName),
                                        FOREIGN KEY (labelName) REFERENCES Label (labelName));
# CREATE TABLE IF NOT EXISTS Concert (    concertId int,
#                                         singerName varchar(50),
#                                         date DATE,
#                                         city varchar(50),
#                                         PRIMARY KEY (concertId),
#                                         CONSTRAINT FK_C_singerName FOREIGN KEY (singerName) REFERENCES Singer (singerName));


INSERT INTO Singer VALUES ("Alina", "Darcy", "Boles", 32), ("Mysterio","Jessie","Chancey",23), ("Rainbow", "Sarah", "Derrick", 47), ("Luna", "Emily", "Seibold", 31);
INSERT INTO Label VALUES ("World Music", 2002, "pop"), ("Dark Matter", 2015, "rock"), ("Four Seasons", 1999, "classical");
INSERT INTO Album VALUES ("World of Mysteries", "Mysterio", 2019, "Dark Matter"), ("Second Mystery", "Mysterio", 2021, "World Music"), ("Concertos", "Luna", 2009, "Four Seasons");
# INSERT INTO Concert VALUES (1, "Mysterio", "2021-06-24", "Quebec"), (2, "Mysterio", "2021-07-01", "Toronto"), (3, "Luna", "2015-08-12", "Prague"), (4, "Alina", "2019-09-21", "Seoul");