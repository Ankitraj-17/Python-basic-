# 1.Input a string and count vowels, consonants, digits, and spaces
s = input("Enter a string: ")
v = sum(ch.lower() in "aeiou" for ch in s)
c = sum(ch.isalpha() and ch.lower() not in "aeiou" for ch in s)
d = sum(ch.isdigit() for ch in s)
sp = sum(ch.isspace() for ch in s)
print(f"Vowels: {v}")
print(f"Consonants: {c}")
print(f"Digits: {d}")
print(f"Spaces: {sp}")

# 2.Check if a given string is a palindrome.
s = input("Enter a string: ")
print("Palindrome" if s == s[::-1] else "Not palindrome")


# 3.Check if a given string is a palindrome.
s = input("Enter a string: ")
print("Palindrome" if s == s[::-1] else "Not palindrome")


# 4.Print characters at even index positions.
s = input("Enter a string: ")
print(s[::2])
s = input("Enter a string: ")
print(s[::2])


# 5.Input a sentence and print each word on a new line.
s = input("Enter a sentence: ")
print(*s.split(), sep="\n")


# 6.Count occurrences of a specific character in a string.
s = input("Enter a string: ")
ch = input("Enter a character to count: ")
print(s.count(ch))

# 7.Find the longest word in a sentence.
s = input("Enter a sentence: ")
w = s.split()
print(max(w, key=len) if w else "")

## 8.Remove duplicate characters from a string.
# s = input("Enter a string: ")
# print(''.join(dict.fromkeys(s)))
