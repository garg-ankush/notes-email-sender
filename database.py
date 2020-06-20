import json

# Ended up using http://beautifytools.com/excel-to-json-converter.php to convert Excel to Json
url = '/Users/ankushgarg/Desktop/email-reading-highlights/notes-email-sender/data/data.json'


def read_json_data():
    with open(url) as json_file:
        response = json.load(json_file)
    return response
