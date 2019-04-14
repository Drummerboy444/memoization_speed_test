from random import randint
from factorial import list_factorial
from memoazation_factorial import list_memoization_factorial

numbers_to_test = 1000
max_value_to_test = 300
times_to_run_test = 10

to_test = []
for _ in range(numbers_to_test):
    to_test.append(randint(0, max_value_to_test))

def test_list_factorial():
    list_factorial(to_test)

def test_list_memoization_factorial():
    list_memoization_factorial(to_test)

if __name__ == '__main__':
    import timeit
    normal_time = timeit.timeit("test_list_factorial()", setup="from __main__ import test_list_factorial", number=times_to_run_test)
    memoization_time = timeit.timeit("test_list_memoization_factorial()", setup="from __main__ import test_list_memoization_factorial", number=times_to_run_test)
    print("normal time: " + str(normal_time))
    print("memoization time: " + str(memoization_time))
    print("memoization is " + str(round(normal_time / memoization_time)) + " times faster")


