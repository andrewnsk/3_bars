import sys
import json
from functools import partial


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def get_biggest_bar(json_data):
    return max(json_data['features'],
               key=lambda ev: ev['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(json_data):
    return min(json_data['features'],
               key=lambda ev: ev['properties']['Attributes']['SeatsCount'])


def _get_distance(user_location, bar_data):
    bar_coordinates = bar_data['geometry']['coordinates']
    distance = (user_location[0] - bar_coordinates[0]) ** 2 + (user_location[1] - bar_coordinates[1]) ** 2
    return distance


def get_closest_bar(_json_data, longitude, latitude):
    coord = longitude, latitude
    return min(_json_data['features'], key=partial(_get_distance, coord))


if __name__ == '__main__':
    json_data = load_data(sys.argv[1])
    longitude = float(input('enter longitude > '))
    latitude = float(input('enter latitude > '))
    print('Biggest bar: ', get_biggest_bar(json_data)['properties']['Attributes']['Name'])
    print('Smallest bar: ', get_smallest_bar(json_data)['properties']['Attributes']['Name'])
    print('Nearest bar: ', get_closest_bar(json_data, longitude, latitude)['properties']['Attributes']['Name'])
