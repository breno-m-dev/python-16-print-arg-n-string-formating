
# ============================================================
# PYTHON ESCAPE SEQUENCES
# ============================================================
#
# Escape sequences begin with a backslash (\).
# They represent special characters or character values.
#
# ============================================================
# 1. NEWLINE: \n
# ============================================================
#
# Inserts a line break.

print("Hello\nWorld")

# Output:
# Hello
# World

# ============================================================
# 2. HORIZONTAL TAB: \t
# ============================================================
#
# Inserts a horizontal tab.

print("Name:\tBowser")

# Output:
# Name:   Bowser
# (The spacing depends on the tab stop.)

# ============================================================
# 3. BACKSLASH: \\
# ============================================================
#
# Represents a literal backslash.

print("C:\\Users\\Bowser")

# Output:
# C:\Users\Bowser

# ============================================================
# 4. SINGLE QUOTE: \'
# ============================================================
#
# Represents a single quote.
# Useful inside strings delimited by single quotes.

print('It\'s Python!')

# Output:
# It's Python!

# ============================================================
# 5. DOUBLE QUOTE: \"
# ============================================================
#
# Represents a double quote.
# Useful inside strings delimited by double quotes.

print("She said: \"Hello!\"")

# Output:
# She said: "Hello!"

# ============================================================
# 6. CARRIAGE RETURN: \r
# ============================================================
#
# Moves the output position to the beginning of the line.
# Subsequent output may overwrite existing characters.

print("Hello\rWorld")

# Typical output:
# World

# ============================================================
# 7. BACKSPACE: \b
# ============================================================
#
# Represents a backspace character.
# Its visible effect depends on the output destination.

print("ABC\bD")

# In a terminal, this may display:
# ABD
#
# Note: Backspace behavior is environment-dependent.

# ============================================================
# 8. FORM FEED: \f
# ============================================================
#
# Represents a form feed character.
# Historically used to indicate a page break.

print("Page 1\fPage 2")

# The form feed character may not be visibly rendered.

# ============================================================
# 9. VERTICAL TAB: \v
# ============================================================
#
# Represents a vertical tab character.

print("Hello\vWorld")

# The visible effect depends on the output destination.

# ============================================================
# 10. BELL: \a
# ============================================================
#
# Represents the ASCII bell character.
# Some terminals may produce a sound or visual alert.

print("\a")

# Note: Modern terminals may ignore this character.

# ============================================================
# 11. OCTAL ESCAPE: \ooo
# ============================================================
#
# Represents a character using one to three octal digits.
# Octal digits range from 0 to 7.

print("\101")

# Output:
# A
#
# Explanation:
# The octal value 101 represents the character "A".

# ============================================================
# 12. HEXADECIMAL ESCAPE: \xhh
# ============================================================
#
# Represents a character using exactly two hexadecimal digits.
# Hexadecimal digits range from 0 to 9 and A to F.

print("\x41")

# Output:
# A
#
# Explanation:
# The hexadecimal value 41 represents the character "A".

# ============================================================
# 13. UNICODE ESCAPE: \uXXXX
# ============================================================
#
# Represents a Unicode code point using four hexadecimal digits.

print("\u2764")

# Output:
# ❤

# ============================================================
# 14. UNICODE ESCAPE: \UXXXXXXXX
# ============================================================
#
# Represents a Unicode code point using eight hexadecimal digits.

print("\U0001F496")

# Output:
# 💖

# ============================================================
# 15. UNICODE CHARACTER NAME: \N{name}
# ============================================================
#
# Represents a Unicode character using its official Unicode name.

print("\N{BLACK HEART SUIT}")

# Output:
# ♥

# ============================================================
# IMPORTANT NOTES
# ============================================================
#
# 1. Escape sequences are interpreted inside ordinary strings.
#
# 2. Raw strings, prefixed with r or R, treat most backslashes
#    as literal characters instead of escape sequences.
#
# Example:

print(r"C:\Users\Bowser")

# Output:
# C:\Users\Bowser
#
# 3. An unrecognized escape sequence may produce a warning.
#    Its handling depends on the sequence and Python version.
#
# 4. Escape sequences are part of string literal syntax.
#    They are not specific to the print() function.
# ============================================================
