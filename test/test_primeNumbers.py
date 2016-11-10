from app import primeNumbers

import unittest


class Prime_Numbers_TestCase(unittest.TestCase):
	
	"""Tests for prime numbers generator function"""
	def test_case_integers(self):
		self.assertEqual(primeNumbers.generate_prime_numbers(""), 'Please ensure that you pass an integer')

	def test_case_primeNumbers(self):
		self.assertEqual(primeNumbers.generate_prime_numbers(10), [2, 3, 5, 7])

	def test_case_Negatives(self):
		self.assertEqual(primeNumbers.generate_prime_numbers(-6), [])

	def test_case_primeNumbers(self):
		self.assertEqual(primeNumbers.generate_prime_numbers(2), [2, 3, 5, 7, 11, 13, 17, 19])

	def test_case_Errors(self):
		self.assertEqual(primeNumbers.generate_prime_numbers(0) )

	def test_case_string(self):
		self.assertEqual(primeNumbers.generate_prime_numbers('2'), 'Please ensure that you pass an integer')

	def test_case_list(self):
		self.assertEqual(primeNumbers.generate_prime_numbers([3, 4, 60]), 'Please ensure that you pass an integer')

	def test_case_primeNumbers(self):
		self.assertEqual(primeNumbers.generate_prime_numbers(100), [[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]])

	def test_case_primeNumbers(self):
		self.assertEqual(primeNumbers.generate_prime_numbers(2), [1])

	def test_case_primeList_Return(self):
		self.assertIsInstance(primeNumbers.generate_prime_numbers(7), list)


if __name__ == '__main__':
	unittest.main()
		