# Source: https://projecteuler.net/problem=1
#  If we list all the natrual numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9.
#  The sum of these multiples es 23.
#
#  Find the sum of all the multiples of 3 or 5 below 1000.

def multiples(number):
    sum = 0

    for i in range(0, number):
        if i%3 == 0 or i%5 == 0:
            sum += i

    print(sum)

multiples(10)
multiples(1000)
