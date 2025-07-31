# contours-to-simplestyle.py - script to convert the styling in ShakeMap contours into styling compatible with simplestyle-spec
# see https://geojson.io/#id=gist:applecuckoo/3be5c1470bb0adbf81f5bd8ba9dc494e&map=5.1/-36.94/144.61 for an example!
# SPDX-FileCopyrightText: applecuckoo <nufjoysb@duck.com>
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import sys
with open(f'{sys.argv[1]}.json', 'r', encoding='utf-8') as contours:
    contours_json = json.loads(contours.read())
    for features in contours_json['features']:
        features['properties']['stroke-width'] = features['properties']['weight']
        features['properties']['stroke'] = features['properties']['color']
        features['properties']['title'] = str(features['properties']['value'])
    with open(f'{sys.argv[1]}_simplestyle.geojson', 'w', encoding='utf-8') as contours_recoloured:
        contours_recoloured.write(json.dumps(contours_json))
        contours_recoloured.close()
