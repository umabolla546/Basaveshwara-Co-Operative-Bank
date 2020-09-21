# def outer():
#     print('outer function')
#     def inner():
#         print('inner function')
#     print('outer function inner function')
#     return inner
# f=outer()
# f()
# f()
# f()
#decarator
# def deck(wish):
#     def inner(name):
#         if name=='anu':
#             print('hello',name,'badmorning')
#         else:
#             wish(name)
#     return inner
#
# def wish(name):
#     print('hello',name,'good morning')
# deckkk=deck(wish)
# wish('uma')
# wish('anu')
# #decatoe calling
# deckkk('uma')
#deckkk('anu')

# def deck(func):
#     def inner(a,b):
#         if b==0:
#             print('oops cannot deivide')
#         else:
#             func(a,b)
#     return inner
# @deck
#
# def smart_division(a,b):
#     print(a/b)
# smart_division(10,20)
# smart_division(10,0)


# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"
#
#     def second_child():
#         return "Call me Liam"
#
#     if num == 1:
#         return first_child
#     else:
#         return second_child
# ff=parent(1)
# print(ff())

# nums=[1,2,5,10,3,100,9,24]
# for i in nums:
#     print(i)
#     if i<5:
#         nums.remove(i)
# print(nums)



# class test:
#     a=10
#     def __init__(self):
#         test.b=20
#     def m1(self):
#         test.c=30
#     @classmethod
#     def m2(cls):
#         test.d=40
#         cls.e=50
#     @staticmethod
#     def m3():
#
#         test.f=60
# print(test.__dict__)
# a=test()
# print(test.__dict__)
# a.m1()
# print(test.__dict__)
# test.m2()
# print(test.__dict__)
# test.m3()
# print(test.__dict__)
# test.r=85
# print(test.__dict__)

# class car:
#     def __init__(self,name,model,coller):
#         self.name=name
#         self.model=model
#         self.coller=coller
#     def getinfo(self):
#         print('car name {},model {}, color {}'.format(self.name,self.model,self.coller))
# class employe:
#     def __init__(self,ename,eno,car):
#         self.name=ename
#         self.eno=eno
#         self.car=car
#     def dispaly(self):
#         print('empname',self.name)
#         print('empnom',self.eno)
#         print('carinfo:')
#         self.car.getinfo()
# c=car('invo',5885,'red')
# c.getinfo()
# e=employe('uma',10000,c)
# e.dispaly()


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eating(self):
#         print('eating birinany drinking ber')
# class employe(person):
#     def __init__(self,name,age,eno,esal):
#      super().__init__( name, age)
#      self.eno=eno
#      self.esal=esal
#     def work(self):
#          print('ebvkabgkagbkagbn')
#     def empinfo(self):
#          print('emplote name',self.name)
#          print('emplote name',self.age)
#          print('emplote name',self.eno)
#          print('emplote name',self.esal)
# e=employe('uma',24,101,70000)
# e.work()
# e.empinfo()
# e.eating()

# class car:
#     def __init__(self,name,color,model):
#         self.name=name
#         self.color=color
#         self.model=model
#     def getinfo(self):
#         print('carname {} \n coller {} \n model {}'.format(self.name,self.color,self.model))
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eating(self):
#         print('eating birinany drinking ber')
# class employe(person):
#     def __init__(self,name,age,eno,esal,car):
#      super().__init__( name, age)
#      self.eno=eno
#      self.esal=esal
#      self.car=car
#
#     def work(self):
#          print('ebvkabgkagbkagbn')
#     def empinfo(self):
#          print('emplote name',self.name)
#          print('emplote name',self.age)
#          print('emplote name',self.eno)
#          print('emplote name',self.esal)
#          self.car.getinfo()
# c=car('invo','red',54465)
# e=employe('uma',24,101,70000,c)
# e.work()
# e.eating()
# e.empinfo()


# class p1:
#     def m1(self):
#         print('paret method')
# class p2:
#     def m1(self):
#         print('paret p2 method')
# class c(p2,p1):
#     def m2(self):
#         print('child class')
# a=c()
# a.m2()
# a.m1()
# a.m1()
# class emp:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def __mul__(self, other):
#         return self.salary*other.days
#
# class stamp:
#     def __init__(self,name,days):
#         self.name = name
#         self.days = days
#
#
#
# e=emp('uma',50)
# s=stamp('durga',20)
# print(e*s)


# class test:
#     def m1(self):
#         print('no argurment method')
#     def m1(self,a):
#         print('no a argurment method')
#     def m1(self,a,b):
#         print('no a,b argurment method')
# c=test()
# c.m1(10,20)



# class test:
#     def sum(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             print(a+b+c)
#         elif a != None and b != None:
#             print(a+b)
#         else:
#             print('provide two or thers value')
# t=test()
# t.sum(10,20,30)
# t.sum(10,20)
# t.sum(10)
#largest number in list
# def max_num_in_list( list ):
#     max = list[ 0 ]
#     for a in list:
#         if a > max:
#             max = a
#     print(max)
# print(max_num_in_list([1, 2, -8, 0]))
# original_list = [10, 22, 44, 23, 4]
# new_list = original_list
# print(original_list)
# print(new_list)

#remove duplicate
# l=[10,10,2,5,8,2]
# lit=[]
# for i in l:
#     if i not in lit:
#         lit.append(i)
# print(lit)
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
# print(color)
