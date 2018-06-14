def mas_s(pal):
	if pal[len(pal) - 1] in ['a','e','o']:
		return True
	return False

def chxx(pal):
	
	splited = pal.split("ch")
	
	aux = []
	aux2 = [splited[0]]
	
	for frag in splited[1:]:
		
		aux = []
		for s in aux2:
			aux.append(s + 'x' + frag)
			aux.append(s + 'ch' + frag)
		
		aux2 = []
		for s in aux:
			aux2.append(s)
	
	return aux

def reducir_silabas(pal):
	splited = pal.split("a")
	new_pal = splited[0]
	for frag in splited[1:]:
		if frag == "":
			new_pal += 'a' + frag
	
	for silaba in ['e','i','o','u']:
		splited = new_pal.split(silaba)
		new_pal = splited[0]
		for frag in splited[1:]:
			if frag != "":
				new_pal += silaba + frag
	
	return new_pal