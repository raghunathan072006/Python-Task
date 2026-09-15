# single inheritance
# class Parent:
#     def f1(self):
#         print("Parent function is working....")

# class Child(Parent):
#     def f2(self):
#         print("child function is working....")

# childObj = Child()
# childObj.f1()
# childObj.f2()


# multiple inheritance

# class Father:
#     def f1(self):
#         print("Father fun is working...")
# class Mother:
#     def f2(self):
#         print("Mother fun is working...")
# class Child(Father,Mother):
#     def f3(self):
#         print("child function is working....")

# objChild = Child()
# objChild.f3()
# objChild.f2()
# objChild.f1()

# multilevel

# class GrandFather():
#     def f1(self):
#         print("GrandFather Fun is workimng......")
# class Father(GrandFather):
#     def f2(self):
#         print("Father Fun is workimng......")
# class Son(Father):
#     def f3(self):
#         print("Son Fun is workimng......")

# ObjSon = Son()
# ObjSon.f1()



# class Parent:
#     def f1(self):
#         print("parent fun")
# class Child1(Parent):
#     def f2(self):
#         print("child1 fun")
# class Child2(Parent):
#     def f3(self):
#         print("child2 fun")
# objChild2 = Child2()
# objChild2.f1()
# objChild1 = Child1()
# objChild1.f1()

#encapsulation
# class emp:
#     def dad(self,name):
#         print(name)
# obj=emp()
# obj.dad("raghu")

# class emp:
#     def __init__(self,name):
#         print(name)
# obj=emp("raghu")
        
# class encap:
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary
# emp=encap("raghu",70000)
# print(emp.name)
# print(emp.__salary)

# class en:
#     def __init__(self,name):
#         self.name=name
#     def d1(self):
#         print(self.name)
# emp=en("raghu")
# emp.d1()
# print(emp.name)

# class employee:
#     def __init__(self,name,age):
#         self.name=name
#     def aa(self):
#         self.__age=age
# emp=employee("raghu",20)
# print(emp.name)
# emp.aa()

#public
# class raghu:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def normal(self):
#         print(self.salary)
# emp=raghu("aa",200)
# print(emp.name)
# print(emp.salary)
# emp.normal()

#public method 2
# class name:
#     def __init__(self,aa,bb):
#         self.aa=aa
#         self.bb=bb
# class age(name):
#     def cc(self):
#         print(self.bb)
# n=age("raghu",20)
# print(n.aa)
# n.cc()

#protected
# class employee:
#     def __init__(self,name,age):
#         self.name=name
#         self._age=age
#     def add(self):
#         print(self._age)
#     def sub(self):
#         print(self._age)
#     def mul(self):
#         print(self._age)
# emp=employee("raghu",20)
# print(emp.name)
# emp.add()
# emp.sub()
# emp.mul()

#protect method 2
# class a:
#     def __init__(self,name,age):
#         self.name=name
#         self._age=age
# class b(a):
#     def dd(self):
#         print(self._age)
# class c(b):
#     def ee(self):
#         print(self._age)
# emp=c("raghu",20)
# print(emp.name)
# emp.ee()
# print(emp._age)

#private
# class aa:
#     def kl(self,name,age):
#         self.name=name
#         self.__age=age
# emp=aa()
# emp.kl("raghu",20)
# print(emp.name)
# print(emp.__age)

