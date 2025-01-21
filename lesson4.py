
# наши модули библиотеки

# import math_utils
# from math_utils import add

# print(add(1, 2))

# # from MyPackage import mathutils
# from MyPackage import add

# print(add(1, 2))

# Встроенные модули и Библиотеки
# import sqlite3
# import base64
# from datetime import time, date, datetime, timedelta
# import tkinter

# tkinter.Tk()
# tkinter.Button(text="Hello")

# import colorama
# # import sys
# from colorama import init, Fore, Back, Style

# init()

# print(Fore.RED + "Hello, World!")


# Фреймворки
# DJANGO = "Django"
# from django.conf import settings
# set = settings
# print(set)


# class MyClass:
    
#     def instance_method(self):
#         print("instance method")
        
# obj = MyClass()
# obj.instance_method()


# class MegaCom:
    
#     def __init__(self):
#         self.__login = get.env("login")
#         self.__password = get.env("password")
    
#     @classmethod
#     def sing_in(cls):
#         return print("Sing in MegaCom")


# class MegaFon(MegaCom):
#     pass
    
    
# obj = MegaFon()
# obj.sing_in()
# print(obj._MegaCom__login)
# print(dir(obj))


# obj = MyClass()
# obj.class_method()


class Mytest:
    def __call__(self, *args, **kwds):
        return print("call")
    

class NikitaService:
    
    def __init__(self):
        self.__login = "admin"
        self.__password = "password"

    @classmethod
    def sing_in_admin(cls):
        return print("Sing in MegaCom")
    
    @staticmethod
    def sing_in_client(login, password):
        print(f"clinet sing in {login} {password}")
    
    @Mytest
    def sing_out_user(login, password):
        print(f"clinet sing in {login} {password}")
        
    
        


MegaComService.sing_in_client("Ardager", "123")

# obj = MegaCom()

# obj.sing_in_client("Ardager", "123")
