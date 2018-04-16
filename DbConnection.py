import 	


class DbConnection:

    @staticmethod
    def connect():
        return MySQLdb.connect(host="localhost",  # your host, usually localhost
                             user="root",  # your username
                             passwd="",  # your password
                             db="python_tutorial")

    @staticmethod
    def close(db):
        db.close()
