# 4) Write a Python Program to remove the duplicate elements of a
# given array of numbers such that each element appears only once
# and return the new length of the given array. 

def remove_duplicates(nums):
    unique_nums = list(set(nums))
    return len(unique_nums), unique_nums


nums = [1,2,3,10,20,30,1,2,30,20,10,3,4,40]
new_length, unique_nums = remove_duplicates(nums)
print(new_length)
print(unique_nums)