class Vacancy:
    vacancy_id = 0

    def __init__(self, title, city, url, salary, description, requirements):
        self.city = city
        self.title = title
        self.url = url
        self.__salary = salary
        self.description = description
        self.requirements = requirements
        self.validate_salary()
        Vacancy.vacancy_id += 1
        self.vacancy_id = Vacancy.vacancy_id

    def validate_salary(self):
        if not self.__salary:
            self.__salary = {'from': 0, 'to': 0}

    @property
    def salary(self):
        if not self.__salary['from']:
            self.__salary['from'] = 0
        if not self.__salary['to']:
            self.__salary['to'] = 0
        if self.__salary['from'] < self.__salary['to']:
            return self.__salary['to']
        return self.__salary['from']

    def __lt__(self, other):
        return self.salary < other.salary

    def __str__(self):
        return (f'Вакансия {self.title}, город - {self.city}, зарплата {self.salary}, '
                f'описание: {self.description}, требования: {self.requirements}, ссылка на вакансию: {self.url}\n')

    def __repr__(self):
        return (f'{self.__class__.__name__}({self.__dict__.items()})')