from mongoengine import *
import pymysql


class Ward(Document):
    city_id = IntField()
    ward_id = IntField(unique=True)
    ward_number = StringField(null=True)
    previous_rank=IntField(null=True)
    titles = ListField(DictField())
    bound_id = IntField(null=True)
    created_at = DateTimeField()
    updated_at = DateTimeField()    

    meta = {'collection': 'wards'}

    def __str__(self):
        return self.ward_number

