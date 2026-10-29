# Password Strength Checker

## Overview
A Python-based cybersecurity project that evaluates password strength locally and provides suggestions for improvement.

## Features
- Password length and character variety checks.
- Common password detection.
- Basic repeated-character and predictable-sequence checks.
- Educational password entropy estimation.
- Suggestions for improving password strength.
- Automated unit tests.

## Technologies Used
- Python 3
- Regular expressions
- Python unittest framework
- Git and GitHub

## Installation
1. Install Python 3.
2. Clone or download this repository.
3. Open the project folder in VS Code.

## Usage
Run:

```bash
python password_checker.py
```

Enter a fictional test password when prompted.

## Run Tests
Execute:

```bash
python -m unittest -v
```

## Privacy and Security
The application evaluates the password locally. It does not intentionally store, log, or transmit the entered password.

The entropy calculation is an educational estimate and should not be interpreted as a guarantee of password security.

## Limitations
- The common password list contains only sample entries.
- Pattern detection covers selected predictable sequences.
- The strength rating is a simplified educational heuristic.

## Future Improvements
- Add a larger, responsibly sourced common-password dictionary.
- Improve detection of keyboard patterns and predictable substitutions.
- Add more comprehensive automated tests.