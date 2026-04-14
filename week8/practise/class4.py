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
    
    @staticmethod #this method does not receive the instance or the class as the first argument, 
                    #it is just a regular function that happens to be in the class
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6: #if the day is Saturday or Sunday
            return False
        return True
    

emp_1 = Employee("John", "Doe", 50000)
emp_2 = Employee("Jane", "Smith", 60000)
emp_3 = Employee("Joe", "Danials", 121000)


import datetime
my_date = datetime.date(2024, 3, 10) #this is a Monday
print("Is {} a workday? {}".format(my_date, Employee.is_workday(my_date))) #this will return True because it is a Monday

