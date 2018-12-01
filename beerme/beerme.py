#!/usr/bin/env python3

import argparse
import json
import sys

from html.parser import HTMLParser

from bs4 import BeautifulSoup
import requests


location_map = {
    'bh-bridge': 'https://business.untappd.com/boards/24264',
    'bh-bitters': 'https://business.untappd.com/boards/24239',
    'bh-huebner': 'https://business.untappd.com/boards/24278',
    'bh-shaenfield': 'https://business.untappd.com/boards/27711'
}

span_items = [
    'brewery',
    'name',
    'style',
    'abv',
    'ibu',
    'brewery-location'
]


def get_tap_list(script_data):
    tap_list = []
    for line in [_l.strip() for _l in script_data.splitlines()]:
        if not line:
            continue
        var, value = line.split('=', 1)
        if var.strip() == 'window.ITEMS_ARRAY':
            scrubbed = value.strip(';')
            tap_list = json.loads(scrubbed)
            break
    return tap_list


def parse_info(tap_list):
    parsed_tap_list = []
    for page in tap_list:
        soup = BeautifulSoup(page['html'], 'html.parser')
        info_elements = soup.find_all('div', {'class': 'info'})
        for info_element in info_elements:
            info_dict = {}
            for item in span_items:
                result = info_element.find('span', {'class': item})
                if result:
                    info_dict[item] = result.string
                else:
                    info_dict[item] = None
            parsed_tap_list.append(info_dict)
    return parsed_tap_list


def list_locations():
    for location, taplist in location_map.items():
        print(f'{location} : {taplist}')


def main():
    a = argparse.ArgumentParser('BeerMe BigHops Script v0.1')
    a.add_argument('--list', action='store_true', help='list available locations')
    a.add_argument('location', help='Beer target', default='', nargs='?')
    namespace = a.parse_args()

    if namespace.list:
        list_locations()
        sys.exit(0)

    if not namespace.location:
        print('Location not provided')
        a.print_usage()
        sys.exit(1)

    url = location_map.get(namespace.location)
    if not url:
        print(f'{namespace.location} does not exist')
        list_locations()
        sys.exit(1)

    _data = requests.get(url).text

    tap_list_page = BeautifulSoup(_data, 'html.parser')
    # Currently, the first script is the one we want
    _tap_list = get_tap_list(tap_list_page.find('script').string)

    print(json.dumps(parse_info(_tap_list), indent=2))


if __name__ == '__main__':
    main()