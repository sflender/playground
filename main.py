from src.fizzbuzz import fizzbuzz_sequence


def main(limit: int = 100) -> None:
    for v in fizzbuzz_sequence(limit):
        print(v)


if __name__ == "__main__":
    main(100)
