from dataclasses import dataclass
@dataclass
class student():
    studentID : int = 0
    email : str =""
    password : str =""
    yearGroup : int = 10



def writeAllStudentsToFile (theStudents):
#3.1 Open new file ‘winningCustomer.txt’
    with open("Students.txt", "w") as writefile:
#3.3 Write winning order number, email and cost to ‘winningCustomer.txt’
        writefile.write(theStudents[index].studentID + "," + str(theStudents.email) + "," +  str(theStudents.password) + "," + theStudents.yearGroup)



# main
# 1. setup students
students = [student() for index in range(10)]
# 2. write all students to file
writeAllStudentsToFile(students)


