# open, Read/write, close file 
file = open("C:\\Users\Dagher\Desktop\employee file2.txt", "rt") # choose the file and open in read mode
list_of_data = [] # Nested list storing distributed info of each employee. [[empID,name,time,gender,salary]]

for i in file:
    new_line_1 = i.strip("\n") # line with no \n
    new_line_2 = new_line_1.split(", ") # remove commas and turn string into a list
    list_of_data.append(new_line_2) # store each line

dictionary_of_employees = {}

for i in list_of_data: # assigning each key to its dictionary of values
    id = i[0]
    name = i[1]
    date = i[2]
    gender = i[3]
    salary = i[4]
    dictionary_of_employees[id] = {"name" : name, "date" : date, "gender" : gender, "salary" : salary}
print("File saved.")
file.close() # Close file

dictionary_of_employees.pop("emp001")
dictionary_of_employees.pop("emp010")
dictionary_of_employees.pop("emp020")
dictionary_of_employees.pop("emp030")
dictionary_of_employees.pop("emp021")
dictionary_of_employees.pop("emp012")
dictionary_of_employees.pop("emp008")

# print(dictionary_of_employees)
adjusted_file = open("C:\\Users\Dagher\Desktop\employee file2.txt", "w")
for i in dictionary_of_employees:
    adjusted_file.write("{}, {}, {}, {}, {} \n".format(i,dictionary_of_employees[i]["name"], dictionary_of_employees[i]["date"], dictionary_of_employees[i]["gender"], dictionary_of_employees[i]["salary"]))

adjusted_file.close()