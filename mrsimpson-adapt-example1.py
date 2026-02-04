from dataclasses import dataclass
@dataclass
class students():
    studentID : int = 0
    name: str =""
    email : str =""
    yearGroup : int = 10

students = [student()for i in range (10)]

def WriteDetailsOfTheWinningCustomer (finalorders, position):
#3.1 Open new file ‘winningCustomer.txt’
    with open("winningCustomer.txt", "w") as writefile:
#3.2 If position is 0 or above then
        if position >= 0 :
#3.3 Write winning order number, email and cost to ‘winningCustomer.txt’
            writefile.write(finalorders[position].orderNum + "," + finalorders[position].email + "," +  str(finalorders[position].cost))
#3.4 Else
        else:
#3.5 Write ‘No winner’ to ‘winningCustomer.txt’
            writefile.write("No winner")


