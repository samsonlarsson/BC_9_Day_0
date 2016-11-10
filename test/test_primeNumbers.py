from app import primeNumbers

import unittest


class Prime_Numbers_TestCase(unittest.TestCase):
	
	"""Tests for prime numbers generator function"""
	def test_case_integers(self):
		self.assertEqual(primeNumbers.generate_prime_numbers(""), 'Please ensure that you pass an integer')


if __name__ == '__Prime_Numbers_Test__':
	Prime_Numbers_TestCase()
		