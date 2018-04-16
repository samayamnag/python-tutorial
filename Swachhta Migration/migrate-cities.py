#!/usr/bin/python
# migrate.py
# Author: Nageswara Rao (nag.samayam@gmail.com)
# Date: Mar 23, 2018
# Version: 1.0.1
# Purpose: Migrate User from MySQL to Mongo Profiles


import pymysql as mydb  # Import MySQL Libraimport sys, tracebackry
from mongoengine import *
from city import City
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
def index(city):
    city_count = City.objects(city_id=city[0]).count()

    if city_count == 0:
        latitude = float(city[4])
        longitude = float(city[5])
        geo_coordinates = {'type' : 'Point', 'coordinates' : [longitude, latitude]} if latitude and longitude else None
        title = (city[1].lower()).title()
        titles = [
            {"en": {"title": title}},
            {"hi": {"title": title}},
            {"te": {"title": title}},
            {"ta": {"title": title}},
            {"mr": {"title": title}},
            {"kn": {"title": title}},
            {"ml": {"title": title}},
            {"bn": {"title": title}}
        ]
        ward_count = int(city[6]) if city[6] else 0
        population_bucket = city[7] if city[7] > 0 else None
        
        City(city_id=int(city[0]),
                    code=city[1],
                    titles=titles,
                    district_id=int(city[2]) if city[2] else None,
                    state_id=int(city[3]) if city[2] else None,
                    geo_coordinates=geo_coordinates,
                    ward_count=ward_count,
                    population_bucket=population_bucket,
                    population=city[8],
                    census_code=city[9],
                    created_at=city[10],
                    updated_at=city[10]).save()

        print('City: ' + str(city[0]) +' indexed')
    else:
        print('City: ' + str(city[0]) + ' already exists')

    return True


# Fetch Users from MySQL
def fetch_cities(offset=0, limit=10000):
    mycon = mydb.connect(myConfig['host'], myConfig['username'],
                         myConfig['password'], myConfig['db'], charset='utf8mb4')
    with mycon:

        cur = mycon.cursor()
        cur.execute(f"SELECT sbm_cities.id, sbm_cities.code, sbm_cities.district_id, \
                    sbm_cities.state_id, sbm_cities.latitude, sbm_cities.longitude, \
                    sbm_cities.ward_count, sbm_cities.population_bucket, sbm_cities.population, \
                    sbm_cities.census_code, \
                    sbm_cities.created_at \
                    FROM sbm_cities \
                    limit {offset}, {limit}")
        users = cur.fetchall()
        return users

# Main Function
def main():
    cities = fetch_cities()

    for city in cities:
        index(city)

main()