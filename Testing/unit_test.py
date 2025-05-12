import unittest
from num import add

class TestAdd(unittest.TestCase):
    def test_add(self):
        test_cases = [
            (1, 2, 3),
            (2, 2, 4),
            (2, 3, 5),
            (2, 4, 6)
        ]
        for a, b, expected in test_cases:
            result = add(a, b)
            print(f"add({a}, {b}) = {result} (expected: {expected})")  # Выводим входы и результат
            self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
