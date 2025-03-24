import unittest

def get_cost(weight: int):
    if weight <= 10:
        result = 'Стоимость доставки: 200 руб.'
    else:
        result = 'Стоимость доставки: 500 руб.'
    return result

class TestGetCost(unittest.TestCase):
    def test_cost_cases(self):
        test_cases = [
            (0, "Стоимость доставки: 200 руб."),    # Минимальный вес
            (5, "Стоимость доставки: 200 руб."),    # Вес меньше 10
            (10, "Стоимость доставки: 200 руб."),   # Граничное значение
            (11, "Стоимость доставки: 500 руб."),   # Вес больше 10
            (50, "Стоимость доставки: 500 руб."),   # Большой вес
        ]
        
        for weight, expected in test_cases:
            with self.subTest(weight=weight, expected=expected):
                result = get_cost(weight)
                self.assertEqual(result, expected,
                               f"Для weight={weight} ожидалось '{expected}', получено '{result}'")

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            get_cost("10")  # Передаём строку вместо числа

if __name__ == '__main__':
    unittest.main()