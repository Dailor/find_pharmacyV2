import requests
import CONST
import point_by_addr


def find_close(toponim, pos):
    params = {"ll": ','.join(str(x) for x in pos),
              "apikey": CONST.SEARCH_MAP_KEY,
              "text": toponim,
              "spn": "0.01,0.01",
              "lang": "en_RU"}
    r = requests.get(CONST.API_SEARCH_MAP, params).json()['features'][1]
    obj = dict()
    obj["pos"] = r["geometry"]["coordinates"]
    obj["box"] = r["properties"]["boundedBy"]
    obj["name"] = r["properties"]["CompanyMetaData"]["name"]
    obj["addr"] = r["properties"]["CompanyMetaData"]["address"]
    try:
        obj["time"] = r["properties"]["CompanyMetaData"]["Hours"]["text"]
    except:
        obj['time'] = "wasn't typed :("
    return obj
