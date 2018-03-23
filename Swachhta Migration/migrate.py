#!/usr/bin/python
# migrate.py
# Author: Nageswara Rao (nag.samayam@gmail.com)
# Date: Mar 23, 2018
# Version: 1.0.1
# Purpose: Migrate User from MySQL to Mongo Profiles


import pymysql as mydb  # Import MySQL Libraimport sys, tracebackry
from mongoengine import *
import ipaddress
from role import Role
from channel import Channel
from profile import Profile
import json
import datetime


# MySQL Config
myConfig = {'host': 'localhost',
            'username': 'root',
            'password': '',
            'db': 'swachh_manch_python'}

# MongoDB connections
connect('swachh_manch_python', host="localhost", port=27017, username="admin", password="Sbm123!123")
#connect(db='swachh_manch', host="10.10.10.227", username="db_admin", password="Sbm123")


# Insert User to MongoDB
def index(user):
    user_count = Profile.objects(user_id=user[0]).count()
    role = Role.objects(name="Citizen").first()
    channel = Channel.objects(slug=map_channel(user[4])).first()

    if user_count == 0:
        #channels = []
        coordinates = str(user[11]) + "," + str(user[12])
        profile = Profile(user_id=int(user[0]),
                    full_name=user[1],
                    sign_up_with="mobile_number",
                    sign_up_ip_address=str(ipaddress.IPv4Address(user[2])),
                    avatar=str(user[3]),
                    roles=[role.id],
                    channels=[{"id": channel.id, "slug": channel.slug, 
                    "mac_address": user[5], "sign_up": True, "device_token": user[6],
                    "last_login_at": user[7],
                    "settings": {"email_notifications_preferred": True, 
                    "sms_notifications_preferred": True, 
                    "push_notifications_preferred": True}}],
                    locations=[{"app_name": channel.app_name, 
                            "location": {"name": user[8], "coordinates": coordinates, 
                            "ward_id": user[9],
                            "city_id": user[10]}}])
        
        profile.save()

        print('User: ' + str(user[0]) +' indexed')
    else:
        print('User: ' + str(user[0]) + ' already exists')

    return True


# Fetch Users from MySQL
def fetch_users(offset=0, limit=250):
    mycon = mydb.connect(myConfig['host'], myConfig['username'],
                         myConfig['password'], myConfig['db'])
    with mycon:

        cur = mycon.cursor()
        cur.execute(f"SELECT users.id, legacy_users.full_name, legacy_users.sign_up_ip, \
                    legacy_users.avatar, legacy_users.source_id, legacy_users.mac_address, \
                    legacy_users.device_token, legacy_users.last_login_at, legacy_users.location, \
                    legacy_users.ward_id, legacy_users.city_id, legacy_users.latitude, legacy_users.longitude \
                    FROM sbm_users as legacy_users \
                    JOIN users as users ON legacy_users.id = users.user_id \
                    limit {offset}, {limit}")
        users = cur.fetchall()
        return users

'''
Handle swachhata channels
'''
def map_channel(id):
    return swachhata_channels()[id]


def swachhata_channels():
    return {
        1: "swachhata-citizen-android",
        2: "swachhata-citizen-ios",
        3: "swachhata-engineer-android",
        4: "swachhata-web",
        5: "swachhata-ms-excel",
        6: "swachhata-bbmp-sahaaya",
        7: "swachhata-icmyc-mumbai",
        8: "swachhata-external",
        9: "swachhata-mrc"
    }


'''
Insert roles
'''
'''
role = Role()

for input_role in role.input_roles():
    role_name = input_role.title()

    role = Role(name=role_name, updated_at=datetime.datetime.now)

    role.save()
    
for role in Role.objects:
    print(role.name)
'''

'''
Insert channels
'''
'''
open_file = open("dump-data.json", 'r')
parsed_data = json.loads(open_file.read())

for input_channel in parsed_data['channels']:
    title = input_channel['title'].title()
    title_to_lower = title.lower()
    slug = title_to_lower.replace(" ", '-')

    channel = Channel(title=title,
                        slug=slug,
                        app_name=input_channel['app_name'],
                        platform=input_channel['platform'],
                        created_at=datetime.datetime.now,
                        updated_at=datetime.datetime.now,
                        type=input_channel['type'],
                        archived=input_channel['archived'])
    channel.save()

# List channels
for channel in Channel.objects:
    print(channel.title)

'''
# Main Function
def main():
    users = fetch_users()

    for user in users:
        index(user)

main()