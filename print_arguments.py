
#============================================================
# THE PYTHON print() FUNCTION
# ============================================================
#
# The print() function displays objects in a text stream,
# usually the console.
#
# Function signature:
#
# print(*objects, sep=" ", end="\n", file=None, flush=False)

# ============================================================
# 1. *objects
# ============================================================
#
# Accepts zero or more positional arguments representing
# the objects to be printed.
#
# Each object is converted into a string representation
# for output.
#
# Example:

print("Hello", 123, True)

# Output:
# Hello 123 True
#
# Multiple objects are separated by a space by default.
#
# Calling print() without objects prints an empty line.

print()

# ============================================================
# 2. sep
# ============================================================
#
# Stands for "separator".
#
# Defines the string inserted BETWEEN multiple objects.
#
# Default value: " " (a single space).
#
# Example:

print("Hello", "World", sep="-")

# Output:
# Hello-World
#
# Another example:

print(10, 20, 30, sep=" | ")

# Output:
# 10 | 20 | 30
#
# Using an empty string removes the separator.

print("A", "B", "C", sep="")

# Output:
# ABC
#
# Note:
# sep only affects the text BETWEEN objects.
# It does not affect the end of the output.

# ============================================================
# 3. end
# ============================================================
#
# Defines the string appended AFTER all objects have
# been printed.
#
# Default value: "\n" (a newline character).
#
# Example:

print("Hello", end=" ")
print("World")

# Output:
# Hello World
#
# The first print() ends with a space instead of a newline.
# Therefore, the second print() continues on the same line.
#
# Another example:

print("Loading", end="...")
print("Done!")

# Output:
# Loading...Done!
#
# An empty string prevents print() from adding a newline.

print("A", end="")
print("B", end="")
print("C")

# Output:
# ABC
#
# Useful escape sequences:
#
# "\n" -> Newline
# "\t" -> Tab
# "\\" -> Backslash 
#
# Note:
# end must be a string.

# ============================================================
# 4. file
# ============================================================
#
# Specifies the destination stream where the output is written.
#
# Default value: None.
#
# When file=None, print() writes to sys.stdout,
# which is usually the console.
#
# Example: Write output to a file.

with open("output.txt", "w", encoding="utf-8") as file:
    print("Hello, World!", file=file)

# The file "output.txt" now contains:
#
# Hello, World!
#
# Another example:

with open("output.txt", "w", encoding="utf-8") as file:
    print("A", "B", "C", sep="-", end="!", file=file)

# The file now contains:
#
# A-B-C!
#
# Note:
# file must be a writable text stream.
# Passing a filename string directly does not work:
#
# print("Hello", file="output.txt")  # TypeError

# ============================================================
# 5. flush
# ============================================================
#
# Specifies whether the output stream's buffer should
# be flushed immediately.
#
# Default value: False.
#
# A buffer temporarily holds output before it is sent
# to the underlying stream.
#
# With flush=True, Python requests that buffered output
# be sent to the underlying stream immediately.
#
# Example:

print("Processing...", end="", flush=True)

# Useful for progress indicators, terminal animations,
# and situations where output needs to appear promptly.
#
# Another example:

import time

for i in range(5):
    print(".", end="", flush=True)
    time.sleep(1)

print(" Done!")

# The dots are displayed progressively.
#
# Note:
# Flushing a stream does not necessarily mean that data
# has been physically written to disk.

# ============================================================
# COMBINING ALL PARAMETERS
# ============================================================
#
# All five parts can be used in the same function call.

with open("output.txt", "w", encoding="utf-8") as file:
    print(
        "Hello",
        "Python",
        sep=" ",
        end="!",
        file=file,
        flush=True,
    )

# The file contains:
#
# Hello Python!
#
# Explanation:
#
# *objects -> The objects to print: "Hello" and "Python".
# sep      -> Inserts a space between the objects.
# end      -> Appends "!" instead of a newline.
# file     -> Sends the output to the file.
# flush    -> Requests that the output buffer be flushed.

# ============================================================
# IMPORTANT NOTES
# ============================================================
#
# 1. sep, end, file, and flush are keyword-only parameters.
#    They must be specified by name when provided.
#
# 2. sep and end must be strings when explicitly provided.
#
# 3. print() returns None when it completes normally.
#
# 4. print() does not return the text it prints.
#
# Example:

result = print("Hello")

print(result)

# Output:
# Hello
# None
#
# ============================================================
# QUICK REFERENCE
# ============================================================
#
# print(*objects, sep=" ", end="\n", file=None, flush=False)
#
# *objects -> What to print.
# sep      -> What goes BETWEEN the objects.
# end      -> What goes AFTER all the objects.
# file     -> WHERE the output is written.
# flush    -> Whether to flush the output buffer immediately.
# ============================================================
