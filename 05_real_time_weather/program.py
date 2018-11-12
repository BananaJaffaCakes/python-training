import requests
from bs4 import BeautifulSoup
import collections

t_weather_data = collections.namedtuple('weatherdata','place, temp, scale, desc')

def main():
    print_header()

    location = get_user_location()
    http_data = fetch_http(location)
    
    weather_data = parse_http_soup(http_data)
    print_weather_report(weather_data)

    print('\nExiting App...')


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
    print('\nFetching weather data from {}'.format(address))
    r = requests.get(address)
    print('Page Status Code: {}'.format(r.status_code))
    print('Page Content Type: {}'.format(r.headers.get('content-type')))
    print('Current Encoding Setting: {}'.format(r.encoding))

    return r.text


def parse_http_soup(http_data):
    http_soup = BeautifulSoup(http_data, 'html.parser')
    #print(http_soup.title)
    
    s_place = http_soup.find(class_='region-content-header').find('h1').get_text()
    s_temp = http_soup.find(class_='condition-data').find(class_='wu-value wu-value-to').get_text()
    s_scale = http_soup.find(class_='condition-data').find(class_='wu-label').get_text()
    s_desc = http_soup.find(class_='condition-icon small-6 medium-12 columns').find('p').get_text()

    weather_data = t_weather_data(
    place=clean_text(s_place), 
    temp=clean_text(s_temp), 
    scale=clean_text(s_scale), 
    desc=clean_text(s_desc)
    )
    return weather_data


def clean_text(dirty_text : str):
    #True if text is empty
    if dirty_text:
        return dirty_text
    
    cleaned_text = dirty_text.strip()
    return cleaned_text


def print_weather_report(nt):
    print('\nThe weather in {} is {} {} and {}'.format(nt.place, nt.temp, nt.scale, nt.desc))


if(__name__ == '__main__'):
    main()
