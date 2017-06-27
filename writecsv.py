
import csv
from iso8601utils import parsers
from bs4 import BeautifulSoup as Soup

list_of_files = ('./Facebook Insights Data Export_010115_061515.xml',
                './Facebook Insights Data Export_010116_061516.xml',
                './Facebook Insights Data Export_061615_113015.xml',
                './Facebook Insights Data Export_061616_113016.xml',
                './Facebook Insights Data Export_120115_123115.xml',
                './Facebook Insights Data Export_120116_052417.xml'
)


def parseXML(file, tab, columns):
    file_prefix = file[24:-4]
    writer = csv.writer(open(file_prefix + tab + ".csv", 'w'))
    handler = open(file).read()
    soup = Soup(handler,"lxml")
    this_rec = []

    for record in soup.findAll("data"):
        rec_attrs = dict(record.attrs)
        if len(record.contents) != 0:
            if rec_attrs['ss:type'] == "Number":
                this_rec.append(float(record.contents[0]))
            if rec_attrs['ss:type'] == "DateTime":
                this_rec.append(parsers.datetime(record.contents[0]))
            if rec_attrs['ss:type'] == "String":
                this_rec.append(record.contents[0])
        else:
            this_rec.append('')

        if tab == 1:
            if len(this_rec) == 19 and this_rec[11] != "Lifetime Total Video Views":
                writer.writerow(this_rec)
                this_rec = []
        else:
            if len(this_rec == 16):
                writer.writerow(this_rec)

if __name__ == '__main__':
    for item in list_of_files:
        parseXML(item)
