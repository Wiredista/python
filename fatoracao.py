#-*- coding: utf-8 -*-
# python 2.7

import sys

# FEITO PARA PYTHON 2.7

print "\033[2J \033[H \n \n"
print "  Entre com o numero a ser fatorado! "

while True:
	try:
		fat = int(raw_input(" > "))
		break
	except ValueError:
		print " Numero invalido."
	except KeyboardInterrupt:
		exit("\n")
numlen = len(str(fat))

def primo( num ):
	if num == 2 or num == 3:
		return 1
	elif num % 2 == 0:
		return 0

	count = 3
	while count < num / 2:
		if num % count == 0:
			return 0
		count += 1
	return 1

primos = []
fatores = []
fatorando = fat
processo = [fat]
count = 5

try:
	sys.stdout.write("\033[1A\033[K") # GAMBIARRA PARA DESIGN
	if fat == 0:
		print " Zero não pode ser fatorado! "
		exit()
	if primo(fat):
		print "\n", fat, "é primo! \n"
		print "  ", fat, (numlen-len(str(fat)))*" "+" │ ", fat	# GAMBIARRA PARA DESIGN
		print 1
		exit()
	while fat % 2 == 0:
		print "  ", fat, (numlen-len(str(fat)))*" "+" │ ", 2	# GAMBIARRA PARA DESIGN
		fatores.append(2)
		fat = fat / 2
		processo.append(fat)

	while fat % 3 == 0:
		print "  ", fat, (numlen-len(str(fat)))*" "+" │ ", 3	# GAMBIARRA PARA DESIGN
		fatores.append(3)
		fat = fat / 3
		processo.append(fat)

	while count < fatorando:
		if primo(count):
			while fat % count == 0:
				print "  ", fat, (numlen-len(str(fat)))*" "+" │ ", count # GAMBIARRA
				fatores.append(count)
				fat = fat / count
				processo.append(fat)
		if fat == 1:
			print "  ", fat, (numlen-len(str(fat)))*" "+" │ \n\n"
			break
		count += 2

	print 5 * "\n", processo, fatores

except KeyboardInterrupt:
	print " \n PROGRAMA INTERROMPIDO! "

