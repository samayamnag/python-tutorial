from swachh_toilets import SwachhToilet
from mongoengine import connect
import csv


connect('swachh_manch')


class ImportToilet():

    possible_open_days = [
        'All Seven Days', 'Monday to Saturday',
        'Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday',
        'Monday to Friday',
    ]

    days = {'Sunday': 'Sun', 'Monday': 'Mon', 'Tuesday': 'Tue',
            'Wednesday': 'Wed', 'Thursday': 'Thu', 'Friday': 'Fri',
            'Saturday': 'Sat'}

    def __init__(self, file):
        self.file = file

    def read(self):
        '''data = pd.read_csv(self.file, header = None)
        data_json = json.loads(data.to_json(orient='records'))
        for value in data_json:
            print(value)
        '''
        csvfile = open(self.file, 'r', encoding="utf8")
        reader = csv.DictReader(csvfile)
        headers = [
                'QCI ID', 'State', 'City', 'Toilet ID', 'Address', 'Category',
                'Open Days', 'Opening Time', 'Closing Time', 'Image',
                'Latitude', 'Longitude', 'Type', 'Seats',
                'Differently Abled Friendly', 'Child Friendly', 'Fee',
                'Cost', 'Gender', 'Category Code', 'Type'
            ]

        for row in reader:
            data = {}
            for header in headers:
                formatted_header = header.lower().replace(' ', '_')
                data[formatted_header] = row[header]
            swachh_toilet = self.save(data)
            print(f'Toilet: {swachh_toilet.id} indexed')

    def save(self, data):
        differntly_abled_friedly = False
        if data['differently_abled_friendly'] == 'Yes':
            differntly_abled_friedly = True
        child_friendly = data['child_friendly']
        swachh_toilet = SwachhToilet(
            qci_id=data.get('qci_id', None).strip(),
            toilet_id=data.get('toilet_id').strip(),
            address=data.get('address', None).strip(),
            latitude=float(data.get('latitude').strip()),
            longitude=float(data.get('longitude').strip()),
            coordinates=[
                float(data['longitude'].strip()),
                float(data['latitude'].strip())
                ],
            state=data.get('state', None).strip(),
            city=data.get('city', None).strip(),
            category=data.get('category', None).strip(),
            category_code=data.get('category_code', None).strip(),
            type=data.get('type', None).strip(),
            open_days=data.get('open_days').strip(),
            opening_time=str(data['opening_time']).strip(),
            closing_time=str(data['closing_time']).strip(),
            seats=int(data['seats']) if data['seats'] else None,
            gender=data.get('gender').strip(),
            child_friendly=True if child_friendly == 'Yes' else False,
            differntly_abled_friedly=differntly_abled_friedly,
            fee_type=data.get('fee'),
            cost=data['cost'].strip() if data['cost'].strip() != '' else None,
            image=data.get('image', None) if data['image'] != '' else None
            ).save()

        return swachh_toilet


if __name__ == '__main__':
    obj = ImportToilet('Chirala Toilet Locator Data.csv')
    obj.read()
