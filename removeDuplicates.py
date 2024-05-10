my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#
og_length = len(my_list)
for i in range(og_length):
    if my_list[i] in my_list[i+1:og_length]:
        continue
    my_list.append(my_list[i])
    
del my_list[0:og_length]
        
        
print("The list with unique elements only:")
print(my_list)


#There was a clause to maintain the original list hence the inefficiency of multiple slices
