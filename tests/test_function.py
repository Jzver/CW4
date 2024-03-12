from src.function import filter_city, filter_vacancies, get_vacancies_by_salary, print_vacancies, sort_vacancies, \
    get_top_vacancies
from src.vacancy import Vacancy

vac1 = Vacancy('title', 'city', 'url', 10000, 25000, 'description', 'requirements')
vac2 = Vacancy('title', 'town', 'url', 3000, 15000, 'description', 'requirements, python')
vac3 = Vacancy('title', 'city', 'url', 6000, None, 'description, python', 'requirements')
some_list = [vac1, vac2, vac3]


def test_filter_city():
    new_list = filter_city(some_list, 'town')
    assert new_list == [vac2]
    new_list = filter_city(some_list, city='нет')
    assert new_list == some_list


def test_filter_vacancies():
    new_list = filter_vacancies(some_list, filter_words='нет')
    assert new_list == some_list
    new_list = filter_vacancies(some_list, 'python')
    assert new_list == [vac2, vac3]


def test_get_vacancies_by_salary():
    new_list = get_vacancies_by_salary(some_list, salary_range='нет')
    assert new_list == some_list
    new_list = get_vacancies_by_salary(some_list, '10000 20000')
    assert new_list == [vac1, vac2]


def test_sort_vacancies():
    new_list = sort_vacancies(some_list)
    assert new_list == [vac1, vac2, vac3]


def test_get_top_vacancies():
    new_list = get_top_vacancies(some_list, 2)
    assert new_list == [vac1, vac2]