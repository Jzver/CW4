from config import VACANCIES_DATA_PATH
from src.hh_API import GetVacancies
from src.function import filter_city, filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, \
    print_vacancies
from src.save_to_json import SaveToJSON
from src.vacancy import Vacancy


# Функция для взаимодействия с пользователем
def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    print('Следующие параметры опциональны, если вам не нужен какой-либо фильтр, напишите "нет" в ответе.\n')
    city = input('Введите название города ')
    filter_words = input("Введите ключевые слова для фильтрации вакансий(через пробел): ").split(' ')
    salary_range = input("Введите диапазон зарплат(через пробел): ")  # Пример: 100000 - 150000

    vacancies_from_api = GetVacancies(search_query)
    vacancies_from_hh = vacancies_from_api.get_vacancies

    file_vacancies = SaveToJSON(VACANCIES_DATA_PATH, vacancies_from_hh)
    file_vacancies.save()

    vacancies_list_json = file_vacancies.show()['items']
    vacancies_list = []

    for vacancy in vacancies_list_json:
        vacancies_list.append(
            Vacancy(vacancy['name'], vacancy['area']['name'], vacancy['alternate_url'], vacancy['salary']['from'],
                    vacancy['salary']['to'], vacancy['responsibility'], vacancy['requirement']))

    city_vacancies = filter_city(vacancies_list, city)

    filtered_vacancies = filter_vacancies(city_vacancies, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()