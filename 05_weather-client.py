#!/usr/local/bin/python3

import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReprot',
                                       'cond, temp, scale, loc')



def print_the_header():
    print('------------------------------')
    print('      WEATHER APP')
    print('------------------------------')


def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    return response.text


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


def find_city_and_state_from_location(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()


def get_weather_from_html(html):
    # cityCss = 'div#location h1'
    # weatherConditionCss ='div#curCond span.wx-value'
    # weatherTempCss = 'div#curTemp span.wx-data span.wx-value'
    # weatherScaleCss = 'div#curTemp span.wx-data span.wx-unit'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()

    loc = cleanup_text(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    loc = find_city_and_state_from_location(loc)

    # print(condition, temp, scale, loc)
    # return (condition, temp, scale, loc)
    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report


def main():
    # print header
    print_the_header()

    # get location / zip code from user
    zipcode = input('What zipcode do you want the weather for ' +
                    '({})? '.format('30114'))

    # get html from web
    html = get_html_from_web(zipcode)

    # parse html
    report = get_weather_from_html(html)

    # dispay forecast
    print('The temp in {} is {}{} and {}'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))

if __name__ == '__main__':
    main()
