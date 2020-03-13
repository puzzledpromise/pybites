def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""
    try:
        decimal_number = int(decimal_number)
    except:
        raise ValueError(f"Excpected an integer but got '{decimal_number}'")

    if decimal_number < 0 or decimal_number >= 4000:
        raise ValueError(
                f"Expected an integer > 0 and < 4000 but got {decimal_number}"
                )
    
    parts = get_parts(decimal_number)
    result = ""

    for x in range(parts[0]):
        result += "M"

    result += format_units(parts[1],"C","D","M")
    result += format_units(parts[2],"X","L","C")
    result += format_units(parts[3],"I","V","X")

    return result

def format_units(number, below_4, equals_5, full_ten):
    if number == 0:
        return ""
    if number < 4:
        return below_4 * number
    if number == 4:
        return below_4 + equals_5
    if number < 9:
        return equals_5 + format_units(number-5,below_4,equals_5,full_ten)
    else:
        return format_units(10 - number,below_4,equals_5,full_ten) + full_ten


def get_parts(number):
    thousands = number // 1000
    number = number % 1000
    hundrets = number // 100
    number = number % 100
    tens = number // 10
    number = number % 10
    units = number
    return (thousands, hundrets, tens, units)


if __name__ == "__main__":
    number = 1
    print(romanize(number))
