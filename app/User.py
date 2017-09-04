from app.BaseUser import BaseUser


class User(BaseUser):

    fname = "nageswara rao"
    lname = "samayam"
    _pro_var = "this is public variable"
    __surname = 'this is private variable'

    def get_full_name(self):
        full_name = self.fname + ' ' + self.lname
        print(self._pro_var)
        return  full_name.title()

    @staticmethod
    def get_static_call():
        return "Inside static method"




user_obj = User();
print(user_obj.get_full_name())
print(user_obj.get_static_call())