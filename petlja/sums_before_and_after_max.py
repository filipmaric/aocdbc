from icontract import ensure, require
from typing import List, Tuple

@require(lambda xs: len(xs) >= 1)
@ensure(lambda xs, result: 0 <= result[0] < len(xs))
@ensure(lambda xs, result: all(xs[i] < xs[result[0]] for i in range(result[0])))
@ensure(lambda xs, result: all(xs[i] <= xs[result[0]] for i in range(result[0] + 1, len(xs))))
@ensure(lambda xs, result: result[1] == sum(xs[:result[0]]))
@ensure(lambda xs, result: result[2] == sum(xs[result[0]+1:]))
def sums_before_and_after_max(xs: List[int]) -> Tuple[int, int, int]:
    # print(xs)
    max_i = 0
    sum_before = 0
    sum_after = 0
    for i in range(1, len(xs)):
        if xs[i] > xs[max_i]:
            sum_before = sum_before + xs[max_i] + sum_after
            max_i = i
            sum_after = 0
        else:
            sum_after = sum_after + xs[i]
    return (max_i, sum_before, sum_after)

@require(lambda xs: len(xs) >= 1)
def difference_of_sums_before_and_after_max(xs: List[int]) -> int:
    _, sum_before, sum_after = sums_before_and_after_max(xs)
    return sum_before - sum_after