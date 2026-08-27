from functools import reduce
#map
# a=[1,2,3,4]
# def add(x):
#     return x+x
# k=map(add,a)
# print(list(k))

#map using lambda
# a=[1,2,3,4]
# b=map(lambda x: x+x,a)
# print(list(b))

#filter
# a=[1,2,3,4]
# def add(x):
#         return x%2==1
# k=filter(add,a)
# print(list(k))

#1
# a=[1,2,3,4,5]
# answer=map(lambda x: x*2,a)
# print(list(answer))

#2
# a=[2,3,4,5]
# num=map(lambda x:x*x ,a)
# print(list(num))

#3
# a=["10","20","30","40"]
# num=map(int,a)
# print(list(num))

#4
# name=["john","alice","bob"]
# num=map(str.upper,name)
# print(list(num))

#5
# name=["apple","banana","kiwi"]
# num=map(len,name)
# print(list(num))

#6
# a=[1,2,3,4,5,6]
# num=filter(lambda x: x % 2==0,a)
# print(list(num))

#7
# a=[1,2,3,4,5,6]
# num=filter(lambda x: x % 2!=0,a)
# print(list(num))

#8
# a=[-5,-2,0,3,8]
# num=filter(lambda x: x>0,a)
# print(list(num))

#9
# words = ["cat", "elephant", "dog", "tiger"]
# answer = list(filter(lambda x: len(x) > 4, words))
# print(answer)

#10
# text="programming"
# a=filter(lambda x: x in "aeiou",text)
# print(list(a))

#11
# a=[1,2,3,4,5]
# num=reduce(lambda acc,curr:acc+curr,a)
# print(num)

#12
# a=[1,2,3,4]
# num=reduce(lambda acc,curr:acc*curr,a)
# print(num)

#13
# a=[4,10,7,25,3]
# num=reduce(lambda x,y:x if x>y else y,a )
# print(num)

#14
# a=[4,10,7,25,3]
# num=reduce(lambda x,y:x if x < y else y,a)
# print(num)

#15
# a=["python","is","awesome"]
# num=reduce(lambda x,y:x+" "+y,a)
# print(num)

#16
# a=[1,2,3,4,5,6]
# num=filter(lambda x: x%2==0,a)
# result=map(lambda x: x**2,num)
# print(list(result))

#17
# a=[1,2,3,4,5,6]
# num=filter(lambda s:s%2==0,a)
# result=reduce(lambda x,y: x+y,num)
# print(result)

#18
# words = ["cat", "apple", "dog", "banana"]
# long_words = filter(lambda word: len(word) > 3, words)
# result = len(list(long_words))
# print(result)

#19
# a=[1,2,3,4,5]
# num=filter(lambda x: x%2!=0,a)
# kum=map(lambda x: x**2,num)
# jum=reduce(lambda x,y: x+y,kum)
# print(jum)

#20
# a=[1,2,3,4,5,6]
# m=filter(lambda x: x%2==0,a)
# n=map(lambda x:x**3,m)
# k=reduce(lambda x,y: x+y,n)
# print(k)