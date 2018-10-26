def print_arr(a, label=""):
    print(label, "**************************")
    for i in range(len(a)):
        print("Elemento ", i+1,":", a[i])
    print("***************************************")

def exercise_01():
    multiples = []
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)

    print_arr(multiples, "Ejercicio 01")

def exercise_02():
    def is_prime(x):
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    x = 0
    primes_counter = 0
    prime_limit = 10001
    prime_numbers = []

    while primes_counter < prime_limit:
        x += 1
        if is_prime(x) and x > 1:
            prime_numbers.append(x)
            primes_counter += 1

    print_arr(prime_numbers, "Ejercicio 02")

exercise_01()
exercise_02()

