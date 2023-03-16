import unittest

def add_numbers(x,y):
    if x == None or y == None:
        raise ValueError("Requires two parameters")
    if not isinstance(x,int) or not isinstance(y,int):
        raise ValueError("Must be type<int>")
    return x + y

class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)
    def test_add_numbers(self):
        result = add_numbers("string", 3)
        self.assertEqual(result, "Must be type<int>")

if __name__ == '__main__':
    unittest.main()
