import json

from overpass import API

api = API()

def get_coords(latitude, longitude):
    overpass_query = f"""
    (
    way
    (around:50,{latitude},{longitude})
    [highway~"^(primary|secondary|tertiary|residential)$"]
    [name];
    >;);out;
    """
    response = api.Get(overpass_query)

    coordinates = list()
    latitudes = list()
    longitudes = list()

    for feature in response['features']:
        if len(feature['geometry']['coordinates']):
            coordinates.append(feature['geometry']['coordinates'])
            longitudes.append(feature['geometry']['coordinates'][0])
            latitudes.append(feature['geometry']['coordinates'][1])
    return latitudes[:5],longitudes[:5]

