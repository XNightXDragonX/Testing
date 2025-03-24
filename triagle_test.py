import unittest

def check_triangle(side1: int, side2: int, side3: int):
    if side1 <= 0 or side2 <= 0 or side3 <= 0 or ((side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1)):
        result = "Треугольник не существует"
    elif side1 == side2 and side2 == side3:
        result = "Равносторонний треугольник"
    elif (side1 == side2 and side1 != side3) or (side1 == side3 and side1 != side2) or (side2 == side3 and side2 != side1):
        result = "Равнобедренный треугольник"
    else:
        result = "Разносторонний треугольник"
    return result

class TestCheckTriangle(unittest.TestCase):
    def test_triangle_cases(self):
        test_cases = [
            # Треугольник не существует
            (0, 1, 1, "Треугольник не существует"),    # Нулевая сторона
            (-1, 2, 2, "Треугольник не существует"),   # Отрицательная сторона
            (1, 1, 3, "Треугольник не существует"),    # Нарушение неравенства треугольника
            (2, 2, 5, "Треугольник не существует"),    # Нарушение неравенства треугольника
            
            # Равносторонний треугольник
            (3, 3, 3, "Равносторонний треугольник"),   # Все стороны равны
            (10, 10, 10, "Равносторонний треугольник"),
            
            # Равнобедренный треугольник
            (3, 3, 4, "Равнобедренный треугольник"),   # Две стороны равны
            (5, 3, 5, "Равнобедренный треугольник"),
            (2, 4, 4, "Равнобедренный треугольник"),
            
            # Разносторонний треугольник
            (3, 4, 5, "Разносторонний треугольник"),   # Все стороны разные
            (7, 8, 9, "Разносторонний треугольник"),
        ]
        
        for side1, side2, side3, expected in test_cases:
            with self.subTest(side1=side1, side2=side2, side3=side3, expected=expected):
                result = check_triangle(side1, side2, side3)
                self.assertEqual(result, expected,
                               f"Для сторон ({side1}, {side2}, {side3}) ожидалось '{expected}', получено '{result}'")

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            check_triangle("3", 4, 5)  # Передаём строку вместо числа

if __name__ == '__main__':
    unittest.main()