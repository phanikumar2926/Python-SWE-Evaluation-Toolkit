
# Python SWE Evaluation Toolkit

A practical Python project demonstrating software engineering task creation, debugging, automated testing, and deterministic verification.

## Project Purpose

This repository demonstrates how to create and evaluate software engineering challenges for AI coding systems.

It includes:
- Intentionally buggy starter implementations.
- Clearly defined task requirements.
- Automated test cases using Pytest.
- Golden reference solutions.
- Candidate implementations.
- Deterministic verification with varied test inputs.

## Technologies

- Python 3.11.4
- Pytest 9.2.0
- Git and GitHub

## Project Structure

```text
Python-SWE-Evaluation-Toolkit/
│
├── tasks/
│   └── bug-fixing/
│       ├── discount_calculator.py
│       └── task.md
│
├── candidate/
│   └── discount_calculator.py
│
├── solutions/
│   └── discount_calculator.py
│
├── tests/
│   ├── test_discount_calculator.py
│   └── test_golden_discount_calculator.py
│
├── verifier/
│   └── test_candidate.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Current Challenge: Discount Calculator

### Problem

The starter implementation calculates discounts incorrectly because it does not convert the discount percentage into a decimal value.

### Expected Behaviour

For example:

```python
calculate_discount(100, 10)
```

Expected result:

```text
90
```

### Requirements

- Calculate discounts correctly.
- Support decimal prices.
- Handle zero and full discounts.
- Reject negative prices.
- Reject discount percentages outside 0 to 100.

## Testing and Verification

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the golden solution tests:

```bash
python -m pytest tests/test_golden_discount_calculator.py -v
```

Run candidate verification:

```bash
python -m pytest verifier/test_candidate.py -v
```

The candidate verifier includes:
- Fixed test scenarios.
- Invalid input checks.
- 100 deterministic varied input combinations.
- Floating-point comparison using `pytest.approx`.

## Project Goals

- Build realistic software engineering challenges.
- Practice debugging and problem-solving.
- Develop reliable automated tests.
- Create deterministic verification systems.
- Maintain reference implementations.
- Improve code quality and test coverage.

## Future Improvements

- Feature development challenges.
- Code refactoring challenges.
- Performance optimization tasks.
- Stronger edge-case and input validation tests.
- More Python software engineering exercises.

## Author

Phani Kumar

