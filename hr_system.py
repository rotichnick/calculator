class Class_Object_employee:
    #Emplpyee constructor
    def __init__(self, emp_id, name, position, department, salary):
        self.emp_id=emp_id
        self.name=name
        self.position=position
        self.department=department
        self.salary=salary
        #Methods
    def promote_employee(self,new_position):
        self.position=new_position
        print(f"Employee {self.name} has been promoted to position of {self.position}")

    def change_department(self,new_department):
        self.department=new_department
    def salary_raise(self,new_salary):
        self.salary=new_salary
    def emp_details(self):
        print(f"ID: {self.emp_id} \n  Name:  {self.name} \n Position: {self.position}\n Department: {self.department}\n Salary: {self.salary}")


class Class_Object_HRSystem:
    #Constructor
    def __init__(self):
        self.employees=[]
    #Methods
    def hire_employees(self, emp_id, name, position, department, salary):
        employee=Class_Object_employee(emp_id, name, position, department, salary)
        self.employees.append(employee)
    def fire_employee(self, emp_id):
        count=0
        for e in self.employees:
            if e.emp_id==emp_id:
                self.employees.remove(e)
                print(f"Employee with ID: {e.emp_id} has been removed!")
            count+=1
            if count==len(self.employees):
                print("Employee not found!")
            
            
    def list_employees(self):
        for emp in self.employees:
            print(f"Employee ID: {emp.emp_id}\n Name: {emp.name}\n Position: {emp.position}\n Department: {emp.department}\n Salary: {emp.salary}\n")

#Employee object
emp1=Class_Object_employee(90, "Jake", "Designer", "Art",43000)
emp1.change_department("Digital")

print(emp1.emp_details())

#New employee
new_employee=Class_Object_HRSystem()

#Menu
while True:
    
    choice=int(input(f"1: to hire employee \n 2: To fire employee \n 3: to List all employees \n 0: to exit program: "))
    if choice==1:
        e_id=input("Enter employee ID")
        name=input("Name: ")
        position=input("Position: ")
        department=input("Department: ")
        salary=input("Salary: ")
        new_employee.hire_employees(e_id, name, position, department, salary)
    elif choice==2:
        emp_id=input("Enter the employee ID of the worker to be fired: ")
        new_employee.fire_employee(emp_id)
    elif choice==3:
        new_employee.list_employees()
    elif choice==0:
        break


        