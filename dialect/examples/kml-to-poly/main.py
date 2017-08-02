from lxml import etree
from io import StringIO, BytesIO
import json

polygon_tag = "{http://www.opengis.net/kml/2.2}Polygon"
description_tag = "{http://www.opengis.net/kml/2.2}description"
coordinates_tag = "{http://www.opengis.net/kml/2.2}coordinates"

provincies = [
    "Groningen",
    "Drenthe",
    "Flevoland",
    "Utrecht",
    "Noord-Holland",
    "Zuid-Holland",
    "Friesland",
    "Noord-Brabant",
    "Zeeland",
    "Limburg",
    "Gelderland",
    "Overijssel"
]


def parse_description(tag):
    for txt in tag.itertext():
        for provincie in provincies:
            if (txt.find(provincie) > 0):
                return provincie

def parse_polygons(polygon_tag):
    result = []
    for ctag in polygon_tag.iter(coordinates_tag):
        for txt in ctag.itertext():
            coor = txt.split(" ")
            for c in coor:
                lnglat = c.split(',')
                tmp = {}
                tmp["lat"] = lnglat[1]
                tmp["lng"] = lnglat[0]
                result.append(tmp)
        return result


tree = etree.parse("provincies.kml")
result = {}
current_provincie = ""
for el in tree.iter([polygon_tag, description_tag]):
    if (el.tag == polygon_tag):
        result[current_provincie] = result[current_provincie] + parse_polygons(el))
    else:
        current_provincie = parse_description(el)
        result[current_provincie] = []
        print(current_provincie)


with open("result.txt", "w") as f:
    json.dump(result, f)





