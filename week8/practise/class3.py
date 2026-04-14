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

    #create a class method to set the raise amount
    @classmethod #now we receive the class as the first argument instead of the instance
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    @classmethod #this can be used as an alternative constructor to create an instance of the class from a string
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay) #we return an instance of the class created from the string

Employee.set_raise_amount(1.05) #we can call the class method without creating an instance of the class

emp_1 = Employee("John", "Doe", 50000)
emp_2 = Employee("Jane", "Smith", 60000)
emp_3 = Employee("Joe", "Danials", 121000)

print(Employee.raise_amount) #we can access the class variable raise_amount directly from the class
print(emp_1.raise_amount) #we can also access the class variable raise_amount from an instance of the class, but it will still refer to the class variable unless we have an instance variable with the same name

emp_str_1 = "John-Doe-50000"
emp_str_2 = "Jane-Smith-60000"
emp_str_3 = "Joe-Danials-121000"

new_emp_1 = Employee.from_string(emp_str_1) #we can create a new instance of the Employee class from a string using the class method from_string
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

#print all the new employees' full names and pay in a loop
for emp in [new_emp_1, new_emp_2, new_emp_3]:
    print(emp.fullname(), emp.pay)