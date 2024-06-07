def solution(number):
    if number < 0:
        return 0

    sum_multiples = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum_multiples += i

    return sum_multiples


print(solution(10))