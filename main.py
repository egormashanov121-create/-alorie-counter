#мужчина(1) или женщина(0), вес и возраст
gender = 0 
weight_in_kg = 80
age = 25

#количество шагов
namber_of_steps = 100

#1 шаг = 0.8 метра у мужчин. 1 шаг = 0.6 метра у женщины
if gender == 1:
    meters_traveled = 0.8 * namber_of_steps
else:
    meters_traveled = 0.6 * namber_of_steps


# 1 километре 1000 метров
kilometrs_traveled = meters_traveled/1000

#Поздарвление относительно пройденных километров
if kilometrs_traveled >= 6.5:
    congratulation = 'Отличный результат! Цель достигнута.'
elif  3.9 <= kilometrs_traveled < 6.5:
    congratulation = 'Неплохо! День был продуктивным.'
elif kilometrs_traveled >= 2 and kilometrs_traveled < 3.9:
    congratulation = 'Маловато, но завтра наверстаем!'
elif kilometrs_traveled >= 0 and kilometrs_traveled < 2:
    congratulation = 'Лежать тоже полезно. Главное — участие, а не победа!'

#срединй расход идет 0,9 ккал на 1 кг веса и 1км растояния
ccal_on_kilometrs = weight_in_kg * 0.9 * kilometrs_traveled


#пройденные километры округляем до 1/10. Ккал округляем до целого числа
print(f'''Сегодня вы прошли {namber_of_steps} шагов
Пройденная дистанция {round(kilometrs_traveled, 1)} км
Потрачено {int(ccal_on_kilometrs)} ккал
{congratulation}''')

print('Версия приложеиня номер 2')

