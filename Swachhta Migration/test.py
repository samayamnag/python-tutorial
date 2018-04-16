from mongoengine import *
import datetime
import json


#connect('swachh_manch_python', host="localhost", port=27017, username="superAdmin", password="Sbm123!123")
#connect(db='swachh_manch', host="10.10.10.227", username="db_admin", password="Sbm123")

class Channel(Document):
    #title = StringField(max_lenght=100, required=True, unique=True)
    #slug = StringField(max_lenght=150, required=True, unique=True)
    title = StringField(max_lenght=100, required=True)
    slug = StringField(max_lenght=150, required=True)
    platform = StringField(default="Swachhata", choices=['Swachhata', 'ICMYC'])
    app_name = StringField(required=True)
    type = StringField(required=True)
    archived = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField()

    meta = {
        'collection': 'channels'
    }

    def __str__(self):
        return self.title