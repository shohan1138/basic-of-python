a=[1,2,4,3]

car ={'brand':'toyota','color':'red','price':'3003230'}
print(car['color'])
print(car)
print(car.keys())

for i in car:
    print(car[i])

for i in car.values():
    print(i)
for i,j in car.items():
    print(i,j)
