#C:\\Users\Dagher\Desktop\employee file

def InputPath(): # Time Complexity is O(n) => the code depends on the user's file input

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
  print("File saved.")
  print()
  print("Enter Username and Password")
  return dictionary_of_employees

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# STEP 3: GREET USER and TAKE USERNAME + PASSWORD

def GreetUser(dict_of_employees): # Worst case answering wrong 5 times. Time Complexity O(n) where n is the input username and pass
    list_of_names = [] # store names

    for i in dict_of_employees:
        list_of_names.append(dict_of_employees[i]["name"])

    username = input("Username: ")
    count = 1
    
    while username != "admin" and username not in list_of_names and count < 5: # user errors (not found, more than 5 tries) note: admin isnt part of the file so we used and not or
        count += 1
        print("User not found!")
        username = input("Username: ")

    if count == 5:
        print("Too many tries...")
        print("Try again.")
        print()
        return GreetUser(dict_of_employees)


    password = input("Password: ") # ask for password
    if username == "admin": # if admin
        count = 1
        while password != "admin123123" and count < 5: #if worng password and exceeded limit
            print("wrong password")
            count += 1
            password = input("Password: ")
        if count == 5: 
            print("Too many tries.")
            print("Try again.")
            print()
            return GreetUser(dict_of_employees)
        if password == "admin123123":
            print("Admin's Menu") ############# RETURN ADMIN'S MENU ############
        
    elif username in list_of_names: # if user
        count = 1
        while password != "" and count < 5:
            print("Wrong password!")
            count += 1
            password = input("Password: ")
        if count == 5:
            print("Too many tries.")
            print("Try again.")
            print()
            return GreetUser(dict_of_employees)
        if password == "":
            print("Hi,", username) ############## RETURN USER'S MENU ##############

            
dict_of_employees = InputPath()
GreetUser(dict_of_employees)