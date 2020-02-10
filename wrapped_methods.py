import methods


def wrap_is_prime(list_data):
    if len(list_data) > 1:
        if list_data[1].isdigit():
            number = int(list_data[1])
            return methods.is_prime(number)
        return f"{list_data[1]} is not a digit"
    else:
        return f"You need at least one argument"


def wrap_is_palindrome(list_data):
    return methods.is_palindrome(list_data[1])


def wrap_sqrt(list_data):
    return methods.sqrt(list_data[1])


def wrap_is_fact(list_data):
    if list_data[1].isdigit():
        number = int(list_data[1])
        return methods.is_fact(number)
    return f"{list_data[1]} is not a digit"
