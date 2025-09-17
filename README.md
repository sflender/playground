# FizzBuzz Playground

Simple FizzBuzz example and tests.

## Run the FizzBuzz script
This repository includes a small runner that prints the FizzBuzz sequence from 1 to 100.

From the project root (macOS / bash):

```bash
python3 main.py
```

You can change the printed limit by editing the `main()` call or by modifying the script.

## Run the unit tests
Tests use `pytest`. From the project root:

```bash
pytest -q
```

The tests are located in `tests/test_fizzbuzz.py` and exercise both the single-value helper and the sequence generator.

## Project layout
- `main.py` - runner that prints FizzBuzz (default limit 100)
- `src/fizzbuzz.py` - fizzbuzz implementation
- `tests/test_fizzbuzz.py` - pytest unit tests
- `README.md` - this file

## Notes
If you run tests and the `src` package isn't importable, the tests add the project root to `sys.path` to ensure imports work when running `pytest` from the project directory.
