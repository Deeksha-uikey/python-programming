# 2) Write a Python Program to reverse only the vowels of a given
# string. 

def reverse_vowels(String):
    vowels = ""
    
    for character in String:
        if character in "aeiouAEIOU":
            vowels = vowels + character
    result_string = "" 
    
    for character in String:
        if character in "aeiouAEIOU":
            result_string = result_string + vowels[-1]
            vowels = vowels[:-1]
        else:
            result_string = result_string + character
    return result_string

print(reverse_vowels("python"))  
print(reverse_vowels("programming"))
print(reverse_vowels("language"))
print(reverse_vowels("Bitcoin Blockchain"))
print(reverse_vowels("Fundamentals of blockchain"))
print(reverse_vowels("aeiouAEIOU"))
print(reverse_vowels("AEIOUaeiou"))  
             
  