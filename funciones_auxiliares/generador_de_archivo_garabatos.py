from generadores_de_variaciones import *

file = open("../data/lista_garabatos.txt", "r")
new_file = open("../data/new_lista_garabatos.txt","w+")


word = file.readline()
while(word != ''):
	has_pal = True

	for pal in chxx(word[:-1].lower()):
		new_file.write(pal.lower() + "\n")
		print(pal)
		if mas_s(pal):
			new_file.write(pal + "s\n")
			print(pal.lower() + "s")
		has_pal = False
	
	if (has_pal):
		print(word[:-1].lower())
		new_file.write(word[:-1].lower() + "\n")
		
		if mas_s(word[:-1]):
			new_file.write(word[:-1].lower() + "s\n")
			print(word[:-1].lower() + "s")
	word = file.readline()
	
file.close()
new_file.close()