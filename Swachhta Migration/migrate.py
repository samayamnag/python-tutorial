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
import time, math, random


# MySQL Config
#myConfig = {'host': 'localhost', 'username': 'root', 'password': '', 'db': 'swachh_manch'}
#myConfig = {'host': 'localhost', 'username': 'admin', 'password': '', 'db': 'swachh_manch'}
#myConfig = {'host': '10.0.0.85', 'username': '', 'password': '', 'db': 'swachh_manch'}

# MongoDB connections
#connect('swachh_manch_python', host="localhost", port=27017, username="admin", password="Sbm123!123")
#connect(db='swachh_manch', host="localhost", username="db_admin", password="Sbm123")
connect('swachh_manch', host="localhost", port=27017, username="", password="")


# Insert User to MongoDB
def index(user):
    user_count = Profile.objects(user_id=user[0]).count()
    role = Role.objects(name="Citizen").first()
    source_id = 1 if user[4] == 0 else user[4]
    channel = Channel.objects(slug=map_channel(source_id)).first()

    if user_count == 0:
        #channels = []
        latitude = user[11]
        longitude = user[12]
        coordinates = [float(longitude), float(latitude)] if latitude and longitude else None
        city_id = None if user[10] == 0 else user[10]
        full_name = (user[1].lower().title()) if user[1] else 'Citizen'
        profile = Profile(user_id=int(user[0]),
                    full_name=full_name,
                    sign_up_with="mobile_number",
                    sign_up_ip_address=str(ipaddress.IPv4Address(user[2])),
                    avatar=user[3],
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
                            "city_id": city_id}}])
        
        profile.save()

        #role.update(push__profile_ids=str(profile.id))

        #print('User: ' + str(user[0]) + '==' + str(profile.id) + ' indexed')
        print('User: ' + str(user[0]) + ' indexed')
    else:
        print('User: ' + str(user[0]) + ' already exists')

    return True


# Fetch Users from MySQL
def fetch_users(offset=7669373, limit=500000):
    mycon = mydb.connect(myConfig['host'], myConfig['username'],
                         myConfig['password'], myConfig['db'], charset='utf8mb4')
    with mycon:

        cur = mycon.cursor()
        cur.execute(f"SELECT users.id, legacy_users.full_name, legacy_users.sign_up_ip, \
                    legacy_users.avatar, legacy_users.source_id, legacy_users.mac_address, \
                    legacy_users.device_token, legacy_users.last_login_at, legacy_users.location, \
                    legacy_users.ward_id, legacy_users.city_id, legacy_users.latitude, \
                    legacy_users.longitude, legacy_users.id as legacy_user_id \
                    FROM swachh_bharat.sbm_users as legacy_users \
                    JOIN users as users ON legacy_users.id = users.user_id \
                    ORDER BY users.id ASC \
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
def uniqid(prefix='', more_entropy=False):
    """uniqid([prefix=''[, more_entropy=False]]) -> str
    Gets a prefixed unique identifier based on the current
    time in microseconds.
    prefix
        Can be useful, for instance, if you generate identifiers
        simultaneously on several hosts that might happen to generate
        the identifier at the same microsecond.
        With an empty prefix, the returned string will be 13 characters
        long. If more_entropy is True, it will be 23 characters.
    more_entropy
        If set to True, uniqid() will add additional entropy (using
        the combined linear congruential generator) at the end of
        the return value, which increases the likelihood that
        the result will be unique.
    Returns the unique identifier, as a string."""
    m = time.time()
    sec = math.floor(m)
    usec = math.floor(1000000 * (m - sec))
    if more_entropy:
        lcg = random.random()
        the_uniqid = "%08x%05x%.8F" % (sec, usec, lcg * 10)
    else:
        the_uniqid = '%8x%05x' % (sec, usec)

    the_uniqid = prefix + the_uniqid
    return the_uniqid

# Main Function
def main():
    users = fetch_users()

    for user in users:
        index(user)
        #print(str(user[0]) + '===' + str(user[1]) + '===' + str(user[13]))

main()
