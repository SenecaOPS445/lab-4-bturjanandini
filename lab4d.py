#!/usr/bin/env python3
# Strings 1
#bturjanandinidia
str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(string):
    # Returns the first five characters of the input string
    return string[:5]

def last_seven(string):
    # Returns the last seven characters of the input string
    return string[-7:]

def middle_number(number):
    # Returns the second and third characters of the number after converting to string
    return str(number)[1:3]

def first_three_last_three(string1, string2):
    # Combines the first three characters of string1 and the last three characters of string2
    return string1[:3] + string2[-3:]

if __name__ == '__main__':
    print(first_five(str1))                     # Output: Hello
    print(first_five(str2))                     # Output: Senec
    print(last_seven(str1))                     # Output: World!!
    print(last_seven(str2))                     # Output: College
    print(middle_number(num1))                  # Output: 50
    print(middle_number(num2))                  # Output: .5
    print(first_three_last_three(str1, str2))   # Output: Helege
    print(first_three_last_three(str2, str1))   # Output: Send!!

