def valid_number(number, total):
    if number.isdigit():
        number = int(number)

        if 1 <= number <= total:
            return True

    return False