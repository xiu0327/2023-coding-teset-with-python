from operator import xor


def xor_(arr):
    try:
        tmp = xor(arr[0], arr[1])
        for i in range(2, len(arr)):
            tmp = xor(tmp, arr[i])
        return tmp
    except IndexError:
        return arr[0]


def solution(data, col, row_begin, row_end):
    items = sorted(data, key=lambda x: [x[col-1], -x[0]])
    result = []
    for i in range(row_begin-1, row_end):
        result.append(sum([value % (i+1) for value in items[i]]))
    return xor_(result)

print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3))