STOP = ""
WAITING_FOR_INPUT = True
PASSIVE_PRODUCT = 1
PASSIVE_SUM = 0


def lst_sum(lst):
    """The function returns the sum of a list of numbers"""
    the_sum = 0
    for i in range(len(lst)):
        the_sum += lst[i]
    return the_sum


def input_list():
    """The Function recieves numbers from users input,
    and returns them in a list from the first to the last one with there sum"""
    lst = []

    while WAITING_FOR_INPUT:
        user_input = input()
        if user_input == STOP:
            break;
        else:
            lst.append(float(user_input))
    return lst + [lst_sum(lst)]


def iter_product(iterable):
    """
    Returns the product of an Iterable
    :param iterable: Any iterable dataset (set, tuple,
    list, etc..) of floats\int
    :return: The inner product of the iterable unit
    """
    output = PASSIVE_PRODUCT
    for num in iterable:
        output *= num
    return output


def inner_product(vec_1, vec_2):
    """
    :param vec_1: a list of numbers(vector)
    :param vec_2: a list of numbers(vector)
    :return: A number(Float) represnting The inner product
    """
    # Validate if the abs of the vectors are equal
    if len(vec_1) != len(vec_2):
        return None
    # Validate if that the lists are not empty
    if len(vec_2) == 0 or len(vec_1) == 0:
        return 0
    # Action
    output = []
    for iterable in zip(vec_1, vec_2):
        output.append(iter_product(iterable))
    return lst_sum(output)


def monotonicity_up(sequence):
    """
    :param sequence: an Iterable of numbers(floats or ints)
    :return: True if given sequence is Monotonicity up, False if not
    """
    cache = []
    for item in zip(sequence[:], sequence[1:]):
        if item[0] <= item[1]:
            cache.append(True)
        else:
            cache.append(False)
    return iter_product(cache)


def monotonicity_up_abs(sequence):
    """
    :param sequence: an Iterable of numbers(floats or ints)
    :return: True if given sequence is Monotonicity very up, False if not
    """
    cache = []
    for item in zip(sequence[:], sequence[1:]):
        if item[0] < item[1]:
            cache.append(True)
        else:
            cache.append(False)
    return iter_product(cache)


def monotonicity_down(sequence):
    """
    :param sequence: an Iterable of numbers(floats or ints)
    :return: True if given sequence is Monotonicity down, False if not
    """
    cache = []
    for item in zip(sequence[:], sequence[1:]):
        if item[0] >= item[1]:
            cache.append(True)
        else:
            cache.append(False)
    return iter_product(cache)


def monotonicity_down_abs(sequence):
    """
    :param sequence: an Iterable of numbers(floats or ints)
    :return: True if given sequence is Monotonicity very down, False if not
    """
    cache = []
    for item in zip(sequence[:], sequence[1:]):
        if item[0] > item[1]:
            cache.append(True)
        else:
            cache.append(False)
    return iter_product(cache)


def sequence_monotonicity(sequence):
    """
    :param sequence: List of Integers
    :return: List of Booleans
    """
    output = []  # The output to store our boolean answers
    if not isinstance(sequence, type(None)):
        if (sequence == [] or len(sequence) == 1):
            return [True, True, True, True]
        else:
            if monotonicity_up(sequence):  # Monotonicity Up Case
                output.append(True)
            else:
                output.append(False)
            if monotonicity_up_abs(sequence):  # Monotonicity Very up Case
                output.append(True)
            else:
                output.append(False)
            if monotonicity_down(sequence):  # Monotonicity Down Case
                output.append(True)
            else:
                output.append(False)
            if monotonicity_down_abs(sequence):  # Monotonicity Very Down Case
                output.append(True)
            else:
                output.append(False)
            return output  # Return answer for monotonicity




def monotonicity_inverse(def_bool):
    if def_bool == [True, True, False, False]:
        return [-4, -3, 2, 5]  # Motonocity VERY UP
    if def_bool == [True, False, False, False]:
        return [1, 2, 2, 3] # MONOTONICITY UP
    if def_bool == [False, False, True, True]:
        return [4.2, 3, 0, -2]  #MONOTONICITY DOWN
    if def_bool == [False, False, True, False]:
        return [4, 3, 3, 1]  # MOTONICITY VERY DOWN
    if def_bool == [True, True, True, True]:
        return None
    if def_bool == [True, False, True, False]:
        return [1, 1, 1, 1]
    if def_bool == [False, False, False, False]:
        return [1, 2, -5, -1]
    else:
        return None


def is_prime(d):
    """True if n is prime number, False if not"""
    i = 2
    while i < d:
        if d % i == 0:
            return False
        i += 1
    return True


def primes_for_asafi(n):
    """ Help Asafi to return the prime numbers from 1 to n"""
    num_range = range(1, 10000)
    primes = []
    for i in num_range:
        if len(primes) == n:
            break
        if is_prime(list(num_range)[i]):
            primes.append(list(num_range)[i])
    return primes


def sum_of_vectors(vec_lst):
    """Returns the sum of of vectors"""
    vector_length = len(vec_lst[0])
    sum_vector = []
    for coordinate in range(vector_length):
        sum_vector_coordinate = []
        for vector_index in range(len(vec_lst)):
            sum_vector_coordinate.append(vec_lst[vector_index][coordinate])
        sum_vector.append(lst_sum(sum_vector_coordinate))
    return sum_vector


def num_of_orthogonal(vectors):
    """
    :param vectors: A Matrix (2D List) of vectors of same length
    :return: The amount of orthogonal Vectors
    """
    count = 0
    for vector_a in range(len(vectors)):
        for vector_b in range(vector_a+1, len(vectors)):
            if inner_product(vectors[vector_a], vectors[vector_b]) == 0:
                count += 1
    return count

