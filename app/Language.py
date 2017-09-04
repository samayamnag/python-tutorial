from app.DbConnection import DbConnection
import json


class Language(DbConnection):

    @staticmethod
    def all():
        db_obj = DbConnection.connect()
        cursor = db_obj.cursor()
        cursor.execute('SELECT * FROM  icmyc_languages where status = %s', (1,))
        items = cursor.fetchall()
        db_obj.close()
        return json.dumps([dict(id=row[0], title=row[1]) for row in items])


obj = Language()
print(obj.all())
