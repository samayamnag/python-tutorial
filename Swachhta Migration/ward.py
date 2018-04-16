from mongoengine import *
import pymysql


class Ward(Document):
    city_id = IntField()
    ward_id = IntField(unique=True)
    ward_number = StringField()
    titles = ListField(StringField())
    created_at = DateTimeField()
    updated_at = DateTimeField()
    

    meta = {'collection': 'wards'}


    def __str__(self):
        return self.ward_id

