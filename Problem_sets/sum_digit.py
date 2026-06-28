#fingd some of all digits of a number.

def sum_digit(n):
    if n == 0:
        return 0
    return n % 10 + sum_digit(n//10)

print(sum_digit(1234))
