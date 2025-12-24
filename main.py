#### list type of data ####

# append #

# x=["apple","banana"]
# x.append("mango")
# print(x)

# # extend #

# x=["apple","banana"]
# y=["mango","orange"]
# x.extend(y)
# print(x)

# # pop #

# x=["apple","banana","mango"]
# x.pop()
# print(x)

# # insert #

# x=["apple","banana"]
# x.insert(1,"mango")
# print(x)

# # remove #

# x=["apple","banana"]
# x.remove("apple")
# print(x)

# # sort #

# x=[5,4,2,6]
# x.sort()
# print(x)

# # clear #

# x=["apple","banana","mango"]
# x.clear()
# print(x)

# # copy #

# x=["orange","pineapple"]
# y=x.copy()
# print(y)

# ## mutable ##

# x=["apple","banana","mango"]
# x[1]="cherry"
# print(x)

# ## immutable ##

# x="anju"
# x[0]="m"
# print(x)

# ### string method ###

# # upper karna #

# x="anju"
# print(x.upper())

# # lower karna #

# x="ANJU"
# print(x.lower())

# # replace karna #

# x="neelam rani"
# print(x.replace("neelam","neel"))

# # isupper karna #

# x="anju"
# print(x.isupper())

# # islower karna #

# x="ANJU"
# print(x.islower())

# # count karna #

# x="neelam"
# print(x.count("e"))

# ## slicing ##

# x="anju"
# print(x[0:2])

# #### operators ####

# ### airthmetic operator ###

# ## for number ##

# # addition #

# x=4
# y=5
# print(x+y)

# # subtract #

# x=9
# y=6
# print(x-y)

# # multiply #
# x=7
# y=6
# print(x*y)

# # divide #

# x=10
# y=2
# print(x/y)

# # percentage #

# x=20
# y=2
# print(x%y)

# ## for string ##

# # addition #

# x="anju"
# y="neelam"
# print(x+y)

# # subtract #

# x="anju"
# y="neelam"
# print(x-y)

# # multiply #

# x="anju"
# y="neelam"
# print(x*y)

# # divide #

# x="anju"
# y="neelam"
# print(x/y)

# # percentage #

# x="anju"
# y="neelam"
# print(x%y)

# ### assignment operators ###

# # simple assignment #

# x=10
# print(x)

# # add and assignment #

# x+=10
# print(x)

# # subtract and assignment #

# x-=10
# print(x)

# # multiply and asignment #

# x*=10
# print(x)

# # divide and assignment #

# x/=10
# print(x)

# # remainder and assignment #

# x%=10
# print(x)

# ### comparison operators ###

# # barabar hai (==) #

# x=5
# y=5
# print(x==y)

# x=5
# y=7
# print(x==y)

# # barabar nhi hai (!=) #

# x=5
# y=7
# print(x!=y)

# x=4
# y=4
# print(x!=y)

# # bada hai (>) #

# x=10
# y=8
# print(x>y)

# x=4
# y=6
# print(x>y)

# # chhota hai (<) #

# x=6
# y=4
# print(x<y)

# x=4
# y=6
# print(x<y)

# # bada ya barabar hai (>=) #

# x=4
# y=5
# print(x>=y)

# x=5
# y=4
# print(x>=y)

# # chhota ya barabar hai (<=) #

# x=8
# y=7
# print(x<=y)

# x=7
# y=8
# print(x<=y)

# ### logical operators ###

# # and [dono condintions true honi chaiye]

# x=5>2
# y=4<6
# print((x>y)and(x<=y))

# x=5>2
# y=4>6
# print((x<y)and(x<=y))

# # or [koi ek condition true ho]

# x=5>2
# y=4>6
# print((x>y)or(x>=y))

# x=3>4
# y=2>5
# print((x>y)or(x<y))




















# a=10
# b=20
# c=30
# d=40
# e=50
# if a>b and a>c and a>d and a>e:
#     print("a is greater")
# elif b>c and b>d and b>e:
#     print("b is greater")
# elif c>d and c>e:
#     print("c is greater")
# elif d>e:
#     print("d is greater")
# else:
    # print("e is greater")


















a=10
b=20
c=30
d=40
e=50
if a>b:
    if a>c:
        if a>d:
            if a>e:
                print("a is greater")
            else:
                print("e is greater")
        elif d>e:
            print("d is greater")
        else:
            print("e is greater")
    elif c>d:
        if c>e:
            print("c is greater")
        else:
            print("e is greater")
    else:
        if d>e:
            print("d is greater")
        else:
            print("e is greater")
elif b>c:
    if b>d:
        if b>e:
            print("b ig greater")
        else:
            print("e is greater")
    elif d>e:
        print("d is greater")
    else:
        print("e is greater")
elif c>d:
    if c>e:
        print("c is greater")
    else:
        print("e is greater")
elif d>e:
    print("d is greater")
else:
    print("e is greater")


a=20
b=30
c=40
d=50
e=60
f=70
if a>b:
    if a>c:
        if a>d:
            if a>e:
                if a>f:
                    print("a is greater")
                else:
                    print("e is greater")
            elif e>f:
                print("e is greater")
            else:
                print("f is greater")
        elif d>e:
            if d>f:
                print("d is greater")
            else:
                print("f is greater")
        else:
            if e>f:
                print("e is greater")
            else:
                print("f is greater")
    elif c>d:
        if c>e:
            if c>f:
                print("c is greater")
            else:
                print("f is greater")
        elif e>f:
            print("e is greater")
        else:
            print("f is greater")
elif b>c:
    if b>d:
        if b>e:
            if b>f:
                print("b is greater")
            else:
                print("f is greater")
        elif e>f:
            print("e is greater")
        else:
            print("f is greater")
    elif d>e:
        if d>f:
            print("d is greater")
        else:
            print("f is greater")
    else:
        if e>f:
            print("e is greater")
        else:
            print("f is greater")
elif c>d:
    if c>e:
        if c>f:
            print("c is greater")
        else:
            print("f is greater")
    elif e>f:
        print("e is greater")
    else:
        print("f is greater")
elif d>e:
    if d>f:
        print("d is greater")
    else:
        print("f is greater")
elif e>f:
    print("e is greater")
else:
    print("f is greater")

    

# a=10
# b=20
# c=30
# d=40
# e=50
# if a>b and a>c and a>d and a>e:
#     print("a is greater")
# elif b>c and b>d and b>e:
#     print("b is greater")
# elif c>d and c>e:
#     print("c is greater")
# elif d>e:
#     print("d is greater")
# else:
#     print("e is greater")





# def palindrome(n):
#     number_str=str(n)
#     return number_str==number_str[::-1]
# x="madam"
# if palindrome(x):
#     print(f"{x} is a palindrome")
# else:
#     print(f"{x} is not a palindrome")