

class Person:
    # 모든 object에 대해 공유되는 class variable
    id = 0

    # init : contructor (초기화 함수)
    # self : reference to the current instance of class person (현재의 객체에 대해서..)
    # name : local 변수 of function __init__

    def __init__(self, name): # 현재 instance와 name을 인자로
       Person.id += 1 # class variable

       # 각 Instance에 대해 Unique한 instance variable
       self.name = name
       self.id   = Person.id


    def hello(self):
        print(f' hello, {self.name}!')

    def get_info(self):
        return self.id, self.name


# Inheritance
class Professor(Person):
    pass