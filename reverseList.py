# This a python code to reverse the element of a list by swapping the values 
# It is very efficient and elegant!

my_list = [10, 1, 8, 3, 5]
length = len(my_list)

print("Original List:", my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)
