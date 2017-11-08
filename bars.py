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


def get_closest_bar(data, longitude, latitude):
    dist = lambda s, d: (s[0] - d['geometry']['coordinates'][0]) ** 2 + (s[1] - d['geometry']['coordinates'][1]) ** 2
    coord = longitude, latitude
    return min(data['features'], key=partial(dist, coord))


if __name__ == '__main__':
    json_data = load_data(sys.argv[1])
    # print(json_data['features'])
    print('Biggest bar: ', get_biggest_bar(json_data)['properties']['Attributes']['Name'])
    print('Smallest bar: ', get_smallest_bar(json_data)['properties']['Attributes']['Name'])
    print('Nearest bar: ', get_closest_bar(json_data,
                          float(input('enter longitude > ')),
                          float(input('enter latitude > ')))['properties']['Attributes']['Name'])
