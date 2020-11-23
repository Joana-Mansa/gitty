# Object Oriented Programming
class Employee:

    raise_amount= 1.04
    
    def __init__ (self,first,last,pay):
        self.first= first
        self.last= last
        self.pay= pay
        self.email= first + "." + last+"@company.com"
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int( self.pay * self.raise_amount )

emp_1 = Employee("Joana", "Owusu-Appiah", 20000)
emp_2 = Employee("Bernard","Owusu-Appiah", 40000)

print(emp_1.__dict__)

print(emp_1.pay)
print(emp_1.apply_raise())

