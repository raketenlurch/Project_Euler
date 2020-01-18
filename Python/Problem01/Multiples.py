def multiples(number):
    sum = 0

    for i in range(0, number):
        if i%3 == 0 or i%5 == 0:
            sum += i

    print(sum)

multiples(10)
multiples(1000)
