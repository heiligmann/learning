import os
import psutil # сторонний модуль - требуется установка через pip
import sys
import shutil

print("Придумайте название программе")
print("Привет, программист!")

name = input('Ваше имя: ')
print(name, ', добро пожаловать в мир Python!')

answer = ''

while answer != 'q':
	answer = input("Давайте поработаем? (Y/N/q)")
	if answer == 'Y':
		print("Отлично!")
		print("Я умею: ")
		print("[1] - вывести список файлов")
		print("[2] - вывести информацию о системе")
		print("[3] - вывести список процессов")
		print("[4] - продублировать файлы в текущей директории")
		do = int(input('Укажите действие: '))
		
		if do == 1:
			print(os.listdir())
		elif do == 2:
			print("Версия Python: ", sys.version)
			print("Количество процессоров в вашей системе: ", os.cpu_count())
			print("Ваш логин: ", os.getlogin())
			print("Платформа: ", sys.platform)
			print("Версия вашей системы: ", sys.getwindowsversion())
			print("Кодировка системы: ", sys.getfilesystemencoding())
			print("Текущая дериктория: ", os.getcwd())
		elif do == 3:
			print(psutil.pids())
		elif do == 4:
			print("Выполняю дублирование файлов в текущей директории")
			file_list = os.listdir()
			i = 0
			while i < len(file_list):
				newfile = file_list[i] + '.dupl'
				shutil.copy(file_list[i], newfile)
				i = i+1
			print("Дублирование завершено")
		else:
			pass
			
	elif answer == 'N':
		print("До свидания!")
	else:
		print("Неизвестный ответ.")