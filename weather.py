import requests

import config


def get_weather(city: str):
    """
    :param city: Для какого города искать погоду
    :return: Данные о погоде
    """

    params = {'access_key': config.weatherToken,
              'query': city}
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    return {'temperature': api_response['current']['temperature'],
            'ico': api_response['current']['weather_icons'][0],
            'feelslike': api_response['current']['feelslike'],
            'visibility': api_response['current']['visibility'],
            'weather_descriptions': api_response['current']['weather_descriptions'][0]}
