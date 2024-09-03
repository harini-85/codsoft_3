import string
import random
print('Welcome to Password Generator!'.center(100,' '))
alphabet = list(string.ascii_letters)
numbers= list(string.digits)
characters = ['!', '#', '@', '$', '&', '%', '^', '*', '(', ')', '+', '_', '-']

n = int(input('NUmber of alphabets you want in your password? '))
m = int(input('NUmber of digits you want in your password? '))
l = int(input('NUmber of symbols you want in your password? '))
password = ''
for i in range(n):
    char = random.choice(alphabet)
    password = password + char
for i in range(m):
    digi = random.choice(numbers)
    password = password + digi
for i in range(l):
    spl = random.choice(characters)
    password = password + spl
print(password)
