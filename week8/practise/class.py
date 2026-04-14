class Employee:

    def __init__(self, first, last, pay): #this is the constructor method that will be called when we create a new instance of the Employee class
        self.first = first #this is an instance variable that will be unique to each instance of the Employee class
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    
    def fullname(self): #this is a method that will return the full name of the employee
        return "{} {}".format(self.first, self.last)


emp_1 = Employee("John", "Doe", 50000)
emp_2 = Employee("Jane", "Smith", 60000)

Employee.fullname(emp_1)  # we kunnen de methode fullname aanroepen op het object emp_1
# of we kunnen de methode fullname aanroepen op de klasse Employee en het object emp_1 als argument meegeven
print(emp_1.fullname())  # we kunnen ook de methode fullname aanroepen op het object emp_1 zonder de klasse naam te gebruiken

