# 1
# a=[1,2,3,4,]
# b=[1,2,5]
# print(set(a).intersection(set(b)))

#5
# a={1,2,3,4}
# b={3,2,1}
# print(a==b)

#6
# sets=[
#     {1,2,3,4},
#     {2,3,4,5},
#     {2,3,4}
# ]
# result = sets[0]

# for i in sets[1:]:
#     result=result.intersection(i)
# print(result)

#7
# a={1,2,3,4}
# b={2,3,5,7}
# print(b.difference(a))

#8
# sets=[
#     {1,2,3},
#     {2,3,4},
#     {2,3,5}
# ]
# result=sets[0].intersection(*set[1:])
# print(result)

#14
# a={1,2,3}
# b={1,3}
# print(a.issubset(b))

#12
# a={1,2,3,4}
# b={3,4,5}
# result=a.symmetric_difference(b)
# print(result)

#13
# def add(num,target):
#     for i in num:
#         for j in num:
#             if i+j==target:
#                 return True
#     return False
# num={1,2,3,6}
# print(add(num,99))

#18
def add(num,target):
    for i in num:
        for j in num:
            if i+j==target:
                return(target)
            else:
                return False
print(add({1,2,4},99))