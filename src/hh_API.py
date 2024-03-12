from abc import ABC, abstractmethod

import requests


class APIData(ABC):
    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        pass


class GetVacancies(APIData):
    def __init__(self, major):
        self.major = major

    def get_vacancies(self):
        params = {
            'per_page': 100,
            'search_field': 'name',
            'text': self.major,
            'currency': 'RUB'
        }

        response = requests.get('http://api.hh.ru/vacancies', params=params)
        return response.json