import unittest
from icontract_hypothesis import test_with_inferred_strategy
from petlja.sums_before_and_after_max import sums_before_and_after_max, difference_of_sums_before_and_after_max


class TestSecondInRank(unittest.TestCase):
    def test_1(self) -> None:
        result = sums_before_and_after_max([10, 13, 7, 13, 4])
        self.assertEqual(result, (1, 10, 24))

    def test_2(self) -> None:
        result = difference_of_sums_before_and_after_max([10, 13, 7, 13, 4])
        self.assertEqual(result, -14)

    def test_verify_with_icontract_hypothesis(self) -> None:
        test_with_inferred_strategy(difference_of_sums_before_and_after_max)
    

if __name__ == "__main__":
    unittest.main()
