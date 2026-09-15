#1
# try:
#     a=10
#     b=0
#     print(a/b)
# except ZeroDivisionError:
#     print("cannot divisible by zero")
# else:
#     print("divisible by zero")
# finally:
#     print("invalid intiger input")

#2
# try:
#     b=int("abc")
#     print(b)
# except ValueError:
#     print("please enter a valid intiger")
# else:
#     print("valid intiger")
# finally:
#     print("final block")

#3
# try:
#     a=int(input())
#     b=int(input())
#     result=a/b
#     print(result)
# except ZeroDivisionError:
#     print("cannot divisible by zero")
# except ValueError:
#     print("invalid error")
# else:
#     print("else part")
# finally:
#     print("finall block")

#4
# list1=[10,20,30,40,50]
# try:
#     index=int(input())
#     print(list1[index])
# except IndexError:
#     print("index out of range")

#5
# stud={
#     "alice":85,
#     "bob":90,
#     "john":78}
# try:
#     a=str(input())
#     print(stud[a])
# except KeyError:
#     print("student not found")

#6
# try:
#     filename=input()
#     a=open("newtitle.txt","r")
#     print(a.read())
# except FileNotFoundError:
#     print("file not found")
# else:
#     print("file opened")
# finally:
#     print("final block")

#7
# try:
#     a=int(input())
#     b=int(input())
#     result=a/b
#     print(result)
# except ZeroDivisionError:
#     print("cannot zero divisible error")
# finally:
#     print("program executed complete")

#8
# try:
#     a=int(input())
# except ValueError:
#     print("value error")
# else:
#     print("square",a**2)

#9
# try:
#     a=float(input("enter a number"))
#     operator=input()
#     b=float(input("enter a number"))
#     if operator=="+":
#         result=a+b
#     elif operator=="-":
#         result=a-b
#     elif operator=="*":
#         result=a*b
#     elif operator=="/":
#         result=a/b
#     else:
#         print("invalid operator")
#     print("result",result)
# except ValueError:
#     print("invalid input")
# except ZeroDivisionError:
#     print("cannot divisible by zero")

#10
# def checkage(age):
#     if age<0:
#         raise ValueError("age cannot ")
#         return age
# try:
#     age=int(input())
#     checkage(age)
#     print("valid age=",age)
# except ValueError:
#     print("age cannot be negative")
    
#11
# try:
#     mark=int(input())
#     if mark<0 or mark>100:
#         raise ValueError("Marks must be between 0 and 100")
#     print("mark is",mark)
# except ValueError:
#     print("error")

#12
# class insuffientbalanceerror(Exception):
#     pass
# try:
#     money=int(input())
#     if money>5000:
#         raise insuffientbalanceerror("insufficientbankbalance")
#     print("money is",money)
# except insuffientbalanceerror as e:
#     print(e)

#13
# try:
#      money=int(input())
#      if money<0:
#          raise ValueError("Withdrawal amount must be positive.")
#      print("money is",money)
# except ValueError as e:
#      print(e)

#14
# student={"Alice": 85, "Bob": 90, "John": 75}
# for i in range(3):
#     name=input()
#     try:
#         print(f"{name} mark",student[name])
#     except KeyError:
#         print(f"error:{name}not found")

#15
# while True:
#     a=(input())
#     try:
#         b=int(a)
#         if a==0:
#             print("stop")
#             break
#         print(a,"accepted")
#     except ValueError:
#         print("error:invalid input")

#16
