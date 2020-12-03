# 1. Print 1-255
# Print all the integers from 1 to 255. 
def allInt(x):
    for i in range (1, 256):
        print(i) 


# 2. Print Odds 1-255
# Print all odd integers from 1 to 255. 
def allOdds(x):
    for i in range (1,256):
        if i % 2 != 0:
            print(i)


# 3. Print Ints and Sum 0-255
# Print integers from 0 to 255, and with each integer print the sum so far. 
def ints_and_sum():
    sum = 0
    for i in range(256):
        sum += i
        print(i, sum)


# 4. Iterate and Print Array
# Iterate through a given array, printing each value. 
def iterate_list(some_list):
    for i in range(0,len(some_list)):
        print(i)


# 5. Find and Print Max
# Given an array, find and print its largest element. 
def printMax(x):
    maxi = 0
    for i in range (len(x)):
        if x[i] < maxi:
            x[i] = maxi
        print(maxi)


# 6. Get and Print Average
# Analyze an array’s values and print the average. 
def average(some_list):
    total = 0
    avg = 0
    for i in range(len(some_list)):
        total += i 
    avg = total / len(some_list)
    return avg



# 7. Array with Odds
# Create an array with all the odd integers between 1 and 255 (inclusive).  
def arrayOdds(x):
    newArr = []
    for i in range (1,256):
        if i % 2 != 0:
            newArr.append(i)
    print(newArr)


# 8. Square the Values
# Square each value in a given array, returning that same array with changed values. 
def square_values(some_list):
    for i in range(len(some_list)):
        some_list[i] = some_list[i] ** 2
    return some_list



# 9. Greater than Y
# Given an array and a value Y, count and print the number of array values greater than Y. 
def greaterY(x,y):
    count = 0
    for i in range (len(x)):
        if y > x[i]:
            count += 1
    print(count)


# 10. Zero Out Negative Numbers
# Return the given array, after setting any negative values to zero. 
def zeroNegative(x):
    for i in range (len(x)):
        if x[i] < 0:
            x[i] = 0


# 11. Max, Min, Average
# Given an array, print the max, min and average values for that array.
def max_min_average(some_list):
    min = 0
    max = some_list[0]
    total = 0
    avg = 0
    for i in range(len(some_list)):
        total += i
        if min < some_list[i]:
            min = some_list[i]
        if max > some_list[i]:
            max = some_list[i]
    avg = total / len(some_list)
    print(avg, min, max)


# 12. Shift Array Values
# Given an array, move all values forward (to the left) by one index, dropping the first value and leaving a 0 (zero) value at the end of the array.
def shiftOver(x):
    for i in range (len(x-1)):
        x[i] = x[i + 1]
    x[len(x-1)] = x[0]
    print(x)


# 13. Swap String For Array Negative Values
# Given an array of numbers, replace any negative values with the string 'Dojo'.
def swap_string_for_negative(some_list):
    for i in range(len(some_list)):
        if some_list[i] < 0:
            some_list[i] = "Dojo"
    return some_list





