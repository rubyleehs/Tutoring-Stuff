# Python Cheat Sheet
I will try to update stuff as we learn things

## Math Operators

From **Highest** to **Lowest** precedence:

| Operators | Operation         | Example         |
| --------- | ----------------- | --------------- |
| /         | Division          | `22 / 8 = 2.75` |
| \*        | Multiplication    | `3 * 3 = 9`     |
| -         | Subtraction       | `5 - 2 = 3`     |
| +         | Addition          | `2 + 2 = 4`     |


## Data Types

| Data Type              | Examples                                   |
| ---------------------- | ------------------------------------------ |
| Booleans               | `True, False`                              |
| Integers               | `-2, -1, 0, 1, 2, 3, 4, 5`                 |
| Floating-point numbers | `-1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25`  |
| Strings                | `'a', "aa", 'aaa', "Hello!", '11 cats'`    |
|||
| Lists                  | `[], [1,2,3], ['A','B'], ["abc", 1, True]` |


## Variables

Variables are "names" that can contain data. (Imagine a named box where you can put things in) You can assign data to a variable by using `=`. (eg. `my_variable = 10`)

You can name a variable anything as long as it obeys the following rules:

1. It can use only letters, numbers, and the underscore (`_`) character.
2. It can’t begin with a number.
3. Variable names starting with an underscore (`_`) are considered as "unuseful" by python coding conventions.


## Comments

Comments are stuff that will be ignored by the computer! Everything after a `#` will be ignored. Use them to explain your code.

Inline comment:

```python
# This is a comment
```

Multiline comment:

```Python
# This is a
# multiline comment
```

Code with a comment:

```python
a = 1  # initialization
```

## Simple Functions

```python
print('Hello!') # prints `Hello!` to console
input('Type here!') # prints `Type here!` to console and wait for user response and returns it.

str(10) # Converts input to a string (if possible). Returns "10".
int("10") # Converts input to an integer (if possible). Returns 10.

len('Meow') # Returns number of things in the input.
len([1,2,3,4]) # Both of these returns 4
range(3) # Simplified, this is equivalent to [1,2,3]
```

## Comparison Operators

| Operators | Meaning               |
| --------- | --------------------- |
| <         | Strictly less than    |
| <=        | Less than or equal    |
| >         | Strictly greater than |
| >=        | Greater than or equal |
| ==        | Equal                 |
| !=        | Not equal             |

## If, elif and else
`if`, `elif` and `else` controls the flow of the program.
- `if` executes the indented code below it if the condition after it evaluates to `True`.
- `else` executes the indented code below it if all the `if` and `elif` above it evaluates to `False`
- `elif` executes the indented code below it if all the `if` and `elif` above it evaluates to `False` AND the condition after it evaluates to `True`.

```python
if (True):
    # This will run
else:
    # This will not run

if (False):
    # This will not run
else:
    # This will run

if (False):
    # This will not run
elif (True):
    # This will run
else:
    # This will not run
```

## Loops
Loops repeats the indented code below it a certain amount of times.

`while` loops repeats until a condition evaluates to `False`
```python
count = 0
while(count < 10):
    count = count + 1
    # This part will be repeated 10 times
```

`for` loops repeats once per item in an iterable (eg. lists).
```python
for sound in ["meow", "woof", "quack"]:  # sound is a variable here!
    print(sound)
# This code will print:
# meow
# woof
# quack
```

`for` loops can also be combined with the `range()` function.
```python
for numberA in [1,2,3]:
    print(numberA)
# This code will print:
# 1
# 2
# 3

for numberB in range(3):
    print(numberB)
# This code will print:
# 1
# 2
# 3
```

`break` allows you to exit a loop immediately!
```python
count = 0
while(count < 10):
    count = count + 1
    # This part will only run 3 times!
    if (count == 3):
        break
print(count) # prints 3
```

## Importing modules
Python allows you to import modules and libraries. These are essentially code someone else have written.

```python
import random # import the random module
```

The [Python Standard Library](https://docs.python.org/3/library/) are modules provided by the Python Foundation. These modules provide standardized solutions for many problems that occur in everyday programming. These modules come together with Python when you install it so you just need to do `import module_name` to use it in your code.
For modules that are not part of the Standard Library, you will need to download them before importing.

## Classes
Its is like declaring a custom datatype that can contain functions.
Or you can imagine it like a blueprint to a factory which can contain goods (data) and machines that process various things (functions), and you can build as many factories as you want from the blueprint.


## Misc
### What are these symbols used for?
| Symbol    | Purpose               |
| --------- | --------------------- |
| ()        | BODMAS rule in math, grouping logic, at the end of functions to pass in variables, tuples. They contains things you want to pass, and always come after the thing you want to pass to.|
| []        | Declare a list, or index into a list or dictionary, always comes after the name you are trying to access.|
| {}        | Declare a dictionary. |
| :         | Generally used with indentations - the thing before will be applied to following line(s) that are indented more. |
