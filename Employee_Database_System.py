from datetime import datetime
# file handling reference 1 and 2
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
            return AdminMenu(dict_of_employees) ############# STEP 4: RETURN ADMIN'S MENU ############
        
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
            print("Hi,", username) ############## STEP 4: RETURN USER'S MENU ##############
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def AdminMenu(dict_of_employees): # O(n) where n is the user's input to more_actions

    def More_Actions(dict_of_employees): # O(n) where n is the number of times it takes the user to answer correctly
        more_actions = input("Would you like to do anything else? ")
        while more_actions != "Yes" and more_actions != "yes" and more_actions != "No" and more_actions != "no":
            print()
            print("Wrong entry! Answer yes or no.")
            more_actions = input("Would you like to do anything else? ")
        
        if more_actions == "Yes" or more_actions == "yes":
            print()
            return AdminMenu(dict_of_employees)
        elif more_actions == "No" or more_actions == "no":
            print()
            print("Goodbye :)")

    def Display_Stats(dict_of_employees): # O(1) since user doesn't have any inputs in this funcction so its a constant. Worst case is if the dictionary is super long.
        males = 0
        females = 0
        total = len(dict_of_employees)
        for i in dict_of_employees:
            if dict_of_employees[i]["gender"] == "male" or dict_of_employees[i]["gender"] == "Male":
                males += 1
            elif dict_of_employees[i]["gender"] == "female" or dict_of_employees[i]["gender"] == "Female":
                females += 1
        perc_of_males = round((males/total)*100, 2)
        perc_of_females = round((females/total)*100, 2)
        print("In the list of employees provided, {} are males and {} are females.".format(males, females))
        print("Your company is currently {}% males and {}% females".format(perc_of_males, perc_of_females))
        return More_Actions(dict_of_employees)
    
    # References for formatted string syntax numbers 3,4, and 5
    def Add_Employee(dict_of_employees): # O(n) where n is the number of tries it takes the user to pass
        id = 'emp{0:03d}'.format(len(dict_of_employees) + 1) 
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d")

        name = input("Employee name: ")
        while len(name) > 20 or name.isdigit():
            if len(name) > 20:
                print()
                print("Name should be maximum 20 characters.")
                name = input("Employee name: ")
                print()
            elif name.isdigit():
                print()
                print("Name should not be a number.")
                name = input("Employee name: ")
                print()


        gender = input("Gender: [Answer male or female] ")
        while gender != "Male" and gender != "male" and gender != "Female" and gender != "female":
            print()
            print("Invalid entry! Enter male or female.")
            gender = input("Gender: [Answer male or female] ")
            print()


        salary = input("Salary: ") 
        while salary.isdigit() != True or int(salary) > 99999999:
            if salary.isdigit() != True:
                print()
                print("Salary must be a number.")
                salary = input("Salary: ") 
                print()
            elif salary.isdigit() and int(salary) > 99999999:
                print()
                print("Salary must be less than that.")
                salary = input("Salary: ") 
                print()

        dict_of_employees[id] = {'name': name, 'date': timestamp, 'gender': gender, 'salary': salary} # add emp to dictionary
        return More_Actions(dict_of_employees)
    
    def Display_Employees(dict_of_employees): # O(n**2) where n is the length of the entire list, which worst case looping over the whole list
        list_of_timestamps = [] # collect the time of joining of each employee
        for i in dict_of_employees: # O(n)
            time = dict_of_employees[i]["date"]
            list_of_timestamps.append(time) 
        # time complexity reference number 6
        list_of_timestamps.sort() # O(nlogn) sort the time from smallest to greatest
        list_of_timestamps.reverse() # reverse the list => greates to smallest (newest to oldest employee)

        for i in list_of_timestamps: #O(n**2) loop over the timestamps
            for j in dict_of_employees: # loop over the IDs of the main dictionary
                if i == dict_of_employees[j]["date"]: # print the details
                    id = j
                    name = dict_of_employees[j]["name"]
                    date = dict_of_employees[j]["date"]
                    gender = dict_of_employees[j]["gender"]
                    salary = dict_of_employees[j]["salary"]
                    print("{}, name: {}, date: {}, gender: {}, salary: {}".format(id, name, date, gender, salary), end="\n")
        print()
        return More_Actions(dict_of_employees)
    
    def Change_Employee_Salary(dict_of_employees): # O(n) where n is the number of times it takes the user to give  the correct input
        employee = input("Choose employee ID: ") # choose ID => O(n)
        list_of_keys = dict_of_employees.keys()

        while employee not in list_of_keys: # Check if ID is in the list of keys => O(n) worst case is that user doesnt get it right
            print("Employee ID not found.")
            print("Make sure to input the right ID.")
            print()
            employee = input("Choose employee ID: ")
        if employee in list_of_keys: 
            new_salary = input("New Salary: ") # If yes choose new salary => O(n) worst case is that user doesnt get it right
            while new_salary.isdigit() == False: 
                if new_salary.isdigit() == False:
                    print()
                    print("Invalid entry!")
                    new_salary = input("New Salary: ")

            dict_of_employees[employee]["salary"] = new_salary # store new value of salary
        print(dict_of_employees)
        return More_Actions(dict_of_employees)
    
    def Remove_Employee(dict_of_employees): # Time Complexity => O(n) where n is the number of times it takes the user to input correctly
        employee = input("Choose employee ID: ") # choose ID => O(n)
        list_of_keys = dict_of_employees.keys()

        while employee not in list_of_keys: # Check if ID is in the list of keys => O(n) worst case is that user doesnt get it right
            print("Employee ID not found.")
            print("Make sure to input the right ID.")
            print()
            employee = input("Choose employee ID: ")
        if employee in list_of_keys:
            dict_of_employees.pop(employee)
        print(dict_of_employees)
        return More_Actions(dict_of_employees)
    
    # print(dict_of_employees)
    # print(list_of_names)
    print("Welcome Admin!")  # display menu items
    print()
    print("""
        1. Display Stats
        2. Add Employee
        3. Display Employees
        4. Change Employee Salary
        5. Remove Employee
        6. Raise Salary
        7. Exit""")
    print()
    action = input("What would you like to do? ") # user input command
    while action.isdigit() == False or int(action) not in range(1, 8) : # if choice is not a digit or not in the menu
        if action.isdigit() == False:
            print("Please choose a number between 1 and 7.")
            print()
            action = input("What would you like to do? ")
        elif int(action) not in range(1, 8):
            print("Make sure the number chosen is in the menu list!")
            print()
            action = input("What would you like to do? ")
        
    
    if action == "1":
        return Display_Stats(dict_of_employees)
    elif action == "2": 
        return Add_Employee(dict_of_employees)
    elif action == "3":
        return Display_Employees(dict_of_employees)
    elif action == "4":
        return Change_Employee_Salary(dict_of_employees)
    elif action == "5":
        return Remove_Employee(dict_of_employees)
    
dict_of_employees = InputPath()
GreetUser(dict_of_employees)