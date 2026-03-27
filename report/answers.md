## Why does Python treat empty containers as `False`?

Python treats empty containers as `False` because they are empty.
If something is inside, then it is `True`. If nothing is inside, then it is `False`.

## When should `is` be used instead of `==`?

The operator `==` is used to compare values.  
The operator `is` is used to check if two variables refer to the same object in memory.  
We usually use `is` when we compare with `None`.  
For example: `if x is None`.

## Why is `match` convenient for analysing structured data?

`match` is convenient because it makes the code shorter and easier to read.
Using `match`, we can check the type of event and get the values at the same time.
For example, if we have `("click", x, y)`, `match` automatically puts the values into `x` and `y`.
With `if`, we would have to write `event[0]`, `event[1]`, `event[2]`, and the code would be longer.
So `match` helps to work with structured data like tuples or lists in a more convenient way.

## What is the difference between a list comprehension and a generator expression?

The difference is that list comprehension creates the whole list at once,
and generator expression creates values one by one.
Because of this, generator does not use so much memory like a list.
So list comprehension is faster if we need the whole list,
but generator is better if we have a lot of data.

## Why are generators considered lazy?

Generators are called lazy because they do not calculate everything immediately.
They only produce values when we ask for them.
So they work step by step, not all at once.

## What happens when a generator finishes execution?

When a generator finishes, it just stops.
It cannot produce more values anymore.
If we try to use it again, nothing will happen because it is already finished.
