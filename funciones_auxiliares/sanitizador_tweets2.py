import time

def save_saniticed_tweets(filename):
	file = open('../data/' + filename + '.tsv', 'r')
	filesan = open('../data/san_' + filename + '.tsv', 'w')

	current_line = file.readline()

	i = 1

	while current_line != '':
		splitedline = current_line.split('\t')
		
		currlen = len(splitedline)
		if currlen == 5:
			splitedline[3] = splitedline[3][2:][:-1].replace('\\xc3\\xa1', 'á')
			splitedline[3] = splitedline[3].replace('\\xc3\\xa9', 'é')
			splitedline[3] = splitedline[3].replace('\\xc3\\xad', 'í')
			splitedline[3] = splitedline[3].replace('\\xc3\\xb3', 'ó')
			splitedline[3] = splitedline[3].replace('\\xc3\\xba', 'ú')
			splitedline[3] = splitedline[3].replace('\\xc3\\xbc', 'ü')
			splitedline[3] = splitedline[3].replace('\\xc3\\x81', 'Á')
			splitedline[3] = splitedline[3].replace('\\xc3\\x89', 'É')
			splitedline[3] = splitedline[3].replace('\\xc3\\x8d', 'Í')
			splitedline[3] = splitedline[3].replace('\\xc3\\x93', 'Ó')
			splitedline[3] = splitedline[3].replace('\\xc3\\x9a', 'Ú')
			splitedline[3] = splitedline[3].replace('\\xc3\\x9c', 'Ü')
			splitedline[3] = splitedline[3].replace('\\xc3\\xb1', 'ñ')
			splitedline[3] = splitedline[3].replace('\\xc3\\x91', 'Ñ')
			splitedline[3] = splitedline[3].replace('\\xc2\\xbf', '¿')
			splitedline[3] = splitedline[3].replace('\\xc2\\xa1', '¡')
			filesan.write('\t'.join(splitedline))
		
		current_line = file.readline()
		
	file.close()
	filesan.close()

file_names = ['peruviantuits_by_user']

for file_name in file_names:
	print('Sanitizando ' + file_name)
	save_saniticed_tweets(file_name)