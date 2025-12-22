
# # # variable & data types
# # a_=12


# # # data type
# # a=14 #integar
# # b="hjdfuioefiuefvreu7yg1236189743875^&$&^%*^*&" #string
# # c=89.09  #float
# # true/false  #boolean

# # operators  -----6
# #1 # arthethmetic op.
# # # +,-,*,%,/
# # a=1
# # b=2
# # print(a+b)

# # 2 assignment op.
# # # =,+=,-=,/=
# # a=12
# # b = a+8
# # print(b)


# # comparsion op.  ==,f
# # a=12
# # b=13
# # print(a>b)

# # a=19+5
# # print(a)

# # asdwsgdrjncfgjmfy uikfyuh aezr gaersdewq`1  `


# # for i in range(2,11):
# #     if i%2==0:
# #         print(i,'even',end=" ,")
# #     else:
# #         print(i,'odd',end= ", ")   


# # for i in range(1,51):
# #     if i %3==0:
# #         print(i,'divided by 3')
# #     else:
# #         print(i,'no')    


# # a=int(input('enter   '))
# # fact=1
# # for i in range(1,a+1):
# #     fact*=i
# # print(fact)


# # def fun(a):
# #     if a==a[::-1]:
# #         print("palin")
# #     else:
# #         print('no')

# # fun("turtle")


# # list1=[1,2,3,4]
# # list2=[4,5,6]
# # d=list1.remove[0]
# # print(d)

# # is_prime
# # for a in range(2, 11):
# #     is_prime = True
# #     for i in range(2, a):
# #         if a % i == 0:
# #             is_prime = False
# #             break
# #     if is_prime:
# #         print(a, end=" ")



# # a="python"
# # b=""
# # for i in range(len(a)-1,-1,-1):
# #     b+=a[i]

# # print(b)


# # # Create a class called Student with marks and name, and method to display result.
# # class Student:
# #     def __init__(self,name,grade):
# #         self.name=name
# #         self.grade=grade
# #     def show_details(self):
# #         print(f"{self.name},{self.grade}")

# # a=Student("annu",98) 
# # a.show_details()           
        


# # logical operator
# # and,or,not
# # a=True
# # print(not(a))

# # memberahip ope
# # typecasting
# # a=False
# # print(type(a))

# # a=int(input("enter..."))
# # string fun.
# # upper,lower,replace,isupper,islower,startswith,split,slicing,formatting
# # a='KHGDKFHGBFHGUFG'
# # # print(a.lower())
# # a="text"
# # print(a.replace("text"," test is coming bebo548465458485584"))
# # a="FGKJUOIGVFHBVGBG "
# # print(a.islower())
# # a="jhfvbgduyfgrf"
# # print(a.startswith("jhfvb"))

# # a="annu sehrawat"
# # print(a.split(","))
# # name="annujhgfh"
# # print(len(name))
# # print(name[0:-3])

# # a="annu"
# # b=19
# # print(f'my name is{a} and im {b} years old...')


# # a=[1,2,3,3,4,5,6,6,7,78]
# # total=0
# # for i in a:
# #     total+=i
# # print(total)

# # a=["a",'e',"i","o","u"]
# # f=[]
# # for i in a:
# #     if i in "aeiou":
# #         f.append(i)
# # print(f)

# # a="olleh unna"
# # r=""
# # for i in range(len(a)-1,-1,-1):
# #     r+=a[i]
# # print(r)

# # class Car:
# #     def __init__(self, brand):
# #         self.__brand = brand  # private variable

# #     @property
# #     def brand(self):         # getter
# #         return self.__brand

# #     @brand.setter
# #     def brand(self, new_brand):   # setter
# #         self.__brand = new_brand

# # # Use
# # c = Car("Toyota")
# # print(c.brand)      # Access via getter

# # c.brand = "Honda"   # Update via setter
# # print(c.brand)      # Updated brand


# # class Animal:
# #     def set_name(self, name):
# #         self.name = name

# #     def speak(self):
# #         print(self.name + " is making a sound")

# # # Child class
# # class Dog(Animal):
# #     def bark(self):
# #         print(self.name + " is barking")

# # # Use
# # d = Dog()
# # d.set_name("Bullu")   # Method from parent
# # d.speak()             # Method from parent
# # d.bark()              # Own method


# class Bird:
#     def sound(self):
#         print("Bird is making sound")

# class Parrot(Bird):
#     def sound(self):  # same method name, different behavior
#         print("Parrot says: Mitthu Mitthu")

# class Crow(Bird):
#     def sound(self):
#         print("Crow says: Kaaw Kaaw")

# # Use
# # for bird in (Parrot(), Crow(), Bird()):
# #     # bird.sound()

# s = "hello"
# rev = ""
# for i in s:
    # rev = i + rev
# print(rev)


# list&types
# # methods
# # append
# a=[1,2,3,4,5,6]
# a.append('hwfuyfdbhdfhderi')
# print(a)
# pop
# a=[1,2,3,4,5,5,6,67,465568678]
# a.pop()
# print(a)
# # remove
# a=[1,2,3,4,"helo"]
# a.remove(3)
# print(a)
# # revrse
# a=[1,2,3,43,5,6,8,8]
# a.reverse()
# print(a )
# SORT
# a=[3435,3535,1,3,5,7,56,346,54575678,756767978568767]
# a.sort()
# print(a)
# insert
# a=[1,2,3,4,5,6,7,8]
# a.insert(2,3)
# print(a)
# index
# a=[1,2,3,4,5,6,7]
# a.index(6)
# print(a)
