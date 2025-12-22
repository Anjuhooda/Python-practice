
# a="annu"
# age=19
# print(f"hello {a} you are {age} year old")

# odd,even
# a=int(input("enter you num.:"))
# if a%2==0:
#     print(f"{a} is even num. ")
# else:
#     print(f"{a} is odd num")    

# greatest num
# a=int(input("enter you num. `1:"))
# b=int(input("enter you num. 2:"))
# c=int(input("enter you num.3:"))
# if a>b and a>c:
#     print("a si gret. num")
# elif b>c:
#     print("b  is gret. num")
# else:
#     print("c is gret. num")    

# leap year
# year=int(input("enter your year.:"))
# if year%400==0:
#     print(f"{year} is an leap year")
# else:
#     print(f"{year} is not an leap year"  )    


# counting 1 to ten
# for i in range(1,11):
#     print(i)

# table 2 to 20
# for i in range(1,11):
#     print(f"2 * {i}",("="),i*2)


# factorial
# a=int(input("enter you num.:"))
# fact=1
# for i in range(1,a+1):
#     fact*=i
#     print("factorial=",fact)


# palindrome
# a=input("enter your name:")
# if a==a[::-1]:
#     print(f"{a} is an pailndrome")
# else:
#     print(f"{a} is  not an pailndrome")
   

# 1to 100 count.
# for i in range(1,101,2):
#     print(i,end=" ")


#  sum of digit
# a=input("enter your name:")
# total=0
# for ch in a:
#     total += int (ch)

# print(total)


# even/odd by function
# a=input("enter your name:")

# def greet(a):
#     if a%2==0:
#         print("even num")
#     else:
#         print('odd')    
    

# a=greet(4)


# factorial
# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     return fact
    
# print("factorial=",fact(5))   

# pailndrome cehck
# def fun(a):
#     if a==a[::-1]:
#         print("palin")
#     else:
#         print('no')
# fun('anu')            


# . Fibonacci Series
# def  Fibonacci_Series(t):
#     a=0
#     b=1
#     for i in range(t):
#         print(a, end=" ")
#         a,b=b,a+b
# (Fibonacci_Series(5))    


# for  i in range(2,22,2):
#     print(i,end=" ")
    
# n=4
# for i in range(n):
#     print( "*" *(n-i))      # pattern print krta h


# for num in range(2, 101):          # 2…100
#     is_prime = True                # मान लेते हैं prime है
#     for i in range(2, num):        # 2…num‑1 तक divide करके देखते हैं
#         if num % i == 0:           # अगर पूरा divide हो गया
#             is_prime = False       # prime नहीं है
#             break                  # आगे देखने की ज़रूरत नहीं
#     if is_prime:
#         print(num, end=" ")


# p=[1,2,3,4,5,6,7,8,8,54,3,3,22,4,5,46]
# for i in p:
#     if i % 2 ==0:
#         print("even num",i,",",end=" ")
#     else:
#         print("odd num",i,",",end=" ")

 

# class Company:
#     def __init__(self,price,details):
#         self.price=price
#         self.details=details
#     def show(self):
#         print(self.price) 
#         print(self.details)


# a=Company(4000,"abc,near jind")
# a.show()    

# class Student:
#     def __init__(self,name,grade ,marks):
#         self.name=name
#         self.grade=grade # attributes
#         self.marks=marks
#     def show_details(self):
#         print(f"{self.name} is in {self.grade} and got {self.marks}.")
#     def grade_check(self):
#         if self.marks>=90:
#             print("a grade")
#         else:
#             print("b grade")        

# a1=Student("annu sehrawat","BCA 1st year ", 90)        
# a2=Student("tanu sehoran","ilets ", 90)  
# print(a1.__dict__) 
# # a1.show_details()
# print(a2.__dict__)
# a1.grade_check()
# # a2.show_details()
# a2.grade_check()



# class Student:
#     def __init__(self,name,percentage):
#         self.name=name
#         self.percentage=percentage
#     def show_details(self):
#         print(f'{self.name} got {self.percentage+2}%')

# a1=Student("annu",90)     
# a2=Student("muskan",89)       
# a1.show_details()
# a2.show_details()


# # child class

# class AbcdStudent(Student):
#     def tree(self):
#        print( f"{self.name}, hello world")
    
# b6=AbcdStudent("muskan",9876)
# b6.show_details()   


# fibonacci series
# a=int(input("enter you num:"))
# b=0
# c=1
# def ang(a,b):
#     print(b,end=" ")
#     b,c=c,b+c

# # ang(1,2)
# # print(ang)


# import math
# a=15
# print(math.sqrt (a)) 

# # import math
# o=9
# print(math.factorial(o))

# import pandas as pd



# if 0.1+0.2==0.3:
#        print("true")
# else:
#        print("false")\


# # # polymorphisum
# # class Bird:
# #     def sound(self):
# #         return "Birds make sounds"

# # class Sparrow(Bird):
# #     def sound(self):
# #         return "Chirp chirp"

# # class Crow(Bird):
# #     def sound(self):
# #         return "Caw caw"

# # def make_sound(bird):
# #     print(bird.sound())

# # a = Sparrow()
# b= Crow()


# make_sound(a)  
# make_sound(b)   


# a='universe'
# p=a[-7:]
# print(p)

# a="annu"
# b=19
# print(f"my name is {a} & im {b} years old")


# # check is_prime
# prime=[]
# comp=[]
# for b in range(2,11):
#     is_prime=True
#     for i in range(2,b):
#         if b%i==0:
#             is_prime=False
#             break
        
#     if is_prime:
#             print(f"prime num{b}",end=",  " )
#     else:
#          print(f'comp{b}',end=" ")


# # remove duplicate
# a=[1,2,3,4,5,6,5,6,4,3,5]
# b=[]
# for i in a:
#       if i not in b:
#            b.append (i)
# print(b)
    

# def fun (a):
#       if a==a[::-1]:
#             print("pailn")
#       else:
#             print("no")    

# fun("mam")           
