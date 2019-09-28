data = []
data_less_100 = []
data_has_good = []
length = 0
Total_length = 0
go = 'N'
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
	length = len(data)
	for d in data:
		Total_length += len(d)
	print('\n')
	print(length, 'reviews in the file.')
	print('Total review ength= ', Total_length)
	print('AVG review length= ', Total_length  / length)
	for d in data:
		if len(d) < 100:
			data_less_100.append(d)
	print('\n')
	print('reveiw length <100 =>', len(data_less_100), ' reviews')
	for d in data:
		if 'good' in d:
			data_has_good.append(d)
	print('\n')
	print('reveiw has good =>', len(data_has_good), 'reviews')
	bad = [d for d in data if 'bad' in d]
	print(len(bad))
	print(bad[100])


	