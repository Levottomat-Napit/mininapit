# OhTu-miniproject for managing LaTeX references

The idea of this project is to practice Scrum framework while trying to produce an app that automatically creates BibTeX files from the references in the database

## Running

* Alernative 1: Clone repository with HTTPS

  ```git clone https://github.com/Levottomat-Napit/mininapit.git```

* Alernative 2: Clone repository with SSH

  ```git clone git@github.com:Levottomat-Napit/mininapit.git```

* Install dependencies

  ```poetry install```

* Set up `.env`

```env
DATABASE_URL=postgresql:///databasename
TEST_ENV=boolean
SECRET_KEY=somethingsecret
```

* Set up database

  `python3 src/db_helper.py`

* Start poetry shell

  ```poetry shell```

* Run app

  ```python3 src/index.py```

## Link to the Product Backlog

[Product Backlog](https://helsinkifi-my.sharepoint.com/:x:/g/personal/memikael_ad_helsinki_fi/EbC2vh1Jn6hJgjfvQTdviaEBbscj52A8DW6_oJqrS8zWdw?e=IHdviw)

## Definition of Done

* Asiakkaan vaatimat ominaisuudet ja tekniset vaatimukset otettu selville
* Vaatimukset analysoitu ja selvitetty minkälaisilla teknisillä valmiuksilla ne voi toteuttaa
* Asiakkaan vaatimukset on kirjattu user storyiksi
* User storyt on pilkottu taskeiksi, ja kirjattu
* Ohjelmistoon vaaditut ominaisuudet on ohjelmoitu ja toteutettu teknisesti
* Ohjelman toiminnallisuutta on testattu
* Ohjelmalla on automatisoituja testejä, unit ja robot
* Projektin edistymisen taso on kirjattu lokiin ja siitä on olemassa burndown-kaavio
