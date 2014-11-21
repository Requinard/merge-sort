"""
Try to find the square root of a number through approximation

Estimated operational time: O((number * 10)*precision)
"""
def brute_sqrt(number, power=2,  precision=13):
    var = 1.0
    mod = 1.0

    # 13 is the max amount of numbers we can actually count with floats, going above 13 is useless
    if precision > 13:
        precision = 13

    # Loop throught the precision, each precision is a number behind the dot
    for i in range(0, precision):
        while True:
            guess = var**power

            if guess > number:
                var -= mod
                mod /= 10
                break

            elif guess == number:
                return number

            else:
                var += mod

    return var


def newton_sqrt(num, power=2,  initial_guess= 10.0, depth=10):
    if depth is 1:
        return initial_guess
    else:
        new_guess = initial_guess-((initial_guess**power-num)/(power*initial_guess))

        if initial_guess is new_guess:
            return initial_guess

        return newton_sqrt(num, power, new_guess, depth - 1)


print brute_sqrt(520, 3)
print brute_sqrt(13.928)

print newton_sqrt(612)
print newton_sqrt(13.928)