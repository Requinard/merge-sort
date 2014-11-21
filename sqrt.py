"""
Try to find the square root of a number through approximation

Estimated operational time: O((number * 10)*precision)
"""
def sqrt(number, power=2,  precision=13):
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

print sqrt(9)
print sqrt(10)
print sqrt(520, 3)
print sqrt(13.928)
print sqrt(13.928, 2, 20)