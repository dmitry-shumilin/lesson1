string1 = input ('Введите строку 1')
string2 = input ('Введите строку 2')
def get_str(string1, string2):
	
	if string1 == string2:
		return (1)
	if len(string1)>len(string2):
		return (2)
	if len (string1) != len(string2):
		
			if str(string2) =='learn':
				return (3)


z = get_str(string1, string2)
print(z)


