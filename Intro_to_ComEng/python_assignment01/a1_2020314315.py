from typing import List
# DO NOT IMPORT ANY OTHER PACKAGES
# Please delete the "pass" lines then fill your answers

def is_prime(num):
    if num == 1:
        return False
    loop = num ** 0.5 # 루프사이즈를 제곱근 크기로 축소
    i = 2
    while i <= loop:
        if num % i == 0:
            return False
        i += 1
    return True

def largest_prime_factor(n: int) -> int:
    loop = n ** 0.5 # 약수를 확인하는 부분도 제곱근으로 축소
    prime = 0;
    i = 1
    while i <= loop:
        if n % i == 0:
            number2 = n / i # 제곱근 이후의 약수 계산
            if is_prime(i):
                prime = i
            if is_prime(number2):
                prime = number2
        i += 1
    return int(prime)
    """problem # 1: return the largest prime factor of a given n

    :param n: integer (0 < n < 1e+12)
    :return: largest prime factor of n
    """




def odd_occurred_number(li: List[int]) -> int:
    di = dict()
    for num in li:
        di[num] = di.get(num, 0) + 1
    result = []
    for k,v in di.items():
        if v % 2 == 1:
            return k


    """problem # 2: return the single number
    which occurs odd times in the list

    :param li: list of integer (0 < len(li) < 1e+6)
    :return: single integer which occurs odd times
    """


if __name__ == "__main__":
    """sample inputs
    below codes do not execute in the "main.py"
    """

    """problem # 1
    sample inputs
    """
    print(largest_prime_factor(1))  # correct answer is 1
    print(largest_prime_factor(124))  # correct answer is 31

    """problem # 2
    sample inputs
    """
    print(odd_occurred_number([1]))  # correct answer is 1
    print(odd_occurred_number([2, 2, 3, 3, 2, 4, 4]))  # correct answer is 2
