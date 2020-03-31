"""
Name: Maher Ibrahim
Class: Fall - INSY-3300
Homework 4: Homework #1
Date: 12/15/2019
Description: This program holds the following data about an employee in attributes: name, ID number, department, and job title
"""



import pickle
import sys
from employee import Employee

try:
    f=open('employee.dat','rb')
  
    d=pickle.load(f)
  
    f.close()
     
except:
    d={}

while True:

    print('\n1. Look up an employee in the dictionary')
    print('2. Add a new employee in the dictionary')
    print("3. Change an existing employee's name,department and job title in the dictionary")
    print('4. Delete an employee from the dicionary')
    print('5. Quit the program\n')

    choice=input('\nEnter a choice: ')

    if choice:
        choice=int(choice)
    else:
        print('\nEnter a number')
        continue  

    if choice == 1:

        while True:

            emp_id=input('\nEnter ID of the employee: ')

            if emp_id:

                emp_id=int(emp_id)
                if emp_id in d:

                    ob=d[emp_id]

                    print('Employee Name: ',ob.getname())
                    print('Employee ID: ',ob.getid())
                    print('Employee department: ',ob.getdepartment())
                    print('Employee job title: ',ob.gettitle())                  
                    break
              
                else:
                    print('\nEmployee not found \n')
                    break
            else:
                print('\nID cannot be empty\n')
                continue
          
    elif choice==2:

        while True:          

            name=input('\nEnter the name of the employee: ')

            if name:
                break
            else:
                print('\nName cannot be empty \n')
                continue

        while True:          

            emp_id=input('\nEnter the employee id: ')

            if emp_id:
                emp_id=int(emp_id)
                break
            else:
                print('\nEmployee ID empty please enter data\n')
                continue

        while True:          

            dept=input('\nEnter employee department: ')

            if dept:
                break
            else:
                print('\nEmployee department empty please enter data\n')
                continue

        while True:          

            title=input('\nEnter employee job title: ')

            if title:
                break
            else:
                print('\nEmployee title empty please enter data\n')
                continue

        ob=Employee(name,emp_id,dept,title)

        d[emp_id]=ob      

    elif choice==3:

        while True:          

            emp_id=input('\nEnter employee ID to change the details: ')

            if emp_id:

                emp_id=int(emp_id)

                ob=''

                if emp_id in d:

                    ob=d[emp_id]

                    while True:          

                        name=input('\nEnter new name of the employee: ')

                        if name:
                            ob.setname(name)
                            break
                        else:
                            print('\nName empty please enter data \n')
                            continue


                    while True:          

                        dept=input('\nEnter new department of the employee: ')

                        if dept:
                            ob.setdepartment(dept)
                            break
                        else:
                            print('\nDepartment empty please enter data \n')
                            continue

                    while True:          

                        title=input('\nEnter new job title of the employee: ')

                        if title:
                            ob.settitle(title)
                            break
                        else:
                            print('\nTitle empty please enter data \n')
                            continue

                    print('Data updated')
                    break
                else:
                    print('\nID not found \n')
                    break
            else:

                print('\nID empty please enter data \n')
                continue
          

    elif choice == 4:

        while True:          

            emp_id=input('\nEnter ID of the employee to delete: ')


            if emp_id:

                emp_id=int(emp_id)

                if emp_id in d:

                    del d[emp_id]
                    print('\nEmployee data deleted \n ')
                    break;
                else:

                    print('\nEmployee not found \n')
                    break
            else:

                print('\nID empty please enter data\n')
                continue

    elif choice == 5:

        f=open('employee.dat','wb')
        pickle.dump(d,f)
        f.close()
        exit()
      
    else:
        print('\nEnter a valid choice ')
 