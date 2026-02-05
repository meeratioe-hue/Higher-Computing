from dataclasses import dataclass
@dataclass
class student():
    studentID : int = 0
    email : str =""
    password : str =""
    yearGroup : int = 10

theStudents = [student() for i in range(10)] 

def writeAllStudentsToFile (theStudents, index):
#3.1 Open new file ‘winningCustomer.txt’
    with open("Students.txt", "w") as writefile:
#3.3 Write winning order number, email and cost to ‘winningCustomer.txt’
        writefile.write(theStudents[index].studentID + "," + str(theStudents[index].email) + "," +  str(theStudents[index].password) + ","+ theStudents[index].yearGroup)


index = writeAllStudentsToFile(theStudents[index])


