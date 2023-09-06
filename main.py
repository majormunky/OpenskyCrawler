import datetime
import json
import os
from dotenv import load_dotenv
from opensky_api import OpenSkyApi


load_dotenv()

USERNAME = os.getenv("OPENSKY_USERNAME")
PASSWORD = os.getenv("OPENSKY_PASSWORD")


def write_data(data):
    date_obj = datetime.datetime.now()
    filename = date_obj.strftime("%Y-%m-%d_%H-%M-%S") + ".json"
    filepath = "data/" + filename
    with open(filepath, "w") as f:
        json.dump(data, f)


def row_to_dict(row):
    return {
        "icao24": row.icao24,
        "callsign": row.callsign,
        "origin_country": row.origin_country,
        "time_position": row.time_position,
        "last_contact": row.last_contact,
        "longitude": row.longitude,
        "latitude": row.latitude,
        "baro_altitude": row.baro_altitude,
        "on_ground": row.on_ground,
        "velocity": row.velocity,
        "true_track": row.true_track,
        "vertical_rate": row.vertical_rate,
        "geo_altitude": row.geo_altitude,
        "squawk": row.squawk,
        "spi": row.spi,
        "position_source": row.position_source,
        "category": row.category,
    }


def main():
    box = (
        47.14706504629255,
        48.33281000890206,
        -117.59488330768617,
        -115.82333797539036,
    )

    api = OpenSkyApi(USERNAME, PASSWORD)
    states = api.get_states(bbox=box)

    data = []

    for s in states.states:
        obj = row_to_dict(s)
        data.append(obj)

    if len(data):
        write_data(data)


if __name__ == "__main__":
    main()
