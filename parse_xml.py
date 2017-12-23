import xml.etree.ElementTree as ET
import MySQLdb


class ParseXml:
    toilets = []

    def __init__(self, file):
        self.file = file

    def reader(self):
        tree = ET.parse(self.file)
        # tree = ET.ElementTree(self.file)
        root = tree.getroot()

        for listings in root:
            toilet = {'locale': 'en'}
            if listings.tag == 'listing':
                for listing in listings:
                    if listing.tag != 'content':
                        toilet[listing.tag] = listing.text
                    if listing.tag == 'content':
                        timings = []
                        for content in listing:
                            if content.tag == 'image':
                                toilet[content.tag] = {'type': content.get('type'), 'url': content.get('url'),
                                                       'height': content.get('height'), 'width': content.get('width')}
                            if content.tag == 'attributes':
                                for attribute in content:
                                    status = 'Closed'
                                    timings_with_day = attribute.text.split(' ')
                                    timing = {'day': timings_with_day[0], 'status': status}
                                    if timings_with_day[1] != 'Closed':
                                        timing_list = timings_with_day[1].split('-')
                                        timing['status'] = 'Opened'
                                        timing['from'] = timing_list[0]
                                        timing['to'] = timing_list[1]
                                    timings.append(timing)
                                toilet['timings'] = timings
                toilet_id = self.store(toilet)
                self.toilets.append(toilet_id)
                # self.toilets.append(toilet) // List of toilets
        return self.toilets

    def store(self, row):
        db_connection = self.db_connect(self)
        db_cursor = db_connection.cursor()

        ''' Insert into master table'''
        image = row.get('image')
        if image is None:
            row['image'] = None

        query = "INSERT INTO public_toilets(latitude, longitude, picture, category) " \
                "VALUES(%s, %s, %s,%s)"
        args = (row['latitude'], row['longitude'], row['image'], row['category'])

        db_cursor.execute(query=query, args=args)
        public_toilet_id = db_cursor.lastrowid

        if public_toilet_id:
            timings = row['timings']
            for timing in timings:
                from_time = timing.get('from')
                to_time = timing.get('to')
                if from_time is None:
                    timing['from'] = None
                if to_time is None:
                    timing['to'] = None

                ''' Insert into translations table'''
                translations_query = "INSERT INTO public_toilet_translations(public_toilet_id, locale, title,address, timings) " \
                                     "VALUES(%s,%s,%s,%s,%s)"
                translations_args = (public_toilet_id, row['locale'], row['name'], row['address'], str(row['timings']))
                db_cursor.execute(query=translations_query, args=translations_args)

                ''' Insert into timings table'''
                timings_query = "INSERT INTO public_toilets_timings(public_toilet_id, locale, day, status, from_time, to_time) " \
                                "VALUES(%s,%s,%s,%s,%s,%s)"
                timings_args = (public_toilet_id, row['locale'], timing['day'], timing['status'], timing['from'], timing['to'])
                db_cursor.execute(query=timings_query, args=timings_args)

        db_connection.commit()

        db_cursor.close()
        self.db_close(self, db=db_connection)

        return public_toilet_id

    @staticmethod
    def db_connect(self):
        return MySQLdb.connect(host="localhost",  # your host, usually localhost
                               user="root",  # your username
                               passwd="",  # your password
                               db="python_tutorial")

    @staticmethod
    def db_close(self, db):
        db.close()


obj = ParseXml("uploads\sample.xml")
toilets = obj.reader()
for toilet in toilets:
    print("Toilet ID: "+str(toilet))
