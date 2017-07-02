
import csv
from iso8601utils import parsers
from bs4 import BeautifulSoup as Soup

filenames = [
    'Facebook Insights Data Export_010116_061516.xml',
    'Facebook Insights Data Export_061615_113015.xml',
    'Facebook Insights Data Export_061616_113016.xml',
    'Facebook Insights Data Export_120115_123115.xml',
]


def parseXML(filename):
    file_prefix = filename[:-4]

    handler = open(filename).read()
    soup = Soup(handler,"lxml")

    # creates an interable results set of worksheets
    worksheet = soup.findAll('worksheet')
    print(len(worksheet))

    # iterate through each worksheet, get name, start writer
    for ws in worksheet:
        ws_name = dict(ws.attrs)['ss:name']

        writer = csv.writer(open(file_prefix + "_" + ws_name + ".csv", 'w'))
        print("processing ", file_prefix + "_" + ws_name)

        columns = int(dict(ws.find('table').attrs)['ss:expandedcolumncount'])
        this_rec = []

        for record in ws.findAll("data"):
            rec_attrs = dict(record.attrs)
            if len(record.contents) == 0:
                this_rec.append('')
            else:
                if rec_attrs['ss:type'] == "Number":
                    this_rec.append(float(record.contents[0]))
                if rec_attrs['ss:type'] == "DateTime":
                    this_rec.append(parsers.datetime(record.contents[0]))
                if rec_attrs['ss:type'] == "String":
                    this_rec.append(record.contents[0])

            # if the list is the right length, write the row to the file
            if len(this_rec) == columns:
                writer.writerow(this_rec)
                this_rec = []


if __name__ == '__main__':
    for f in filenames:
        parseXML(f)
