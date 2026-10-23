# ============================================================
# PYTHON STRING FORMATTING
# ============================================================
#
# String formatting allows us to insert values into strings
# and control how those values are displayed.
#
# Common approaches include:
#
# 1. F-strings
# 2. str.format()
# 3. %-formatting
# 4. String concatenation
# 5. Multiple arguments in print()
#
# ============================================================
# 1. F-STRINGS
# ============================================================
#
# An f-string is a formatted string literal.
# It starts with the letter f or F before the opening quote.
#
# Expressions inside curly braces {} are evaluated
# and their results are inserted into the string.
#
# Example:

name = "Warriv"
age = 25

print(f"My name is {name} and I am {age} years old.")

# Output:
# My name is Warriv and I am 25 years old.

# F-strings can contain variables, expressions, and function calls.

a = 10
b = 5

print(f"Sum: {a + b}")
print(f"Product: {a * b}")
print(f"Uppercase name: {name.upper()}")
print(f"Name length: {len(name)}")

# Output:
# Sum: 15
# Product: 50
# Uppercase name: Warriv
# Name length: 5

# ============================================================
# 2. STRING CONCATENATION
# ============================================================
#
# Concatenation joins strings using the + operator.
#
# Non-string values must generally be converted to strings
# before concatenation.

name = "Warriv"
age = 25

print("Hello, " + name + "!")
print("Age: " + str(age))

# Output:
# Hello, Warriv!
# Age: 25

# The following expression raises a TypeError because
# a string and an integer cannot be concatenated directly.
#
# print("Age: " + age)

# ============================================================
# 3. MULTIPLE ARGUMENTS IN print()
# ============================================================
#
# print() accepts multiple objects as positional arguments.
# By default, the objects are separated by a single space.
#
# Example:

name = "Warriv"
age = 25

print("Name:", name, "Age:", age)

# Output:
# Name: Warriv Age: 25

# The sep parameter controls the separator between objects.

print("Name:", name, sep="")
print("A", "B", "C", sep="-")

# Output:
# Name:Warriv
# A-B-C

# ============================================================
# 4. str.format()
# ============================================================
#
# The format() method inserts values into replacement fields
# represented by curly braces {}.
#
# Example:

name = "Warriv"
age = 25

print("My name is {} and I am {} years old.".format(name, age))

# Output:
# My name is Warriv and I am 25 years old.

# Replacement fields can use positional indexes.

print("{1} is {0} years old.".format(age, name))

# Output:
# Warriv is 25 years old.

# Named fields can also be used.

print("Name: {n}, Age: {a}".format(n=name, a=age))

# Output:
# Name: Warriv, Age: 25

# ============================================================
# 5. PERCENT-FORMATTING
# ============================================================
#
# Percent-formatting is an older string formatting technique.
#
# Common format specifiers:
#
# %s -> String representation
# %d -> Decimal integer
# %f -> Floating-point number
#
# Example:

name = "Warriv"
age = 25
price = 19.99

print("Name: %s" % name)
print("Age: %d" % age)
print("Price: %f" % price)

# Output:
# Name: Warriv
# Age: 25
# Price: 19.990000

# Multiple values can be supplied in a tuple.

print("%s is %d years old." % (name, age))

# Output:
# Warriv is 25 years old.

# ============================================================
# 6. FLOATING-POINT PRECISION
# ============================================================
#
# F-strings can control the number of decimal places.
#
# The format specification :.2f means:
#
# :  -> Start the format specification.
# .2 -> Display two digits after the decimal point.
# f  -> Use fixed-point floating-point notation.

price = 19.9876

print(f"Price: {price:.2f}")

# Output:
# Price: 19.99

# Another example:

pi = 3.141592653589793

print(f"Pi: {pi:.3f}")

# Output:
# Pi: 3.142

# ============================================================
# 7. PERCENTAGE FORMATTING
# ============================================================
#
# The % format type multiplies a numeric value by 100
# and appends a percent sign.

success_rate = 0.875

print(f"Success rate: {success_rate:.1%}")

# Output:
# Success rate: 87.5%

# ============================================================
# 8. THOUSANDS SEPARATORS
# ============================================================
#
# A comma in the format specification adds thousands separators.

population = 1234567

print(f"Population: {population:,}")

# Output:
# Population: 1,234,567

# An underscore can also be used as the separator.

print(f"Population: {population:_}")

# Output:
# Population: 1_234_567

# ============================================================
# 9. STRING ALIGNMENT AND FIELD WIDTH
# ============================================================
#
# A format specification can control alignment and field width.
#
# <  -> Left alignment
# >  -> Right alignment
# ^  -> Center alignment
#
# The number specifies the minimum field width.

name = "Warriv"

print(f"|{name:<10}|")
print(f"|{name:>10}|")
print(f"|{name:^10}|")

# Output:
# |Warriv     |
# |     Warriv|
# |  Warriv   |

# A custom fill character can be specified.

print(f"{name:*^10}")

# Output:
# **Warriv***

# ============================================================
# 10. DEBUGGING WITH SELF-DOCUMENTING EXPRESSIONS
# ============================================================
#
# The = sign inside an f-string field displays the expression
# together with its value.
#
# This feature is useful for debugging.

value = 42

print(f"{value=}")

# Output:
# value=42

a = 10
b = 5

print(f"{a + b = }")

# Output:
# a + b = 15

# ============================================================
# 11. LITERAL CURLY BRACES
# ============================================================
#
# Double curly braces produce literal curly braces
# instead of starting a replacement field.
#
# {{ -> {
# }} -> }

name = "Warriv"

print(f"{{name}}")
print(f"{{{name}}}")

# Output:
# {name}
# {Warriv}

# ============================================================
# 12. F-STRING CONVERSION FLAGS
# ============================================================
#
# Conversion flags control how an expression is converted
# before formatting.
#
# !s -> Calls str()
# !r -> Calls repr()
# !a -> Calls ascii()
#
# Example:

text = "hello\nworld"

print(f"{text!s}")
print(f"{text!r}")
print(f"{text!a}")

# Output:
# hello
# world
# 'hello\nworld'
# 'hello\nworld'
#
# repr() is particularly useful for debugging because it
# can make special characters visible in the output.
#
# ascii() escapes non-ASCII characters in its representation.

# ============================================================
# 13. RAW F-STRINGS
# ============================================================
#
# Prefixing a string with fr or rf combines raw-string behavior
# with f-string interpolation.
#
# Most backslashes are treated literally, while expressions
# inside curly braces are still evaluated.

username = "Warriv"

print(fr"C:\Users\{username}")

# Output:
# C:\Users\Warriv

# ============================================================
# 14. CREATING A FORMATTED STRING WITHOUT print()
# ============================================================
#
# An f-string creates a string value.
# It does not automatically display that value.
#
# The resulting string can be assigned to a variable,
# returned from a function, saved to a file, or printed later.

name = "Warriv"

message = f"Hello, {name}!"

print(message)

# Output:
# Hello, Warriv!

# ============================================================
# QUICK REFERENCE
# ============================================================
#
# f"Hello, {name}"       -> F-string formatting
# "Hello, " + name       -> String concatenation
# print("Hello", name)   -> Multiple print() arguments
# "Hello, {}".format(name) -> str.format()
# "Hello, %s" % name     -> Percent-formatting
#
# Recommended for most new Python code:
# Use f-strings when inserting variables or expressions
# into strings.
# ============================================================
