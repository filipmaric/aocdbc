import unittest
from icontract_hypothesis import test_with_inferred_strategy
from petlja.max3 import max3_ver0, max3_ver1, max3_ver2, max3_error1

max3 = max3_error1

class TestMax3(unittest.TestCase):
    def test_1(self) -> None:
        result = max3(3, 2, 4)
        self.assertEqual(result, 4)

    def test_verify_with_icontract_hypothesis(self) -> None:
        test_with_inferred_strategy(max3)
    

if __name__ == "__main__":
    unittest.main()
