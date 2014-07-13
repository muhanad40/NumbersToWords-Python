from unittest import TestCase
from lib import NumbersToWords

class NumbersToWordsTest(TestCase):

	def test_1_prints_One(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(1), "One")

	def test_5_prints_Five(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(5), "Five")

	def test_12_prints_Twelve(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(12), "Twelve")

	def test_20_prints_Twenty(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(20), "Twenty")

	def test_21_prints_Twenty_One(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(21), "Twenty One")

	def test_55_prints_Fifty_Five(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(55), "Fifty Five")

	def test_99_prints_Ninty_Nine(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(99), "Ninty Nine")

	def test_100_prints_One_Hundred(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(100), "One Hundred")

	def test_101_prints_One_Hundred_and_One(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(101), "One Hundred and One")

	def test_109_prints_One_Hundred_and_Nine(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(109), "One Hundred and Nine")

	def test_115_prints_One_Hundred_and_Fifteen(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(115), "One Hundred and Fifteen")

	def test_138_prints_One_Hundred_and_Thirty_Eight(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(138), "One Hundred and Thirty Eight")

	def test_581_prints_Five_Hundred_and_Eighty_One(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(581), "Five Hundred and Eighty One")

	def test_999_prints_Nine_Hundred_and_Ninty_Nine(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(999), "Nine Hundred and Ninty Nine")

class NumbersToWordsEdgeCaseTests(TestCase):

	def test_000_prints_nothing(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert_segment(000), "")

class NumbersToWordsLargeNumberTests(TestCase):

	def test_split_numbers_into_segments_of_3s(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.make_segments(1234), ["1", "234"])

	def test_1000_prints_One_Thousand(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(1000), "One Thousand")

	def test_1001_prints_One_Thousand_One(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(1001), "One Thousand, One")

	def test_1011_prints_One_Thousand_Eleven(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(1011), "One Thousand, Eleven")

	def test_1020_prints_One_Thousand_Twenty(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(1020), "One Thousand, Twenty")

	def test_1058_prints_One_Thousand_Fifty_Eight(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(1058), "One Thousand, Fifty Eight")

	def test_1100_prints_One_Thousand_One_Hundred(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(1100), "One Thousand, One Hundred")

	def test_1553_prints_One_Thousand_Five_Hundred_and_Fifty_Three(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(1553), "One Thousand, Five Hundred and Fifty Three")

	def test_4835_prints_Four_Thousand_Eight_Hundred_and_Thirty_Five(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(4835), "Four Thousand, Eight Hundred and Thirty Five")

	def test_9999_prints_Nine_Thousand_Nine_Hundred_and_Ninty_Nine(self):
		numbers_to_words = NumbersToWords.NumbersToWords()
		self.assertEqual(numbers_to_words.convert(9999), "Nine Thousand, Nine Hundred and Ninty Nine")
