from mongoengine import connect
import xml.etree.ElementTree as ET
from swachh_toilets import SwachhToilet


# Mongo DB connection
connect('swachh_manch')


class ImportToilet():

    def __init__(self, file, city):
        self.file = file
        self.city = city

    def parse_xml(self):
        tree = ET.parse(self.file)
        root = tree.getroot()
        data = dict()

        for listings in root:
            if listings.tag == 'listing':
                for listing in listings:
                    if listing.tag != 'content':
                        data[listing.tag] = listing.text
                    else:
                        data['content'] = self.parse_content_tag(listing)

                swachh_toilet = self.save(data)
                print(f'Toilet: {swachh_toilet.id} indexed')

    def parse_content_tag(self, content_tag):
        content_data = {}
        for content in content_tag:
            if content.tag == 'image':
                content_data[content.tag] = self.parse_image_tag(content)
            else:
                content_data['timings'] = self.parse_attributes_tag(content)
        return content_data

    def parse_attributes_tag(self, attributes_tag):
        timings = []
        for attribute in attributes_tag:
            status = 'Closed'
            timings_with_day = attribute.text.split(' ')
            timing = {
                'day': timings_with_day[0],
                'status': status,
                'from': None,
                'to': None
                }
            if timings_with_day[1] != 'Closed':
                timing_list = timings_with_day[1].split('-')
                timing['status'] = 'Opened'
                timing['from'] = timing_list[0]
                timing['to'] = timing_list[1]
            timings.append(timing)
        return timings

    def parse_image_tag(self, image_tag):
        return {
            'type': image_tag.get('type'),
            'url': image_tag.get('url'),
            'height': image_tag.get('height'),
            'width': image_tag.get('width')
            }

    def save(self, data):
        swachh_toilet = SwachhToilet(
            name={"en": data['name']},
            address=data['address'],
            coordinates=[float(data['longitude']), float(data['latitude'])],
            city=self.city,
            category=data['category'],
            timings=data['content']['timings'],
            image=data.get('content').get('image', None)
        ).save()

        return swachh_toilet


if __name__ == "__main__":
    # Need to care take about city name also
    obj = ImportToilet('sample_xml.xml', city='Bengaluru')
    obj.parse_xml()
