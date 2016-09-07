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
    data = load_data('bars.json')
    print(get_biggest_bar(data))
    print(get_smallest_bar(data))
    lon = float(input('Enter longtitude: '))
    lat = float(input('Enter latitude: '))
    print(get_closest_bar(data, lon, lat))
