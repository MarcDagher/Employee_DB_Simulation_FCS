# open, Read/write, close file 
f = open("C:\\Users\Dagher\Desktop\SE-Midterm.txt", "rt") # choose the file and open in read mode

list1 = f.read().split('\n') # apply read funtcion and remove empty lines 
Data = [] 
for i in list1: # loop over the file and remove empty lines then empty spaces between the lines.
    if i.strip(): # if non white-spaces
        Data.append(i) # non-empty lines are added to Data
print(Data)

f.close() # close the file to continue


# Using with statement
# with open("C:\\Users\Dagher\Desktop\SE-Midterm.txt", "r") as file:
#     data = file.read()
#     print(data)

# print(file.read)