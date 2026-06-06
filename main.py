
# # name= input('magacaa sir: ')

# # print('magacaagu waa :'+ name)

# # name = 'mahamed'
# # print(name[0:5])

# # tiryooyin  dhaban 

# # num='123456789'
# # print(num[1::2])

# # name = input('name:')
# # age = input('age:')

# # print (f"your name {name} and your age {type(age)}")

# # NAME = 'ahmed'
# # print(NAME.replace("ahmed", "hasan"))


# # name= 'abdirahmaan'
# # print(len(name))

# # name= 'mahamed hasan abdi'
# # namelist= name.find()
# # print('your name is',namelist)

# # name =input('enter your name: ')
# # password= input('enter your password: ')
# # hiden_pass= '*' * len(password)
# # len_pass= len(password)
# # print(f'asc {name} your password {hiden_pass} {len(password)}')

# # x= 10
# # if x < 5:
# #     print('x is less than 5')

# # elif x == 5:
# #     print('x is 5')

# # else:
# #      print('x is greater than 5')

# # x = 11
# # if x % 2 == 0:
# #     print('the number is evven ')
# # else:
# #     print('the number is odd ')    

# # number= int(input('enter the number: ')) 
# # if number < 0:
# #     print(number, 'the number is negative')

# # elif number == 0:
# #     print('the number is zero')

# # else:
# #     print(number, 'the number is positive')    

# # x = 10
# # y = 6
# # z = 3

# # print(x > y and y > z)
# # print(x > y or y < z)
# # print(not (x>y))

# # if x == y:
# #     print('x is equal y')

# # elif x != y:
# #     print('x isnot equal y')

# # for i in range(1, 10):
# #     print(i)

# # name = 'mubarak'

# # for character in name:
# #     print(character)


# # fruits = ['banana', 'apple', 'orange']

# # print(fruits)
# # fruits.pop(cherry)
# # print(fruits)
# # for x in fruits:
# #     if x == 'banana':
# #         break
# #     print(x)


# # NESTED LOOP

# # adj = ["red", "big", "tasty"]
# # fruits = ["apple", "banana", "cherry"]

# # for x in adj:
# #     for y in fruits:
# #         print(x, y)

# # i = 1
# # while i <= 3:
# #     print(i)
# #     i +=1 


# # print('welcome to distance converter')

# # while True:
# #     choice = input('(MI) for miles, (KM) for killometers & (Q) for quit: ')
# #     if choice == 'q':
# #         break

# #     elif choice == 'mi':
# #         km = int(input('enter the killometrs: '))
# #         mi = km / 1.609
# #         print(f'{km} killometrs waxay udhiganttaa intaas oo  {mi} miles')

# #     elif choice == 'km':
# #         mi = int(input('enter the miles: '))    
# #         km = mi * 1.609
# #         print(f'{mi} miles is {km} killometrs: ')
# #     else:
# #         print('invalid distance')  
# # 
# #
# # my_list= [1,2,3,3,4, 'hello',[5,6,7,8,]]  
# # # my_list [-5] = 'wolrd'
# # my_list.append(100)
# # my_list.remove(100)
# # print(my_list)

# # matrix = [
# #     [1,2,3],
# #     [4,5,6],
# #     [7,8,9]
# # ]
# # print(matrix[1][5])

# # i = 1
# # while i <= 3:
# #     print('meow')
# #     i += 1

# # for i in range(3):
# #     print('meow')

# # for i in [0,1,2]:
# #     print('meow')

# # print('meow\n' * 3, end="")
# # while True:
# #     n = int(input('what is n? '))
# #     if n > 0:
# #         break

# # for _ in range(n):
# #     print("meow")   

# # def main():
# #     meow(3)

# # def meow(n):
# #     for _ in range(n):
# #         print('meow')    

# # main()

# # def main():
# #     number = get_number()
# #     meow(number)

# # def get_number():
# #     while True:
# #         n = int(input('what is n? '))
# #         if n > 0:
# #             break
# #     return n

# # def meow(n):
# #     for _ in range(n):
# #         print('meow')  

# # main()


# # for _ in student:
# #     print(_)

# # for student in student:
# #     print(student)
# # for i in range(len(student)):
# #     print(i + 1, student[i])

# # students = {'mahamed':'150', 'ahmed': 'xawaadle', 'ali': 'gedgoble'}
# # for student in students:
# #     print(student, students[student], sep=", ") 

# def main():
# #     print_column(3)

# # def print_column(height):
# #     # for _ in range(height):
# #     #     print('#')   
# #     print("#\n" * height, end='')

#     print_row(4)

# def print_row(width):
#     # for _ in range(width):
#         print('?' * width , end='')

# main() 

# def main():
#     print_square(3)

# def print_square(size):
#     # for i in range(size):
#     #     for j in range(size):
#     #        print('#', end='')
#     for i in range(size):
#         print("#" * size)    
   

# main()
# while True:
#    try:
#     x = int(input('what is x? '))
#    except ValueError:
#     print('x is not integer')
#    else:
#       break
# print(f"x is {x}")
       
# def get_details(**info):
#  for key , value in info.items():
#       print(f"{key}: {value}")      

# get_details(name="ahmed", age=25, city="hargeisa")


# x = 30
# def may_func():
#     global x
#     x = 20
#     print(x)
# may_func()
# print(x)   
# 
# def multiply(x, y):
#     return x * y
# result = multiply(4, 5)
# print(result)          
# result = lambda x,y: x*y
# print(result(4,5))

#  
# def calculate_bmi(weihgt, height):
#     bmi= weihgt/(height**2)
#     bmi = round(bmi, 1)
#     category = ""

#     if bmi < 18.5:
#         category= "underweight"
#     elif bmi >18.5 and bmi < 24.9:
#         category= "normalweight"
#     elif bmi > 25.0 and bmi < 29.9:
#         category = "overweihgt"
#     else:
#         category = "obase"
#     return bmi,category      
# weight = float(input("entr the weight in kg: "))        
# height = float(input("entr the height in meter: ")) 
# Result = calculate_bmi(weight,height)
# print(f"BMI: {Result[0]},category: {Result[1]}")

# import mymodule
# print(mymodule.message)
# greet= mymodule.greet("ahmed")
# print(greet)
# import math
# # print(math.sqrt(16))
# import sys
# print(sys.path)
# import random
# numbers = random.random()
# print(numbers)

# class User():
#     pass
# user_1 = User()
# user_1.firstname = "ahmed"
# user_1.lastname = "osman"
# print(f"{user_1.firstname} {user_1.lastname}")
# del user_1.firstname

# class User():
#     def __init__(self, fname, lname, password):
#         self.firstname = fname
#         self.lastname = lname
#         self.password = password
#         self.email = fname + lname +"@gmail.com"
#     def print_details(self): 
# #         print(f"{self.firstname} {self.lastname}{self}")   

# # user_1 = User("ahmed", "ali", "1223pass")
# # user_1.print_details()

# class Car():
#     def __init__(self, model, year, miles=0.0 ):
#         self.model = model
#         self.year = year
#         self.miles = miles
#     def increase_miles(self, miles):
#         self.miles += miles
#     def details(self):     
#         print(f"model: {self.model} year: {self.year} miles: {self.miles}")                

# car_1 = Car("tesla", 2025, 10)
# car_1.details()
# car_2 = Car("BMW", 2020, 20)
# car_2.details()
# car_1.increase_miles(40)
# car_2.increase_miles(44)
# car_2.details()
# car_1.details()
# class product:
#     taxt_rate = 0.08

#     def __init__(self, name, price, discount = 0):
#         self.name = name
#         self.price = price
#         self.discount = discount
#         self.finalprice = 0
#     def calculate_price(self):
#         discounted_price = self.price * (1 - self.discount)
#         total_price = discounted_price * (1 + product.taxt_rate)
#         self.finalprice = round(total_price, 2)
#     def summary(self):
#         print(f"{self.name}: original ${self.price}")
#         print(f"discount: {int(self.discount * 100)}%")    
#         print(f"final price: ${self.finalprice}")

# p1 = product("laptop", 1000, 0.1)
# p1.calculate_price()
# print(p1.summary())
# 
# 
# class BankAccount:
#     def __init__(self, accont_number, holder_name, balance = 0):
#         self.accont_number = accont_number
#         self.holder_name = holder_name
#         self.balance = balance
    
#     def deposit(self, amount):
#         if  amount > 0:
#             self.balance += amount
#             print(f"Deposited ${amount}. new balance ${self.balance}")
#         else:
#             print("deposit must be positive. ")    
            
#     def withdraw(self, amount):
#         if  0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"withdraw ${amount}. new balance ${self.balance}")
#         else:
#             print("insufficient funds invalid  withdraw amount.")    
#     def display_account(self):
#         print(f"Account number: {self.accont_number}")
#         print(f"Holder name: {self.holder_name}")
#         print(f"balance: {self.balance}")
#     @classmethod 
#     def set_interest_rate(cls, new_rate):
#         if 0 <= new_rate <= 1:
#             cls.interest_rate = new_rate
#             print(f"interest rate updated to {cls.interest_rate * 100}% for all accounts. ")   
#         else:
#             print("invalid interest rate")    
#     @staticmethod
#     def is_valid_accont_number(accont_number):
#         return len(accont_number) == 10 and accont_number.isdigit()   

# accounts1= BankAccount("1234556","ahmed ali", 1000)
# accounts2 = BankAccount("12345677","maryam ali", )
# # accounts1.deposit(400)
# # accounts1.withdraw(500)
# # accounts1.display_account()
# # BankAccount.set_interest_rate(0.20)

# print(BankAccount.is_valid_accont_number("123411567811"))

# class person():
     
#     def __init__(self,name, email,age, ):
        
#         self.name = name
#         self.age = age
#         self.email = email

#     def display_info(self):
#         print(f"name:{self.name}")
#         print(f"age:{self.age}")
#         print(f"email:{self.email}")



# class Student(person):

#     def __init__(self,name, email,age,subject ,studentId):
#         super().__init__(name, age, email)
#         self.subject = subject
#         self.studentId = studentId

#     def print_subject(self):
#         print(f"{self.name} is studying.")
#         for subject in self.subject:
#             print(subject) 

    
                   

# class Teacher(person):
#     def __init__(self, name, email, age, subject):
#         super().__init__(name, age, email)

#         # self.name = name
#         # self.age = age
#         self.subject = subject
#         # self.email = email

#     def teach(self):
#         print(f"{self.name} is teaching {self.subject}. ") 


# stud1 = Student("ahmed ali", 21, "ahmed@.com",['english','math'],'232')

# stud1.display_info()
# stud1.print_subject()

# teach1 = Teacher('ali ahmed',40, 'ali@gmail.com','math')
# teach1.display_info()
# teach1.teach()


# file = open('mymodule.py', 'r')
# # content = file.read()
# print(file.read())
# file.close()

# with open('mymodule.py','r') as file:
#     for line in file:
#         print(line, end=" ")

# with open("newfile.txt","a") as file:
#     file.write("wan ficanahay" +"\n")
#     file.write("alxamdulilah" +"\n")

while True:
    name = input('plesse enter the full name: ')

    if name.lower() == 'exit':
       
       break
    else:
      
      print(f"hello{name.title()}")

      with open("friends.txt", "a") as file:
         file.write(name.title() + "\n") 

print("the name are: ")   

with open("friends.txt", "r") as file:
   for line in file:
      print(line)