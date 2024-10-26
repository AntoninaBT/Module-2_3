# Teplova //
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5] #list
# iterate over a list by referring to the index. Take the element
index = 0
element = my_list[index]
# If the index > 0, output it while the negative number appears.
# Take each element from the list and compare with 0. The list is restricted by the length of the list
while index < len(my_list): # restricted by the length of the list
    element = my_list[index] # the meaning of the element (the first is 42, the second is 69) referring to each element of the list
    index = index + 1 # ????
    if element < 0: # If the index < 0, stop
        break
    elif element == 0: # If the index = 0, continue, If the index > 0, output it and refer to the next index in the list
        continue
    print(element)
