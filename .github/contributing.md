# Welcome to the Spark-Database Contributing Document
This file outlines the role of the software used by spark-database, how to set up a local version of the repository, and how to contribute to the development and maintainence of the project. Command Line instructions will assume use of the Ubuntu Distribution of Linux or Windows Subsystem for Linux (WLS). If using WSL, setup instructions are available at [Microsoft's WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/install-win10). If using a Mac, System Setup Instructions are avaialble at [Sourabh Bajaj's Blog](http://sourabhbajaj.com/mac-setup/). If on a Military Network, the same information is available on [Sourabh Bajaj's GitHub](https://github.com/sb2nov/mac-setup).

## Using the Database
Instructions on interacting with the database are available in the README of the [spark-database code page](https://github.com/TravisSpark/spark-database).

## Overview Programming Concepts
For new developers, an overview of essential programming concepts are available at the [spark-website wiki](https://github.com/TravisSpark/spark-website/wiki). While all of the concepts are important, the especially relevant pages are:
- [Development Tools](https://github.com/TravisSpark/spark-website/wiki/Development-Tools)
- [Version Control](https://github.com/TravisSpark/spark-website/wiki/Collaboration#version-control)

## Local Setup

Update BASH

```sudo apt-get update```

### Download Local copy of Spark-Database 

Install git to manage software versions

```sudo apt install git```

[Fork](https://guides.github.com/activities/forking/) the [spark-database repository](https://github.com/travisspark/spark-database)

[Clone](https://help.github.com/articles/cloning-a-repository/) the personal repository

```git clone https://github.com/[YOUR-ACCOUNT]/spark-database.git```

Switch to project directory:

```cd spark-database```

Add the production repository:

```git remote add upstream https://github.com/travisspark/spark-database.git```

Check both repositories are present:

```git remote -v```

Conventionally, personal repositories are labeled *origin*. publication repositories are labeled *upstream*
Checkout a new branch before making edits:

```git checkout -b [clear-concise-branch-name]```

### Python

Version 3.6.5

```sudo apt install python3``` 

Python Pip3 to install Python requirements

```sudo apt install python3-pip```

### Virtual Environment 

Install

```sudo apt install virtualenv```

Create a virtual envirnment named *venv*. Make sure to be in spark-database directory.

```virtualenv -p python3 venv ```

Activate the virtual environment.

```source venv/bin/activate```

### Python Dependencies

Use pip3 to install the required Python packages into the virtual environment.

```pip3 install -r requirements.txt```

### Database

Install PostgreSQL 

```sudo apt install postgresql-client-10```

Check Install

```psql --version```

Local Server Install

```sudo apt-get install postgresql postgresql-contrib```

Activate Postgres

```sudo -u postgres psql postgres```

If exeperiencing trouble

```sudo apt install postgresql-common```

```sudo pg_ctlcluster 10 main start```

Set a password

```\password```

*enter password*

Create database

```sudo -u postgres createdb spark-database```

Don't be alarmed by:
"*WARNING:  could not flush dirty data: Function not implemented*"

## Python
Python is becoming increasingly more popular. It is a high level language that is open source, relatively friendly to beginners, facilitates quick project development, is highly versatile, and well supported by its community. Consequently, it is applied to fields as diverse as website development and machine learning. 

### Python: Versions
While version two of Python is still common, spark-database is written with version three. The syntax and capabilities between the two versions of python are different enough that is vital to be using the same version of python throughout a project.

### Python: Installation
*Reminder: Commands are written for Ubuntu BASH*

Update BASH
* ```sudo apt-get update```

Install Python Version Three
* ```sudo apt install python3```

## Relational Databases
* Purpose of Relational Databases
* Real World Implications
* Software Applications

## Database Engines
* Maria
* sqlite
* postgresql
* mysql
* sql

## PostgreSQL installation Commands
* install postgresql
* create password
* create spark-database 
* Stale PID: pg_ctlcluster 10 main start

## [GitHub Intructions](Main GitHub tutorial)
- [Spark-Website Wiki Version](local link)
- Fork
- Clone
- Add Upstream

## [Virtual Environment](Link to Overview)
```sudp apt-get install python3-venv```
* Purpose
* Importance
* Docker is becoming a new standard

## Create Virtual Environment
* Initialize
* Start
* Install Requirements
* pip
* install requirements

## [SQLAlchemy](Main Documentation)
* Purpose
* Importance

## [Alembic](Link to Alembic Tutorial)
* Importance of Migrating databases
* Initialize the user table

## [Linting](Link to pylint tutorial)
* Importance of Linting
* Commands to lint files, before submitting pull requests

## [Pick](Link to Pick)
* Utilization of Pick to go beyond text inputs
