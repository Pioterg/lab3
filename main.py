import random
#zad1
# a = [1-x for x in range(1, 11)]
# print(a)
# b = [4 ** i for i in range(8)]
# print(b)
# c = [x for x in b if x % 2 == 0]
# print(c)

#zad2
# listy1 = []
# for i in range(10):
#     listy1.append(random.randint(0, 1000))
# listy2 = [x for x in listy1 if x % 2 == 0]
# print(listy1)
# print(listy2)

#zad3
produkty = {'jajka':'sztuki', 'mięso':'kg',  'mleko':'litry', 'jabłko':'sztuki', 'chleb':'sztuki'}
lista_produktow = [x for x, y in produkty.items() if y == 'sztuki']
print(lista_produktow)

#zad4
# print('Podaj 3 długości boków trójkąta w celu sprawdzenia czy jest to trójkąt prostokątny')
# a = int(input())
# b = int(input())
# c = int(input())
# if (a**2 + b**2 == c**2):
#     print("Trójkąt jest prostokątny")
# else:
#     print("Trójkąt nie jest prostokątny")
