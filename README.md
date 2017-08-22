# Mastermind Simplified

## Description

This code can only be interacted via tests found in `test_mmind.py`, where the most simple cases for a guess (a turn on which the codecraker tries to guess the pattern from the codemaker) are tested. The pattern is composed of a set of four different coloured pegs. No duplicated pegs are allowed.

# Prerequisites

### Python

* Python3 (developed and tested in 3.6.2)
* Pipenv: http://docs.pipenv.org/en/latest/

## Installation

Assuming you have Pipenv installed and you are in the project root folder:

```
pipenv shell --three  # activate virtualenv in new shell
pipenv install --dev  # install packages
```

## Run tests

```
python test_mmind.py
```
