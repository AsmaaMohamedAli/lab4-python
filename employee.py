import re

from car import Car
from person import Person


class Employee(Person):

    def __init__(self, id, car, email, salary, distanceToWork, name, money, mood, healthRate):
        super(Employee, self).__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if isinstance(value, int) and value >= 1000:
            self.__salary = value
        else:
            raise Exception("salary must be int and >=1000")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        emailRegex = "^[a-zA-Z]([a-zA-Z0-9]|\.|_)*@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$"
        x = re.fullmatch(emailRegex, email)
        if x:
            self.__email = email
        else:
            raise Exception("invalid Email")

    @property
    def car(self):
        return self.__car

    @car.setter
    def car(self, car: Car):
        if isinstance(car, Car):
            self.__car = car
        else:
            raise Exception("car must be from Car Class")

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if isinstance(id, int) and id >= 0:
            self.__id = id
        else:
            raise Exception("id must be int and >=0")

    @property
    def distanceToWork(self):
        return self.__distanceToWork

    @distanceToWork.setter
    def distanceToWork(self, d):
        if isinstance(d, int) or isinstance(d, float) and d > 0:
            self.__distanceToWork = d
        else:
            raise Exception("the distance must be int or float and >0")

    def work(self, hours):
        if (isinstance(hours, int) or isinstance(hours, float)) and hours >= 0:
            if hours == 8:
                self.mood = "happy"
            elif hours < 8:
                self.mood = "lazy"
            else:
                self.mood = "tired"
        else:
            raise Exception("Hours must be (int or Float) >= 0")

    def drive(self,d,v):
        self.Car.run(d,v)

    def refuel(self,gasAmount = 100):
        self.Car.fuelRate+=gasAmount

    def send_mail(self, to, subject, msg, receiver_name):

        while True:
            emailRegex = "^[a-zA-Z]([a-zA-Z0-9]|\.|_)*@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$"
            x = re.fullmatch(emailRegex, to)
            if x:
                with open("email.txt", 'w', encoding='utf-8') as f:
                    f.write("From: from@gmail.com\n")
                    f.write(f"To: {to} \n")
                    f.write(f"Subject: {subject} \n\n")
                    f.write(f"Hi, {receiver_name}\n")
                    f.write(f"{msg} \n\n")

                break
            else:
                to=input("enter valid email")


