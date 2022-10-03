#Proyecto Lenguajes y Automatas 7B - C1
#Verificación de estructura for en python

#Hiram Emilio Lache Toledo 203420

import tkinter as tk
from tkinter import filedialog 

#Interfaz
window = tk.Tk()
window.title('Validar estructura for en archivo python')
window.resizable(False, False)
window.geometry('950x500')

scrollbar=tk.Scrollbar(window)
txt = tk.Text(window, width=35, height=20, wrap=tk.NONE, yscrollcommand=scrollbar.set)
scrollbar.config(command=txt.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


alfabeto= [' ',':','_','-','[',']','(',')', ',','"','0','1','2','3','4','5','6','7','8','9',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z',
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']

#Transiciones
q19_t = {':': "q20"}
q18_t = {'0': "q18",'1': "q18",'2': "q18",'3': "q18",'4': "q18",'5': "q18",'6': "q18",'7': "q18",'8': "q18",'9': "q18",')': "q19"}
q17_t = {'0': "q18",'1': "q18",'2': "q18",'3': "q18",'4': "q18",'5': "q18",'6': "q18",'7': "q18",'8': "q18",'9': "q18"}
q16_t = {'-': "q17",'0': "q18",'1': "q18",'2': "q18",'3': "q18",'4': "q18",'5': "q18",'6': "q18",'7': "q18",'8': "q18",'9': "q18"}
q15_t = {',': "q16",'0': "q15",'1': "q15",'2': "q15",'3': "q15",'4': "q15",'5': "q15",'6': "q15",'7': "q15",'8': "q15",'9': "q15",')': "q19"}
q14_t = {'0': "q15",'1': "q15",'2': "q15",'3': "q15",'4': "q15",'5': "q15",'6': "q15",'7': "q15",'8': "q15",'9': "q15"}
q13_t = {'-': "q14",'0': "q15",'1': "q15",'2': "q15",'3': "q15",'4': "q15",'5': "q15",'6': "q15",'7': "q15",'8': "q15",'9': "q15",')': "q19"}
q12_t = {'_':"q12",'A':"q12",'B':"q12",'C':"q12",'D':"q12",'E':"q12",'F':"q12",'G':"q12",'H':"q12",'I':"q12",'J':"q12",'K':"q12",'L':"q12",'M':"q12",'N':"q12",'Ñ':"q12",'O':"q12",'P':"q12",'Q':"q12",'R':"q12",'S':"q12",'T':"q12",'U':"q12",'V':"q12",'W':"q12",'X':"q12",'Y':"q12",'Z':"q12"
,'a': "q12",'b': "q12",'c': "q12",'d': "q12",'e': "q12",'f': "q12",'g': "q12",'h': "q12",'i': "q12",'j': "q12",'k': "q12",'l': "q12",'m': "q12",'n': "q12",'ñ': "q12",'o': "q12",'p': "q12",'q': "q12",'r': "q12",'s': "q12",'t': "q12",'u': "q12",'v': "q12",'w': "q12",'x': "q12",'y': "q12",'z': "q12"
,'0': "q12",'1': "q12",'2': "q12",'3': "q12",'4': "q12",'5': "q12",'6': "q12",'7': "q12",'8': "q12",'9': "q12", '(': "q13", ':': "q20"}
q11_t = {':': "q20"}
q10_t = {',': "q7",']': "q11"}
q9_t = {'A':"q9",'B':"q9",'C':"q9",'D':"q9",'E':"q9",'F':"q9",'G':"q9",'H':"q9",'I':"q9",'J':"q9",'K':"q9",'L':"q9",'M':"q9",'N':"q9",'Ñ':"q9",'O':"q9",'P':"q9",'Q':"q9",'R':"q9",'S':"q9",'T':"q9",'U':"q9",'V':"q9",'W':"q9",'X':"q9",'Y':"q9",'Z':"q9"
,'a': "q9",'b': "q9",'c': "q9",'d': "q9",'e': "q9",'f': "q9",'g': "q9",'h': "q9",'i': "q9",'j': "q9",'k': "q9",'l': "q9",'m': "q9",'n': "q9",'ñ': "q9",'o': "q9",'p': "q9",'q': "q9",'r': "q9",'s': "q9",'t': "q9",'u': "q9",'v': "q9",'w': "q9",'x': "q9",'y': "q9",'z': "q9"
,'0': "q9",'1': "q9",'2': "q9",'3': "q9",'4': "q9",'5': "q9",'6': "q9",'7': "q9",'8': "q9",'9': "q9", '"': "q10"}
q8_t = {',': "q7",'0': "q8",'1': "q8",'2': "q8",'3': "q8",'4': "q8",'5': "q8",'6': "q8",'7': "q8",'8': "q8",'9': "q8",']': "q11"}
q7_t = {'0': "q8",'1': "q8",'2': "q8",'3': "q8",'4': "q8",'5': "q8",'6': "q8",'7': "q8",'8': "q8",'9': "q8",'"': "q9"}
q6_t = {"[": "q7", '_':"q12",'A':"q12",'B':"q12",'C':"q12",'D':"q12",'E':"q12",'F':"q12",'G':"q12",'H':"q12",'I':"q12",'J':"q12",'K':"q12",'L':"q12",'M':"q12",'N':"q12",'Ñ':"q12",'O':"q12",'P':"q12",'Q':"q12",'R':"q12",'S':"q12",'T':"q12",'U':"q12",'V':"q12",'W':"q12",'X':"q12",'Y':"q12",'Z':"q12"
,'a': "q12",'b': "q12",'c': "q12",'d': "q12",'e': "q12",'f': "q12",'g': "q12",'h': "q12",'i': "q12",'j': "q12",'k': "q12",'l': "q12",'m': "q12",'n': "q12",'ñ': "q12",'o': "q12",'p': "q12",'q': "q12",'r': "q12",'s': "q12",'t': "q12",'u': "q12",'v': "q12",'w': "q12",'x': "q12",'y': "q12",'z': "q12"}
q5_t = {"n": "q6"}
q4_t = {"i": "q5"}
q3_t = {"_": "q4", 'A':"q4",'B':"q4",'C':"q4",'D':"q4",'E':"q4",'F':"q4",'G':"q4",'H':"q4",'I':"q4",'J':"q4",'K':"q4",'L':"q4",'M':"q4",'N':"q4",'Ñ':"q4",'O':"q4",'P':"q4",'Q':"q4",'R':"q4",'S':"q4",'T':"q4",'U':"q4",'V':"q4",'W':"q4",'X':"q4",'Y':"q4",'Z':"q4"
,'a': "q4",'b': "q4",'c': "q4",'d': "q4",'e': "q4",'f': "q4",'g': "q4",'h': "q4",'i': "q4",'j': "q4",'k': "q4",'l': "q4",'m': "q4",'n': "q4",'ñ': "q4",'o': "q4",'p': "q4",'q': "q4",'r': "q4",'s': "q4",'t': "q4",'u': "q4",'v': "q4",'w': "q4",'x': "q4",'y': "q4",'z': "q4"}
q2_t = {"r": "q3"}
q1_t = {"o": "q2"}
q0_t = {"f": "q1"}

#Estados
grafo = { "q0": q0_t,"q1": q1_t,"q2": q2_t,"q3": q3_t, "q4": q4_t, "q5": q5_t, "q6": q6_t, "q7": q7_t, "q8": q8_t, "q9": q9_t, "q10": q10_t
, "q11": q11_t, "q12": q12_t, "q13": q13_t, "q14": q14_t, "q15": q15_t, "q16": q16_t, "q17": q17_t, "q18": q18_t, "q19": q19_t}
#q0 = q0     Qf = q20


def automata(values):
	estadoInicial = "q0"
	estadoActual = estadoInicial

	recorrido = []
	recorrido.append(estadoActual)

	for v in values:
		estado = grafo[estadoActual]
		try:
			estadoActual = estado[v]
			recorrido.append(estadoActual)
		except KeyError:
			charError = v
			break

	
	if estadoActual == "q20":
		txt.insert(tk.END, recorrido)
		txt.insert(tk.END, "\nResultado: Cadena aceptada")
	else:
		txt.insert(tk.END,"\nResultado: Cadena no valida."+"\nCarater incorrecto: "+charError+"\nEstado final: " +estadoActual)
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
	d = data.replace(" ","")
	values = list(d)
	for i in values: 
		if i == " ": 
			values.remove(" ")
		if i == "\t": 
			values.remove("\t")
		if i == "\n": 
			values.remove("\n")
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




