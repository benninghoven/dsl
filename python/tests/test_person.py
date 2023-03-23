import unittest
from person import Person

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person = Person("Alice", 25)

    def test_person_name(self):
        self.assertEqual(self.person.name, "Alice")

    def test_person_age(self):
        self.assertEqual(self.person.age, 25)

    def test_person_is_adult(self):
        self.assertTrue(self.person.is_adult())

