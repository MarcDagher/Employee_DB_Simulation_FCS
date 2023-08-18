#C:\\Users\Dagher\Desktop\employee file

def InputPath():

  ## STEP 1: Receive input file and OPEN
  path = input("Insert Employee File location: ") # determine the file's path
  file_path = path + ".txt" # add the file's extention to complete path

  file = open(file_path, "r") 

  ## STEP 2: Store file's info in dictionary
  list_of_data = [] # list of nested lists storing distributed info of each employee. [empID,name,time,gender,salary]

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
  print(dictionary_of_employees)


InputPath()