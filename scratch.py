from datetime import datetime
# challenges:

# - How will i open an inputted file?
# - Create a function for tracing timestamp


# repetitive functions:
# - go back to the beginninning of menu 

# C:\Users\Dagher\Desktop\employee file
# dict1 = {
# 'emp001': {'name': 'cdaoud', 'date': '20220802', 'gender': 'male', 'salary': '12000'}
# }

# list1 = ['cdaoud', 'manuella', 'jsmith', 'akim', 'lparker']
# name = input("hi: ")
# while name not in list1:
#   name = input("hi: ")

# print("Name is found")
###########
#males = 0
# females = 0
# total = len(dict_of_employees)
# for i in dict_of_employees:
#     if dict_of_employees[i]["gender"] == "male" or dict_of_employees[i]["gender"] == "Male":
#         males += 1
#     elif dict_of_employees[i]["gender"] == "female" or dict_of_employees[i]["gender"] == "Female":
#         females += 1
# perc_of_males = (males/total)*100
# perc_of_females = (females/total)*100
# print("In the list of employees provided, {} are males and {} are females.".format(males, females))
# print("Your company is currently", perc_of_males, "% males and", perc_of_females,"%", "females")
###########



# id = 'emp{0:03d}'.format(len(dict_of_employees) + 1) 
# now = datetime.now()
# timestamp = now.strftime("%Y%m%d")

# name = input("Employee name: ")
# while len(name) > 20 and name.isdigit():
#     if len(name) > 20:
#         print()
#         print("Name should be maximum 20 characters.")
#         name = input("Employee name: ")
#         print()
#     elif name.isdigit():
#         print()
#         print("Name should not be a number.")
#         name = input("Employee name: ")
#         print()


# gender = input("Gender: [Answer male or female] ")
# while gender != "Male" and gender != "male" and gender != "Female" and gender != "female":
#     print()
#     print("Invalid entry! Enter male or female.")
#     gender = input("Gender: [Answer male or female] ")
#     print()


# salary = input("Salary: ") 
# while salary.isdigit() != True and int(salary) > 99999999:
#     if salary.isdigit() != True:
#         print()
#         print("Salary must be a number.")
#         salary = input("Salary: ") 
#         print()
#     elif int(salary) > 99999999:
#         print()
#         print("Salary must be less than that.")
#         salary = input("Salary: ") 
#         print()

# dict_of_employees[id] = {'name': name, 'date': timestamp, 'gender': gender, 'salary': salary}
#########################
# def Display_Employees(dict_of_employees):
#   list_of_timestamps = []
#   for i in dict_of_employees:
#     time = dict_of_employees[i]["date"]
#     list_of_timestamps.append(time)
#   list_of_timestamps.sort()
#   list_of_timestamps.reverse()
#   for i in list_of_timestamps:
#     for j in dict_of_employees:
#       if i == dict_of_employees[j]["date"]:
#         id = j
#         name = dict_of_employees[j]["name"]
#         date = dict_of_employees[j]["date"]
#         gender = dict_of_employees[j]["gender"]
#         salary = dict_of_employees[j]["salary"]
#         print("{}, name: {}, date: {}, gender: {}, salary: {}".format(id, name, date, gender, salary), end="\n")

# Display_Employees(dict_of_employees)




# def Display_Employees(dict_of_employees):
#     dict_of_time = {} # time stamps with the index of the employee
#     for i in dict_of_employees:
#         id = i
#         key = dict_of_employees[i]["date"]
#         dict_of_time[key] = id

#     sorted_dictionary = {}
#     for i in dict_of_time:
#         key = dict_of_time[i]
#         sorted_dictionary[key] = dict_of_employees[key]

#     print(sorted_dictionary)

# Display_Employees(dict_of_employees)
#######################################

# def Change_Employee_Salary(dict_of_employees): # O(n) where n is the number of times it takes the user to give  the correct input
#     employee = input("Choose employee ID: ") # choose ID => O(n)
#     list_of_keys = dict_of_employees.keys()

#     while employee not in list_of_keys: # Check if ID is in the list of keys => O(n) worst case is that user doesnt get it right
#         print("Employee ID not found.")
#         print("Make sure to input the right ID.")
#         print()
#         employee = input("Choose employee ID: ")
#     if employee in list_of_keys: 
#         new_salary = input("New Salary: ") # If yes choose new salary => O(n) worst case is that user doesnt get it right
#         while new_salary.isdigit() == False or int(new_salary) < 0: # negative numbers returning => please insert a number
#             if new_salary.isdigit() == False:
#                 print()
#                 print("Invalid entry, please insert a number!")
#                 new_salary = input("New Salary: ")
#             elif int(new_salary) < 0:
#                 print()
#                 print("Invalid entry, salary can't be negative!")
#                 new_salary = input("New Salary: ")

#         dict_of_employees[employee]["salary"] = new_salary # store new value of salary

# Change_Employee_Salary(dict_of_employees)
########################################################################################################


dict_of_employees = {
'emp001': {'name': 'cdaoud', 'date': '20220811', 'gender': 'male', 'salary': '12000'}, 
'emp002': {'name': 'manuella', 'date': '20220821', 'gender': 'female', 'salary': '1200'}, 
'emp003': {'name': 'jsmith', 'date': '20220701', 'gender': 'male', 'salary': '15000'}, 
'emp004': {'name': 'akim', 'date': '20220605', 'gender': 'male', 'salary': '10500'}, 
'emp005': {'name': 'lparker', 'date': '20220806', 'gender': 'female', 'salary': '13000'}, 
'emp006': {'name': 'bnguyen', 'date': '20220807', 'gender': 'male', 'salary': '14000'}, 
'emp007': {'name': 'cwong', 'date': '20220208', 'gender': 'female', 'salary': '11500'}, 
'emp008': {'name': 'rkumar', 'date': '20220809', 'gender': 'male', 'salary': '16000'}, 
'emp009': {'name': 'spatel', 'date': '20220810', 'gender': 'female', 'salary': '12500'}, 
'emp010': {'name': 'dlee', 'date': '20220811', 'gender': 'male', 'salary': '11000'}, 
'emp011': {'name': 'jgonzalez', 'date': '20220812', 'gender': 'female', 'salary': '13500'}, 
'emp012': {'name': 'tsmith', 'date': '20220113', 'gender': 'male', 'salary': '17000'}, 
'emp013': {'name': 'kmurphy', 'date': '20220814', 'gender': 'female', 'salary': '12200'}, 
'emp014': {'name': 'hrodriguez', 'date': '20220815', 'gender': 'female', 'salary': '13200'}, 
'emp015': {'name': 'jramirez', 'date': '20220816', 'gender': 'male', 'salary': '12700'}, 
'emp016': {'name': 'wjohnson', 'date': '20220917', 'gender': 'male', 'salary': '14500'}, 'emp017': {'name': 'mgarcia', 'date': '20220818', 'gender': 'female', 'salary': '12800'}, 'emp018': {'name': 'kparker', 'date': '20220819', 'gender': 'male', 'salary': '11200'}, 'emp019': {'name': 'nanderson', 'date': '20220820', 'gender': 'male', 'salary': '10300'}, 'emp020': {'name': 'amiller', 'date': '20220821', 'gender': 'female', 'salary': '12900'}, 'emp021': {'name': 'ssmith', 'date': '20220822', 'gender': 'female', 'salary': '13800'}, 'emp022': {'name': 'bbrown', 'date': '20130823', 'gender': 'male', 'salary': '15500'}, 'emp023': {'name': 'rmartinez', 'date': '20220824', 'gender': 'female', 'salary': '14200'}, 'emp024': {'name': 'cwright', 'date': '20220825', 'gender': 'male', 'salary': '14800'}, 'emp025': {'name': 'ajackson', 'date': '20220826', 'gender': 'female', 'salary': '11700'}, 'emp026': {'name': 'mgonzalez', 'date': '20220827', 'gender': 'female', 'salary': '13300'}, 'emp027': {'name': 'djones', 'date': '20220828', 'gender': 'male', 'salary': '15800'}, 'emp028': {'name': 'bsmith', 'date': '20220829', 'gender': 'male', 'salary': '11900'}, 'emp029': {'name': 'erobinson', 'date': '20220830', 'gender': 'female', 'salary': '12300'}, 'emp030': {'name': 'cgonzalez', 'date': '20220831', 'gender': 'female', 'salary': '13700'}
}

