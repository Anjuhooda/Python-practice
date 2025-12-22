# # # operators
# # # arthemetic operator
# # a=4
# # b=4
# # print((a+b),(a-b))

# # # comparsion operator
# # a=5
# # b=8
# # print(a>b   ,  a<b  , a==b  ,a>=b  ,a<=b)

# # # assignment operator
# # a=2
# # a+=3
# # print(a)

# # # logical operator
# # a=4
# # c=5
# # print(a>c and a<c)
# # print(a>c or a<c )
# # print(not(a>c))

# # # membership operator
# # a="name"
# # print("a" in "name")
# # print("t"  not in"name")

# # # string method
# # # lower
# # a="sehrawat"
# # b=a.lower()
# # print(b)
    
# # #  upper
# # a="annu"
# # c=a.upper()
# # print(c)

# # # is lower
# # a="SEHRAWAT"
# # b=a.islower()
# # print(b)

# # # is upper
# # d="name"
# # f=d.isupper()
# # print(f)

# # # startswith
# # a="name"
# # d=a.startswith("name")
# # print(d)

# # # split
# # a="annu,tanu,"
# # print(a.split())

# # # slicing
# # a="universe"
# # print(a[-3:])

# # # formatting
# # name="annu"
# # city="jind"
# # print(f"my name is {name} , & im from {city}")

# # # list method
# # # append
# # a=[1,2,3]
# # b=[5,6,7]
# # a.append(b)
# # print(a)

# # # pop
# # a=[10,20,30]
# # a.pop()
# # print(a)

# # # extend
# # a=[1,2,3,4]
# # b=[6,7,8]
# # a.extend(b)
# # print(a)

# # # clear
# # d=[10,20,30]
# # d.clear()
# # print(d)


# # # copy
# # list1=[1,2,34,"annu"]
# # list2=list1.copy()
# # print(list1)
# # print(list2)

# # # reverse
# # a=[1,2,3,4]
# # a.reverse()
# # print(a)

# # # remove
# # a=[40,50,60]
# # a.remove(40)
# # print(a)

# # # sort
# # a=[9,8,7,6,5,4,3,2,1]
# # a.sort()
# # print(a)

# # # insert
# # a=[1,2,3,"narwal"]
# # a.insert(1,45)
# # print(a)

# # # index
# # a=["apple","tuple","set"]
# # print(a.index("tuple"))
# # print(a)

# # # length
# # name="annusehrawat"
# # print(len(name))

# # # join
# # a=["name","annu"]
# # n="  ".join(a)
# # print(n)


# # # dict
# my_dict={
#     "name":"annu","age":18,"city":"jind"
# }
# print(my_dict)
# print(my_dict.values())
# print(my_dict.keys())
# a=my_dict.get("name")
# print(a)

# my_dict.update({"surname" :"sehrawat"})
# print(my_dict)

# my_dict.popitem()
# print(my_dict)

# my_dict.pop("age")
# print(my_dict)




# tuple
a=(1,2,3,"annu")
print(a)
print(a.count(3))
print(a.index("annu"))

# set
a={1,1,1,2,3,4}
print(a)

# typecating
a=145
b=float(a)
print(b)
print(type(b))

a=-12
if(a>13):
    print("true")
else:
    print("false")

numbers = [3, -5, 0, 7, -2]

if ("n" in numbers):
        print( "is positive")
    
else:
        print( "is zero")