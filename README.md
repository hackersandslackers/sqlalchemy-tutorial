# SQLAlchemy Tutorial

![Python](https://img.shields.io/badge/Python-v^3.10-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-v^2.0.20-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![PyMySQL](https://img.shields.io/badge/PyMySQL-v^1.1.0-red.svg?longCache=true&style=flat-square&logo=scala&logoColor=white&colorA=4c566a&colorB=bf616a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c&logo=GitHub)
[![GitHub Issues](https://img.shields.io/github/issues/hackersandslackers/sqlalchemy-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/sqlalchemy-tutorial/issues)
[![GitHub Stars](https://img.shields.io/github/stars/hackersandslackers/sqlalchemy-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/sqlalchemy-tutorial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/hackersandslackers/sqlalchemy-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/sqlalchemy-tutorial/network)

![SQLAlchemy Tutorial](https://github.com/hackersandslackers/sqlalchemy-tutorial/blob/master/.github/img/sqlalchemy@2x.jpg?raw=true)

This repository contains the source code for a four-part tutorial series on SQLAlchemy:

1. [Databases in Python Made Easy with SQLAlchemy](https://hackersandslackers.com/python-database-management-sqlalchemy)
2. [Implement an ORM with SQLAlchemy](https://hackersandslackers.com/implement-sqlalchemy-orm)
3. [Relationships in SQLAlchemy Data Models](https://hackersandslackers.com/sqlalchemy-data-models)
4. [Constructing Database Queries with SQLAlchemy](https://hackersandslackers.com/database-queries-sqlalchemy-orm)

## Getting Started

Get set up locally in two steps:

### Environment Variables

Replace the values in **.env.example** with your values and rename this file to **.env**:

* `DATABASE_USERNAME`: Username for a SQL database.
* `DATABASE_PASSWORD`: Corresponding password for the above SQL database user.
* `DATABASE_HOST`: Host of the SQL database.
* `DATABASE_PORT`: Numerical port of the SQL database.
* `DATABASE_TABLE`: Name of the SQL database table.
* `DATABASE_CERT_FILE` _(optional)_: Path to SSL certificate file for database.

*Remember never to commit secrets saved in .env files to Github.*

### Installation

Get up and running with `make run`:

```shell
git clone https://github.com/hackersandslackers/sqlalchemy-tutorial.git
cd sqlalchemy-tutorial
make run
```

-----

**Hackers and Slackers** tutorials are free of charge. If you found this tutorial helpful, a [small donation](https://www.buymeacoffee.com/hackersslackers) would be greatly appreciated to keep us in business. All proceeds go towards coffee, and all coffee goes towards more content.
