

from firstapp.models import Employee
import string
import random

#  exec(open(r"E:\My_Revesion\django\casetest\firstapp\db_shell.py").read())


des = ["Software Enginner", "developer","assistant manager","programer", "Branch Head", "Deputy manager"]

for i in range(50):
    letters = string.ascii_lowercase     # it will give you A to z list
    nme = ''.join(random.choice(letters)for i in range(10))

    letters = string.digits
    saly = ''.join(random.choice(letters)for i in range(5))


    letters = string.ascii_uppercase
    cmpany = ''.join(random.choice(letters) for i in range(10))

    desi = random.choice(des)
    print(desi)

    emp = Employee(name=nme, company= cmpany, salary = saly, designation=desi, active= True)   # here we are creating employee i database
    emp.save()


