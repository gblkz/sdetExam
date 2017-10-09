# C-python 3.6.2, Windows.

import requests
import sys


def main(argv):
    input_value = str(argv)
    url = 'http://services.groupkt.com/state/get/USA/all'
    found = 'false'  # flag to track search success.

    # Determine key from user input.
    if input_value.__len__() > 2:
        my_key = 'name'
    else:
        my_key = 'abbr'

    # Required: character encoding, use requests module to manage encoding.
    # Required: keep connection alive, use Session to persist TCP connection.
    s = requests.Session()
    r = s.get(url)
    full_dict = r.json()  # parse json, store in dictionary.

    # Search each state container dict for the user input.
    for k in full_dict['RestResponse']['result']:
        if k[my_key].lower() == input_value.lower():
            # Determine the state's largest_city and capital.
            try:
                largest_city = k['largest_city']
                msgcity = 'The largest city in ' + input_value + ' is ' + largest_city + '.'
            except KeyError:
                msgcity = 'The largest city in ' + input_value + ' is undefined' + '.'

            try:
                capital = k['capital']
                msgcapital = 'The capital of ' + input_value + ' is ' + capital + '.'
            except KeyError:
                msgcapital = 'The capital of ' + input_value + ' is undefined' + '.'

            # Required: print the state's largest_city and capital.
            found = 'true'
            print(msgcity)
            print(msgcapital)
    if found == 'false':
        print('No state or territory matches ' + input_value + '.')


if __name__ == "__main__":
    if sys.argv.__len__() == 2:
        main(sys.argv[1])
    else:
        print('Please provide an argument for state (name or abbreviation).')
        print('Use double quotes to enclose multi-word arguments.')
