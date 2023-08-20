from datetime import datetime

# file handling reference 1 and 2
def InputPath(): # Time Complexity is O(n) => where n is the number of user's errors

  ## STEP 1: Receive input file and OPEN
  path = input("Insert Employee File location without extension: ") # determine the file's path

  # reference folder number 8
  global file_path # in order to call file_path in exit function
  file_path = path + ".txt" # add the file's extention to complete path

  # Reference file number 12
  try:
    file = open(file_path, "r") 
  except OSError:
      print("Please enter a valid file.")
      print()
      return InputPath()
      

  ## STEP 2: Store file's info in dictionary
  list_of_data = [] # Nested list storing distributed info of each employee. [[empID,name,time,gender,salary]]

    # Reference file number 13
  for i in file.readlines():
      if i.strip(): 
        new_line_1 = i.strip("\n ") # line with no \n and space
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
#   print(dictionary_of_employees)
  file.close() # Close file
  print()
  print("Enter Username and Password")
  return dictionary_of_employees

# STEP 3: GREET USER and TAKE USERNAME + PASSWORD

def GreetUser(dict_of_employees): # Worst case answering wrong 5 times. Time Complexity O(n**2) where n is the input of username and pass
    list_of_names = [] # store names

    for i in dict_of_employees:
        list_of_names.append(dict_of_employees[i]["name"])

    username = input("Username: ")
    count = 1
    
    while username != "admin" and username not in list_of_names and count < 5: # user errors (not found, more than 5 tries) note: admin isnt part of the file so we used and not or
        count += 1
        print("User not found!")
        print()
        username = input("Username: ")

    if count == 5:
        print("Too many tries...")
        print("Goodbye :)")
        return 

    password = input("Password: ") # ask for password
    if username == "admin": # if admin
        count = 1
        while password != "admin123123" and count < 5: #if worng password and exceeded limit
            print("wrong password")
            count += 1
            print()
            password = input("Password: ")
        if count == 5: 
            print("Too many tries.")
            print("Goodbye :)")
            return

        if password == "admin123123":
            return AdminMenu(dict_of_employees) ############# STEP 4: RETURN ADMIN'S MENU ############
        
    elif username in list_of_names: # if user
        count = 1
        while password != "" and count < 5:
            print("Wrong password!")
            count += 1
            print()
            password = input("Password: ")
        if count == 5:
            print("Too many tries.")
            print("Goodbye :)")
            print()
        
        if password == "": # if password is correct
            for i in dict_of_employees:
                if dict_of_employees[i]["name"] == username:
                    id = i
                    if dict_of_employees[i]["gender"] == "male" or dict_of_employees[i]["gender"] == "Male":
                        pronoun = "Mr."
                    elif dict_of_employees[i]["gender"] == "Female" or dict_of_employees[i]["gender"] == "female":
                        pronoun = "Ms."

            print("Hi,", pronoun, username) ############## STEP 4: RETURN USER'S MENU ##############
            return User_Menu(dict_of_employees, id)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def User_Menu(dict_of_employees, id): # O(n) * O(function chosen) where is is the user's number of errors
    def More_Actions(dict_of_employees, id): # O(n ** 2) where n is the number of times it takes the user to answer correctly
        more_actions = input("Would you like to do anything else? ")
        while more_actions != "Yes" and more_actions != "yes" and more_actions != "No" and more_actions != "no": # O(n)
            print()
            print("Wrong entry! Answer yes or no.")
            more_actions = input("Would you like to do anything else? ")
        
        if more_actions == "Yes" or more_actions == "yes":
            print()
            return User_Menu(dict_of_employees, id)
        
        elif more_actions == "No" or more_actions == "no":
            print()
            confirm = input("Are you sure you want to exit? ")
            while confirm != "Yes" and confirm != "yes" and confirm != "No" and confirm != "no": # nested O(n)
                print()
                print("Wrong entry! Answer yes or no.")
                confirm = input("Are you sure you want to exit? ")
        ## Reference page number 7
            if confirm == "Yes" or confirm == "yes":
                print()
                print("Changes Saved.")
                Exit(dict_of_employees, id) ##### exit and save file#####
            elif confirm == "No" or confirm == "no":
                print()
                return User_Menu(dict_of_employees, id)
            
    def Check_My_Salary(dict_of_employees, id): # O(1) complexity
        print()
        print("Your salary is {}$.".format(dict_of_employees[id]["salary"]))
        return More_Actions(dict_of_employees, id)
    # Reference file number 10
    def Exit(dict_of_employees, id):# O(1) Complexity
        time_file = open("timestamps.txt", "w")
        now = datetime.now()
        date = now.strftime("%d-%B-%Y")
        time = now.strftime("%I:%M %p")
        time_file.write("{} logged in on {} at {}".format(dict_of_employees[id]["name"], date, time))
        print()
        print("Login timestamp saved on timestamps.txt file.")
        print("Goodbye :)")
     #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END of SUB-FUNCTIONS   
    print()
    print("""
        1. Check My Salary
        2. Exit
          """)
    print()
    action = input("What would you like to do? ") # user input command 
    while action.isdigit() == False or int(action) not in range(1, 3) : # if choice is not a digit or not in the menu O(n)
        if action.isdigit() == False:
            print("Please choose a number between 1 and 2.")
            print()
            action = input("What would you like to do? ")
        elif int(action) not in range(1, 3):
            print("Make sure the number chosen is in the menu list!")
            print()
            action = input("What would you like to do? ")
    if action == "1":
        return Check_My_Salary(dict_of_employees, id)
    elif action == "2":
        return Exit(dict_of_employees, id)


def AdminMenu(dict_of_employees): # O(n) * O(function chosen) where n is the user's input to more_actions
    
    def More_Actions(dict_of_employees): # O(n ** 2) where n is the number of times it takes the user to answer correctly
        more_actions = input("Would you like to do anything else? ")
        while more_actions != "Yes" and more_actions != "yes" and more_actions != "No" and more_actions != "no": # O(n)
            print()
            print("Wrong entry! Answer yes or no.")
            more_actions = input("Would you like to do anything else? ")
        
        if more_actions == "Yes" or more_actions == "yes":
            print()
            return AdminMenu(dict_of_employees)
        
        elif more_actions == "No" or more_actions == "no":
            print()
            confirm = input("Are you sure you want to exit? ")
            while confirm != "Yes" and confirm != "yes" and confirm != "No" and confirm != "no": # nested O(n)
                print()
                print("Wrong entry! Answer yes or no.")
                confirm = input("Are you sure you want to exit? ")
        ## Reference page number 7
            if confirm == "Yes" or confirm == "yes":
                print()
                return Exit(dict_of_employees, file_path) ##### exit and save file #######
            elif confirm == "No" or confirm == "no":
                print()
                return AdminMenu(dict_of_employees)

                

    def Display_Stats(dict_of_employees): # O(n) since user doesn't have any inputs in this funcction so its a constant. Worst case is if the dictionary is super long.
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
        print()
        return More_Actions(dict_of_employees)
    
    # References for formatted string syntax numbers 3,4, and 5
    def Add_Employee(dict_of_employees): # O(3n) = O(n) where n is the number of tries it takes the user to pass
        id = 'emp{0:03d}'.format(len(dict_of_employees) + 1) 
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d")

        name = input("Employee name: ")
        while len(name) > 20 or name.isdigit(): #O(n)
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
        while gender != "Male" and gender != "male" and gender != "Female" and gender != "female":# O(n)
            print()
            print("Invalid entry! Enter male or female.")
            gender = input("Gender: [Answer male or female] ")
            print()


        salary = input("Salary: ") 
        while salary.isdigit() != True or int(salary) > 99999999:  # O(n)
            if salary.isdigit() != True:
                print()
                print("Invalid Entry!")
                salary = input("Salary: ") 
                print()
            elif salary.isdigit() and int(salary) > 99999999:
                print()
                print("Invalid Entry! Salary must be less than that.")
                salary = input("Salary: ") 
                print()

        dict_of_employees[id] = {'name': name, 'date': timestamp, 'gender': gender, 'salary': salary} # add emp to dictionary
        print()
        return More_Actions(dict_of_employees)
    
    def Display_Employees(dict_of_employees): # O(n**2) where n is the length of the entire list. worst case is looping over the whole list in both loops line 170
        list_of_timestamps = [] # collect the time of joining of each employee
        for i in dict_of_employees: # O(n)
            time = dict_of_employees[i]["date"]
            list_of_timestamps.append(time) 
        # time complexity reference file number 6
        list_of_timestamps.sort() # O(nlogn) sort the time from smallest to greatest
        list_of_timestamps.reverse() # reverse the list => greates to smallest (newest to oldest employee)

        print("Employees sorted from new to old.")
        print()
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
    
    def Change_Employee_Salary(dict_of_employees): # O(n**2) where n is the number of times it takes the user to give  the correct input
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
            
            print("Done.")
            print()

            dict_of_employees[employee]["salary"] = new_salary # store new value of salary
        # print(dict_of_employees)
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
            print("Employee removed.")
        # print(dict_of_employees)
        print()
        return More_Actions(dict_of_employees)
    
    def Raise_Salary(dict_of_employees): # O(n) where n is the number of possible errors
        employee = input("Choose employee ID: ") # choose ID => O(n)
        list_of_keys = dict_of_employees.keys()

        while employee not in list_of_keys: # Check if ID is in the list of keys => O(n) worst case is that user doesnt get it right
            print("Employee ID not found.")
            print("Make sure to input the right ID.")
            print()
            employee = input("Choose employee ID: ")
        current_salary = dict_of_employees[employee]["salary"]
        name = dict_of_employees[employee]["name"]
        print("{}'s salary is {}$.".format(name, current_salary))
        print()
        ## Solution for float number reference file number 11
        percentage = input("Input percentage of raise: ") # O(n) n is ammount of errors
        while percentage.replace(".","",1).isdigit() == False or float(percentage) > 1000: 
            if percentage.replace(".","",1).isdigit() == False:
                print("Invalid entry!")
                print()
                percentage = input("Input percentage of raise: ")
                print()
            elif float(percentage) > 1000:
                print("Can't be more than 1000.")
                print()
                percentage = input("Input percentage of raise: ")
                print()

        new_salary = (float(current_salary) * (float(percentage)/100)) + float(current_salary)
        dict_of_employees[employee]["salary"] = str(new_salary)
        print("{}'s salary is now {}$.".format(name, new_salary))
        print()
        # print(dict_of_employees)
        return More_Actions(dict_of_employees)
    
    def Exit(dict_of_employees, file_path): # O(n) => where n is the length of the dictionary
        # print(file_path)
        adjusted_file = open(file_path, "w") # "w" to overwrite existing lines and add new ones
        for i in dict_of_employees:
            adjusted_file.write("{}, {}, {}, {}, {} \n".format(i,dict_of_employees[i]["name"], dict_of_employees[i]["date"], dict_of_employees[i]["gender"], dict_of_employees[i]["salary"]))

        adjusted_file.close()
        print()
        print("Changes have been saved!")
        print("Goodbye :)")

    
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
    while action.isdigit() == False or int(action) not in range(1, 8) : # if choice is not a digit or not in the menu O(n)
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
    elif action == "6":
        return Raise_Salary(dict_of_employees)
    elif action == "7":
        return Exit(dict_of_employees, file_path)
    
# ~~~~~~ END OF FUNCTIONS ~~~~~~~    

dict_of_employees = InputPath()
GreetUser(dict_of_employees)