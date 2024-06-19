# 3) Write a Python Program to check whether a given integer is a
# palindrome or not

def is_palindrome(num):
    if num < 0:
        return False
    original = str(num)
    reversed_num = original[::-1]
    return original == reversed_num

num = 121
print(is_palindrome(num))

num = -141
print(is_palindrome(num))

num = 100
print(is_palindrome(num))

num = 838
print(is_palindrome(num))