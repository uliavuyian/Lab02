# LAB02: Expressions & Control Flow in Python

This lab is about practicing Python expressions and control flow.
In this lab we worked with truthiness, identity vs equality, `if` statements, `match` statement, comprehensions and generators.

---

## Project Structure
```
lab02/
├── README.md
├── requirements.txt
├── report/
│   └── answers.md
└── src/
    └── main.py
```

---

## Requirements

- Python 3.10 or higher (because `match` statement is used)
- No external libraries are needed

---

## Environment Setup

**Create virtual environment:**
```
python -m venv .venv
```

**Activate it:**

Windows:
```
.venv\Scripts\activate
```

macOS / Linux:
```
source .venv/bin/activate
```

**Install requirements:**
```
pip install -r requirements.txt
```

---

## Running the Program
```
python src/main.py
```

---

## What the Program Does

### Task A — Truthiness
The program shows how Python understands `True` and `False` for different values like `0`, `1`, empty list, string and `None`.

### Task B — Identity vs Equality
This part shows the difference between `==` and `is`. `==` compares values, and `is` checks if it is the same object in memory.

### Task C — Control Flow
This part uses `if`, `elif` and `else` to describe a number (negative, zero, small positive, large positive).

### Task D — Pattern Matching
This part uses `match` to work with events like mouse click, key press, or quit event.

### Task E — Comprehensions
Here we create lists and a dictionary using comprehensions (for example list of squares and even squares).

### Task F — Generators
This part shows how generators work and how they save memory. It also calculates the sum of squares of even numbers using a generator expression.
