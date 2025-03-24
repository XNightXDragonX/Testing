import unittest

def check_auth(login: str, password: str):
    if login == "admin" and password == "password":
        result = 'Добро пожаловать'
    else:
        result = 'Доступ ограничен'
    return result

class TestCheckAuth(unittest.TestCase):
    def test_auth_cases(self):
        test_cases = [
            ("admin", "password", "Добро пожаловать"),  # Корректные данные
            ("admin", "wrong", "Доступ ограничен"),     # Неправильный пароль
            ("user", "password", "Доступ ограничен"),   # Неправильный логин
            ("user", "wrong", "Доступ ограничен"),      # Оба неправильные
            ("", "", "Доступ ограничен"),              # Пустые строки
            ("ADMIN", "password", "Доступ ограничен"), # Регистр имеет значение
        ]
        
        for login, password, expected in test_cases:
            with self.subTest(login=login, password=password, expected=expected):
                result = check_auth(login, password)
                self.assertEqual(result, expected, 
                               f"Для login='{login}', password='{password}' ожидалось '{expected}', получено '{result}'")

if __name__ == '__main__':
    unittest.main()