words_list = ["АВТОМОБИЛЬ","КОТ","САМОЛЁТ","УНИВЕРСАЛ","ЛИНГВИСТ"]
import tkinter as tk
import random
while True:
	MAX_ERRORS = 10

	errors_counter = 0

	def print_list_as_str(arg):
		print("".join(arg))
	def r():
		i = 0
		while i != 50:
			print("")
			i += 1

	secret_word = random.choice(words_list)

	user_word = ["*"] * len(secret_word)
	r()
	print("Начать Играть [1]")
	print("Выход [2]")
	act = str(input("Введите индекс действия:"))
	if act == "1":
		r()
		print_list_as_str(user_word)
		while True:
			letter = input("Введите букву: ").upper()
			r()
			if len(letter) == 1:
				coding = ord(letter)

			if len(letter) != 1 or not letter.isalpha() or coding < 1000:
				continue	

			if letter in secret_word:
				idx = 0
				for char in secret_word:
					if char == letter:
						user_word[idx] = letter
					idx += 1
				if "*"not in user_word:
					print("Вы выиграли!!!")
					break
			else:
				errors_counter += 1
				print("Ошибок", errors_counter)
				if errors_counter == MAX_ERRORS :
					print("Вы проиграли! ")
					break

			print_list_as_str(user_word)
		print("Слово",secret_word)
		print("Enter - Выйти в меню")
		input()
	else:
		break