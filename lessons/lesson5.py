# # 1 Декоратор без аргументов

# def simple_dec(func): # 2 второй шаг - создание декоратора
#     def wrapper(): # 3 третий шаг - создание обертки
# #         print("start") # 5 пятый шаг - вызов декорируемой функции
# #         func() 
# #         print("end")
        
# #     return wrapper # 4 четвертый шаг - вызов декорируемой функции


# # @simple_dec # 1 первый шаг - вызов декоратора
# # def print_text(): 
# #     print("text")
    
# # print_text()


# # # 2 Декоратор с аргументами

# # def is_admin(func):
# #     def wrapper(name):
# #         if name == "admin":
# #             func(name)
# #         else:
# #             print("You are not admin")
# #     return wrapper

# # def is_subcriber(func):
# #     def wrapper(name):
# #         if name == "subscriber":
# #             func(name)
# #         else:
# #             print("You are not subscriber")
# #     return wrapper


# # @is_admin
# # def ban_user(*args, **kwargs):
# #     print("Hello", name)
    
# # ban_user("John")


# # # permission decorator PermissionsMixin


# # # O(1)


# # # def get_by_index(index):
# #     # return LS[index]

# # # print(get_by_index(2))


# # # O(log n)
# # def binary_search(num, value):
# #     left, right = 0, len(num) - 1
    
# #     while left <= right:
# #         mid = (left + right ) // 2
# #         if num[mid] == value:
# #             return True
# #         elif num[mid] < value:
# #             left = mid + 1
# #         else:
# #             right = mid - 1
# #     return False


# # print(binary_search([1,7,3,8,5,6,2,4], 15))


# # # O(n)
# # def linear_search(num, value):
# #     for i in num:
# #         if i == value:
# #             return True
# #     return False


# # # linear_search([1,7,3,8,5,6,2,4], 15)



# # # dict_1 = {
# # #     "a": 1,
# # #     "b": 2,
# # #     "c": 3,
# # #     "d": 4,
# # #     "e": 5,
# # #     "f": 6,
# # #     "g": 7,
# # #     "h": 8,
# # #     "i": 9,
# # #     "j": 10,
# # #     "k": 11,}



# # Магические методы

# class MyAdd:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
        
#     def __add__(self, other):
#         print(self.a)
#         return MyAdd(self.a + other.a, self.b + other.b)
    
#     def __str__(self):
#         return f"{self.a} + {self.b} = {self.a + self.b}"
    
    
# # v1 = MyAdd(1, 2) # a=1 b=2
# # v2 = MyAdd(3, 4) # a=3 b=4
     
     
# #     # a=1 b=2  __add__  a=3 b=4
# # v3 = v1 + v2
# #  # a=4 b=6  
 
# # print(v3)


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
        
#     def __eq__(self, other):
#         return self.price == other.price
    
#     def __gt__(self, other):
#         return self.price > other.price
    
#     def __lt__(self, other):
#         return self.price < other.price

# # ==
    
# p1 = Product("Laptop", 1000)
# p2 = Product("Phone", 100)


# print(p1 < p2)


class CustomAttributes:
    
    def __init__(self):
        self.attributes = {}
        
    def __getattr__(self, name):
        return self.attributes.get(name, None)
    
    def __setattr__(self, name, value):
        print(name, value)
        if name == "attributes":
            print(name, value,  "if")
            super().__setattr__(name, value)
        else:
            print(name, value,  "else")
            self.attributes[name] = value
        
    def __delattr__(self, name):
        del self.attributes[name]
        

obj = CustomAttributes()

obj.x = 10 # __setattr__

print(obj.a) # __getattr__

