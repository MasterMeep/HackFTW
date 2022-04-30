import requests
import json
import xmltodict # will need to pip install xmltodict
def getData():
    return json.loads(json.dumps(xmltodict.parse(requests.get('https://api.globalgiving.org/api/public/projectservice/themes?api_key=b65a4229-29bd-42ca-8267-eb7768a8110c').content)))['themes']['theme']

def get_thingy():
    for i in getData():
        print (f'<option value="{i["name"]}">{i["name"]}</option>')
        
