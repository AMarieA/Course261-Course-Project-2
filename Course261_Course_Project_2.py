#Alaina Acton
#CIS261
#Course Project
#3
def getempName():
    empName = input("Enter Employee Name: ")
    return empName
#4
def getHoursWorked():
    hours = float(input("Enter total amount of hours worked: "))
    return hours
#5
def getHourlyRate():
    rate = float(input("Enter hourly rate: "))
    return rate
#6    
def getIncomeTax():
    tax = float(input("Enter tax rate: "))
    tax = tax / 100
    return tax
#7
def CalcTaxAndNetpay(hours, rate, tax):
    gPay = hours * rate
    incomeTax = gPay * tax
    netPay = gPay - incomeTax
    return gPay, incomeTax, netPay

def printinfo(empName, hours, rate, gPay, tax, incomeTax, netPay):
    print(empName, f"{hours:,.2f}", f"{rate:.2f}", f"{gPay:.2f}", f"{tax:.1%}", f"{incomeTax:,.2f}", f"{netPay:,.2f}")

def PrintTotals(totalEmp, totalHours, totalGpay, totalTax, totalNetpay):
    print(f"\nTotal numer of employees: {totalEmp}")
    print(f"Total hours: {totalHours:,.2f}")
    print(f"Total Gross Pay: {totalGpay:,.2f}")
    print(f"Total Tax: {totalTax:,.2f}")
    print(f"Total Net Pay: {totalNetpay:,.2f}")
    
if __name__ == "__main__":
    totalEmp = 0
    totalHours = 0.00
    totalGpay = 0.00
    totalTax = 0.00
    totalNetpay = 0.00
    
    while True:
        empName = getempName()
        if (empName.upper() == "END"):
            break
        hours = getHoursWorked()
        rate = getHourlyRate()
        tax = getIncomeTax()
        gPay, incomeTax, netPay = CalcTaxAndNetpay(hours, rate, tax)
        
        printinfo(empName, hours, rate, gPay, tax, incomeTax, netPay)
        
        totalEmp += 1
        totalHours += hours
        totalGpay +=  gPay
        totalTax += incomeTax
        totalNetpay += netPay
        
PrintTotals(totalEmp, totalHours, totalGpay, totalTax, totalNetpay)
        
