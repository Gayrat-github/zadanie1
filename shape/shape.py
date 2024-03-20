'''
get_area() - метод расчитывает площадь заданной фигуры
    по умолчанию: одно значение - круг, два значения - квадрат/прямоугольник, три - треугольник
    значения счтитаются верными если они являются положительными целочисленными или положительными вещественными
    во всех не корректных случаях метод будет возвращать - None

is_right_triangle() - метод возвращает True для прямоугольного треугольника и False в противном случае
    во всех не корректных случаях метод будет возвращать - None
'''

from math import pi

def get_area(*args, obj = None):
    # переменная obj может использоватьс в дальнейшем для расширения функционала и явного указания типа фигуры
    if not all([type(x) in (int, float) and x > 0 for x in args]):
        return None
    if len(args) == 1 and obj == None:      # круг
        return pi * (args[0] ** 2)
    if len(args) == 2 and obj == None:      # квадрат-прямоугольник
        return args[0] * args[1]
    if len(args) == 3 and obj == None:      # треугольник
        p = (args[0] + args[1] + args[2]) / 2
        return (p * (p - args[0]) * (p - args[1]) * (p - args[2])) ** 0.5
    return None

def is_right_triangle(*args):
    if not all([type(x) in (int, float) and x > 0 for x in args]):
        return None
    if len(args) == 3:
        lst = list(args)
        c = max(lst)
        lst.remove(c)
        if c**2 == lst[0]**2 + lst[1]**2:
            return True
        else:
            return False
    return None