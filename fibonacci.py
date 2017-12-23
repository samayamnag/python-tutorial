from functools import lru_cache


class Fibonacci:
    fibonacci_cache = {}

    def normal(self, n):
        # Check that the input is a positive integer
        if type(n) != int:
            raise TypeError("n must be positive integer")
        if n < 1:
            raise TypeError("n must be positive integer")

        # Compute the Nth item
        if n == 1:
            return 1
        elif n == 2:
            return 1
        elif n > 2:
            return self.normal(n - 1) + self.normal(n - 2)

    def with_custom_memoization(self, n):
        # Check that the input is a positive integer
        if type(n) != int:
            raise TypeError("n must be positive integer")
        if n < 1:
            raise TypeError("n must be positive integer")

        # If we have cached the value, then return it
        if n in self.fibonacci_cache:
            return self.fibonacci_cache[n]

        # Compute the Nth item
        if n == 1:
            return 1
        elif n == 2:
            return 1
        elif n > 2:
            value = self.with_custom_memoization(n - 1) + self.with_custom_memoization(n - 2)

            # Cache the value and return it
            self.fibonacci_cache[n] = value
            return value

    @lru_cache(maxsize=1000)
    def with_built_in_cache(self, n):
        # Check that the input is a positive integer
        if type(n) != int:
            raise TypeError("n must be positive integer")
        if n < 1:
            raise TypeError("n must be positive integer")

        # Compute the nth term
        if n == 1:
            return 1
        elif n == 2:
            return 1
        elif n > 2:
            return self.with_built_in_cache(n - 1) + self.with_built_in_cache(n - 2)


obj = Fibonacci()
print('=========== Normal ===========')
for n in range(1, 10):
    print(obj.normal(n))

print('=========== Normal Cache ===========')
for n in range(1, 10):
    print(obj.with_custom_memoization(n))

print('=========== Builtin Cache ===========')
for n in range(1, 10):
    print(obj.with_built_in_cache(n))
