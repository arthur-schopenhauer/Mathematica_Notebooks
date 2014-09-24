#!/usr/bin/env python3
#-*- coding: utf-8 -*-


"""DESCRIPTION
         This module is a list of coding exercises. The intention 
         is to emulate some functions from other languages.
"""



#==================================================================
#                     Generate a list of divisors
#==================================================================


def divisors_of(number_to_divide):
    """Find the integer divisors of <number_to_divide>
    param: number_to_divide."""
    number_to_divide = number_to_divide + 1
    possible_divisors_list = list(range(number_to_divide))
    if 0 in possible_divisors_list:
        possible_divisors_list.remove(0)
    if 1 in possible_divisors_list:
        possible_divisors_list.remove(1)
    divisors_list = [1]
    number_to_divide = number_to_divide - 1
    for each_possible_divisor in list(possible_divisors_list):
        if number_to_divide % each_possible_divisor == 0:
            divisors_list.append(each_possible_divisor)
        elif number_to_divide % each_possible_divisor != 0:
            possible_divisors_list.remove(each_possible_divisor)
    return divisors_list



#==================================================================
#           Generate a range of prime numbers
#==================================================================


def prime_range(how_many_primes_you_need):
    """Return a range of prime numbers.
    param: how_many_primes_you_need"""
    primes = []
    for each_number in range(how_many_primes_you_need):
        if len(divisors_of(each_number)) == 2:
            primes
            primes.append(each_number)
    return primes


#====================================================
#           Partition a lists into sublists of size x
#====================================================

def partition_list(working_list, size_of_partition):
    """ Return a list of lists of the size of <size_of_partition>."""
    final_list = []
    for each_elem in range(0, len(working_list) + 1, size_of_partition):
        elem = working_list[each_elem: each_elem + size_of_partition]
        final_list.append(elem)
    for each_sublist in final_list:
        if len(each_sublist) != size_of_partition:
            final_list.remove(each_sublist)
    return list(final_list)



#==================================================================
#                       Factorial function
#==================================================================


def factorial_increment(limit_of_factorial_increment):
    """Return the factorial product of the sequence
    with limit <limit_of_factorial_increment> """
    limit_of_factorial_increment = limit_of_factorial_increment + 1
    limit_of_factorial_increment = int(limit_of_factorial_increment)
    terms_of_factorial_sequence_list = \
        list(range(1, limit_of_factorial_increment, 1))
    limit_of_factorial_increment = limit_of_factorial_increment - 1
    factorial_product = 1
    if limit_of_factorial_increment == 1:
        return 1
    elif limit_of_factorial_increment == 0:
        return 1
    while len(terms_of_factorial_sequence_list) != 0:
        for each_term in terms_of_factorial_sequence_list:
            if each_term == 1:
                term, *rest = terms_of_factorial_sequence_list
                next_term, *next_rest = rest
                factorial_product = term * next_term
                terms_of_factorial_sequence_list.remove(term)
                terms_of_factorial_sequence_list.remove(next_term)
            elif each_term != 1:
                term, *rest = terms_of_factorial_sequence_list
                factorial_product = factorial_product * term
                terms_of_factorial_sequence_list.remove(term)
    return factorial_product



#==================================================================
#                      Riffle elements of two lists
#==================================================================


def interleave_lists(first_list, second_list):
    """Returns a single list with elements of first_list interlaced
    with elements of second_list."""
    first_list = first_list[:]
    second_list = second_list[:]
    len_of_first_list = int(len(first_list))
    riffled_list = []
    if len_of_first_list == 0:
        return riffled_list
    else:
        while len_of_first_list != 0:
            len_of_first_list -= 1
            for each_element in first_list[:]:
                global riffled_list
                element_of_first_list, *rest_of_first_list = first_list
                element_of_second_list, *rest_of_second_list = second_list
                riffled_list.append(element_of_first_list)
                riffled_list.append(element_of_second_list)
                first_list.remove(element_of_first_list)
                second_list.remove(element_of_second_list)
                first_list = rest_of_first_list
                second_list = rest_of_second_list
    return riffled_list



#==================================================================
#                           Prime Factorization
#==================================================================

def prime_factors(input_number):
    """
    Return a list with prime factors of argument <int_number>.
    param: input_number
    Arguments:
                Integer type input. -> List
    """
    prime_factors_list = []
    first_prime = 2
    while first_prime**2 <= input_number:
        while (input_number % first_prime) == 0:
            prime_factors_list.append(first_prime)
            input_number //= first_prime
        first_prime += 1
    if input_number > 1:
        prime_factors_list.append(input_number)
    return prime_factors_list

#==================================================================
#                           Fibonacci Series
#==================================================================


def fibonacci_range(size_of_fibonacci_range):
    """Fibonacci series:
        Returns a list with a sequnce of numbers
        in which the next is the sum of the las two.
        Arguments:
            limit of the series.
     """
    fibonacci_number_list = [1]
    term, next_term = 0, 1
    while True:
        term, next_term = next_term, term + next_term
        fibonacci_number_list.append(next_term)
        if len(fibonacci_number_list) == int(size_of_fibonacci_range):
                break
    return fibonacci_number_list



#==================================================================
#                            Module runs as script
#==================================================================


if __name__ == '__main__':
    fibonacci_range()
    prime_factors()
    factorial_increment()
