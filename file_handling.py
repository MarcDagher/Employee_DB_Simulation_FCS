# # open, Read/write, close file 
# file = open("C:\\Users\Dagher\Desktop\employee file2.txt", "rt") # choose the file and open in read mode
# list_of_data = [] # Nested list storing distributed info of each employee. [[empID,name,time,gender,salary]]


# # for i in file:
# #     if i == " ":
# #         continue
# #     new_line_1 = i.strip("\n") # line with no \n
# #     new_line_2 = new_line_1.split(", ") # remove commas and turn string into a list
# #     list_of_data.append(new_line_2) # store each line

# # dictionary_of_employees = {}

# # for i in list_of_data: # assigning each key to its dictionary of values
# #     id = i[0]
# #     name = i[1]
# #     date = i[2]
# #     gender = i[3]
# #     salary = i[4]
# #     dictionary_of_employees[id] = {"name" : name, "date" : date, "gender" : gender, "salary" : salary}
# # print("File saved.")
# # file.close() # Close file

# # print(dictionary_of_employees)

# f = open("C:\\Users\Dagher\Desktop\employee file3.txt", "x")
f = open("C:\\Users\Dagher\Desktop\employee file.txt", "w")