import xml.etree.ElementTree as ET


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
                                        timings = timings_with_day[1].split('-')
                                        timing['status'] = 'Opened'
                                        timing['from'] = timings[0]
                                        timing['to'] = timings[1]
                                    timings.append(timing)
                                toilet['timings'] = timings
                self.toilets.append(toilet)
        return self.toilets


obj = ParseXml("uploads\sample.xml")
print(obj.reader())
