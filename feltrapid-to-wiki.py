# feltrapid-to-wiki.py - script to convert GeoNet FELT Rapid files into MediaWiki-compatible maps
# see https://geojson.io/#id=gist:applecuckoo/3be5c1470bb0adbf81f5bd8ba9dc494e&map=5.1/-36.94/144.61 for an example!
# SPDX-FileCopyrightText: applecuckoo <nufjoysb@duck.com>
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import sys

geojson_template = {
    "description": {"en": ""},

    "sources": "",

	"license": "CC-BY-3.0",

    "zoom": 5,
    "latitude":  -37.49,
    "longitude": 146.35,

    "data": {}
}

description = input('Please enter an English description of your map data: ')
sources = input('Please enter the GeoNet link: ')
zoom = int(input('Please enter zoom level: '))
lat = float(input('Please enter latitude: '))
long = float(input('Please enter longitude: '))

geojson_template['description']['en'] = description
geojson_template['sources'] = f'Available from [{sources} GeoNet] under [https://creativecommons.org/licenses/by/3.0/nz/deed.en CC BY 3.0 NZ]'
geojson_template['zoom'] = zoom
geojson_template['latitude'] = lat
geojson_template['longitude'] = long
with open(f'{sys.argv[1]}.json', 'r') as feltrapid:
    feltrapid_json = json.loads(feltrapid.read())
    for features in feltrapid_json['features']:
        match features['properties']['mmi']:
            case 3:
                features['properties']['marker-color'] = '#FDD0A2'
            case 4:
                features['properties']['marker-color'] = '#FDAE6B'
            case 5:
                features['properties']['marker-color'] = '#FD8D3C'
            case 6:
                features['properties']['marker-color'] = '#F16913'
            case 7:
                features['properties']['marker-color'] = '#F03B20'
            case 8:
                features['properties']['marker-color'] = '#BD0026'
        features['properties']['marker-symbol'] = str(features['properties']['mmi'])
        if features['properties']['mmi'] in range(3, 5):
            features['properties']['marker-size'] = 'small'
        elif features['properties']['mmi'] == 5:
            features['properties']['marker-size'] = 'medium'
        else:
            features['properties']['marker-size'] = 'large'
        del features['properties']['mmi']
        del features['properties']['count_mmi']
        del features['properties']['count']
    del feltrapid_json['count_mmi']
    del feltrapid_json['count']
    geojson_template['data'] = feltrapid_json
    with open(f'{sys.argv[1]}_wiki.json', 'w') as wikified:
        wikified.write(json.dumps(geojson_template))
