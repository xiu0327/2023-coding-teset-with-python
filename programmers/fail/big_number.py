def replace(num):
    return str(num) * 3


def solution(numbers):
    replace_ = sorted([[replace(number), number] for number in numbers], reverse=True, key=lambda x: x[0])
    answer = "".join([str(item[1]) for item in replace_])
    if int(answer) == 0: return "0"
    return answer


print(solution([3, 30, 34, 5, 9]))

print(sorted([[1, 1, 2, 4], [1, 1, 2]]))
