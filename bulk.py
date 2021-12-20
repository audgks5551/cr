from elasticsearch import Elasticsearch, helpers
import csv
# Create the elasticsearch client.
es = Elasticsearch(host="localhost", port=9200)
# Open csv file and bulk upload
with open('article.csv', 'rt', encoding='UTF8') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='article2')
