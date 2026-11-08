# Python SWE Evaluation Toolkit

A practical Python project demonstrating software engineering task creation, debugging, code refactoring, feature development, performance optimization, automated testing, and deterministic verification.

## Project Purpose

This repository demonstrates how to create and evaluate software engineering challenges for AI coding systems.

It includes:
- Intentionally buggy starter implementations.
- Code refactoring challenges.
- Feature development exercises.
- Performance optimization tasks.
- Candidate implementations.
- Golden reference solutions.
- Automated tests using Pytest.

## Technologies

- Python 3.11
- Pytest 9.2
- Git and GitHub

## Project Structure

```text
Python-SWE-Evaluation-Toolkit/
│
├── tasks/
│   ├── bug-fixing/
│   ├── code-refactoring/
│   ├── feature-development/
│   └── performance-optimization/
│
├── candidate/
├── solutions/
├── tests/
├── verifier/
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Software Engineering Challenges

### 1. Bug Fixing – Discount Calculator
- Fix incorrect percentage calculations.
- Handle decimal prices.
- Validate input values.
- Test boundary conditions.

### 2. Code Refactoring – User Validation
- Remove duplicated code.
- Improve readability and maintainability.
- Reuse validation logic.
- Preserve expected behaviour.

### 3. Feature Development – Task Manager
- Add new tasks.
- Mark tasks as completed.
- List existing tasks.
- Handle invalid and missing tasks.

### 4. Performance Optimization – Duplicate Detection
- Identify duplicate values.
- Replace inefficient nested loops with set-based lookups.
- Improve average time complexity from O(n²) to O(n).
- Handle large input lists.

## Installation

Clone the repository and install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Testing

Run individual challenge tests:

```bash
python -m pytest tests/test_golden_discount_calculator.py -v
python -m pytest tests/test_user_validation.py -v
python -m pytest tests/test_task_manager.py -v
python -m pytest tests/test_duplicate_detection.py -v
```

Run the selected test suite:

```bash
python -m pytest tests/test_user_validation.py tests/test_task_manager.py tests/test_duplicate_detection.py tests/test_golden_discount_calculator.py -v
```

Run candidate verification:

```bash
python -m pytest verifier/test_candidate.py -v
```

## Current Test Results

The selected test suite currently contains 37 passing tests.

## Project Goals

- Develop realistic software engineering challenges.
- Practice debugging and problem-solving.
- Improve Python programming skills.
- Build reliable automated tests.
- Evaluate candidate code against expected behaviour.
- Understand code quality and performance.

## Author

Phani Kumar



