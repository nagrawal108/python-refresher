import unittest
from InstantiatingClass import Student

class TestStudent(unittest.TestCase):
    def test_str(self):
        s = Student("Bob", 21, 75)
        self.assertEqual(str(s), "Student(name=Bob, age=21, marks=75)")

    def test_calculate_grade_A(self):
        s = Student("A", 18, 95)
        self.assertEqual(s.calculate_grade(), 'A')

    def test_calculate_grade_B(self):
        s = Student("B", 19, 85)
        self.assertEqual(s.calculate_grade(), 'B')

    def test_calculate_grade_C(self):
        s = Student("C", 20, 75)
        self.assertEqual(s.calculate_grade(), 'C')

    def test_calculate_grade_D(self):
        s = Student("D", 22, 65)
        self.assertEqual(s.calculate_grade(), 'D')

    def test_calculate_grade_F(self):
        s = Student("F", 23, 50)
        self.assertEqual(s.calculate_grade(), 'F')

if __name__ == "__main__":
    unittest.main()
