from py import FizzBuzz
from unittest import TestCase


class Test(TestCase):
    def setUp(self):
        self.f = FizzBuzz()

    def test_all_numbers_not_multiple_three_or_five(self):
        #print self.f.getNumbers(range(1,3,1))
        self.assertListEqual(self.f.getNumbers(range(1,3,1)),[1, 2],
                             "should fail if not equal to [1, 2]")

    def test_all_multiples_three(self):
        #print self.f.getNumbers([3,6,9])
        self.assertListEqual(self.f.getNumbers([3,6,9]),['Fizz', 'Fizz', 'Fizz'],
                             "should fail if not equal to ['Fizz', 'Fizz', 'Fizz']")

    def test_all_multiples_three_and_others(self):
        #print self.f.getNumbers([1,3,6,9,11])
        self.assertListEqual(self.f.getNumbers([1,3,6,9,11]),[1, 'Fizz', 'Fizz', 'Fizz', 11],
                             "should fail if not equal to [1, 'Fizz', 'Fizz', 'Fizz', 11]")

    def test_all_multiples_five(self):
        #print self.f.getNumbers([5,10,20])
        self.assertListEqual(self.f.getNumbers([5,10,20]),['Buzz', 'Buzz', 'Buzz'],
                             "should fail if not equal to ['Buzz', 'Buzz', 'Buzz']")

    def test_all_multiples_five_and_others_and_not_multiples_three(self):
        #print self.f.getNumbers([1,5,10,20,22])
        self.assertListEqual(self.f.getNumbers([1,5,10,20,22]),[1, 'Buzz', 'Buzz', 'Buzz', 22],
                             "should fail if not equal to [1, 'Buzz', 'Buzz', 'Buzz', 22]")

    def test_all_multiples_five_or_multiples_three_and_others(self):
        #print self.f.getNumbers([x * 2 + 1 for x in range(5)]) #[1,3,5,7,9]
        self.assertListEqual(self.f.getNumbers([x * 2 + 1 for x in range(5)]),[1, 'Fizz', 'Buzz', 7, 'Fizz'],
                             "should fail if not equal to [1, 'Fizz', 'Buzz', 7, 'Fizz']")

    def test_all_multiples_three_and_five(self):
        #print self.f.getNumbers([15,30,45])
        self.assertListEqual(self.f.getNumbers([15,30,45]),['FizzBuzz','FizzBuzz','FizzBuzz'],
                             "should fail if not equal to ['FizzBuzz','FizzBuzz','FizzBuzz']")

    def test_all_multiples_three_and_five_with_other(self):
        #print self.f.getNumbers([1,15,30,45])
        self.assertListEqual(self.f.getNumbers([1,15,30,45]),[1, 'FizzBuzz', 'FizzBuzz', 'FizzBuzz'],
                             "should fail if not equal to [1, 'FizzBuzz', 'FizzBuzz', 'FizzBuzz']")

    def test_all_multiples_three_and_five_with_other_and_multiples_three(self):
        #print self.f.getNumbers([1, 3, 15,30,45])
        self.assertListEqual(self.f.getNumbers([1, 3, 15,30,45]),[1, 'Fizz', 'FizzBuzz', 'FizzBuzz', 'FizzBuzz'],
                             "should fail if not equal to [1, 'Fizz', 'FizzBuzz', 'FizzBuzz', 'FizzBuzz']")

    def test_all_multiples_three_and_five_with_other_and_multiples_three_and_multiples_five(self):
        ##print self.f.getNumbers([1,3,5,15,30,45])
        self.assertListEqual(self.f.getNumbers([1,3,5,15,30,45]),[1, 'Fizz', 'Buzz', 'FizzBuzz', 'FizzBuzz', 'FizzBuzz'],
                             "should fail if not equal to [1, 'Fizz', 'Buzz', 'FizzBuzz', 'FizzBuzz', 'FizzBuzz']")

    def test_all_random_numbers_up_15(self):
        self.f = FizzBuzz()
        ##print self.f.getNumbers()
        self.assertListEqual(self.f.getNumbers(),[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz'],
                             "should fail if not equal to [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']")

    def test_all_random_numbers_up_100(self):
        #print self.f.getNumbers(xrange(1, 101))
        self.assertListEqual(self.f.getNumbers(xrange(1, 101)),[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz', 31, 32, 'Fizz', 34, 'Buzz', 'Fizz', 37, 38, 'Fizz', 'Buzz', 41, 'Fizz', 43, 44, 'FizzBuzz', 46, 47, 'Fizz', 49, 'Buzz', 'Fizz', 52, 53, 'Fizz', 'Buzz', 56, 'Fizz', 58, 59, 'FizzBuzz', 61, 62, 'Fizz', 64, 'Buzz', 'Fizz', 67, 68, 'Fizz', 'Buzz', 71, 'Fizz', 73, 74, 'FizzBuzz', 76, 77, 'Fizz', 79, 'Buzz', 'Fizz', 82, 83, 'Fizz', 'Buzz', 86, 'Fizz', 88, 89, 'FizzBuzz', 91, 92, 'Fizz', 94, 'Buzz', 'Fizz', 97, 98, 'Fizz', 'Buzz'],
                             "should fail if not equal to [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz', 31, 32, 'Fizz', 34, 'Buzz', 'Fizz', 37, 38, 'Fizz', 'Buzz', 41, 'Fizz', 43, 44, 'FizzBuzz', 46, 47, 'Fizz', 49, 'Buzz', 'Fizz', 52, 53, 'Fizz', 'Buzz', 56, 'Fizz', 58, 59, 'FizzBuzz', 61, 62, 'Fizz', 64, 'Buzz', 'Fizz', 67, 68, 'Fizz', 'Buzz', 71, 'Fizz', 73, 74, 'FizzBuzz', 76, 77, 'Fizz', 79, 'Buzz', 'Fizz', 82, 83, 'Fizz', 'Buzz', 86, 'Fizz', 88, 89, 'FizzBuzz', 91, 92, 'Fizz', 94, 'Buzz', 'Fizz', 97, 98, 'Fizz', 'Buzz']")
