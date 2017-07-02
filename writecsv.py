
import csv
from iso8601utils import parsers
from bs4 import BeautifulSoup as Soup

filenames = [
    'Facebook Insights Data Export_010115_061515.xml',
    'Facebook Insights Data Export_010116_061516.xml',
    'Facebook Insights Data Export_061615_113015.xml',
    'Facebook Insights Data Export_061616_113016.xml',
    'Facebook Insights Data Export_120115_123115.xml',
]


# dict_files = {'total v unique': {
#                 'files': [
#                     './Facebook Insights Data Export_010115_061515.xml',
#                     './Facebook Insights Data Export_010116_061516.xml',
#                     './Facebook Insights Data Export_061615_113015.xml',
#                     './Facebook Insights Data Export_061616_113016.xml',
#                     './Facebook Insights Data Export_120115_123115.xml',
#                 ],
#                 'columns': 19,
#                 'tab': 1
#                 },
#             'lifetime post by type':{
#                 'files': [
#                     './lifetime_post_cons_type_010115_061515.xml',
#                     './lifetime_post_cons_type_010116_061516.xml',
#                     './lifetime_post_cons_type_061615_113015.xml',
#                     './lifetime_post_cons_type_120115_123115.xml',
#                 ],
#                 'columns':16 ,
#                 'tab': 2
#                 },
#             'lifetime post by act':{
#                 'files' :[
#                     './lifetime_post_stories_by_act_010115_061515.xml',
#                     './lifetime_post_stories_by_act_010116_061516.xml',
#                     './lifetime_post_stories_by_act_061615_113015.xml',
#                     './lifetime_post_stories_by_act_120115_123115.xml',
#                 ],
#                 'columns':15 ,
#                 'tab':3,
#             },
#             'ten sec views time spent':{
#                 'files': [
#                     './ten_sec_views_time_spent_010115_061515.xml',
#                     './ten_sec_views_time_spent_010116_061516.xml',
#                     './ten_sec_views_time_spent_061615_113015.xml',
#                     './ten_sec_views_time_spent_120115_123115.xml',
#                 ],
#                 'columns': 13,
#                 'tab': 4,
#             },
#             'lifetime vid views by dist': {
#                 'files': [
#                     './lifetime_vid_views_by_dist_010115_061515.xml',
#                     './lifetime_vid_views_by_dist_010116_061516.xml',
#                     './lifetime_vid_views_by_dist_061615_113015.xml',
#                     './lifetime_vid_views_by_dist_120115_123115.xml',
#                 ],
#                 'columns': 4,
#                 'tab': 5,
#             }
# }

def parseXML(filename):
    file_prefix = filename[:-4]

    handler = open(filename).read()
    soup = Soup(handler,"lxml")

    # creates an interable results set of worksheets
    worksheet = soup.findAll('worksheet')

    # iterate through each worksheet, get name, start writer
    for ws in worksheet:
        ws_name = dict(ws.attrs)['ss:name']
        writer = csv.writer(open(file_prefix + "_" + ws_name + ".csv", 'w'))

        for record in ws.findAll("data"):
            this_rec = []
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
            writer.writerow(this_rec)
            this_rec = []


if __name__ == '__main__':
    for f in filenames:
        parseXML(f)
