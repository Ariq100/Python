'''
number_string is a string with a list of numbers separated by the addition operator. 
Write an algorithm that splits the numbers to integer and adds them together. 
Store the result in another variable named total_value.
   
number_string = "3+5+18+20+35"
'''

# number_string = "3+5+18+20+35"

# number_string_list = number_string.split("+")

# total_value = 0

# for item in number_string_list:
#     total_value = total_value + int(item)

# print(total_value)


'''
Write an algorithm that takes 5 integer inputs and stores them in a list named user_inputs. 
The input can only be in the range of 3 to 27 and so perform a check on the input. 
If the user enters an integer outside the range then he/she will be again asked to give the current input.
And total the inputs
'''

# user_inputs = []

# counter = 1

# for taking user inputs
# while counter <= 5:
#     num_input = int(input(f"Number {counter}: "))

#     if (num_input >=3 and num_input <= 27):
#         user_inputs.append(num_input)
#     else:
#         counter -= 1

#     counter += 1

# for adding
# total = 0
# for item in user_inputs:
#     total += item

# print(f"Total: {total}")