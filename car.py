class Car:
    def __init__(self,name, fuelRate, velocity):
        self.name=name
        self.fuelRate=fuelRate
        self.velocity=velocity
        print("car constuctor")
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,n):
        if isinstance(n,str):
            self.__name=n
        else:
            raise Exception("the name of care must be string")
    @property
    def fuelRate(self):
        return self.__fuelRate
    @fuelRate.setter
    def fuelRate(self,fR):
        if isinstance(fR,int) or isinstance(fR,float) and 0<=fR<=100:
            self.__fuelRate=fR
        else:
            raise Exception("the fuleRate must be in ot float and betwen 0 and 100")
    @property
    def velocity(self):
        return self.__velocity
    @velocity.setter
    def velocity(self,v):
        if isinstance(v,int) or isinstance(v,float) and 0<=v<=200:
            self.__velocity=v
        else:
            raise Exception("the velocity must be in ot float and betwen 0 and 200")



    def run(self,v,d):
        self.__velocity=v
        self.__fuelRate-=(.1*d)/10
        if self.__fuelrate <= 0 or d == 0:
            self.stop(d)
    def stop(self,d):
        self.__velocity = 0
        if d== 0:
            print("you arrived to destination")
        else:
            print(f"remain distance to destination : {d}")
