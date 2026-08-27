# dictionary=[
#     {
#         "name"="raghu",
#         "age"=20,

#     },
#     {
        
#     }
# ]
# def raghu():
#     a="ktm"
#     b="r15"
#     def p():
#         b="knowledge"
#         def k():
#             nonlocal b
#             b="this nested fuction"
#         k()
#     p()
#     print(b)
# raghu()

def name(**num):
    for i in num.items():
        a,b=i
        print(f"{a}:{b}")
name(kj="th",jk="jj",hh="ll")

def name(**num):
    for i in num.items():
     c,d=i
     print(f"{c}:{d}")
name(a=10,b=20,k=70)

# lambdaclass=lambda a :a*a
# print(lambdaclass(5))

#add set
# set={"apple","banana","mango"}
# set.add("orange")
# print(set)

#clear set
# set={1,2,3,4}
# set.clear()
# print(set)

#update set
# set={3,4,5}
# set.update([11])
# print(set)

#dicard set
# set={5,4,2,4,6}
# set.discard(4)
# print(set)

#remove set
# set={2,3,4,1}
# set.remove(8)
# print(set)

# pop set
# set={"apple","orange","banana"}
# set.pop()
# print(set)

# copy set
# set={"aa","cc","hh"}
# a=set.copy()
# print(a)

# intersection
# a={1,2,3,4,5}
# b={1,2,3,9}
# c={2,5,7}
# d={3,2,5,8}
# print(a.intersection(b,c,d))

#intersection update
# a={"apple","guava","mango"}
# b={"grapes","orange","guava"}
# a.intersection_update(b)
# print(a)

# a={"apple","guava","mango"}
# b={"grapes","orange","guava"}
# print(a.intersection(b))

# mySet = { 1,2,3,4,5,6,7,8,9,10,5}
# print(type(mySet))
# print(mySet)

# unordered, unidexed, does not allow duplicates,mutable
# set1 = {"aaa","bbb","ccc","ddd"}
# print(set1)
# print(len(set1))

# for i in set1:
#     print(i)

# a={1,2,3,4}
# b={2,6,4}
# b.intersection_update(a)
# print(b)

# # difference
# a = {1,2,3,4}
# b = {3,4,5,6}

# a.symmetric_difference_update(b)
# print(a)

#isdisjoint

# a = {1,2,3}
# b = {5,4,6}

# print(a.isdisjoint(b))


# #issubset
# #true statement
# a = {1,2,3}
# b = {1,2,3,4,5}

# print(a.issubset(b))
#  #false statement
# c = {1,2,3}
# d = {2,3,4,5}
# print(c.issubset(d))


#issuperset

# a = {1,2,3,4,}
# b = {1,5}

# print(a.issuperset(b))