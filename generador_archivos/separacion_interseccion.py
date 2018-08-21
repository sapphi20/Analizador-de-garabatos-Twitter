nombre_archivo_chile = ""
nombre_archivo_argentina = ""
nombre_archivo_peru = ""
nombre_archivo_inter = ""

file_chile = open(nombre_archivo_chile + ".tsv", "r")
file_argentina = open(nombre_archivo_argentina + ".tsv", "r")
file_peru = open(nombre_archivo_peru + ".tsv", "r")
file_inter = open(nombre_archivo_inter + ".tsv", "r")

out_chile = open("out_chile.tsv", "w")
out_argentina = open("out_argentina.tsv", "w")
out_peru = open("out_peru.tsv", "w")

lineas_inter = file_inter.readlines()
file_inter.close()

current_line = file_argentina.readline()
while current_line != "":
	splited_line = current_line.split("\t")
	if not (splited_line[0] in lineas_inter):
		out_chile.write(current_line)
		
	current_line = file_argentina.readline()

current_line = file_chile.readline()
while current_line != "":
	splited_line = current_line.split("\t")
	if not (splited_line[0] in lineas_inter):
		out_argentina.write(current_line)
		
	current_line = file_chile.readline()

current_line = file_peru.readline()
while current_line != "":
	splited_line = current_line.split("\t")
	if not (splited_line[0] in lineas_inter):
		out_peru.write(current_line)
		
	current_line = file_peru.readline()

	

file_chile.close()
file_argentina.close()
file_peru.close()

out_chile.close()
out_argentina.close()
out_peru.close()


