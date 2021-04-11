# Given the start and the end of a bus ride in hours, minutes and
# seconds, calculate the duration of the ride in hours, minutes and
# seconds. The bus ride lasts strictly less than 24 hours, but it can
# start in one and finish in the next day (it can include the midnight).

from icontract import ensure, require
from typing import Tuple

def valid_time(h, m, s):
    return 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60

@require(lambda h, m, s: valid_time(h, m, s))
@ensure(lambda result: 0 <= result < 24 * 60 * 60)
def to_sec(h, m, s):
    return h * 60 * 60 + m * 60 + s

@require(lambda S: 0 <= S < 24 * 60 * 60)
@ensure(lambda result: valid_time(result[0], result[1], result[2]))
@ensure(lambda S, result: to_sec(result[0], result[1], result[2]) == S)
def from_sec(S):
    s = S % 60
    m = (S // 60) % 60
    h = S // (60 * 60)
    return h, m, s

@require(lambda h_begin, m_begin, s_begin: valid_time(h_begin, m_begin, s_begin))
@require(lambda h_end, m_end, s_end: valid_time(h_end, m_end, s_end))
@ensure(lambda result: result != None)
@ensure(lambda result: (lambda h, m, s: valid_time(h, m, s))(*result))
@ensure(lambda h_begin, m_begin, s_begin,
               h_end, m_end, s_end, result:
        (to_sec(h_begin, m_begin, s_begin) + to_sec(result[0], result[1], result[2])) % (24 * 60 * 60) == to_sec(h_end, m_end, s_end))
def bus_ride(h_begin:int, m_begin:int, s_begin:int,
             h_end:int, m_end:int, s_end:int) -> Tuple[int, int, int]:
    S_begin = to_sec(h_begin, m_begin, s_begin)
    S_end = to_sec(h_end, m_end, s_end)
    if S_end < S_begin:
        S_end += 24 * 60 * 60
    return from_sec(S_end - S_begin)
