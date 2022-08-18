import requests

JSKOS_SERVER = "http://localhost:3000/mappings"

def get_mappings_from_jskos(ids: list):
    mapped_ids = set()
    res = {}
    for _id in ids:
        res = requests.get(JSKOS_SERVER, params={
            "from": _id,
            "direction": "both"
        })
        for match in res.json():
           mapped_ids.add(match["from"]["memberSet"][0]["uri"])
           # TODO add other urls to set
           mapped_ids.add(match["to"]["memberSet"][0]["uri"])
    return mapped_ids
