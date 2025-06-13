from argparse import ArgumentError
import time
from functools import wraps

class RegistryClass(type):
    registry = {}

    def __new__(cls,name,base,fields): 
        created_class = super().__new__(cls,name,base,fields) #konstruktor klasy
        RegistryClass.registry[name] = created_class
        return created_class 
    
class C1(metaclass=RegistryClass):
    def __init__(self):
        self.name = "C1"

# def main():
#     c1 = C1()
#     print(RegistryClass.registry)



#zad 5 metaklasa z atrybutami

class NewClass(type):
    _allowed_args = ["first_name","last_name","email"]
    def __new__(cls,name,base,fields_dic):
            for key in NewClass._allowed_args:
                if key not in fields_dic:
                    raise ArgumentError(None,f"key{key} is not in the list of allowed args")
            return super().__new__(cls,name,base,fields_dic)
##zad6 
def measure_exec_time(func):
     def wrapper(*args,**kwargs):
          start_time = time.time()
          res = func(*args,**kwargs)
          print(f"time exec function = {time.time() - start_time}")
          return res
     return wrapper
     

def decorator(func):
        def wrapper(*args,**kwargs):
            print("before method execution")
            res = func(*args,**kwargs)
            print("after method execution")
            return res
        return wrapper

class Person(metaclass=NewClass):
    first_name = None
    last_name = None
    email = None

    @measure_exec_time
    def hello(self):
        for a in range(0,1000000):
             a+=1
        print("hello")   

#Napisz dekorator, który wyświetla napisy, jeżeli znajdą się w wywołaniu funkcji debug().

def debug_printer(func):
    @wraps(func) #pozwala zachowac dane funkcji na ktorej jest uzywany jak __name__, __doc__, __module__
    def wrapper(*args,**kwargs):
            if args or kwargs:
                for i, args in enumerate(args):
                   print(f"positional args [{i}] : {args}")
                for key, vaule in kwargs.items():
                     print(f"keyword args [{key}] : {vaule}")
            else:
                 print("no args")
            return func(*args,**kwargs)
    return wrapper

@debug_printer
def debug(*args,**kwargs):
     pass
#https://www.geeksforgeeks.org/python/decorators-in-python/
#inf przy odczycie i zapisie danych
class VerboseValue:
    def __init__(self,value):
          self.value = value
    @property
    def value(self):
         print("pobrano wartosc")
         return self.__value
    @value.setter
    def value(self,value):
         self.__value = value
         print(f"ustawiono wartosc na {value}")
#deskryptor to klasa co kortroluje dostaep do atrybutów obiektu
#implentuje metody __get__, __set__, __delete__
#dekorator modyfikuje funkcje 
#deskryptor modyfikuje dostep do pola a nie funkcji
class Money:
    def __init__(self):
        self.value = 0

    def __get__(self, instance, owner):
        # return self.value
        return round(self.value/100, 2)

    def __set__(self, instance, value):
        self.value = value*100

class Wallet():
    money = Money()
  
def main():
    #p1 = Person()
    #p1.hello()
    debug(abc="cba")
    x = VerboseValue(7)
    x.value = 32
    print(x.value)
    x.value += 1

    wallet = Wallet()
    wallet.money = 123
    print(wallet.money)


if __name__ == '__main__':
    main()