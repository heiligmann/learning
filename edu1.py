import os
import psutil # сторонний модуль - требуется установка через pip
import sys

print("Придумайте название программе")
print("Привет, программист!")

name = input('Ваше имя: ')
print(name, ', добро пожаловать в мир Python!')

answer = input("Давайте поработаем? (Y/N)")

if answer == 'Y':
	print("Отлично!")
	print("Я умею: ")
	print("[1] - вывести список файлов")
	print("[2] - вывести информацию о системе")
	print("[3] - вывести список процессов")
	do = int(input('Укажите действие: '))
	
	if do == 1:
		print(os.listdir())
	elif do == 2:
		print("Версия Python: ", sys.version)
		print("Количество процессоров в вашей системе: ", os.cpu_count())
		print("Ваш логин: ", os.getlogin())
		print("Версия вашей системы: ", sys.platform, sys.getwindowsversion())
	elif do == 3:
		print(psutil.pids())
	else:
		pass
		
elif answer == 'N':
	print("До свидания!")
else:
	print("Неизвестный ответ.")