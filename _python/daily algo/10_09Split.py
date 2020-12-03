def rotate_string(string, num): 
    new_string = ''
    for i in range(-num, len(string)-num):
        new_string += string[i]

    return new_string

print(rotate_string("Hello World", 4))
print(rotate_string("Hello World", 2))

def rotate(string, num):
    return string[-num:] + string[:-num]

print(rotate('Hello World', 4))