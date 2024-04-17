import requests


class StudentsAPI:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_all_clothes(self):
        url = self.base_url
        res = requests.get(url).json()
        return res

    def get_cloth_by_id(self, cloth_id: int):
        url = f"{self.base_url}{cloth_id}"
        res = requests.get(url).json()
        return res


def test_get_all_clothes(api: StudentsAPI):
    res = api.get_all_clothes()
    assert (res == [{'student_id': 1,
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

def test_get_cloth_by_id(api: StudentsAPI):
    res = api.get_cloth_by_id(1)
    assert (res == {'student_id': 1,
             'name': 'John Smith',
             'gender': 'Male',
             'age': 20,
             'learning': 'Computer Science',
             'city': 'New York'})


def test_get_cloth_by_name(api: StudentsAPI):
    # Проверка получения информации по имени
    clothes = api.clothes()
    clothes_name = clothes[0]['name']  # Предполагаем, что компания существует в списке
    res = api.get_cloth_by_name(clothes_name)
    assert (res['name'] == clothes_name)


if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/api/v1/students/'
    api = StudentsAPI(URL)
    test_get_cloth_by_id(api)
    test_get_all_clothes(api)
    test_get_cloth_by_name(api)
