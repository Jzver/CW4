from src.vacancy import Vacancy

some_vacancy = Vacancy('title', 'city', 'url', 10000, None, 'description', 'requirements')
other_vacancy = Vacancy('title', 'city', 'url', 3000, 15000, 'description', 'requirements')


def test_init():
    assert some_vacancy.title == 'title'
    assert some_vacancy.city == 'city'
    assert some_vacancy.url == 'url'
    assert some_vacancy.salary_from == 10000
    assert some_vacancy.salary_to == 0
    assert some_vacancy.description == 'description'
    assert some_vacancy.requirements == 'requirements'
    assert some_vacancy.vacancy_id == 1


def test_validate_salary():
    some_vacancy.salary_to = None
    some_vacancy.validate_salary()
    assert some_vacancy.salary_to == 0


def test_salary():
    assert some_vacancy.salary == 10000


def test_lt():
    is_lt = (some_vacancy < other_vacancy)
    assert is_lt == True


def test_str():
    assert str(some_vacancy) == ('Вакансия title, город - city, зарплата от 10000 до 0, '
                                 'описание: description, требования: requirements, ссылка на вакансию: '
                                 'url\n')


def test_repr():
    assert repr(other_vacancy) == 'Вакансия №2, title'
