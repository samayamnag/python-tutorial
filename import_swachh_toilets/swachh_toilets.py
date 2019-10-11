from mongoengine import (
    Document, StringField, DictField, ListField, DateTimeField, IntField, BooleanField, FloatField
)
from datetime import datetime


class SwachhToilet(Document):
    qci_id = StringField(null=True, unique=True)
    toilet_id = StringField(null=True, unique=True)
    address = StringField(required=True)
    latitude = FloatField(null=True)
    longitude = FloatField(null=True)
    coordinates = ListField()
    state = StringField(null=True)
    city = StringField(required=True)
    category = StringField(null=True)
    category_code = StringField(null=True)
    type = StringField(null=True)
    opening_time = StringField(null=True)
    closing_time = StringField(null=True)
    open_days = StringField(default='All Seven Days')
    seats = IntField(default=0)
    gender = StringField(default='Gents and Ladies')
    child_friendly = BooleanField(default=False)
    differntly_abled_friedly = BooleanField(default=False)
    fee_type = StringField(default='Free of Charge')
    cost = StringField(null=True)
    image = StringField(null=True)
    timestamp = DateTimeField(default=datetime.now)
    comments = ListField(DictField(), default=None)

    meta = {
        'collection': 'swachh_toilets',
        'indexes': [
            {
                'fields': ('coordinates',),
                'name': 'swachh_toilets_coordinates_index'
            },
            {
                'fields': ('city',),
                'name': 'swachh_toilets_city_index'
            }
        ]
    }

    def __str__(self):
        return self.qci_id

    def __repr__(self):
        return f'Public Toilet: {self.id}'
