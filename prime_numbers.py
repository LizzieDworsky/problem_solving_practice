#a prime number is a number that is divisible by one and itself
#write a method that prints out all the prime numbers between 1 and 100

#to find prime numbers, need to divide by numbers below and find factors
#for sure need a loop that counts 1-100
#then ned to find a way to modulo == 0 for only the numbers less than that number
#after that we need to count how many times 0 was the remainder and if it is only itself and 1
#then it is a prime number (so modulo would return  only two)


def prime_numbers_one_to_hundred ():
    for number in range (1, 101, 1):
        counter = 0
        for second_number in range (1, number, 1):
            if number % second_number == 0:
                counter += 1
        if counter == 1:
            print (number)