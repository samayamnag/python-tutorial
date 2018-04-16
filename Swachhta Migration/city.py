from mongoengine import *
import pymysql


class City(Document):
    city_id = IntField()
    code = StringField()
    titles = ListField(DictField())
    state_id = IntField(null=True)
    district_id = IntField(null=True)
    geo_coordinates = PointField()
    ward_count = IntField(default=0)
    population = IntField(default=0)
    population_bucket = IntField(choices=[1, 2, 3, None])
    census_code = IntField(null=True)
    created_at = DateTimeField()
    updated_at = DateTimeField()
    

    meta = {'collection': 'cities'}


    def __str__(self):
        return self.city_id

