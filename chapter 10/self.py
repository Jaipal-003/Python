class Employee:
     company ="Google"
     salary = 100
     def getSalary(self):
          print(f"Salary for this employee working in {self.company} is {self.salary}")
harry =Employee()
jason =Employee()

harry.salary = 100000

harry.getSalary() #  == Employee.getSalary(harry)   
jason.getSalary()
