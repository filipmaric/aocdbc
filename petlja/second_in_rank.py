# Given a list of points of students in a programming contest,
# determine the number of points of the second student in the list
# when the list is sorted in descending order of points

from icontract import ensure, require
from typing import List

@require(lambda elements: len(elements) >= 2)
@require(lambda elements: all(x >= 0 for x in elements))
@ensure(lambda elements, result: result == sorted(elements, reverse=True)[1])
def second_in_rank(elements: List[int]) -> int:
    first_max = -1
    second_max = -1
    for x in elements:
        if x > first_max:
            second_max = first_max
            first_max = x
        elif x > second_max:
            second_max = x
    return second_max
