# Задача 10

import random

def coin():
    n = int(input('Введите число:'))
    while n:
        x = random.randint(1, 2)
        if x == 1:
            print ('Орел')
        else:
            print ('Решка')
        n -= 1
coin()

# Задача 14

n = int(input("Введите число: "))
m = 1
while m < n:
    print(m, end=' ')
    m = m * 2