# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

from functools import reduce

def normalize(L):
    # TODO:_____________________
    return L

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积

def add(a,s):
    return a+s
def mult(a,s):
    return a*s
def sum(L):
    # TODO:_____________________

def prod(L):
    # TODO:_____________________

L=[1,2,3,4]
print(sum(L))
print(prod([3,5,7,9]))