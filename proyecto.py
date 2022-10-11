#Proyecto Lenguajes y Automatas 7B - C1
#Verificación de estructura for en python

#Hiram Emilio Lache Toledo 203420

import tkinter as tk
from tkinter import filedialog 

#Interfaz
window = tk.Tk()
window.title('Validar estructura for en archivo python')
window.resizable(False, False)
window.geometry('1000x600')

scrollbar=tk.Scrollbar(window)
txt = tk.Text(window, width=35, height=24, wrap=tk.NONE, yscrollcommand=scrollbar.set)
scrollbar.config(command=txt.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


alfabeto= [' ',':','_','-','[',']','(',')', ',','"','0','1','2','3','4','5','6','7','8','9',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z',
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']

#Transiciones
q26_t = {" ": "q26", ":": "q27"}
q25_t = {" ": "q25", ")": "q26"}
q24_t = {" ": "q25", ")": "q26", '0': "q24",'1': "q24",'2': "q24",'3': "q24",'4': "q24",'5': "q24",'6': "q24",'7': "q24",'8': "q24",'9': "q24"}
q23_t = {'0': "q24",'1': "q24",'2': "q24",'3': "q24",'4': "q24",'5': "q24",'6': "q24",'7': "q24",'8': "q24",'9': "q24"}
q22_t = {" ": "q22", "-": "q23", '0': "q24",'1': "q24",'2': "q24",'3': "q24",'4': "q24",'5': "q24",'6': "q24",'7': "q24",'8': "q24",'9': "q24"}
q21_t = {" ": "q21", ",": "q22",')': "q26"}
q20_t = {" ": "q21", ",": "q22",')': "q26", '0': "q20",'1': "q20",'2': "q20",'3': "q20",'4': "q20",'5': "q20",'6': "q20",'7': "q20",'8': "q20",'9': "q20"}
q19_t = {'0': "q20",'1': "q20",'2': "q20",'3': "q20",'4': "q20",'5': "q20",'6': "q20",'7': "q20",'8': "q20",'9': "q20"}
q18_t = {" ": "q18", "-": "q19", '0': "q20",'1': "q20",'2': "q20",'3': "q20",'4': "q20",'5': "q20",'6': "q20",'7': "q20",'8': "q20",'9': "q20",')': "q26"}
q17_t = {" ": "q17", "(": "q18",':': "q27"}
q16_t = {" ": "q17", "(": "q18", "_": "q16", 'A':"q16",'B':"q16",'C':"q16",'D':"q16",'E':"q16",'F':"q16",'G':"q16",'H':"q16",'I':"q16",'J':"q16",'K':"q16",'L':"q16",'M':"q16",'N':"q16",'Ñ':"q16",'O':"q16",'P':"q16",'Q':"q16",'R':"q16",'S':"q16",'T':"q16",'U':"q16",'V':"q16",'W':"q16",'X':"q16",'Y':"q16",'Z':"q16"
,'a': "q16",'b': "q16",'c': "q16",'d': "q16",'e': "q16",'f': "q16",'g': "q16",'h': "q16",'i': "q16",'j': "q16",'k': "q16",'l': "q16",'m': "q16",'n': "q16",'ñ': "q16",'o': "q16",'p': "q16",'q': "q16",'r': "q16",'s': "q16",'t': "q16",'u': "q16",'v': "q16",'w': "q16",'x': "q16",'y': "q16",'z': "q16"
,'0': "q16",'1': "q16",'2': "q16",'3': "q16",'4': "q16",'5': "q16",'6': "q16",'7': "q16",'8': "q16",'9': "q16",':': "q27"}
q15_t = {',': "q10"," ": "q15",']': "q13"}
q14_t = {'"': "q15", " ": "q14", "_": "q14", "-": "q14", 'A':"q14",'B':"q14",'C':"q14",'D':"q14",'E':"q14",'F':"q14",'G':"q14",'H':"q14",'I':"q14",'J':"q14",'K':"q14",'L':"q14",'M':"q14",'N':"q14",'Ñ':"q14",'O':"q14",'P':"q14",'Q':"q14",'R':"q14",'S':"q14",'T':"q14",'U':"q14",'V':"q14",'W':"q14",'X':"q14",'Y':"q14",'Z':"q14"
,'a': "q14",'b': "q14",'c': "q14",'d': "q14",'e': "q14",'f': "q14",'g': "q14",'h': "q14",'i': "q14",'j': "q14",'k': "q14",'l': "q14",'m': "q14",'n': "q14",'ñ': "q14",'o': "q14",'p': "q14",'q': "q14",'r': "q14",'s': "q14",'t': "q14",'u': "q14",'v': "q14",'w': "q14",'x': "q14",'y': "q14",'z': "q14"
,'0': "q14",'1': "q14",'2': "q14",'3': "q14",'4': "q14",'5': "q14",'6': "q14",'7': "q14",'8': "q14",'9': "q14"}
q13_t = {" ": "q13",':': "q27"}
q12_t = {',': "q10"," ": "q12",']': "q13"}
q11_t = {',': "q10"," ": "q12",']': "q13" , '0': "q11",'1': "q11",'2': "q11",'3': "q11",'4': "q11",'5': "q11",'6': "q11",'7': "q11",'8': "q11",'9': "q11"}
q10_t = {" ": "q10", '0': "q11",'1': "q11",'2': "q11",'3': "q11",'4': "q11",'5': "q11",'6': "q11",'7': "q11",'8': "q11",'9': "q11",'"': "q14"}
q9_t = {" ": "q9", '[': "q10","_": "q16", 'A':"q16",'B':"q16",'C':"q16",'D':"q16",'E':"q16",'F':"q16",'G':"q16",'H':"q16",'I':"q16",'J':"q16",'K':"q16",'L':"q16",'M':"q16",'N':"q16",'Ñ':"q16",'O':"q16",'P':"q16",'Q':"q16",'R':"q16",'S':"q16",'T':"q16",'U':"q16",'V':"q16",'W':"q16",'X':"q16",'Y':"q16",'Z':"q16"
,'a': "q16",'b': "q16",'c': "q16",'d': "q16",'e': "q16",'f': "q16",'g': "q16",'h': "q16",'i': "q16",'j': "q16",'k': "q16",'l': "q16",'m': "q16",'n': "q16",'ñ': "q16",'o': "q16",'p': "q16",'q': "q16",'r': "q16",'s': "q16",'t': "q16",'u': "q16",'v': "q16",'w': "q16",'x': "q16",'y': "q16",'z': "q16"}
q8_t = {" ": "q9"}
q7_t = {"n": "q8"}
q6_t = {" ": "q6", "i": "q7"}
q5_t = {" ": "q6", "_": "q5", 'A':"q5",'B':"q5",'C':"q5",'D':"q5",'E':"q5",'F':"q5",'G':"q5",'H':"q5",'I':"q5",'J':"q5",'K':"q5",'L':"q5",'M':"q5",'N':"q5",'Ñ':"q5",'O':"q5",'P':"q5",'Q':"q5",'R':"q5",'S':"q5",'T':"q5",'U':"q5",'V':"q5",'W':"q5",'X':"q5",'Y':"q5",'Z':"q5"
,'a': "q5",'b': "q5",'c': "q5",'d': "q5",'e': "q5",'f': "q5",'g': "q5",'h': "q5",'i': "q5",'j': "q5",'k': "q5",'l': "q5",'m': "q5",'n': "q5",'ñ': "q5",'o': "q5",'p': "q5",'q': "q5",'r': "q5",'s': "q5",'t': "q5",'u': "q5",'v': "q5",'w': "q5",'x': "q5",'y': "q5",'z': "q5"
,'0': "q5",'1': "q5",'2': "q5",'3': "q5",'4': "q5",'5': "q5",'6': "q5",'7': "q5",'8': "q5",'9': "q5"}
q4_t = {" ": "q4", "_": "q5", 'A':"q5",'B':"q5",'C':"q5",'D':"q5",'E':"q5",'F':"q5",'G':"q5",'H':"q5",'I':"q5",'J':"q5",'K':"q5",'L':"q5",'M':"q5",'N':"q5",'Ñ':"q5",'O':"q5",'P':"q5",'Q':"q5",'R':"q5",'S':"q5",'T':"q5",'U':"q5",'V':"q5",'W':"q5",'X':"q5",'Y':"q5",'Z':"q5"
,'a': "q5",'b': "q5",'c': "q5",'d': "q5",'e': "q5",'f': "q5",'g': "q5",'h': "q5",'i': "q5",'j': "q5",'k': "q5",'l': "q5",'m': "q5",'n': "q5",'ñ': "q5",'o': "q5",'p': "q5",'q': "q5",'r': "q5",'s': "q5",'t': "q5",'u': "q5",'v': "q5",'w': "q5",'x': "q5",'y': "q5",'z': "q5"}
q3_t = {" ": "q4"}
q2_t = {"r": "q3"}
q1_t = {"o": "q2"}
q0_t = {"f": "q1"}

#Estados
grafo = { "q0": q0_t,"q1": q1_t,"q2": q2_t,"q3": q3_t, "q4": q4_t, "q5": q5_t, "q6": q6_t, "q7": q7_t, "q8": q8_t, "q9": q9_t, "q10": q10_t
, "q11": q11_t, "q12": q12_t, "q13": q13_t, "q14": q14_t, "q15": q15_t, "q16": q16_t, "q17": q17_t, "q18": q18_t, "q19": q19_t, "q20": q20_t
, "q21": q21_t, "q22": q22_t, "q23": q23_t, "q24": q24_t, "q25": q25_t, "q26": q26_t}
#q0 = q0     Qf = q27

def automata(values):
	estadoInicial = "q0"
	estadoActual = estadoInicial
	recorrido = []
	recorrido.append(estadoActual)

	for v in values:
		e = grafo[estadoActual]
		try:
			estadoActual = e[v]
			recorrido.append(estadoActual)
		except KeyError:
			txt.insert(tk.END,"\nResultado: Cadena no valida."+"\nCarater incorrecto: "+v+"\nEstado final: " +estadoActual)
			break

	if estadoActual == "q27":
		txt.insert(tk.END, recorrido)
		txt.insert(tk.END, "\nResultado: Cadena aceptada")
		
	txt.pack(fill=tk.X, padx=5)


def validate_data(values):
	validate = 0
	for v in values:
		if v in alfabeto:
			validate+=1
	if validate == len(values):
		automata(values)
	else:
		txt.insert(tk.END, "\nError de sintaxis. Se ingreso un caracter no valido")

def save_data(data):
	d = data.strip()
	values = list(d)	
	validate_data(values)


def get_data(path):
	with open(path) as archivo:
		lineas = archivo.readlines()
		for i in lineas:
			if "for " in i:
				if " in " in i:	
					txt.insert(tk.END, "\n----------------------------------------------------")
					txt.insert(tk.END, "\nCadena evaluada: "+i)
					save_data(i)
					txt.insert(tk.END, "\n----------------------------------------------------\n")

def validate_archive(path):
	if path != "":
		get_data(path)

def get_archive():
	window.filename = filedialog.askopenfilename(title="Seleccciona un archivo", filetypes=(("Python", "*.py"),))
	path = window.filename
	validate_archive(path)

def open_window():
	titulo = tk.Label(window, text="Agregar un archivo", bg = "#46685b", fg = "#fafafa", font=("Verdana",26), padx = 10, pady=20)
	titulo.pack(fill = tk.X)
	btn = tk.Button(window, text="Selecionar archivo", padx = 15, pady=12, command =  get_archive)
	btn.pack()
	window.mainloop()
			
if __name__=="__main__":
	open_window()