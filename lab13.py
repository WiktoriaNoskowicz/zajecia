class Account:
    arguments = ["email","code"]
    def __init__(self,login,password,**kwargs):
        self.login = login
        self.password = password

        for k,val in kwargs.items():
            if k in self.arguments:
                setattr(self,k,val) ##setattr(object, attribute, value) 
            else:
                raise Exception(f"{k} is not in the list of allowed arguments!")

    def __str__(self):
        res = f"login = {self.login}, password = {self.password} "
        for a in self.arguments:
            if hasattr(self,a):
                res+= f" {a}: {getattr(self,a)} " ##hasattr(object, attribute)
        return res 

class Student:
    def __init__(self,name,**kwargs):
        self.name = name
        for key,value in kwargs.items():
            setattr(self,key,value)
        
    def avg(self):
        res =0
        i = 0
        for key,value in self.__dict__.items():
            if key!="name":
                res+= value
                i+=1
        return res/i

##jesli zapisuje sie argumenty przez setattr to trafiaja do __dict__

def main():   
    ac = Account(231,"password123",email="example@gmail.com")
    print(ac)
    s = Student("Anna",chemistry=3,biology=2,math=3,physics=5)
    print(s.avg())

if __name__=='__main__':
    main()