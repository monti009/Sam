Cars = 100
space_in_a_car = 4.0
drivers = 30
Passengers = 90
Cars_not_driven = Cars - drivers
Cars_driven = drivers
Carpool_capacity = Cars_driven * space_in_a_car
Average_Passengers_per_Car = Passengers / Cars_driven


print("В наличии ", Cars, "автомобилей.")
print("И только", space_in_a_car, "водителей вышло на работу.")
print("Получается, что", Cars_not_driven, "машин пустуют.")
print("Мы можем перевести сегодня", Carpool_capacity, "человек.")
print("Сегодня нужно отвезти ", Passengers, "человек.")
print("В каждой машине будет примерно ", Average_Passengers_per_Car , "человек.")