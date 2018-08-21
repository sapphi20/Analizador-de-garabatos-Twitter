current_gram = 4

nombre_archivo_chile = "../data/chile/" + str(current_gram) + "gram/part-r-00000"
nombre_archivo_argentina = "../data/argentina/" + str(current_gram) + "gram/part-r-00000"
nombre_archivo_peru = "../data/peru/" + str(current_gram) + "gram/part-r-00000"
nombre_archivo_inter = "interseccion_" + str(current_gram) + "gram.tsv"

file_chile = open(nombre_archivo_chile, "r")
file_argentina = open(nombre_archivo_argentina, "r")
file_peru = open(nombre_archivo_peru, "r")
file_inter = open(nombre_archivo_inter, "w")


lineas_inter = []

lineas_argentina = file_argentina.readlines()
lineas_chile = file_chile.readlines()
lineas_peru = file_peru.readlines()

for i in range(len(lineas_argentina)):
	lineas_argentina[i] = lineas_argentina[i].split("\t")[0]

for i in range(len(lineas_chile)):
	lineas_chile[i] = lineas_chile[i].split("\t")[0]

for i in range(len(lineas_peru)):
	lineas_peru[i] = lineas_peru[i].split("\t")[0]
	
for linea in lineas_argentina:
	if (linea in lineas_chile) and (linea in lineas_peru):
		file_inter.write(linea)

file_chile.close()
file_argentina.close()
file_peru.close()
file_inter.close()

