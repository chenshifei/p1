def p(n):
    if n <= 0:
        return 1
    elif n % 2 == 0:
        return 3 * p(n / 2)
    else:
        return p(n - 1) + p(n - 3)
# When p(7) is calculated, p(6), p(3), p(2), p(1), p(0), p(-2), p(4) are also calculated

def candy(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return candy(n - 1) + candy(n - 5) + candy(n - 20)
# candy(55) = 2816604

def slices_substrs(s, result):
    slice_length = len(s) - 1
    if slice_length > 1:
        s1 = s[:slice_length]
        if s1 not in result:
            result.append(s1)
        slices_substrs(s1, result)
        s2 = s[-slice_length:]
        if s2 not in result:
            result.append(s2)
        slices_substrs(s2, result)

def slices_recursion(s):
    result = [s]
    slices_substrs(s, result)
    return result

def slices(s):
    result = []
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            result.append(s[i:j])
    return result
