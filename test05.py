def inputdata ( ) :
    id = str(input('รหัสพนักงาน : '))
    name = str(input('ชื่อพนักงาน : '))
    salary = float(input ('เงินเดือน'))
    return id,name,salary

def calTax(salary) :
    tax = salary*(7/100)
    return tax


def socialSecurity ( ) :
    socialSecurity = 500
    return socialSecurity

def calNetsalary(salary,tax,socialSecurity) :
    netsalary = salary - tax - socialSecurity
    return netsalary

def showSalarytaxSocialSecurityAndNetsalary(salary,tax,socialSecurity,netsalary) :
    print(f'ภาษีเป็นเงิน {tax:.2f} บาท')
    print(f'เงินเดือนสุทธิเป็นเงิน {netsalary:.2f} บาท')

print('------------------------------')
print('-----คำนวณเงินเดือนพนักงาน-----')
print('------------------------------')
id,name,salary = inputdata( )
tax = calTax ( salary)
socialSecurity = socialSecurity()
netsalary = calNetsalary(salary,tax,socialSecurity)
showSalarytaxSocialSecurityAndNetsalary(salary,tax,socialSecurity,netsalary)
print('------------------------------')