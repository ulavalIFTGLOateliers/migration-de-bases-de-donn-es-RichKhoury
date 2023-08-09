# Schémas des différents états de la BD

## État initial

### singer

| **<u>singerName</u>**: varchar(50) | **firstName**: varchar(50) | **lastName**: varchar(50) | **age**: int |
| --- | --- | --- | --- |
| Alina | Darcy | Boles | 32 |
| Mysterio | Jessie | Chancey | 23 |
| Rainbow | Sarah | Derrick | 47 |
| Luna | Emily | Seibold | 31 |


### label

| **<u>labelName</u>**: varchar(50) | **creation**: YEAR | **genre**: ENUM("rock", "rap", "pop", "classical", "jazz") |
| --- | --- | --- |
| World Music | 2002 | pop |
| Dark Matter | 2015 | rock |
| Four Seasons | 1999 | classical |


### album

| **<u>albumName</u>**: varchar(50) | **singerName**: varchar(50) | **year**: YEAR | **labelName**: varchar(50) |
| --- | --- | --- | --- |
| World of Mysteries | Mysterio | 2019 | Dark Matter |
| Second Mystery | Mysterio | 2021 | World Music |
| Concertos | Luna | 2009 | Four Seasons |


singerName -> singer.singerName

labelName -> label.labelName


## Migration 1

### band

| **<u>bandName</u>**: varchar(50) | **creation**: YEAR | **genre**: ENUM("rock", "rap", "pop", "classical", "jazz") |
| --- | --- | --- |
| Crazy Duo | 2015 | rock |
| Luna | 2009 | classical |
| Mysterio | 2019 | pop |


### musician (ancienne table singer)

| **<u>musicianName</u>**: varchar(50) | **firstName**: varchar(50) | **lastName**: varchar(50) | **age**: int | role: ENUM("vocals", "guitar", "bass", "percussion", "violin", "piano", "other") | bandName: varchar(50) |
| --- | --- | --- | --- | --- | --- |
| Alina | Darcy | Boles | 32 | vocals | Crazy Duo |
| Mysterio | Jessie | Chancey | 23 | guitar | Mysterio |
| Rainbow | Sarah | Derrick | 47 | percussion | Crazy Duo |
| Luna | Emily | Seibold | 31 | piano | Luna |


### label

| **<u>labelName</u>**: varchar(50) | **creation**: YEAR | **genre**: ENUM("rock", "rap", "pop", "classical", "jazz") |
| --- | --- | --- |
| World Music | 2002 | pop |
| Dark Matter | 2015 | rock |
| Four Seasons | 1999 | classical |


### album

| **<u>albumName</u>**: varchar(50) | **singerName**: varchar(50) | **year**: YEAR | **labelName**: varchar(50) |
| --- | --- | --- | --- |
| World of Mysteries | Mysterio | 2019 | Dark Matter |
| Second Mystery | Mysterio | 2021 | World Music |
| Concertos | Luna | 2009 | Four Seasons |


singerName -> musician.musicianName

labelName -> label.labelName


## Migration 2

### band

| **<u>bandName</u>**: varchar(50) | **creation**: YEAR | **genre**: ENUM("rock", "rap", "pop", "classical", "jazz") |
| --- | --- | --- |
| Crazy Duo | 2015 | rock |
| Luna | 2009 | classical |
| Mysterio | 2019 | pop |


### musician

| **<u>musicianName</u>**: varchar(50) | **firstName**: varchar(50) | **lastName**: varchar(50) | **age**: int | role: ENUM("vocals", "guitar", "bass", "percussion", "violin", "piano", "other") | bandName: varchar(50) |
| --- | --- | --- | --- | --- | --- |
| Alina | Darcy | Boles | 32 | vocals | Crazy Duo |
| Mysterio | Jessie | Chancey | 23 | guitar | Mysterio |
| Rainbow | Sarah | Derrick | 47 | percussion | Crazy Duo |
| Luna | Emily | Seibold | 31 | piano | Luna |

band -> band.bandName


### label

| **<u>labelName</u>**: varchar(50) | **creation**: YEAR |
| --- | --- |
| World Music | 2002 |
| Dark Matter | 2015 |
| Four Seasons | 1999 |


### album

| **<u>albumName</u>**: varchar(50) | **bandName**: varchar(50) | **year**: YEAR | **labelName**: varchar(50) |
| --- | --- | --- | --- |
| World of Mysteries | Mysterio | 2019 | Dark Matter |
| Second Mystery | Mysterio | 2021 | World Music |
| Concertos | Luna | 2009 | Four Seasons |


bandName -> band.bandName

labelName -> label.labelName