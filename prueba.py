def get_List1():
	return ["a", 19, "qz"]

def prueba():
	l____ = ["5","6","7"]
	data = ["aaa", "b", "Z"]
	#Se espera aceptación
	for a in l____:
		print(a) 
	#Se espera aceptación
	for A in ["1","2","3"]:
		print(A)
	#Se espera aceptación
	for Z in [1,"2"]:
		print(Z)
	#Se espera aceptación
	for _ in range(5):
		print("3")
	#Se espera NO aceptación
	for xFDa in range(-5, 7):
		print("5")
	#Se espera NO aceptación		
	for 9n in data:
		print(9n)
	#Se espera aceptación
	for g in get_List1():
		print(g)
	#Se espera NO aceptación
	for *AB in range(4):
		print(*AB)
	#Se espera NO aceptación
	for datos in range(-5,-1):
		print(datos)

if __name__=="__main__":
	prueba()


