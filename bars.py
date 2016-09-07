import sys
import json


def load_data(filepath):
    data = ''
    with open(filepath, 'r') as infile:
        data = infile.read()
    return json.loads(data)


def get_biggest_bar(data):
    return max(data, key=lambda x: x['Cells']['SeatsCount'])


def get_smallest_bar(data):
    return min(data, key=lambda x: x['Cells']['SeatsCount'])


def get_closest_bar(data, longitude, latitude):

    def get_distance(bar):
        lon, lat = bar['Cells']['geoData']['coordinates']
        return ((lon - longitude) ** 2 + (lat - latitude) ** 2) ** 0.5

    return min(data, key=get_distance)


if __name__ == '__main__':
    data = load_data(sys.argv[1])
    print('Biggest bar - {}'.format(get_biggest_bar(data)['Cells']['Name']))
    print('Smallest bar - {}'.format(get_smallest_bar(data)['Cells']['Name']))
    lon = float(input('Enter longtitude: '))
    lat = float(input('Enter latitude: '))
    print('Closest bar - {}'.format(
        get_closest_bar(data, lon, lat)['Cells']['Name'])
    )
