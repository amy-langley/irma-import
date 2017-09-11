import logging
import json
from lxml import etree

def get_field_text(tree, path):
    nsmap = {"n1": tree.getroot().nsmap['n1']}
    node = tree.xpath(path, namespaces=nsmap)
    if len(node) > 0:
        return node[0].text
    return ''

def parse_metadata(scene, xml_filename, json_filename):
    logger = logging.getLogger(scene)
    logger.info("Parsing XML metadata from {0}".format(xml_filename))

    result = {'!scene': scene}

    tree = etree.parse(xml_filename)
    with open(json_filename, 'r') as myfile:
        tile_json = myfile.read()
    tile = json.loads(tile_json)

    scene_time = get_field_text(tree, "n1:General_Info/SENSING_TIME")
    result['acquired_date'] = scene_time.split('T')[0]
    result['acquired_time'] = scene_time.split('T')[1]

    coords = tile['tileGeometry']['coordinates'][0]
    result["#scene_corner_UL_x"] = coords[0][0]
    result["#scene_corner_UL_y"] = coords[0][1]
    result["#scene_corner_UR_x"] = coords[1][0]
    result["#scene_corner_UR_y"] = coords[1][1]
    result["#scene_corner_LR_x"] = coords[2][0]
    result["#scene_corner_LR_y"] = coords[2][1]
    result["#scene_corner_LL_x"] = coords[3][0]
    result["#scene_corner_LL_y"] = coords[3][1]

    result["#utm_zone"] = tile["utmZone"]

    return result
