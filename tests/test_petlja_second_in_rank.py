import unittest
from hypothesis import given, settings, HealthCheck
import hypothesis.strategies as st
from icontract_hypothesis import test_with_inferred_strategy, infer_strategy, make_assume_preconditions
from petlja.second_in_rank import second_in_rank

from typing import List


class TestSecondInRank(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.assume_preconditions = make_assume_preconditions(second_in_rank)

    def test_1(self) -> None:
        result = second_in_rank([80, 95, 75, 50, 95])
        self.assertEqual(result, 95)

    @given(xs=st.lists(st.integers(min_value=0), min_size=2))
    def test_icontract_hypothesis_manual(self, xs: List[int]) -> None:
        print(xs)
        self.assume_preconditions(xs)
        second_in_rank(xs)

    @settings(suppress_health_check=[HealthCheck.filter_too_much])
    def test_verify_with_icontract_hypothesis(self) -> None:
        test_with_inferred_strategy(second_in_rank)
    

if __name__ == "__main__":
    print(infer_strategy(second_in_rank))
    unittest.main()
