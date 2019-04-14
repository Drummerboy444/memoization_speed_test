def list_memoization_factorial(numbers):
    results = []
    memos = {}

    def memoization_factorial(n):
        if n in memos:
            return memos[n]

        if n is 0:
            return 1 

        ans = n * memoization_factorial(n - 1)
        memos[n] = ans
        return ans

    for n in numbers:
        results.append(memoization_factorial(n))

    return results
