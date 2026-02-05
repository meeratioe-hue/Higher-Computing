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
            writefile.write(str(theStudents[index].studentID) + "," + theStudents[index].email + "," +  theStudents[index].password + ","+ str(theStudents[index].yearGroup))

index = 0
writeAllStudentsToFile(theStudents, index)


