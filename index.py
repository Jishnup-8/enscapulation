# Access specifies ..

#1 ) Public access..
# acccesibles from anywere (inside or outside the class)

# class Student:
#     def __init__(self):
#         self.name = 'john'  # public variables ..
#         print(f'my name is {self.name}')

# s1 = Student()
# s1.name = 'jishnu'  # modify public variables and methods ...
# print(s1.name)


# 2) Protected access ..
# only inside and the class and subclass ...

# class Student:
#     def __init__(self):
#         self.mark = 50   # protected variable


# s1 = Student()
# s1._mark = 100 
# print(s1.mark)

# Privet access (double underscore)

# only access indode the class , cant acces outside the class or subclass 
# class student :
#     def __init__(self):
#        self.__age = 30 # privet variable
#        print(self.__age)
#     def greet(self):  # privetv method
#         print(' i am a privet method')

# s1 = student()
# # print(s1.__age)
# print(s1.__greet())



# getters and setters

# class Student :
#     def __init__(self):
#        self.__age = 30                # privet variable
#     # getters 
#     def get_age(self):
#         return self.__age

#     def set_age(self , new_age):
#         self.__age = new_age


# # print(s1.get_age())

# s1 = Student()
# print(s1.get_age())
# s1.set_age(60)
# print(s1.get_age())




    










