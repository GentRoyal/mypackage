import unittest
from mypackage.myModule import maths, others 

class TestMathsFunctions(unittest.TestCase):

    def test_minimum(self):
        self.assertEqual(maths.minimum([3, 1, 4, 1, 5]), 1)
        self.assertEqual(maths.minimum([-5, -10, 0, 10]), -10)
        self.assertEqual(maths.minimum([2]), 2)  # Test with a single element

    def test_maximum(self):
        self.assertEqual(maths.maximum([3, 1, 4, 1, 5]), 5)
        self.assertEqual(maths.maximum([-5, -10, 0, 10]), 10)
        self.assertEqual(maths.maximum([2]), 2)  # Test with a single element

    def test_mean(self):
        self.assertAlmostEqual(maths.mean([3, 1, 4, 1, 5]), 2.8)
        self.assertAlmostEqual(maths.mean([10, 20, 30]), 20.0)
        self.assertEqual(maths.mean([5]), 5)  # Test with a single element

    def test_mode(self):
        self.assertEqual(maths.mode([3, 3, 4, 4, 5]), [3, 4])  # Test with multiple modes
        self.assertEqual(maths.mode([3, 1, 4, 1, 5]), 1)
        self.assertEqual(maths.mode([5, 5, 5, 5]), 5)  # All values are the same

    def test_median(self):
        self.assertEqual(maths.median([3, 1, 4, 1, 5]), 3)
        self.assertEqual(maths.median([10, 20, 30, 40]), 25)  # Test with even number of elements
        self.assertEqual(maths.median([5]), 5)  # Test with a single element

    def test_length(self):
        self.assertEqual(maths.length([3, 1, 4, 1, 5]), 5)
        self.assertEqual(maths.length([]), 0)  # Test with empty list
        self.assertEqual(maths.length([7]), 1)  # Test with a single element

    def test_sort(self):
        self.assertEqual(maths.sort([3, 1, 4, 1, 5]), [1, 1, 3, 4, 5])
        self.assertEqual(maths.sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(maths.sort([]), [])  # Test with empty list
        self.assertEqual(maths.sort([2]), [2])  # Test with a single element


class TestOthersFunctions(unittest.TestCase):

    def test_OTP_length(self):
        otp_length = 6
        otp = others.OTP(otp_length)
        self.assertEqual(len(otp), otp_length)  # Ensure OTP has correct number of digits
        self.assertTrue(otp.isdigit())  # Ensure OTP consists only of digits

    def test_OTP_unique(self):
        otp1 = others.OTP(6)
        otp2 = others.OTP(6)
        self.assertNotEqual(otp1, otp2)  # Ensure OTPs are unique

if __name__ == "__main__":
    unittest.main()
    
