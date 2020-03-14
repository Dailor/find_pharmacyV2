import requests
import CONST


def get_map(p1, p2):
    p1, p2 = map(lambda x: map(str, x), (p1, p2))
    params = {
        'l': 'map',
        'pt': f"{','.join(p1)},pmwtm1~{','.join(p2)},pmwtm1"}
    r = requests.get(CONST.API_STATIC_MAP, params)
    return r
