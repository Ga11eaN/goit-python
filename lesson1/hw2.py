a = float(input('Enter a in ax^2+bx+c:'))
b = float(input('Enter b in ax^2+bx+c:'))
c = float(input('Enter c in ax^2+bx+c:'))
D = b** 2 - 4 * a * c
x1 = (-b - D ** (0.5)) / (2 * a)
x2 = (-b + D ** (0.5)) / (2 * a)
print(f"x1={x1}; x2={x2}")
