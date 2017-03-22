age=input('Введите свой возраст ')
if int(age) < 7:
	print ('Бегом в сад!')
elif int(age) < 16:
	print ('Бегом в школу!')
elif int(age) < 22:
	print ('Бегом в ВУЗ!')
elif int(age) < 60:
	print ('Бегом на работу!')
elif int(age) < 80:
	print ('Можете отдохнуть')
elif int(age) > 80:
	print ('Извините, срок дожития в РФ установлен в 20 лет. Пора и честь знать')