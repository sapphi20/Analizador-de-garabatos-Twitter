current_gram = 4

nombre_archivo_chile = "../data/chile/" + str(current_gram) + "gram/part-r-00000"
nombre_archivo_argentina = "../data/argentina/" + str(current_gram) + "gram/part-r-00000"
nombre_archivo_peru = "../data/peru/" + str(current_gram) + "gram/part-r-00000"
nombre_archivo_inter = "../data/intersecciones/interseccion_" + str(current_gram) + "gram.tsv"

file_chile = open(nombre_archivo_chile, "r")
file_argentina = open(nombre_archivo_argentina, "r")
file_peru = open(nombre_archivo_peru, "r")
file_inter = open(nombre_archivo_inter, "r")

out_chile = open("out_chile_" + str(current_gram) + "gram.tsv", "w")
out_argentina = open("out_argentina_" + str(current_gram) + "gram.tsv", "w")
out_peru = open("out_peru_" + str(current_gram) + "gram.tsv", "w")

lineas_inter = file_inter.readlines()
file_inter.close()

current_line = file_argentina.readline()
while current_line != "":
	splited_line = current_line.split("\t")
	bool = False
	for linea in lineas_inter:
		if linea.replace("\n","") == splited_line[0].replace("\n",""):
			bool = True
	
	if not bool:
		out_argentina.write(current_line)
	
	current_line = file_argentina.readline()

current_line = file_chile.readline()
while current_line != "":
	splited_line = current_line.split("\t")
	bool = False
	for linea in lineas_inter:
		if linea.replace("\n","") == splited_line[0].replace("\n",""):
			bool = True
	
	if not bool:
		out_chile.write(current_line)
	
	current_line = file_chile.readline()

current_line = file_peru.readline()
while current_line != "":
	splited_line = current_line.split("\t")
	bool = False
	for linea in lineas_inter:
		if linea.replace("\n","") == splited_line[0].replace("\n",""):
			bool = True
	
	if not bool:
		out_peru.write(current_line)
	
	current_line = file_peru.readline()


file_chile.close()
file_argentina.close()
file_peru.close()

out_chile.close()
out_argentina.close()
out_peru.close()


