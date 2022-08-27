#Program Name: employeeManagement
#Author: Cole Pedersen
#Date: 11/21/2021
#Program Description: This program creates a dictionary through the use of classes
#This is used to put employees in the dictionary and allows you to update, delete, search, add, and view them

import random

#This is the class funtion that is used threwout the rest of the program
class Employee:
    def __init__(self, department, jobtitle, fulltime):
        self.__department = department
        self.__jobtitle = jobtitle
        self.__fulltime = fulltime
    
    def set_department(self, department):
        self.__department = department

    def set_jobtitle(self, jobtitle):
        self.__jobtitle = jobtitle

    def set_fulltime(self, fulltime):
        self.__fulltime = fulltime

    def get_department(self):
        return self.__department

    def get_jobtitle(self):
        return self.__jobtitle

    def get_fulltime(self):
        return self.__fulltime

#This is used to choice what funtion you want to do
def main():
    employee_dic = {}
    again = True
    while again == True:
        start_message()
        valid = False
        while valid == False:
            choice = (input('Enter option: '))
            print('')
            if choice == '1':
                valid = True
                search(employee_dic)
            elif choice == '2':
                valid = True
                employee_dic = add(employee_dic)
                print (employee_dic)
            elif choice == '3':
                valid = True
                update(employee_dic)
            elif choice == '4':
                valid = True
                employee_dic = delete(employee_dic)
            elif choice == '5':
                valid = True
                display_all(employee_dic)
            elif choice == '6':
                valid = True
                again = False
            else:
                print('Invalid option')

#its the start message
def start_message():
    print('EMPLOYEE MANAGEMENT SYSTEM')
    print('---------------------------')
    print('1. Search')
    print('2. Add')
    print('3. Update')
    print('4. Delete')
    print('5. Display All')
    print('6. Quit')

#Searchs a given ID and desplays its information
def search(employee_dic):
    print('EMPLOYEE INFORMATION')
    print('---------------------')
    key = int(input('Enter ID: '))
    value = employee_dic.get(key, 'ID does not exist')
    if value != 'ID does not exist':
        print(f'ID: {key}')
        print(f'Department: {value.get_department()}')
        print(f'Job Title: {value.get_jobtitle()}')
        print(f'Full-time: {value.get_fulltime()}\n')
    else:
        print(value)
        print('')

#Adds an employee to the dictionary
def add(employee_dic):
    print('ADD EMPLOYEE')
    print('-------------')
    department = input('Department: ')
    jobtitle = input('title: ')
    fulltime = input('Full-time (Y/N): ').upper()
    ID = random.randint(10000, 99999)
    employee_info = Employee(department, jobtitle, fulltime)
    employee_dic[ID] = employee_info
    print (f'Employee {ID} has been added\n')
    return employee_dic

#Updates an employee of the given ID
def update(employee_dic):
    print('UPDATE EMPLOYEE')
    print('----------------')
    key = int(input('Enter ID: '))
    value = employee_dic.get(key, 'ID does not exist')
    if value != 'ID does not exist':
        department = input('Department: ')
        jobtitle = input('Title: ')
        fulltime = input('Full-time (Y/N): ').upper()
        value.set_department(department)
        value.set_jobtitle(jobtitle)
        value.set_fulltime(fulltime)
        print('New values set\n')
    else:
        print(value)
        print('')

#Deletes an employee of the given ID
def delete(employee_dic):
    print('DELETE EMPLOYEE')
    print('----------------')
    key = int(input('Enter ID: '))
    value = employee_dic.get(key, 'ID does not exist')
    if value != 'ID does not exist':
        del employee_dic[key]
        print('')
        return employee_dic
    else:
        print(value)
        print('')

#Displays all employees and their information
def display_all(employee_dic):
    for val in employee_dic:
        print(f'ID: {val}')
        value = employee_dic.get(val)
        print(f'Department: {value.get_department()}')
        print(f'Job Title: {value.get_jobtitle()}')
        print(f'Full-time: {value.get_fulltime()}\n')

main()