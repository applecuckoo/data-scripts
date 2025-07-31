# feltrapid-to-simplestyle.py - script to convert GeoNet FELT Rapid files into simplestyle
# see https://geojson.io/#id=gist:applecuckoo/3be5c1470bb0adbf81f5bd8ba9dc494e&map=5.1/-36.94/144.61 for an example!
# SPDX-FileCopyrightText: applecuckoo <nufjoysb@duck.com>
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import sys

with open(f'{sys.argv[1]}.json', 'r', encoding='utf-8') as feltrapid:
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
    with open(f'{sys.argv[1]}_simplestyle.json', 'w', encoding='utf-8') as wikified:
        wikified.write(json.dumps(feltrapid_json))
