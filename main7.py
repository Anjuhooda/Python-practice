# Q1 what is result

a = 5
b = 2
result = a / b
print(type(result))


# Q2: Use if-else to check whether a number is positive or negative.
x=5
x=-5

if (x >-5):
    print("x is greater than -5 ")
else:
    print("x is smaller than -5")   
    
#Q3 remove item with index
a=[1,2,3,4]
b=a.pop()
print(b)
# Q4: What is the output of the following?
x = "python"
print(x[1:4])


# Q5: What is the result of this operation?
a = "10"
b = 5
print(a * b)

# Q6: Which method is used to convert a string into a list of words?

text = "apple mango orange"
a=text.split()
print(a)

# Q7: What is the output of the following code?
x = [1, 2, 3]
x.insert(1, 100)
print(x)


#  Q8: Convert this string to integer and add 5
num = "15"
d=int(num)+5
print(d)

# Q9: Slice the last 3 characters from this string
name = "ComputerScience"
print(name[-3:])

# Q10: What will this code output?
a = True
b = False
print(a and b)

# Q11: How to check if a key "name" exists in a dictionary?
person = {"name": "John", "age": 25}
if "name" in person:
    print("name in person dict")
else:
    print("name not in person dict")    

# Q12: Print the length of this list
# x = [10, 20, 30, 40]
a=x.__len__()
print(a)
# Q13: What happens here?
a = [1, 2, 3]
b = a
b.append(4)
print(a)

# Q14: Use if-else to check if a string contains "@"
email = "test@gmail.com"
if( "@" in email):
    print("yes @ stands in email dict")
else:
    print("@ not stands in email dict")    

#  Q15: Replace "apple" with "banana"
x = "I like apple"
b=x.replace("apple","bannana")
print(b)
# Q16: Check if a number is divisible by 3
num = 9
if(9 % 3 ==0):
    print("yes,9 is totally divided by 3 ")
else:
    print("no,9 is not totally divided by 3")    


# Q17: What is the output of this code?
a = "python"
print(a[-1])

# Q18: Convert 3.14 into an integer.
pi = 3.15
a=(int(pi))
print(a)
print(type(a))

# Q19: Join list elements into a string separated by a dash
fruits = ["apple", "banana", "cherry"]
d="-".join(fruits)
print(d)          


# Q20: Replace the last element in the list with 100
a = [5, 10, 15]
c=a[-1]=100
print(a)

# Q21: Check if 4 is in the list
nums = [1, 2, 3, 4, 5]
if (4 in nums):
    print("yes,4 in nums dict")
else:
    print("no, 4 is not in nums dict")    

# Q22: Get the number of chararacter in the string
text = "OpenAI"
d=len(text)
print(d)
#  Q23: Use if-else to check if a number is zero
x = 0
if(5==0):
    print("the number is zero")
else:
    print("the number is not zero")    

#  Q24: What will this print?
print(type({}))

#  Q25: Print the keys from a dictionary
person = {"name": "Alice", "age": 22}
d=person.keys()
print(d)

# Q26: What is the result of this comparison?
print(10 != 5)