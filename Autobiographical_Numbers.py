Possible_Candidates = []
Likely_Candidates =[]
FDigit = []
CDigit = 0
SDigit = 0
TDigit = 0
QDigit = 0
Autobiographical_Numbers =[]
Maha_String = ""

User_Input = input("Enter a number from 1 to 7:   ")


if (User_Input.isnumeric() == True):
	User_Input = int(User_Input)
	if (User_Input >= 1 and User_Input <= 7):
		for i in range ((10 ** (User_Input - 1)), (10 ** (User_Input))):
			n = i
			Total = 0
			while (n > 0):
				Digit = n % 10
				Total = Total + Digit
				n = n // 10
			if(Total == User_Input):
				Possible_Candidates.append(i)
				FDigit.append((i // (10 ** (User_Input - 1))))
		Counter = 0
		while(Counter < len(Possible_Candidates)):
			if (FDigit[Counter] >= User_Input):
				FDigit.remove(FDigit[Counter])
				Possible_Candidates.remove(Possible_Candidates[Counter])
			Counter = Counter + 1

		Counter = 0
		while(Counter < len(Possible_Candidates)):
			Maha_String = str(Possible_Candidates[Counter])
			CDigit = int(Maha_String[0])
			SDigit = int(Maha_String[1])
			TDigit = int(Maha_String[2])
			Number_Of_Times_Zero = 0
			How_Many_Ones = 0
			Count_of_twos = 0
			Total_Of_Threes = 0
			if User_Input > 4:
				QDigit = int(Maha_String[3])
				for z in Maha_String:
					if z == '3':
						Total_Of_Threes = Total_Of_Threes + 1
			for w in Maha_String:
				if w == '0':
					Number_Of_Times_Zero = Number_Of_Times_Zero + 1
			for x in Maha_String:
				if x == '1':
					How_Many_Ones = How_Many_Ones + 1
			for y in Maha_String:
				if y == '2':
					Count_of_twos = Count_of_twos + 1
			Counter = Counter + 1
			if Number_Of_Times_Zero == CDigit and How_Many_Ones == SDigit and Count_of_twos == TDigit and Total_Of_Threes == QDigit:
				Likely_Candidates.append(int(Maha_String))
		if (Likely_Candidates != []):
			print("Autobiographical numbers generated of "+str(User_Input)+" digits are as:")
			print(Likely_Candidates)
		else:
			print("No Autobiographical numbers were found of  "+ str(User_Input)+ " digits")

	else:
		print("Number must be in range from 1 and 7")
else:
	print("Input must only contain positive non-decimal whole numbers")

