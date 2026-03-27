# Task A: Truthiness

values = [0, 1, [], [1], "", "hello", None]

for v in values:
    print("value:", v, "->", bool(v))


# Task B: Identity vs Equality

# 1. Equal values but different objects
a = [1, 2, 3]
b = [1, 2, 3]
print("Case 1:")
print("a == b ->", a == b)
print("a is b ->", a is b)

# 2. Identical objects
c = [1, 2, 3]
d = c
print("\nCase 2:")
print("c == d ->", c == d)
print("c is d ->", c is d)

# 3. Immutable values
x = 5
y = 5
print("\nCase 3:")
print("x == y ->", x == y)
print("x is y ->", x is y)


# Task C: Control Flow

def describe_number(x):
    if x < 0:
        return "negative"
    elif x == 0:
        return "zero"
    elif x < 10:
        return "small positive"
    else:
        return "large positive"
print(describe_number(-5))
print(describe_number(0))
print(describe_number(3))
print(describe_number(15))


# Task D: Pattern Matching

def handle_event(event):
    match event:
        case ("click", x, y):
            print("click at", x, y)
        case ("keypress", key):
            print("key pressed:", key)
        case ("quit",):
            print("quit event")
        case _:
            print("unknown event")
    
handle_event(("click", 10, 20))
handle_event(("keypress", "A"))
handle_event(("quit",))


# Task E: Comprehensions

# 1. a list of squares from 1 to 20
squares = [x * x for x in range(1, 21)]
print("Squares:", squares)

# 2. a list of even squares
even_squares = [x * x for x in range(1, 21) if x % 2 == 0]
print("Even squares:", even_squares)

# 3. a dictionary {x: x²} for numbers 1..10
squares_dict = {x: x * x for x in range(1, 11)}
print("Squares dictionary:", squares_dict)


# Task F: Generators

# Task F — Generators

def even_numbers(limit):
    for x in range(limit + 1):
        if x % 2 == 0:
            yield x

# test generator
for num in even_numbers(10):
    print(num)

# sum of squares of even numbers < 1,000,000
sum_even_squares = sum(x * x for x in range(1000000) if x % 2 == 0)
print("Sum of even squares:", sum_even_squares)
