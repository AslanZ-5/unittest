import unittest
import test
from test import Employee


# class TestCalc(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(test.add(10, 5), 15)
#         self.assertEqual(test.add(-1, 1), 0)
#         self.assertEqual(test.add(-1, -1), -2)
#
#     def test_substract(self):
#         self.assertEqual(test.substract(10, 5), 5)
#         self.assertEqual(test.substract(-1, 1), -2)
#         self.assertEqual(test.substract(-1, -1), 0)
#
#     def test_multiply(self):
#         self.assertEqual(test.multiply(10, 5), 50)
#         self.assertEqual(test.multiply(-1, 1), -1)
#         self.assertEqual(test.multiply(-1, -1), 1)
#
#     def test_divide(self):
#         self.assertEqual(test.divide(10, 5), 2)
#         self.assertEqual(test.divide(-1, 1), -1)
#         self.assertEqual(test.divide(-1, -1),1)
#         self.assertEqual(test.divide(5, 2),2.5)
#         with self.assertRaises(ValueError):
#             test.divide(10,0)
#
# if __name__ == '__main__':
#     unittest.main()


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')
    @classmethod
    def tearDownClass(cls):
        print('teardownClasssss')

    def setUp(self):
        print('setup')
        self.emp_1 = Employee('Aslan', 'Zurabov', 50000)
        self.emp_2 = Employee('Shamil', 'Hamhoev', 60000)

    def tearDown(self):
        print('tesrdown')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Aslan.Zurabov@email.com')
        self.assertEqual(self.emp_2.email, 'Shamil.Hamhoev@email.com')

        self.emp_1.first = 'Mansur'
        self.emp_2.last = 'Musaev'

        self.assertEqual(self.emp_1.email, 'Mansur.Zurabov@email.com')
        self.assertEqual(self.emp_2.email, 'Shamil.Musaev@email.com')

    def test_fullname(self):
        print('test_fullname')

        self.assertEqual(self.emp_1.fullname, 'Aslan Zurabov')
        self.assertEqual(self.emp_2.fullname, 'Shamil Hamhoev')

        self.emp_1.first = 'Isa'
        self.emp_2.first = 'Hamza'

        self.assertEqual(self.emp_1.fullname, 'Isa Zurabov')
        self.assertEqual(self.emp_2.fullname, 'Hamza Hamhoev')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()
