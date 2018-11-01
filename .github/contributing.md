# Contributing
This file outlines the software used by spark-database, how to set up a local version of the repository, and how to contribute to the development and maintainence of the project.

## Guide
* [Software](#software)
* [Programming Concepts](#programming-concepts)
* [Local Setup](#local-setup)
* [Database Migration](#database-migration)

## Software
* [Python 3.6](https://www.python.org/about/gettingstarted/)
* [PostgreSQL 10.5](https://www.postgresql.org/about/)
* [Virtual Environment 15.1.0](https://virtualenv.pypa.io/en/latest/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Alembic](https://alembic.zzzcomputing.com/en/latest/#)
* [Pylint](https://pylint.readthedocs.io/en/latest/intro.html)
* [Pick](https://github.com/wong2/pick)


## Programming Concepts
For new developers, an overview of essential programming concepts are available at the [spark-website wiki](https://github.com/TravisSpark/spark-website/wiki). While all of the concepts are important, the especially relevant pages are:
- [Development Tools](https://github.com/TravisSpark/spark-website/wiki/Development-Tools)
- [Version Control](https://github.com/TravisSpark/spark-website/wiki/Collaboration#version-control)


## Local Setup

Command Line instructions will assume use of the Ubuntu Distribution of Linux or Windows Subsystem for Linux (WLS). If using WSL, setup instructions are available at [Microsoft's WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/install-win10). If using a Mac, System Setup Instructions are avaialble at [Sourabh Bajaj's Blog](http://sourabhbajaj.com/mac-setup/). If on a Military Network, the same information is available on [Sourabh Bajaj's GitHub](https://github.com/sb2nov/mac-setup).

### Update BASH

```sudo apt-get update```

### Download Spark-Database 

* Install git to manage software versions

```sudo apt install git```

* [Fork](https://guides.github.com/activities/forking/) the [spark-database repository](https://github.com/travisspark/spark-database)

* [Clone](https://help.github.com/articles/cloning-a-repository/) the personal repository

```git clone https://github.com/[YOUR-ACCOUNT]/spark-database.git```

* Switch to project directory:

```cd spark-database```

* Add the production repository:

```git remote add upstream https://github.com/travisspark/spark-database.git```

* Check both repositories are present:

```git remote -v```

* **Note:** Conventionally, personal repositories are labeled *origin*. publication repositories are labeled *upstream*
* Checkout a new branch before making edits:

```git checkout -b [clear-concise-branch-name]```

### Install Python

* Version 3.6

```sudo apt install python3``` 

* Python Pip3 to install Python requirements

```sudo apt install python3-pip```

### Setup Virtual Environment 

* Install

```sudo apt install virtualenv```

* Create a virtual envirnment named *venv*. Make sure to be in spark-database directory.

```virtualenv -p python3 venv ```

* Activate the virtual environment.

```source venv/bin/activate```

### Install Python Packages

* Use pip3 to install the required Python packages into the virtual environment.

```pip3 install -r requirements.txt```

### Setup Database

* Install PostgreSQL 

```sudo apt install postgresql-client-10```

* Check Install

```psql --version```

* Local Server Install

```sudo apt-get install postgresql postgresql-contrib```

* Activate Postgres Commands

```sudo -u postgres psql postgres```

* If experiencing trouble

```sudo apt install postgresql-common```

```sudo pg_ctlcluster 10 main start```

* Set a password

```\password```

*enter password*

* Exit Directory

```\q```

* Create database

```sudo -u postgres createdb spark-database```

Don't be alarmed by:
"*WARNING:  could not flush dirty data: Function not implemented*"

## Settings

* Create a copies of ```alembic.ini.example``` and ```settings.py.example```
* Rename the copies to ```alembic.ini``` and ```settings.py```
* For ```alembic.ini```, in ```sqlalchemy.url = postgres://postgres:[password]@localhost/spark-database``` replace [password] with the password set for the PostgreSQL User
* For ```settings.py```, set the ```password:``` value equal to the password set for the PostgreSQL User (same as the alembic.ini password)
* ```settings.py``` and ```alembic.ini``` are set in ```.gitignore``` to be overlooked when sharing code in git. This is to avoid the passwords being shared.

## Database Migration

* The database versions have already been setup
* To initialize the database with the current version, run:

```alembic upgrade head```

## Run the program

```python3 spark_database/main.py```
