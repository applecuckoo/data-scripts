# contours-to-wiki.py - script to convert a ShakeMap contour file into MediaWiki-compatible map data
# see https://geojson.io/#id=gist:applecuckoo/3be5c1470bb0adbf81f5bd8ba9dc494e&map=5.1/-36.94/144.61 for an example!
# SPDX-FileCopyrightText: applecuckoo <nufjoysb@duck.com>
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import sys

license_list = ['CC0-1.0', 'CC-BY-1.0', 'CC-BY-2.0', 'CC-BY-2.5', 'CC-BY-3.0', 'CC-BY-4.0', 'CC-BY-4.0+', 'CC-BY-SA-1.0', 'CC-BY-SA-2.0', 'CC-BY-SA-2.5', 'CC-BY-SA-3.0', 'CC-BY-SA-4.0', 'CC-BY-SA-4.0+', 'ODbL-1.0', 'dl-de-zero-2.0', 'dl-de-by-1.0', 'dl-de-by-2.0', 'GeoNutzV']

geojson_template = {
    "description": {"en": ""},

    "sources": "",

	"license": "CC0-1.0",

    "zoom": 5,
    "latitude":  -37.49,
    "longitude": 146.35,

    "data": {}
}
print('Licenses available:')
i = 0
for licenses in license_list:
    print(f'{i}: {licenses}')
    i = i + 1
license_index = int(input('Please pick a license: '))
description = input('Please enter an English description of your map data: ')
sources = input('Please enter your source: ')
zoom = int(input('Please enter zoom level: '))
lat = float(input('Please enter latitude: '))
long = float(input('Please enter longitude: '))

geojson_template['license'] = license_list[license_index]
geojson_template['description']['en'] = description
geojson_template['sources'] = sources
geojson_template['zoom'] = zoom
geojson_template['latitude'] = lat
geojson_template['longitude'] = long
with open(f'{sys.argv[1]}.json', 'r', encoding='utf-8') as contours:
    contours_json = json.loads(contours.read())
    for features in contours_json['features']:
        features['properties']['stroke-width'] = features['properties']['weight']
        features['properties']['stroke'] = features['properties']['color']
        features['properties']['title'] = str(features['properties']['value'])
    geojson_template['data'] = contours_json
    with open(f'{sys.argv[1]}_wiki.json', 'w', encoding='utf-8') as wikified:
        wikified.write(json.dumps(geojson_template))
