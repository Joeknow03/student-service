import requests


def test_get_all_companies(url: str):
    res = requests.get(url).json()
    assert (res == [{'students_id': 1, 'name': 'John Smith', 'gender': 'Male', 'age': 20, 'learning': 'Computer Science',
                     'city': 'New York'},
                    {'students_id': 2, 'name': 'Emma Johnson', 'gender': 'Female', 'age': 21, 'learning': 'Biology',
                     'city': 'Los Angeles'},
                    {'students_id': 3, 'name': 'Michael Lee', 'gender': 'Male', 'age': 19, 'learning': 'History',
                     'city': 'Chicago'},
                    {'students_id': 4, 'name': 'Sophia Garcia', 'gender': 'Female', 'age': 22, 'learning': 'Psychology',
                     'city': 'London'},
                    {'students_id': 5, 'name': 'Daniel Kim', 'gender': 'Male', 'age': 20, 'learning': 'Engineering',
                     'city': 'Tokyo'}])


def test_get_company_by_id(url: str):
    res = requests.get(url).json()
    assert (res == {'students_id': 1, 'name': 'John Smith', 'gender': 'Male', 'age': 20, 'learning': 'Computer Science',
                    'city': 'New York'})


if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/api/v1/students/'
    test_get_company_by_id(URL + '1')
    test_get_all_companies(URL)
