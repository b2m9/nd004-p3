# Udacity: Log analysis

**Advise: This repo contains a 129 MB large SQL dump!**

This repo is part of Udacity's nd004 course.

CLI report script to analyse an SQL dump and print a simple report on the
command line.

## Kudos

- Udacity for providing the foundation of the [Vagrantfile used in this repo](https://github.com/udacity/fullstack-nanodegree-vm).

## What

- Script answers 3 questions based on SQL dump in `data/newsdata.sql`:
    - What are the 3 most popular articles?
    - Who are the most popular authors?
    - Which days have a higher error than 1%?
- Reporting script in `src/report.py`
- Queries in `src/queries.py`
- Example report in `report.txt`
- Materialised views in `data/views.sql`
    - Cronjobs can update materialised views in regular intervals
    - Views not appropriate since tables do not have to be updated
    instantaneously all the time

## How

- `vagrant up` to create the VM and initialise the database:
    - [Vagrant will load the SQL dump into PostgreSQL](Vagrantfile#L28)
    - [Vagrant will create the materialised views](Vagrantfile#L29)
- `vagrant ssh` into the VM
- Run `python3 /vagrant/src/report.py` to view the report
