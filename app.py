class Employee:

    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def get_info(self):
        # Simply print the employee's information
        print(f"Name: {self.name}, ID: {self.id}, Salary: {self.salary}")

    def apply_raise(self, percent):
        # Apply the raise using the percentage passed as an argument
        raise_amount = self.salary * (percent / 100)
        self.salary += raise_amount
        print(f"Salary after {percent}% raise: {self.salary}")

    def __str__(self):
        # Return a string representation of the employee object
        return f"Employee [ID: {self.id}, Name: {self.name}, Salary: {self.salary}]"



employee1 = Employee("Charan", 1, 4000)
employee2 = Employee("Sriya", 2, 3500)


employee1.get_info()
employee2.get_info()

employee2.apply_raise(20)


print(employee1)
print(employee2)



