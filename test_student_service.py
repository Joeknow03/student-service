import requests


def test_get_all_companies(url: str):
    res = requests.get(url).json()
    assert(res == [{'student_id': 1,
             'name': 'John Smith',
             'gender': 'Male',
             'age': 20,
             'learning': 'Computer Science',
             'city': 'New York'},
            {'student_id': 2,
             'name': 'Emma Johnson',
             'gender': 'Female',
             'age': 21,
             'learning': 'Biology',
             'city': 'Los Angeles'},
            {'student_id': 3,
             'name': 'Michael Lee',
             'gender': 'Male',
             'age': 19,
             'learning': 'History',
             'city': 'Chicago'},
            {'student_id': 4,
             'name': 'Sophia Garcia',
             'gender': 'Female',
             'age': 22,
             'learning': 'Psychology',
             'city': 'London'},
            {'student_id': 5,
             'name': 'Daniel Kim',
             'gender': 'Male',
             'age': 20,
             'learning': 'Engineering',
             'city': 'Tokyo'}])


def test_get_company_by_id(url: str):
    res = requests.get(url).json()
    assert(res == {'student_id': 1,
             'name': 'John Smith',
             'gender': 'Male',
             'age': 20,
             'learning': 'Computer Science',
             'city': 'New York'})


if __name__ == '__main__':
    URL = 'http://127.0.0.1:79/api/v1/students/'
    test_get_company_by_id(URL + '1')
    test_get_all_companies(URL)
