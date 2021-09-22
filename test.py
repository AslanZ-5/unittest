# from typing import List, Tuple
# # a1 = ['##.##','#...#','....#','#...#','##...#','#....#','#####.']
# a1 = ['#######', '....#','#.....#', '#.#.###', '#.#', '###']
# s = 'ddddd'
#
# a = list(map(lambda x: str(x).rjust(len(max(a1))), a1))
# # for i in range(len(a)):
# #     for j in range(len(a)):
# #         if a[0][j] == ".":
# #             print(0,j)
# #
# #         elif a[-1][j] == ".":
# #             print(a.index(a[-1],j))
# # for i in range(len(a)):
# #     for j in range(len(a[0])):
# #         if i == 0 and  a[0][j] == '.':
# #             print(j,i)
# #
# #         if i == len(a)-1 and  a[len(a)-1][j] == '.':
# #             print(j,i)
# #         elif j == len(a[i])-1 and a[i][j] == '.':
# #             print(j,i)
# #         elif j == 0 and a[i][j] == '.':
# #             print(j,i)
# #         elif a[i][j] == ' ' and a[i][j+1] == '.':
# #             print(j,i)
# #         elif a[i][j] == '.' and a[i+1][j] == " " or a[i-1][j] == " ":
# #             print(j,i)
#
#
#
# # for i in range(len(a)):
# #     for j in range(len(a[0])):
# #         print(j,i)
# #         if i == 0 and a[j] == '.':
# #             print(j,i)
# #         elif i == a[i] and a[j] == '.':
# #             print(j,i)
# #         elif a[i][0] == '.':
# #             print(0,i)
# #         elif a[i][len(a[0])] == '.':
# #             print(i,len(a[0]))
# #         elif a[i][1] == '.' and a[i][0] == ' ':
# #             print(1,i)
#
#
#
# # for i in range(len(a)):
# #     for j in range(len(a[0])-1):
# #         if i == 0 and  a[0][j] == '.':
# #             print(j,i)
# #         if i == len(a) - 1 and a[len(a) - 1][j] == '.':
# #             print(j,i)

# def add(x, y):
#     return x + y
#
#
# def substract(x, y):
#     return x - y
#
#
# def multiply(x, y):
#     return x * y
#
#
# def divide(x, y):
#     if y == 0:
#         raise ValueError('Can not divide by zero')
#     return x / y


class Employee:
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
