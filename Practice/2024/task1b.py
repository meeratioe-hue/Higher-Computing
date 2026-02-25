items = []
company = []
numEmployees = []
ceoSalary = []

#Read from file into parallel arrays
def ReadFromFileIntoParallelArrays():
    with open ("companies.text") as readfile:
        line = readfile.readline().rstrip('\n')
        while line:
            items = line.split(",")
            company.append(items[0])
            numEmployees.append(items[1])
            ceoSalary.append(items[2])
            line = readfile.readline().rstrip('\n')
    return company, numEmployees, ceoSalary
print(company, numEmployees, ceoSalary)

#Find and display the difference between the chosen company's CEO salary
#and the highest CEO salary
def FindDifferenceBetweenCEOs(company, ceoSalary):
# 2.1 Ask user to enter the name of chosen company
# 2.2 Set found to false
# 2.3 Call findMaxPos function to return the position of highest CEO salary
# 2.4 Loop for company array
# 2.5   If current company is the chosen company
# 2.6        Set found to true
# 2.7       Set position to current index
# 2.8 End if
# 2.9 End loop
# 2.10 If chosen company name is in list
# 2.11   Subtract and store chosen company’s CEO salary from highest CEO salary
# 2.12   Display message containing name of company with highest CEO salary, name of chosen company, and difference in salaries
# 2.13 Else
# 2.14  Display “Company not found”
# 2.15 End if
    pass

#Find and display the highest number of employees employed by a single
#company and the number of companies who employ within 10% of that figure
def DisplayHighestEmployees(numEmployees):
    pass

#main program

