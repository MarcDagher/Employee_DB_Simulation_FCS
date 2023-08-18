# challenges:

# - How will i open an inputted file?
# - Create a function for tracing timestamp


# repetitive functions:
# - go back to the beginninning of menu 

# C:\Users\Dagher\Desktop\employee file

## STEP 1: Receive input file and OPEN

path = input("Insert Employee File location: ") # determine the file's path
file_path = path + ".txt" # add the file's extention to complete path

file = open(file_path, "r") 

## STEP 2: Store file's info in dictionary
list_of_data = [] # stores distributed info. but list contains a list of one single string

for i in file:
    list_of_data.append([i.strip("\n")])
    
list_for_dict = []

for i in list_of_data: # loop over single strings and divide them
    info = i[0].strip(",") # remove commas
    # list_for_dict.append(info.split(", ")) 
    print(i)

# print(list_for_dict)