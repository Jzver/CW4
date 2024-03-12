from src.hh_API import APIData, GetVacancies

get_vac = GetVacancies('some_major')


def test_init():
    assert get_vac.major == 'some_major'
