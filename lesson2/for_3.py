summ_all_klasses = 0
numbers_of_all_scores = 0
numbers_of_klasses = 0
average_all = 0
digits = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '5a', 'scores': [2,5,4,5,3]}, {'school_class': '5b', 'scores': [3,4,3,5,2]}]
for klass in digits:
	numbers_of_klasses = numbers_of_klasses +1
	c = (klass['scores'])
	for digits_in_klass in c:
		summ_all_klasses = digits_in_klass + summ_all_klasses
		numbers_of_all_scores += 1
	average = summ_all_klasses / numbers_of_all_scores
	print ('Средний балл ', klass['school_class'], 'класса = ', average)
	average_all = average + average_all
print('Всего классов в школе', numbers_of_klasses)
print('Средний балл по всей школе = ', average_all / numbers_of_klasses)
		
