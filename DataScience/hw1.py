import numpy as np

#Zadacha 1
a = np.matrix("1,1,1; 0.05,0.07,0; 0.05, 0, 0.06")
b = np.matrix("50000;2250;1400")
x = np.linalg.solve(a,b)
print(f'Zadacha 1:\nBank 1: {x[0,0]}\nBank 2: {x[1,0]}\nBank 3: {x[2,0]}\n')

#Zadacha 2
a = np.matrix("1,1,1; -1,1,0; 1, 0, -1")
b = np.matrix("1328;120;100")
x = np.linalg.solve(a,b)
print(f'Zadacha 2:\nIphone 6: {x[0,0]}\nIphone 11: {x[1,0]}\nIphone 12: {x[2,0]}\n')

#Zadacha 3
a = np.matrix("3,0,3; 6,0.25,0; 1, 0.33, 1")
b = np.matrix("1;1;1")
x = np.linalg.solve(a,b)
x[0,0] = 1/x[0,0]
x[1,0] = 1/x[1,0]
x[2,0] = 1/x[2,0]
print(f'Zadacha 3:\na^2: {x[0,0]}\nb^2: {x[1,0]}\nc^2: {x[2,0]}\n')

#Zadacha 4
a = np.matrix("1,1,1; 9,3,0; 1, -1, 1")
b = np.matrix("12;54;2")
x = np.linalg.solve(a,b)
print(f'Zadacha 4:\na: {x[0,0]}\nb: {x[1,0]}\nc: {x[2,0]}\n')

#Zadacha 5
def get_polynom(coords):
    matrix_a = ''
    matrix_b = ''
    for i in coords:
        matrix_a += str(i[0]*i[0]) + ',' + str(i[0]) + ',1;'
        matrix_b += str(i[1])+';'

    a = np.matrix(matrix_a[:-1])
    b = np.matrix(matrix_b[:-1])
    print(a)
    print(b)
    return np.linalg.solve(a,b)

x = get_polynom(((1,1),(2,2),(3,3)))
print(f'Zadacha 5:\n{x}')