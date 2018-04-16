#!/usr/bin/python
# migrate.py
# Author: Nageswara Rao (nag.samayam@gmail.com)
# Date: Apr 16, 2018
# Version: 1.0.1
# Purpose: Migrate User from MySQL to Mongo Profiles


import pymysql as mydb  # Import MySQL Libraimport sys, tracebackry
from mongoengine import *
from ward import Ward
import json
import datetime


# MySQL Config
myConfig = {'host': 'localhost', 'username': 'root', 'password': '', 'db': 'swachh_manch'}
#myConfig = {'host': 'localhost', 'username': 'admin', 'password': 'Sbm123!123', 'db': 'swachh_manch'}

# MongoDB connections
#connect('swachh_manch_python', host="localhost", port=27017, username="admin", password="Sbm123!123")
#connect(db='swachh_manch', host="localhost", username="db_admin", password="Sbm123")
connect('swachh_manch', host="localhost", port=27017, username="", password="")


# Insert User to MongoDB
def index(ward):
    ward_count = Ward.objects(ward_id=ward[0]).count()

    if ward_count == 0:
        title = (ward[6].lower()).title() if ward[6] else None
        titles = [
            {"en": {"title": title}},
            {"hi": {"title": title}},
            {"te": {"title": title}},
            {"ta": {"title": title}},
            {"mr": {"title": title}},
            {"kn": {"title": title}},
            {"ml": {"title": title}},
            {"bn": {"title": title}}
        ] if title else None
        
        Ward(ward_id=int(ward[0]),
                    city_id=ward[1],
                    titles=titles,
                    ward_number=str(ward[2]) if ward[2] else '',
                    bound_id=int(ward[3]) if ward[3] else None,
                    previous_rank=int(ward[4]) if ward[4] else None,
                    created_at=ward[5],
                    updated_at=ward[5]).save()

        print('Ward: ' + str(ward[0]) +' indexed')
    else:
        print('Ward: ' + str(ward[0]) + ' already exists')

    return True


# Fetch Users from MySQL
def fetch_wards(offset=75000, limit=150000):
    mycon = mydb.connect(myConfig['host'], myConfig['username'],
                         myConfig['password'], myConfig['db'], charset='utf8mb4')
    with mycon:

        cur = mycon.cursor()
        cur.execute(f"SELECT sbm_wards.id, sbm_wards.city_id, sbm_wards.ward_no, \
                    sbm_wards.bound_id, sbm_wards.previous_rank, \
                    sbm_wards.created_at, sbm_ward_localize.title \
                    FROM sbm_wards \
                    LEFT JOIN sbm_ward_localize on sbm_ward_localize.ward_id = sbm_wards.id \
                    AND sbm_ward_localize.locale = 'en' \
                    where sbm_wards.deleted = 0 \
                    limit {offset}, {limit}")
        wards = cur.fetchall()
        return wards

# Main Function
def main():
    wards = fetch_wards()

    for ward in wards:
        index(ward)

main()