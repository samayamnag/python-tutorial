from mongoengine import *
import datetime


#connect('swachh_manch_python', host="localhost", port=27017, username="superAdmin", password="Sbm123!123")
#connect(db='swachh_manch', host="10.10.10.227", username="db_admin", password="Sbm123")

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
            'Super admin',
            'Admin',
            'Moderatior',
            'Citizen',
            'State admin',
            'District admin',
            'ULB admin',
            'Civic agency admin',
            'Civic agency user',
            'Engineer',
            'Escalations Engineer',
            'MP',
            'MLA',
            'Corporator',
            'SQS admin',
            'Nodal officer',
            'MOUH',
            'Event admin',
            'Event moderator',
        ]

    
