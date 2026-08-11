mylist=[10,20,30,40]
print(mylist)

mylist1=list(("raghu",1234567890,20))
print(mylist1[2])
print(type(mylist1))
print(len(mylist1))

#append method
mylist1.append("raam")
print(mylist1)

#insert
mylist.insert(3,77)
print(mylist)

#extend
myset={"raja"}
mylist1.extend(myset)
print(mylist1)

#removing elements
#pop
mylist1.pop(4)
print(mylist1)

#remove
mylist1.remove(20)
print(mylist1)

#index
myindex=mylist.index(77)
print(myindex)

mylist.append(30)
print(mylist)

#count
print(mylist.count(30))

#using for condition
for i in mylist:
    if i==20:
        print(i)
