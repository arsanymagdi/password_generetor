import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
Symbols = "@#$%-*/\?"

Use_for = lower_case + upper_case + numbers + Symbols
length_for_pass = 25

password = "".join(random.sample(Use_for , length_for_pass))

print("Your generated password is :", password)
