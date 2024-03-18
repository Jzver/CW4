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
        # params = {
        #     'per_page': 100,
        #     'text': self.major,
        #     'search_field': 'name'
        #     # 'currency': 'RUB'
        # }

        response = requests.get(f'http://api.hh.ru/vacancies?text={self.major}&search_field=name')
        return response.json()