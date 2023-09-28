import math
 
print("Введите коэффициенты ")
g = float(input("g = "))
r = float(input("r = "))
m = float(input("m = "))
 
z = r ** 2 - 4 * g * m
print("Дискриминант D = %.2f" % z)
 
if z > 0:
    x1 = (-r + math.sqrt(z)) / (2 * g)
    x2 = (-r - math.sqrt(z)) / (2 * g)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif z == 0:
    x = -r / (2 * g)
    print("x = %.2f" % x)
else:
    print("Корней нет")