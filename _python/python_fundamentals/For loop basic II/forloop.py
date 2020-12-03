# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
x = [-1, 3, 5, -5]
for i in range (len(x)):
    if x[i] > -1:
        x[i] = "big"
        print(x)

# # Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# # Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# # Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def countPositives(x):
    count = 0
    for i in range(len(x)):
        if x[i] > 0:
            count = count + 1
    x[len(x)-1] = count
    return x
print(countPositives([1,6,-4,-2,-7,-2]))


# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sumTotal(x):
    sum = 0
    for i in range (len(x)):
        sum += x[i]
    return(sum)

# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5
def avg(x):
    sum = 0
    for i in range (len(x)):
        sum += x[i]
        return sum/len(x)

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
x = [37,2,1,-9]
def length(x):
    return len(x)

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(x):
    if len(x) < 1:
            return "false" 
    mini = 0
    for i in range (0,len(x),1):
        if x[i] < mini:
            mini = x[i]
    return mini

print(minimum([37,2,1,-9]))

# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(x):
    if len(x) < 1:
            return "false"
    maxi = 0 
    for i in range (len(x)):
        if x[i] > maxi:
            maxi = x[i]
        return maxi
    
print(maximum([37,2,1,-9]))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
x = [37,2,1,-9]
def analysis(x):
    results = {
        'sumTotal': sumTotal(x),
        'average': avg(x),
        'minimum': minimum(x),
        'maximum': maximum(x),
        'length': length(x)
    }
    return results
print(analysis([37,2,1,-9]))
    
    
    
#     sumTotal = 0
#     mini = 0
#     maxi = 0
#     for i in range (len(x)):
#         sumTotal += x[i]
#         if x[i] < mini:
#             mini = x[i] 
#             print ("Minium is", mini)
#         elif x[i] > maxi:
#             maxi = x[i]
#             print ("Maximum is", maxi)
#     print ("Sum is", sumTotal)
#     print ("Average is", sumTotal/len(x))
#     print ("Length is", len(x))
# print(analysis(x))

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37] 

        
import math
def reverse_list(list):
    for i in range(math.floor(len(list)/2)):
        (list[i],list[len(list)-1-i]) = (list[len(list)-1-i], list[i])
    return list
print(reverse_list([37,2,3,1,-9]))

def reverse_lists(x):
    x.reverse()
    return x
print(reverse_lists([37, 2, 3, 1,-9]))