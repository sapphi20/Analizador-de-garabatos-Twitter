
def save_saniticed_tweets(filename):
	file = open(filename + '.tsv', 'r')
	filesan = open('san_' + filename + '.tsv', 'w')

	current_line = file.readline()

	i = 1

	while current_line != '':
		splitedline = current_line.split('\t')
		
		currlen = len(splitedline)
		while currlen < 5:
			current_line = file.readline()
			newsplitedline = current_line.split('\t')
			splitedline[len(splitedline) - 1] = splitedline[len(splitedline) - 1].replace('\n','') + '[:enter:]' + newsplitedline[0]
			splitedline += newsplitedline[1:]
			currlen += len(newsplitedline) - 1
		
		filesan.write('\t'.join(splitedline))
		
		current_line = file.readline()
		
	file.close()
	filesan.close()
	
def get_users(filename):
	file = open('san_' + filename + '.tsv', 'r')
	fileus = open('users_' + filename + '.tsv', 'w')

	current_line = file.readline()
	dict = {}
	while current_line != '':
		splitedline = current_line.split('\t')
		user = splitedline[1]
		if not user in dict:
			fileus.write(user + '\n')
			dict[user] = 1
		
		current_line = file.readline()
		
	file.close()
	fileus.close()
	
file_names = ['argentineantuits','chileantuits','peruviantuits']

for file_name in file_names:
	print('Sanitizando ' + file_name)
	save_saniticed_tweets(file_name)
	print('Sacando Usuarios de san_' + file_name)
	get_users(file_name)