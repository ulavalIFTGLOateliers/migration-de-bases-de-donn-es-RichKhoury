CREATE DATABASE IF NOT EXISTS atelier_db;

CREATE TABLE IF NOT EXISTS Singer (singerName varchar(50), firstName varchar(50), lastName varchar(50), age int, PRIMARY KEY(singerName));

CREATE TABLE IF NOT EXISTS Label (labelName varchar(50), creation YEAR, genre ENUM("rock", "rap", "pop", "classical", "jazz"), PRIMARY KEY (labelName));

CREATE TABLE IF NOT EXISTS Album (  albumName varchar(50),
                                    singerName varchar(50),
                                    year YEAR,
                                    label varchar(50),
                                    PRIMARY KEY (albumName),
                                    FOREIGN KEY (singerName) REFERENCES Singer (singerName),
                                    FOREIGN KEY (label) REFERENCES Label (labelName));

CREATE TABLE IF NOT EXISTS Tour (   tourName varchar(50),
                                    singerName varchar(50),
                                    year YEAR,
                                    continent ENUM("North America", "South America", "Africa", "Europe", "Asia", "Oceania"),
                                    PRIMARY KEY (tourName, singerName),
                                    FOREIGN KEY (singerName) REFERENCES Singer (singerName));

