from random import randint
from math import ceil

# Создание классов и объектов

# 1.
# class warrior:
#     health = 100
#     def decrease_health(self):
#         self.health -= 20

# warrior1 = warrior()
# warrior2 = warrior()

# while True:
#     if warrior1.health == 0:
#         break
#     if warrior2.health == 0:
#         break

#     random_number = randint(1,2)
#     if random_number == 1:
#         warrior2.decrease_health()
#         print('Warrior 1 > Warrior 2',warrior2.health)
#     elif random_number == 2:
#         warrior1.decrease_health()
#         print('Warrior 2 > Warrior 1',warrior1.health)

# if warrior1.health > warrior2.health:
#     print('Warrior 1 win')
# else:
#     print('Warrior 2 win')

# Конструктор класса - метод __init__()

# 1. 2. 3. 4.
# class Person:
#     def __init__(self, name, full_name, job_level = 1):
#         self.name = name
#         self.full_name = full_name
#         self.job_level = job_level
#     def get_info_about_user(self):
#         return self.name + ' ' + self.full_name + ' Job Level: ' + str(self.job_level)
#     def __del__(self):
#         print('До свидания, мистер ', self.name, self.full_name)

# Andrey = Person('Andrey','Igorev',2)
# Ina = Person('Ina','Igorevna',3)
# Igor = Person('Igor','Igorev')

# print(Andrey.get_info_about_user())
# print(Ina.get_info_about_user())
# print(Igor.get_info_about_user())

# del Igor

# input()

# Наследование

# 1.
# class Person:
#     count = 0
#     def __init__(self,team):
#         self.id_original = Person.count
#         Person.count += 1
#         self.team = team

# class soldier(Person):
#     def __init__(self,team):
#         Person.__init__(self,team)
#         self.my_hero = None
#     def going_to_the_hero(self, hero):
#         self.my_hero = hero.id_original

# class hero(Person):
#     def __init__(self, team):
#         Person.__init__(self,team)
#         self.level = 1
#     def up_level(self):
#         self.level += 1

# hero1 = hero(1)
# hero2 = hero(2)

# army1 = []
# army2 = []

# for i in range(10):
#     random_number = randint(1,2)
#     if random_number == 1:
#         army1.append(soldier(random_number))
#     elif random_number == 2:
#         army2.append(soldier(random_number))

# print(len(army1), len(army2))

# if len(army1) > len(army2):
#     hero1.up_level()
# elif len(army2) > len(army1):
#     hero2.up_level()

# army1[0].going_to_the_hero(hero1)

# print('Hero1: ', hero1.id_original)
# print('Soldier : ', army1[0].id_original)

# Полиморфизм

# class NumberSum:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def __add__(self,other):
#         print(other.a,other.b)
#         return NumberSum(other.a,other.b)

# my_number = NumberSum(10,20)
# other_number = NumberSum(30,40)

# print(other_number + my_number)
# print(my_number + other_number)
# print(my_number + other_number + my_number)

# Инкапсуляция

# class user_id:
#     __id = 0
#     def __init__(self):
#         user_id.__id += 1
#     @staticmethod
#     def get_id():
#         return(user_id.__id)
#     def __get_dict(self):
#         return(user_id.__dict__)
#     def __setattr__(self,attr,value):
#         if attr == '__id':
#             self.__dict__[attr] = value
#         else:
#             raise AttributeError

#     print(__get_dict)

# print(user_id.get_id())
# user1 = user_id()
# print(user_id.get_id())
# user1.id2 = 0

# Композиция
# class win_door:
#     def __init__(self,x,y):
#         self.square = x * y

# class Room:
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.wd = []
#         self.list_weight = []
#     def add_win_door(self,w,h):
#         self.wd.append(win_door(w,h))
#     def work_surface(self):
#         new_square = self.square_for_use
#         for i in self.wd:
#             new_square -= i.square
#         return new_square
#     def change_size(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.save_weight()
#     def save_weight(self):
#         self.list_weight.append([self.x,self.y])
#     def calculate_squere(self):
#         self.square = 2*self.z*(self.x+self.y)
#         self.square_for_use = self.square
#     def number_of_rolls(self,x,y):
#         return ceil(self.square_for_use / (x*y))



# r1 = Room(6,3,2.7)
# r1.calculate_squere()
# print(r1.square_for_use)
# r1.add_win_door(1,1)
# r1.add_win_door(1,1)
# r1.add_win_door(1,2)
# print(r1.work_surface())
# r1.save_weight()
# r1.change_size(2,3,4)
# print(r1.square_for_use)
# r1.save_weight()
# print(r1.list_weight)
# print(r1.number_of_rolls(2,2))

# r2 = Room(int(input()),int(input()),int(input()))
# r2.calculate_squere()
# print(r2.square)
# print(r2.number_of_rolls(int(input()),int(input())))