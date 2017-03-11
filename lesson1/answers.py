question1 = input('Привет! ')
question2 = input('Как дела? ')
question3 = input('Пока! ')
def get_answer():
	answers = {"привет": question1, "как дела": question2, "пока": question3}
	question = input ('Скажите что-нибудь по теме ')
	print(answers[question])

	

get_answer()
print (question1)