import json

from car import Car
from employee import Employee


class Office:
    employeesNum = 0

    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def officeData(self):

        with open("office_data.json", 'r+') as file:
            file_data = json.load(file)
            employeeList=[]
            for emp in self.__employees:
                empCar=vars(emp.car)
                e=vars(emp)
                e["_Employee__car"]=empCar
                print(e)
                employeeList.append(e)

            file_data["office_details"].append({
                    self.__name:employeeList
                    })
            file.seek(0)
            json.dump(file_data, file, indent=4)



    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise Exception("office name should be string")

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, emps):
        if isinstance(emps, list):
            for e in emps:
                if not isinstance(e, Employee):
                    print("must be list of employees  so employees will be none by default")
                    self.__employees = None
                    break

            self.__employees = emps

        else:
            print("must be list of employees  so employees will be empty list by default")
            self.__employees = []
    @classmethod
    def change_emps_num(cls,num):
        cls.employeesNum+=num

    def get_all_employees(self):
        return self.__employees

    def get_employee(self, empid):
        for e in self.__employees:
            if e.id == empid:
                return e
            else:
                return False

    def hire(self, emp):
        if isinstance(emp, Employee):
            self.__employees.append(emp)
            self.change_emps_num(1)
        else:
            raise Exception("you should hire instance of Employee Class")

    def fire(self, empId):
        index = 0
        for emp in self.__employees:
            index += 1
            if emp.id == empId:
                del self.__employees[index]
                self.change_emps_num(-1)
                break

    def deduct(self, empId, deduction):
        for e in self.__employees:
            if e.id == empId:
                e.salary -= deduction
            else:
                print(f"can't find this employee with id : {empId}")

    def reward(self,empId, reward):
        for e in self.__employees:
            if e.id == empId:
                e.salary += reward
            else:
                print(f"can't find this employee with id : {empId}")
    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        time = distance / velocity
        if moveHour + time < targetHour:
            return False
        else:
            return True

    def check_lateness(self, empId, moveHour):
        for emp in self.__employees:
            if emp.id == empId:
                if self.check_lateness(8, moveHour, emp.distance, emp.car.velocity):
                    emp.salary -= 10
                else:
                    emp.salary += 10

"""myCar = Car("fiat 128", 50, 50)
myCar2 = Car("nissan 8", 30, 10)



emp1 = Employee(1, myCar, "n@n.com", 3000, 20, "nora", 5000, "tired", 50)
emp2 = Employee(2, myCar2, "d@d.com", 4000, 60, "doaa", 6000, "happy", 50)
emp=[emp1,emp2]
o=Office("iti",emp)
o.officeData()"""