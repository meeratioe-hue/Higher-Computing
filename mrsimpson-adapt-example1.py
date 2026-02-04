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
            writefile.write(finalorders[position].orderNum + "," + finalorders[position].email + "," +  str(finalorders[position].cost))
#3.4 Else
        else:
#3.5 Write ‘No winner’ to ‘winningCustomer.txt’
            writefile.write("No winner")


