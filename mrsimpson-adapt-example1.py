from dataclasses import dataclass
@dataclass
class student():
    studentID : int = 0
    email : str =""
    password : str =""
    yearGroup : int = 10

theStudents = [student() for i in range(10)] 

def writeAllStudentsToFile (theStudents, index):
    with open("Students.txt", "w") as writefile:
        for i in theStudents:
            writefile.write(i.studentID) + "," + i.email + "," +  i.password + ","+ str(i.yearGroup)


writeAllStudentsToFile(theStudents)


