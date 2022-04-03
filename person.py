class Person:
    def __init__(self,name,money,mood,healthRate):
        self.name=name
        self.money=money
        self.mood=mood
        self.healthRate=healthRate
        print("person constractor")
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        if isinstance(name,str):
            self.__name=name
        else:
            raise ValueError("the name must be string")

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        if isinstance(money, int) and money>= 0:
            self.__money = money
        else:
            raise Exception("Money must be an Integer >= 0")

    @property
    def mood(self):
        return self.__mood

    @mood.setter
    def mood(self, m):
        acceptedMoods = ("happy", "tired", "lazy")
        if isinstance(m, str):
            m = m.lower()
            if m in acceptedMoods:
                self.__mood = m
            else:
                raise Exception(f"Undefined mood, mood must be one of {acceptedMoods}")
        else:
            raise Exception("Mood must be a String")

    @property
    def healthRate(self):
        return self.__healthRate

    @healthRate.setter
    def healthRate(self, h):
        if isinstance(h, int):
            if h >= 0 and h <= 100:
                self.__healthRate= h
            else:
                raise Exception("Health Care must be between 0 and 100 ")
        else:
            raise Exception("Health Care must be an Integer")

    def sleep(self, hours:int):
        if (isinstance(hours, int) or isinstance(hours, float)) and hours >= 0:
            if hours == 7:
                self.mood = "happy"
            elif hours < 7:
                self.mood = "tired"
            else:
                self.mood = "lazy"
        else:
            raise Exception("Hours must be (int or Float) >= 0")

    def eat(self,mealsNum):
        if isinstance(mealsNum, int) and mealsNum>= 0:
            if mealsNum == 3:
                self.healthRate = 100
            elif mealsNum== 2:
                self.healthRate = 75
            elif mealsNum == 1:
                self.healthRate = 50

        else:
            raise Exception("meals must be (int) >= 0")

    def buy(self,itemNums):
        if isinstance(itemNums,int) and itemNums>=0:
            if itemNums*10<=self.money:
                self.money-=itemNums*10
            else:
                raise Exception("no enough money ")
        else:
            raise  ValueError("Items count must be a positive integer")


    
