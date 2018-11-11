def main():
    print_header()
    location = get_user_location()
    fetch_http(location)
        
    #user input for weather location
    #create a http request to site with location
    #scrape page for weather info


def print_header():
    print('--------------------')
    print('    WEATHER-APP')
    print('--------------------')


def get_user_location():
    input_location = input('Weather Location: ')
    location = input_location.lower().strip()
    return location


def fetch_http(location):
    address = "https://www.wunderground.com/weather/gb/{}".format(location)
    print('Fetching weather data from {}'.format(address))


if(__name__ == '__main__'):
    main()
