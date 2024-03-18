    
class PrivilegeException(Exception):
    pass

class Person(object):
    def __init__(self, id: str | int, name: str, age: int):
        self.id = str(id)
        self.name = name
        self.age = age

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}"
    
class Staff(Person):
    
    def __init__(self, id: str | int, name: str, age: int, salary: float, position: str):
        super().__init__(id, name, age)
        self.salary = salary
        self.position = position

    def __str__(self):
        return f"Staff {super().__str__()}, Annual salary: ${self.salary}, Position: {self.position}"
    
    def get_salary(self):
        if self.position == "Manager":
            raise PrivilegeException("You lack privileges to see manager salaries.")
        else:
            print(f"This person's salary is ${self.salary}")
            return self.salary
    
class Customer(Person):

    def __init__(self, id: str | int, name: str, age: int, owing=0.0):
        super().__init__(id, name, age)
        self.owing = self.check_balance()
    
    def __str__(self):
        return f"Customer {super().__str__()}, Owes: ${self.owing}"
    
    def check_balance(self):
        return 0
