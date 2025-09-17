def fizzbuzz_value(n: int) -> str:
    """Return FizzBuzz value for a single integer."""
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def fizzbuzz_sequence(n: int):
    """Yield fizzbuzz values from 1 to n inclusive."""
    for i in range(1, n + 1):
        yield fizzbuzz_value(i)