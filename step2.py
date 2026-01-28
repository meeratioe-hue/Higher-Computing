def ReadFromFileIntoArrayOfRecords():
    return orders 

def FindThePositionOfTheCustomer (orders) :
#2.1 Set position to -1
    position = -1 
#2.2 Set index to 0
    index = 0
#2.3 Ask user to enter month to search for
    month = input("Enter the month you want to search for:")
#2.4 While position is -1 and index is less than the length of the array
    while position == -1 and index < len(orders):
#2.5 If current month is equal to searched month and current rating is 5 then
        if orders [index].month == month:
#2.6 Set position to index
            position = index 
#2.7 End if
#2.8 Add 1 to index
    index = index + 1
#2.9 End while
#2.10 Return position
    return position 

def WriteDetailsOfTheWinningCustomer (orders, position):
    pass
#3.1 Open new file ‘winningCustomer.txt’
#3.2 If position is 0 or above then
#3.3 Write winning order number, email and cost to ‘winningCustomer.txt’
#3.4 Else
#3.5 Write ‘No winner’ to ‘winningCustomer.txt’
#3.6 End if
#3.7 Close ‘winningCustomer.txt’





def DisplayTheTotalNumberOfOrders (orders):
    pass


#main program
orders =ReadFromFileIntoArrayOfRecords()
position = FindThePositionOfTheCustomer (orders)
WriteDetailsOfTheWinningCustomer (orders, position)
DisplayTheTotalNumberOfOrders (orders)
                                    