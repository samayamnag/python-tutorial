from mongoengine import *
import datetime


class Role(Document):
    name = StringField(required=True, max_length=50)
    guard_name = StringField(max_length=50, default="api")
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(null=True)

    meta = {
        "collection": 'roles'
    }

    def __str__(self):
        return self.name

    @staticmethod
    def input_roles():
        return [
            'User',
            'Corporator',
            'Moderatior',
            'MLA',
            'MP',
            'Editor',
            'Moderator',
            'Saas Administrator',
            'civic_agency',
            'SQS Admin',
            'Engineer',
            'Nodal Officer',
            'Agency Head'
        ]

    
