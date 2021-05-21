import os
import requests

import config


def get_weather(city: str):
    """
    Возвращает данные о погоде для определённого города
    :param city: Для какого города искать погоду
    :return: Данные о погоде
    """

    params = {'access_key': os.environ.get(config.weatherToken),
              'query': city}
    api_result = requests.get(config.weatherURL, params)
    api_response = api_result.json()
    return {'temperature': api_response['current']['temperature'],
            'ico': api_response['current']['weather_icons'][0],
            'feelslike': api_response['current']['feelslike'],
            'visibility': api_response['current']['visibility'],
            'weather_descriptions': api_response['current']['weather_descriptions'][0]}
