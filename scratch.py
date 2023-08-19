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

dict_of_employees = {
'emp001': {'name': 'cdaoud', 'date': '20220802', 'gender': 'male', 'salary': '12000'}, 
'emp002': {'name': 'manuella', 'date': '20220803', 'gender': 'female', 'salary': '1200'}, 
'emp003': {'name': 'jsmith', 'date': '20220804', 'gender': 'male', 'salary': '15000'}, 
'emp004': {'name': 'akim', 'date': '20220805', 'gender': 'male', 'salary': '10500'}, 
'emp005': {'name': 'lparker', 'date': '20220806', 'gender': 'female', 'salary': '13000'}
}

print("cj222".isdigit())