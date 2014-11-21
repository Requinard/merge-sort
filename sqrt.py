
def sqrt(number, precision=13):
    var = 1.0
    mod = 1.0

    for i in range(0, precision):
        while True:
            guess = var**2

            if guess > number:
                var -= mod
                mod /= 10
                break

            elif guess == number:
                return number

            else:
                var += mod

    return var

print sqrt(9)
print sqrt(10)