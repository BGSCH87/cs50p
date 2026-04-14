class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1  # we kunnen de class variable num_of_emps verhogen met 1 elke keer dat er een nieuw object/instance van de Employee class wordt gemaakt   

    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    



emp_1 = Employee("John", "Doe", 50000)
emp_2 = Employee("Jane", "Smith", 60000)
emp_3 = Employee("Joe", "Danials", 121000)


print(Employee.num_of_emps)  # we kunnen de class variable num_of_emps aanroepen op de klasse Employee

# emp_1.raise_amount = 1.05  # we kunnen de class variable raise_amount overschrijven voor het object emp_1
# Employee.raise_amount = 1.06  # we kunnen de class variable raise_amount overschrijven voor de klasse Employee
# print(emp_1.__dict__)  # we kunnen de __dict__ attribute van het object emp_1 aanroepen om te zien welke instance variables er zijn 
# print(Employee.__dict__)  # we kunnen de __dict__ attribute van de klasse Employee aanroepen om te zien welke class variables er zijn   
# print(emp_1.raise_amount)  # we kunnen de class variable raise_amount aanroepen op het object emp_1
# print(Employee.raise_amount)  # we kunnen de class variable raise_amount aanroepen op de klasse Employee
# print(emp_1.__dict__)  # we kunnen de __dict__ attribute van het object emp_1 aanroepen om te zien welke instance variables er zijn
# print(Employee.__dict__)  # we kunnen de __dict__ attribute van de klasse Employee aanroepen om te zien welke class variables er zijn