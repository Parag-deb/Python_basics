# All major Python string functions with examples and comments

text = "  Parag is the Boss!  "
sample = "Python3"

# 1. strip() – Removes whitespace from both ends
print("1:", text.strip())

# 2. lstrip() – Removes leading spaces
print("2:", text.lstrip())

# 3. rstrip() – Removes trailing spaces
print("3:", text.rstrip())

# 4. lower() – Converts to lowercase
print("4:", text.lower())

# 5. upper() – Converts to uppercase
print("5:", text.upper())

# 6. capitalize() – Capitalizes first character
print("6:", "parag is the boss".capitalize())

# 7. title() – Capitalizes the first letter of each word
print("7:", "parag is the boss".title())

# 8. swapcase() – Swaps case of each character
print("8:", "Parag Is The Boss".swapcase())

# 9. replace() – Replaces part of the string
print("9:", text.replace("Boss", "King"))

# 10. split() – Splits string into a list
print("10:", text.strip().split(" "))

# 11. join() – Joins a list into a string
words = ['Parag', 'is', 'the', 'Boss']
print("11:", " ".join(words))

# 12. find() – Returns the first index of a substring
print("12:", text.find("Boss"))

# 13. rfind() – Finds last occurrence
print("13:", text.rfind("s"))

# 14. index() – Like find(), but raises error if not found
print("14:", text.index("Boss"))

# 15. count() – Counts occurrences
print("15:", text.count("s"))

# 16. startswith() – Checks if string starts with a substring
print("16:", text.strip().startswith("Parag"))

# 17. endswith() – Checks if string ends with a substring
print("17:", text.strip().endswith("!"))

# 18. isalpha() – Checks if all characters are letters
print("18:", "Parag".isalpha())
print("18.1:", "Parag123".isalpha())

# 19. isdigit() – Checks if all characters are digits
print("19:", "12345".isdigit())

# 20. isalnum() – Checks if all characters are alphanumeric
print("20:", "Parag123".isalnum())

# 21. isnumeric() – Checks if all characters are numeric
print("21:", "²³".isnumeric())

# 22. isdecimal() – Checks if all characters are decimal numbers
print("22:", "123".isdecimal())

# 23. isspace() – Checks if string contains only whitespace
print("23:", "   ".isspace())

# 24. istitle() – Checks if each word starts with uppercase
print("24:", "Parag Is The Boss".istitle())

# 25. islower() – Checks if all characters are lowercase
print("25:", "parag".islower())

# 26. isupper() – Checks if all characters are uppercase
print("26:", "PARAG".isupper())

# 27. format() – Formats string with placeholders
name = "Parag"
role = "Boss"
print("27:", "My name is {} and I am the {}.".format(name, role))

# 28. f-string – Modern formatting (Python 3.6+)
print("28:", f"My name is {name} and I am the {role}.")

# 29. encode() – Encodes string to bytes
print("29:", "Parag".encode())

# 30. zfill() – Pads with zeros on the left
print("30:", "42".zfill(5))

# 31. casefold() – More aggressive lowercasing
print("31:", "Parag".casefold())

# 32. partition() – Splits into 3 parts: before, match, after
print("32:", text.partition("is"))

# 33. rpartition() – Same as partition but from right
print("33:", text.rpartition("s"))

# 34. center() – Centers string with padding
print("34:", "Parag".center(10, "-"))

# 35. ljust() – Left justifies the string
print("35:", "Parag".ljust(10, "-"))

# 36. rjust() – Right justifies the string
print("36:", "Parag".rjust(10, "-"))

# 37. slice – String slicing
s = "Parag is the Boss!"
print("37:", s[0:5])     # "Parag"
print("37.1:", s[:5])    # "Parag"
print("37.2:", s[10:])   # "the Boss!"
print("37.3:", s[-5:])   # "Boss!"
print("37.4:", s[:-6])   # "Parag is the"
print("37.5:", s[::2])   # "PrgisteBs!"
print("37.6:", s[::-1])  # "!ssoB eht si garaP"
