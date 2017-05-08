#!/usr/bin/python 

# CALCULATOR BY ERROR #
# CREATE FOR LEARNING #
# --- THANKS GUYS --- #
# >CALCULATOR PART I< #

""" calculator with while loop and if statement """

import time

print " CALCULATOR.py \n"

walk = True


while walk:
	print " 1> ADDTIONAL \n 2> SUBTRACT \n 3> MULTIPLE \n 4> DIVIDE \n 5> MODULUS \n 0> to close CALCULATOR.py PROGRAM \n "

	choose = int(input("select with number 1 - 5 and 0 to close Program: "))
	print "\n"

	if choose == 1:
		print "ADDTIONAL"
		num1 = int(input("put your first number here: "))
		num2 = int(input("put your seccond number here: "))
		results = num1 + num2
		print "Processing. . ."
		time.sleep(1.10)
		print num1, "+", num2, "=", results

	elif choose == 2:
		print "SUBTRACT"
		num1 = int(input("put your first number here: "))
		num2 = int(input("put your seccond number here: "))
		results = num1 - num2
		print "Processing. . ."
		time.sleep(1.10)
		print num1, "-", num2, "=", results

	elif choose == 3:
		print "MULTIPLE"
		num1 = int(input("put your first number here: "))
		num2 = int(input("put your seccond number here: "))
		results = num1 * num2
		print "Processing. . ."
		time.sleep(1.10)
		print num1, "x", num2, "=", results

	elif choose == 4:
		print "DIVIDE"
		num1 = int(input("put your first number here: "))
		num2 = int(input("put your seccond number here: "))
		results = num1 / num2 
		print "Processing. . ."
		time.sleep(1.10)
		print num1, "/", num2, "=", results

	elif choose == 5:
		print "MODULUS"
		num1 = int(input("put your first number here: "))
		num2 = int(input("put your seccond number here: "))
		results = num1 % num2
		print "Processing. . ."
		time.sleep(1.10)
		print num1, "%", num2, "=", results

	elif choose == 0:
		print "Thanks for use ^_^"
		time.sleep(1.10)
		print "P"
		time.sleep(0.10)
		print "Pr"
		time.sleep(0.10)
		print "Pro"
		time.sleep(0.10)
		print "Proc"
		time.sleep(0.10)
		print "Proce"
		time.sleep(0.10)
		print "Proces"
		time.sleep(0.10)
		print "Process"
		time.sleep(0.10)
		print "Processi"
		time.sleep(0.10)
		print "Processin"
		time.sleep(0.10)
		print "Processing\n"
		time.sleep(1.30)
		print "Have a nice day :)"
		time.sleep(2.10)
		walk = False
	else:
		print "ooppss sorry :( please type 1,2,3,5 and 0 for using :D"