from mongoengine import *
import pymysql


class Profile(Document):
    user_id = IntField(unique=True)
    full_name = StringField(required=True, max_length=255)
    sign_up_with = StringField(default='email')
    settings = DictField(default={"email_notifications_preferred": True, 
    "sms_notifications_preferred": True, 
    "push_notifications_preferred": True})
    sign_up_ip_address = StringField(null=True)
    sign_up_user_agent = StringField(null=True)
    has_at_least_one_social_account = BooleanField(default=False)
    locations = ListField(DictField())
    social_accounts = ListField(DictField())
    channels = ListField(DictField())
    avatar = StringField(null=True)
    roles = ListField(ObjectIdField())

    meta = {'collection': 'profiles'}


    def __str__(self):
        return self.full_name

