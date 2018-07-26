#file = open("text.txt","r")
string = ["to", "meet", "not", "snake", "ate"]
count = 0

for x in string:
	if(len(x.strip()) == 2 or len(x.strip()) == 1):
		count = count + 0
	elif(len(x.strip()) == 3):
		count = count + 1
	elif(len(x.strip()) == 4):
		count = count + 2
	elif(len(x.strip()) == 5):
		count = count + 3
	elif(len(x.strip()) == 6):
		count = count + 4
	elif(len(x.strip()) == 7):
		count = count + 5
	elif(len(x.strip()) == 8):
		count = count + 6
	elif(len(x.strip()) == 9):
		count = count + 7
	elif(len(x.strip()) == 10):
		count = count + 8
	elif(len(x.strip()) == 11):
		count = count + 9
	elif(len(x.strip()) == 12):
		count = count + 10
	elif(len(x.strip()) == 13):
		count = count + 11
	elif(len(x.strip()) == 14):
		count = count + 12
	elif(len(x.strip()) == 15):
		count = count + 13
	elif(len(x.strip()) == 16):
		count = count + 14
	else:
		print "nada"
print count