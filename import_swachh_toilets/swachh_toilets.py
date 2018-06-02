from mongoengine import (
    Document, StringField, DictField, ListField, DateTimeField
)
from datetime import datetime


class SwachhToilet(Document):
    name = DictField(required=True)
    address = StringField(required=True)
    coordinates = ListField()
    city = StringField(required=True)
    category = StringField(null=True)
    timings = ListField(DictField(required=True))
    image = DictField(default=None)
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
        return self.name['en']

    def __repr__(self):
        return f'Public Toilet: {self.id}'
