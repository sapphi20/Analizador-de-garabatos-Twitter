
def divide_file_in_size(file_name, batch_size):
	file = open(file_name, "r")
	i = 0
	while True:
		print("Creando archivo " + file_name.replace(".tsv","_batch" + str(i) + ".tsv") + " con batches tamanho " + str(batch_size))
		new_file = open(file_name.replace(".tsv","_batch" + str(i) + ".tsv"), "w")
		for j in range(batch_size):
			curr_line = file.readline()
			if curr_line == '':
				file.close()
				new_file.close()
				return
			new_file.write(curr_line)
		new_file.close()
		i += 1
		
file_names = ['../data/saniticed_tweets/san_peruviantuits_by_user.tsv']

for name in file_names:
	divide_file_in_size(name, 200000)
