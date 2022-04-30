import requests
import json
import xmltodict # will need to pip install xmltodict
import csv
import xml.etree.ElementTree as ET
def getData(code):
    return json.loads(json.dumps(xmltodict.parse(requests.get(f'https://api.globalgiving.org/api/public/projectservice/countries/{code}/projects?api_key=b65a4229-29bd-42ca-8267-eb7768a8110c').content)))['projects']['project']

print(getData('in'))