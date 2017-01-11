"""
    A program to generate the first n Fibonacci numbers and print
    * 'Buzz' when F(n) is divisible by 3
    * 'Fizz' when F(n) is divisible by 5
    * 'FizzBuzz' when F(n) is divisible by 15
    * 'BuzzFizz' when F(n) is prime
    * F(n) otherwise
    assumption: only one string is printed per 'n' and 15 has priority over divisibility by 3 or 5.
"""
import math


def comp_fib_slow(n: int) -> int:
    """ compute the n'th Fibonacci number using recursion
    :param n: specifies the Fibonacci number to compute, zero based.
    :return: F(n) - the value of the n'th Fibonacci number
    """
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    if n == 0:
        f_n = 0  # by definition F(0) = 0
    elif n == 1:
        f_n = 1  # by definition F(1) = 1
    else:
        f_n = comp_fib_slow(n-1) + comp_fib_slow(n-2)  # recursive definition of all other values on F(n)
    return f_n


def comp_fib(n: int) -> int:
    """ compute the n'th Fibonacci number using a fast algorithm.
    :param n: specifies the Fibonacci number to compute, zero based.
    :return: F(n) - the value of the n'th Fibonacci number
    """
    def _fib(nx: int) -> (int, int):
        if nx == 0:
            return 0, 1
        else:
            a, b = _fib(nx // 2)
            c = a * (b * 2 - a)
            d = a * a + b * b
            if nx % 2 == 0:
                return c, d
            else:
                return d, c + d
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return _fib(n)[0]


def is_prime(n: int) -> bool:
    """ is n a prime? Use a sieve to check.
    :param n: the number to check for primality
    :return: True - if prime, False if not prime
    """
    if n == 0:
        return False
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def gen_fib_and_str(n: int) -> (int, str):
    """ generate the Fibonacci number F(n) and a dependent string
    :param n: specifies the number of Fibonacci numbers to compute
    :return: a tuple F(n), a dependent string
    """
    f_n = comp_fib(n)  # compute the n'th Fibonacci number

    if f_n % 15 == 0:
            out_str = 'FizzBuzz'  # divisible by 15
    elif f_n % 3 == 0:
            out_str = 'Buzz'  # divisible by 3
    elif f_n % 5 == 0:
            out_str = 'Fizz'  # divisible by 5
    elif is_prime(f_n):
        out_str = 'BuzzFizz'  # is prime
    else:
        out_str = str(f_n)  # otherwise just return the value as a string
    
    return f_n, out_str


def test_case(fib_n: int, result_fib: int, result_str: str):
    """ test to see if gen_fib_and_str(fib_n) == (results_fib, result_str)
    :param fib_n: argument to Fibonacci function
    :param result_fib: F(n)
    :param result_str:  string result
    :return: True -> good test case, False -> bad test case
    """
    fib, fib_str = gen_fib_and_str(fib_n)
    if fib == result_fib and fib_str == result_str:
        print('good:', 'F(', fib_n, ')=', fib, '->', fib_str)
        return True
    else:
        print('bad: ', 'F(', fib_n, ')=', fib, '->', fib_str)
        return False


def print_prime(n: int):
    """ Print all the prime number in the range 0 to n
    :param n: range specifier
    :return: nothing
    """
    for i in range(0, n+1):
        if is_prime(i):
            print(str(i)+',',  end='')
    print('...')


def test_fast_and_slow_fibonacci(n: int):
    """ test two methods of computing Fibonacci numbers against each other
    :param n: range to test over
    :return: Test result True/False
    """
    no_fib_errors = True
    for i in range(0, n+1):
        if comp_fib(i) != comp_fib_slow(i):
            print('error in comparison between fast and slow Fibonacci computation on ', i)
            no_fib_errors = False
    if no_fib_errors:
        print('no errors between fast and slow Fibonacci computation.')
    return no_fib_errors


def gen_fib_and_print_first_n(n: int, verbose=False):
    """ generate the first n Fibonacci numbers and print some output
    :param n: specifies the number of numbers to compute
    :param verbose: True -> print for debug, False -> print for problem solution
    :return: nothing returned, just print output
    """
    for fib_count in range(0, n):
        f_n, out_str = gen_fib_and_str(fib_count)
        if verbose:
            print('F(', fib_count, ') =', f_n, '->', out_str, flush=True)
        else:
            print(out_str+',', end='', flush=True)


# -----------------------
# tests
# -----------------------

# test Fibonacci functions, not argument should be less than about 31 allow slow function
# to finish in a reasonable time.
test_fast_and_slow_fibonacci(30)

# test prime check function 'is_prime' by printing prime numbers
print_prime(30)

# individual tests
test_case(0, 0, 'FizzBuzz')  # zero is divisible by anything (but first check is for 15)
test_case(1, 1, '1')  # not divisible by (3,5,15) or prime
test_case(2, 1, '1')  # not divisible by (3,5,15) or prime
test_case(3, 2, 'BuzzFizz')  # 2 is prime
test_case(4, 3, 'Buzz')  # divisible by 3
test_case(5, 5, 'Fizz')  # divisible by 5
test_case(6, 8, '8')  # not divisible by (3,5,15) or prime
test_case(7, 13, 'BuzzFizz')  # 13 is prime
test_case(8, 21, 'Buzz')  # 21 is divisible by 3
test_case(9, 34, '34')  # not divisible by (3,5,15) or prime
test_case(10, 55, 'Fizz')  # 55 is divisible by 5

# test main function
gen_fib_and_print_first_n(80, True)

# test main function as specified
gen_fib_and_print_first_n(80)
