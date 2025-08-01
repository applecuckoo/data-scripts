# contours-to-simplestyle.py - script to convert the styling in ShakeMap contours into styling compatible with simplestyle-spec
# see https://geojson.io/#id=gist:applecuckoo/3be5c1470bb0adbf81f5bd8ba9dc494e&map=5.1/-36.94/144.61 for an example!
# SPDX-FileCopyrightText: applecuckoo <nufjoysb@duck.com>
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import sys

cont_colours = {
    0: "#FFFFFF",
    1: "#FFF7F3",
    1.5: "#FEF2E8",
    2: "#FEEDDE",
    2.5: "#FEDFC2",
    3: "#FDD0A2",
    3.5: "#FDBF86",
    4: "#FDAE6B",
    4.5: "#FD9E54",
    5: "#FD8D3C",
    5.5: "#F77B28",
    6: "#F16913",
    6.5: "#F0511A",
    7: "#F03B20",
    7.5: "#D61D23",
    8: "#BD0026",
    8.5: "#B00024",
    9: "#A30021",
  }

with open(f'{sys.argv[1]}.json', 'r', encoding='utf-8') as contours:
    contours_json = json.loads(contours.read())
    for features in contours_json['features']:
        features['properties']['stroke-width'] = features['properties']['weight']
        # features['properties']['stroke'] = features['properties']['color']
        for mmi, colours in cont_colours.items():
          if features['properties']['value'] == mmi:
            features['properties']['stroke'] = colours
        features['properties']['title'] = str(features['properties']['value'])
    with open(f'{sys.argv[1]}_simplestyle.geojson', 'w', encoding='utf-8') as contours_recoloured:
        contours_recoloured.write(json.dumps(contours_json))
        contours_recoloured.close()
