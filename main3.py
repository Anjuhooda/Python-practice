
# class Age:
#     def __init__(self):
#         print("hello ")

# s1=Age()

# class car:
#     def __init__(self,fullname,marks):
#        self.name=fullname
#        self.marks=marks
#        print("ammiu")

# s1=car('ammu',12)       
# print(s1.name)  #ammiu,ammu 12
# print(s1.marks)

# class Student:
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll

# a=Student("annu,sehrawat",18)
# print(a)        

# class Student:
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll

#     def display(self):
#         print("Name:", self.name)
#         print("Roll:", self.roll)

# s1 = Student("Annu", 101)
# s1.display()



# class Car:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print (f"my name is { self.name},i got { self.marks}")
    
# a=Car("annu",95)  
# # a.Car()



# #   encapsulation
# class Person:
#     def __init__(self,name,age):
#     self      

# a=123
# b="annu"
# c=[11,22]
# print(isinstance(a,int))


# class Person:
#     _name="annu"
#     def __init__(self):
#       print(self._name)
#       self._display()
#     def _display(self):
#         print("hiii")
# obj=Person()

# # setter
# class Pen:
#     def __init__(self,ink):
#         self._ink=ink

#     def show(self):
#            print(self._ink)

#     @property
#     def ink(self):
#         return 10* self._ink

#     @new_ink.setter
#     def ink (self,new_ink):
#         self._ink=new_ink

# a=Pen(12)      
# print(a.ink_setter)    
# a.ink=40
# a.ink





# Q1: Write a program to swap two numbers.

# Q2: Check the data type of multiple variables using type() function.
# a=[12,12,1,3]
# b=list(a)
# print((type(b)))

# ✅ 2. Input/Output & Typecasting
# Q3: Take name, age from user and print them.

# Q4: Take two numbers input from user and print their sum (use typecasting).
# a=int(input("enter 1"))
# b=int(input("enter"))
# print("the sum of a and b is =",a+b)
# ✅ 3. Conditional Statements (if, elif, else)
# a=12
# b=13
# c=15
# if a>b:
#     print("a")
# elif b>c:
#     print("b")
# else:
    # print("c")
# Q5: Check whether a number is even or odd.
# a=12
# if a%2==0:
#     print("eee")
# else:
#     print('odd')
# Q6: Find the greatest of 3 numbers.
# a=1
# b=3
# c=2
# if a>b:
#     print("a")
# elif b>c:
#     print('b')
# else:
#     print('c')


# Q7: Check if a number is divisible by both 3 and 5.
# a=10
# if a%3 and a%5:
#     print("yuhh")
# else:
#     print('nouh')
#  ✅ 4. Loops (for, while)
# Q8: Print all numbers from 1 to 100 using for loop.
# for i in range(1,101):
#     print(i,end=" ")

# Q9: Print table of a number (like 5 ka table).
# a=5
# for i in range(1,11):
#     print(i*a)

# Q10: Rei*verse a string using for loop.
# a="1,2,3,4,5"
# b=""
# for i in range(len(a)-1,-1,-1):
#             b+=a[i]
# print(b)

# Q11: Print Fibonacci series of first n numbers.///????//??

# Q12: Calculate the sum of digits of a number.
# num=1,2,3,4
# print(sum(num))
# ✅ 5. Strings
# Q13: Check whether a string is palindrome or not.

# Q14: Count vowels in a string.
# a="aeiou"
# if "a" in a:
#     print("vowel")
# else:
#     print('no')

# Q15: Remove spaces from a string.

# Q16: Convert string to uppercase without using .upper().
# a="fbtvh"
# print()
# ✅ 6. Lists
# Q17: Find the largest number in a list.
# numbers = [5, 9, 2, 88, 15, 34]

# largest = numbers[0]  

# for num in numbers:
#     if num > largest:
#         largest = num

# print("Largest number is:", largest)


# Q18: Remove duplicates from list.
# a=[1,2,3,23,2,32,3,3,3]
# b=[]
# for c in a:
#     if c not in b:
#         b.append(c)

# print(b)
# # Q19: Sort a list without using built-in functions.

# Q20: Count how many times each element occurs in a list.
# a=[1,2,3,3,3,44,5,6,3,3,3,3]
# print(a.count(3))

# ✅ 7. Functions
# Q21: Write a function to check if number is prime.

# Q22: Write a function to find factorial of number.

# Q23: Write a function that returns sum of even numbers in a list.

# ✅ 8. Dictionary
# Q24: Create a dictionary of student names and marks. Print all students with marks > 80.

# Q25: Count frequency of characters in a string using dictionary.

# ✅ 9. Sets
# Q26: Find common elements in two lists using set.

# Q27: Remove duplicates from list using set.


# a=1
# b=10

# for g in range(a,b+1):
#     if g %2==0:
#         print(f'{g}"yupp"')
#     else:
#         print("noo")


# a=[2,3,4,5,6,7,8,9]
# even=[]
# odd=[]
# for t in a:
#     if t%2==0:
#        even.append(t)
#     else:
#         odd.append(t)

# print(even)
# print(odd) 

# a = [1, 2, 3, 4, 54, 6, 7, 78, "annu", "sehrawat"]
# string = []
# inte = []

# for t in a:
#     if isinstance(t, str):
#         string.append(t)
#     elif isinstance(t, int):
#         inte.append(t)

# print("Strings:", string)
# print("Integers:", inte)

# prime = []
# comp = []

# for t in range(2, 11):
#     is_prime = True
#     for i in range(2, t):
#         if t % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         prime.append(t)
#     else:
#         comp.append(t)

# print("Prime numbers:", prime)
# print("Composite numbers:", comp)


# a = [1, 2, [3, 4], [5, 6], 7, [8, 9]]
# flat = []

# for item in a:
#     if isinstance(item, list):
#         for subitem in item:
#             flat.append(subitem)
#     else: 
#         flat.append(item)

# print("Flattened List:", flat)

# a="olleh"
# # b=""
# def fun(a):
#  b=""  
#  for i in range(len(a)-1,-1,-1):
#         b+=a[i]
#  print(b)
# fun("olleh")


# for a in range(2,11):
#   is_prime=True
#   for i in range(2,a):
#      if a%i==0:
#       is_prime=False
#       break
#   if is_prime:
#         print(a,"prime num",end=" ,")

# a=int(input("enter..."))
# if a%3 and a%5==0:
#     print("good")
# else:
#     print("httttt")  

# def fun(a):
#  if a==a[::-1]:
#     print('wow bebo')
#  else:
#     print('htt sale')

# fun("annu")    

# encapsulation
# class Person:
#     def __init__(self,name,qualification):
#         self.name=name
#         self.__qualification=qualification 

#     def show(self, new_term):   # setter
#         self.__qualification = new_term


#     def get_details(self):
#         print(f'{self.name} & their qualification{self.__qualification}')

# a1=Person("annu",'BCA topper')
# a1.get_details()        
# a1.name()


# class Person:
#     def __init__(self, name, qualification):
#         self.name = name
#         self.__qualification = qualification

#     @property
#     def qualification(self):         
#         return self.__qualification

#     @qualification.setter
#     def qualification(self, new_term):  
#         self.__qualification = new_term

#     def get_details(self):
#         print(f'{self.name} & their qualification: {self.__qualification}')



# a1 = Person("Annu", "BCA topper")
# print("Before update:", a1.qualification)  
# a1.qualification = "BCA Gold Medalist"     
# a1.get_details()



#  with return value
# def add(a, b):
#     result = a + b
#     return result

# sum_result = add(10, 5)
# print("Sum is:", sum_result)


# a=int(input('enter...'))
# fact=1
# for i in range(1,a+1):
#     fact*=i

# # print(fact)


# prime_list=[]
# for a in range(2,10):
#     is_prime=True
#     for i  in  range(2,a):
#         if a%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         prime_list.append(a)
# print(prime_list,end=" ",)
# import datetime

# current_time = datetime.datetime.now().time()
# print(current_time)

# # Q12. Encapsulation (private var)
# class Person:
#     def __init__(self, name):
#         self.__name = name  # private

#     def get_name(self):
#         return self.__name

#     def set_name(self, name):
#         self.__name = name

# p = Person("Annu")
# print(p.get_name())
# p.set_name("Pihu")
# print(p.get_name())

# class Mother:
#     def __init__(self,name):
#         self.name=name

#     def cook(self):
#         print("Cooking daal chawal...")

# class Daughter(Mother):
#     def __init__(self,grade):
#         self.grade=grade

#     def dance(self):
#         print("Dancing on stage...")

# # Object create
# d = Daughter("annu")
# d.cook()
# d=Daughter(89)
# d.dance()

# enheritance,polymorphisum,encapsulation,abstraction

# is_prime1=[]
# for a in range(2,50):
#     is_prime=True
#     for i in range(2,a):
#         if a%i==0:
#          is_prime=False
#          break
#     if is_prime:
#         is_prime1.append(a)

#         print(a,end=" ")           


# a=int(input('enter....'))
# for i in range(1,11):
#     print(f'{a}*{i} = {a*i}')


# a=[1,2,3,2,3,23,3]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

# a=[12,2,343,45,5,756,86798574521441251652185686,7]
# c=a[0]
# for i in a:
#     if i>c:
#       c=i
# print('largest..:',c)    
# 
#     
# sublist=[]
# a=[12,12,[12,1],[12,12]]
# falt=[]
# for sublist in  a:
#     for i in sublist:
#       falt.append(i)
# print(falt)        

# n=10
# a=0
# b=1
# for i in range(n):
#     print  (a,end=" ")
#     a,b=b,a+b

# for i in range(1,6):
#     print("*"*i)


# a=int(input('enter..'))
# f=1
# for i in range(1,a+1):
#     f *=i
# print(f)    

# a=int(input('enter..'))
# fact=1
# for i in range(1,a+1):
#     fact *=i
# print(fact)    

# a=50
# if a%2==0:
#     for i in range(1,11):
#         print(a*i)
# else:
#    for i in range(1,0,-1):
#         print(a*i)
   

