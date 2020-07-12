
import math
                                                      
print(' ██▓     █    ██  ▄████▄   ██▓  █████▒▓█████  ██▀███  ')
print('▓██▒     ██  ▓██▒▒██▀ ▀█  ▓██▒▓██   ▒ ▓█   ▀ ▓██ ▒ ██▒')
print('▒██░    ▓██  ▒██░▒▓█    ▄ ▒██▒▒████ ░ ▒███   ▓██ ░▄█ ▒')
print('▒██░    ▓▓█  ░██░▒▓▓▄ ▄██▒░██░░▓█▒  ░ ▒▓█  ▄ ▒██▀▀█▄  ')
print('░██████▒▒▒█████▓ ▒ ▓███▀ ░░██░░▒█░    ░▒████▒░██▓ ▒██▒')
print('░ ▒░▓  ░░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░░▓   ▒ ░    ░░ ▒░ ░░ ▒▓ ░▒▓░')
print('░ ░ ▒  ░░░▒░ ░ ░   ░  ▒    ▒ ░ ░       ░ ░  ░  ░▒ ░ ▒░')
print('  ░ ░    ░░░ ░ ░ ░         ▒ ░ ░ ░       ░     ░░   ░ ')
print('    ░  ░   ░     ░ ░       ░             ░  ░   ░     ')

print('___ç$$$ç________________')
print('__$$$$$$$_####______####_')
print('___*$$$$$$ç####___########')
print('_____*$$$$$$$$$$$##########')
print('_____$$$$$$$$$$$$$##########')
print('______$$$$$$$$$$$$$##########')
print('______$$$$$$$$$$_$$$##########')
print('______$$$$$$$$$$##$$$##########')
print('_______$$$$$$$$$_##$$##########')
print('______$$$$$$$$$$___$$#########')
print('_____$_$$$$$$$$$$__$$_########')
print('___$$__$$$$$$$$$$_$$$__######')
print('______$$$$$$$$$$__$$$___#####')
print('______$$$$$$$$$___$$____####')
print('______$$$$$$$$$_________###')
print('______$$$$$$$$__________##')
print('_______$$$$$$___________##')
print('_______$$$$$$______________')
print('_______$$$$$$$$____________')
print('_______$$$$$$$$____________')
print('_______$$$$_$$$$___________')
print('_______$$$$_$$$$___________')
print('_______$$$___$$$$__________')
print('__ççç$$$$$$_çç$$$$__________')
def even(start,end,evec):
		for i in range(start,end+1):
			if i % 2 == 0:
				evec += 1
				print("\neven number:",i,end ='\t ')
		print("\n \tEven count = ",evec)
def odd(start,end,oddc):
		for j in range(start,end+1):
			if j % 2 !=0:
				oddc += 1
				print("\n odd number:",j,end = '\t')
		print("\n \tOdd count = ",oddc)
def eve(n):
		if n%2 == 0:
			print("this is Even number")
		elif n == 1:
			print("number is 1")
		else:
			print('This is odd number')
ch = int(input("1.even number\n2.Odd number\n3.check exact number(even)\n4.Add Two numbes\n5.Substract Two numbers\n6.Divide two numbers\n7.Multiply two numbers\n8.Square of a numbers\n9.Square root of a number\n10.Cube of number\n11.Cube-root of number\n12.factorial of a number\n13.Check number prime or not\n14.Mod of a number\n15.Degree of number\n16.Calculate percentage\n99.Exit\n\nEnter your choice:"))
if ch == 1:
	start = int(input('ENter start point:'))
	end = int(input('ENter end point:'))
	evec = 0
	even(start,end,evec)
elif ch == 2:
	start = int(input('ENter start point:'))
	end = int(input('ENter end point:'))
	oddc = 0
	odd(start,end,oddc)	
elif ch == 3:
	n = int(input("Enter a number:"))
	eve(n)
elif ch == 4:
	a = int(input("Enter 1'st number:"))
	b = int(input("ENter 2'nd number:"))
	print("Addition is :",a+b)
elif ch == 5:
	a = int(input("Enter 1'st number:"))
	b = int(input("ENter 2'nd number:"))
	print("Substraction is :",a-b)
elif ch == 6:
	a = int(input("Enter 1'st number:"))
	b = int(input("ENter 2'nd number:"))
	if a < 0 and b < 0:
		print(" plz ENter the number grater than 0")
	else:
		print("Division is :",a/b)
elif ch == 7:
	a = int(input("Enter 1'st number:"))
	b = int(input("ENter 2'nd number:"))
	print("Multiplication  is :",a*b)
elif ch == 8:
	a = int(input("ENter number:"))
	print("Square of number is:",a*a)
elif ch == 9:
	import math
	a = int(input("ENter number:"))
	print("Square root of number is :",math.sqrt(a))
elif ch == 10:
	a = int(input("ENter number:"))
	print("cube is :",a*a*a)
elif ch == 11:
	a = int(input("ENter number:"))
	print(a**(1/3))
elif ch == 12:
	from factorial import*
elif ch == 13:
	num = int(input("Enter a number: "))  
  
	if num > 1:  
	   for i in range(2,num):  
	       if (num % i) == 0:  
	           print(num,"is not a prime number\nbecause")  
	           print(i,"times",num//i,"is",num)  
	           break  
	   else:  
	       print(num,"is a prime number")  
	         
	else:  
	   print(num,"is not a prime number")  

elif ch == 14:
	num = int(input("Enter a number: "))
	num2 = int(input("Enter a number: "))
	c = num % num2
	print(c)
elif ch == 15:
	num = int(input("Enter a number: "))
	num2 = int(input("Enter a Degree: "))
	c = pow(num,num2)
	print(c)
elif ch == 16:
	num = int(input("Enter value: "))
	num2 = int(input("ENter total value:"))
	c = (num/num2)*100
	print(c,"%")
elif ch == 99:

	print('				██████████───────')
	print('			──────────────████████████──────')
	print('			──────────────██────────██──────')
	print('			──────────────██▄▄▄▄▄▄▄▄▄█──────')
	print('			──────────────██▀███─███▀█──────')
	print('			█─────────────▀█────────█▀──────')
	print('			██──────────────────█───────────')
	print('			─█──────────────██──────────────')
	print('			█▄────────────████─██──████')
	print('			─▄███████████████──██──██████ ──')
	print('			────█████████████──██──█████████')
	print('			─────────────████──██─█████──███')
	print('			──────────────███──██─█████──███')
	print('			──────────────███─────█████████')
	print('			──────────────██─────████████▀')
	print('			────────────────██████████')
	print('			────────────────██████████')
	print('			─────────────────████████')
	print('			──────────────────██████████▄▄')
	print('			────────────────────█████████▀')
	print('			─────────────────────████──███')
	print('			────────────────────▄████▄──██')
	print('			────────────────────██████───▀')
	print('			────────────────────▀▄▄▄▄▀')
	

else:


	print('	░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄☆')
	print('	░███████████████████████')
	print('	░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤')
	print('	╬▀░▐▓▓▓▓▓▓▌▀█░░░█▀░')
	print('	▒░░▓▓▓▓▓▓█▄▄▄▄▄█▀╬░')
	print('	░░█▓▓▓▓▓▌░▒▒▒▒▒▒▒▒▒')
	print('	░▐█▓▓▓▓▓░░▒▒▒▒▒▒▒▒▒')
	print('	░▐██████▌╬░▒▒▒▒▒▒▒▒')

	print("\n\n\n invalid choice")
