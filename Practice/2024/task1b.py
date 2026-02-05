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
    pass

#Find and display the highest number of employees employed by a single
#company and the number of companies who employ within 10% of that figure
def DisplayHighestEmployees(numEmployees):
    pass

#main program

