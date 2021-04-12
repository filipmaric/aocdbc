# manually implement the algorithm that finds the maximum of three
# given integers

from icontract import ensure, require

# canonical solution
@ensure(lambda result, x, y, z: result == max(x, y, z))
def max3_ver0(x:int, y:int, z:int) -> int:
    print(x, y, z)
    m = x
    if y > m:
        m = y
    if z > m:
        m = z
    return m

# correct, but too complicated student solution
@ensure(lambda result, a, b, c: result == max(a, b, c))
def max3_ver1(a:int, b:int, c:int) -> int:
    print(a, b, c)
    max = a
    if b > max and b > c:
        max = b
    elif c > max:
        max = c
    return max

# correct, but too complicated student solution
@ensure(lambda result, i, j, k: result == max(i, j, k))
def max3_ver2(i:int, j:int, k:int) -> int:
    print(i, j, k)
    if i > j and i > k:
        max = i
    elif j > k:
        max = j
    else:
        max = k
    return max

# erroneous student solution
@ensure(lambda result, o, p, q: result == max(o, p, q))
def max3_error1(o:int, p:int, q:int) -> int:
    if o > p and o > q:
        return o
    elif p > o and p > q:
        return p
    else:
        return q