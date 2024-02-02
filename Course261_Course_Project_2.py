#Alaina Acton
#CIS261
#Course Project

def getdates():
    fromDate = (input("Enter date started in mm/dd/yyyy format: "))
    endDate = (input("Enter date ended in mm/dd/yyyy format: "))
    return fromDate, endDate
    
def getempName():
    empName = input("Enter Employee Name: ")
    return empName

def getHoursWorked():
    hours = float(input("Enter total amount of hours worked: "))
    return hours

def getHourlyRate():
    rate = float(input("Enter hourly rate: "))
    return rate
    
def getTaxRate():
    tax = float(input("Enter tax rate: "))
    tax = tax / 100
    return tax

def CalcTaxAndNetpay(hours, rate, tax):
    gPay = hours * rate
    incomeTax = gPay * tax
    netPay = gPay - incomeTax
    return gPay, incomeTax, netPay

def printinfo(empDetailList):
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00
    for empList in empDetailList:
        fromDate = empList[0]
        endDate = empList[1]
        empName = empList[2]
        hours = empList[3]
        rate = empList[4]
        tax = empList[5]
        
        grosspay, incomeTax, netPay = CalcTaxAndNetpay(hours, rate, tax)
        print(fromDate, endDate, empName, f"{hours:,.2f}", f"{rate:.2f}", f"{grosspay:.2f}", f"{tax:.1%}", f"{incomeTax:,.2f}", f"{netPay:,.2f}")
        
        totalEmployees += 1
        totalHours += hours
        totalGrossPay += grosspay
        totalTax += incomeTax
        totalNetPay += netPay
        
        empTotals['totEmp'] = totalEmployees
        empTotals['totHours'] = totalHours
        empTotals['totGross'] = totalGrossPay
        empTotals['totTax'] = totalTax
        empTotals['totNet'] = totalNetPay

def printTotals(empTotals):
    print(f"\nTotal numer of employees: {empTotals['totEmp']}")
    print(f"Total hours: {empTotals['totHours']}")
    print(f"Total Gross Pay: {empTotals['totGross']}")
    print(f"Total Tax: {empTotals['totTax']}")
    print(f"Total Net Pay: {empTotals['totNet']}")
    
if __name__ == "__main__":
   empDetailList = []
   empTotals = {}
   while True:
       empName = getempName()
       if (empName.upper() == "END"):
           break
       fromDate, EndDate = getdates()
       hours = getHoursWorked()
       rate = getHourlyRate()
       tax = getTaxRate()
       empDetail = []
       empDetail.insert(0, fromDate)
       empDetail.insert(1, EndDate)
       empDetail.insert(2, empName)
       empDetail.insert(3, hours)
       empDetail.insert(4, rate)
       empDetail.insert(5, tax)
       empDetailList.append(empDetail)
   printinfo(empDetailList) #if not indented correctly, will not print
   printTotals(empTotals)  #if not indented correctly, will not print
        
