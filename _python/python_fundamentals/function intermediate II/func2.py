x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 15, 'y': 20} ]

x[1][0] = int("15")
print(x)

students[0]["last_name"] = "Bryant"
print(students)
    
sports_directory["soccer"][0] = "Andres"
print(sports_directory)

z[0]['y']=30
print(z)

# def Value(z):

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30



students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# def iterateDictionary(students):
#     for i in range (len(students)):
#         print(students[i]['first_name'])
#         print(students[i]['last_name'])
        
# print(iterateDictionary(students))
    


def iterateDictionary2(key_name, some_list):
    for i in range (len(students)):
        print(students[i]['first_name'])
    for i in range (len(students)):
        print(students[i]['last_name'])




dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}



def printInfo(dojo):
    print("7 Locations")
    
    for i in range (len(dojo['locations'])):
        print(dojo['locations'][i])
    print("8 Instructors")
    for i in range (len(dojo['instructors'])):
        print(dojo['instructors'][i])

print(printInfo(dojo))



