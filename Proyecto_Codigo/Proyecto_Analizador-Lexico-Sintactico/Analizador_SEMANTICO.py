txt = " "
cont = 0
def incrementarCont():
	global cont
	cont +=1
	return "%d" %cont

class Nodo():
	pass

class p_inicio(Nodo):
	def __init__(self, son1, name):
		self.name = name
		self.son1 = son1
	
	def imprimir(ident):
		self.son1.imprimir(" " +  ident)
		print ident + "Nodo: " + self.name

	def traducir(self):
		global txt
		id = incrementarCont()
		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + "->"+son1+"\n\t"

		return "digraph G {\n\t"+txt+"}"

    

def principal(Nodo):
	def __init__(self, name):
		self.name = name
	
	def imprimir(ident):
		self.son1.imprimir(" " +  ident)

	def traducir(self):
		global txt
		id = incrementarCont()

		return id
    

def variable_declaracion(Nodo):
	def __init__(self, name):
		self.name = name
	
	def imprimir(ident):
		self.son1.imprimir(" " +  ident)

	def traducir(self):
		global txt
		id = incrementarCont()

		return id
    

def variable_asignacion(Nodo):
	def __init__(self, name):
		self.name = name
	
	def imprimir(ident):
		self.son1.imprimir(" " +  ident)

	def traducir(self):
		global txt
		id = incrementarCont()

		return id
    

def exp_aritmetica(Nodo):
	def __init__(self, name):
		self.name = name
	
	def imprimir(ident):
		self.son1.imprimir(" " +  ident)

	def traducir(self):
		global txt
		id = incrementarCont()

		return id
    

def expresion(Nodo):
	def __init__(self, name):
		self.name = name
	
	def imprimir(ident):
		self.son1.imprimir(" " +  ident)

	def traducir(self):
   global      txt
   id = incrementarCont()

   return id


def termino(Nodo):
	def __init__(self, name):
		self.name = name
	
	def imprimir(ident):
		self.son1.imprimir(" " +  ident)

	def traducir(self):
		global txt
		id = incrementarCont()

		return id
    
    
def factor(Nodo):
	def __init__(self, name):
		self.name = name
	
	def imprimir(ident):
		self.son1.imprimir(" " +  ident)

	def traducir(self):
		global txt
		id = incrementarCont()

		return id
    
    
def error(Nodo):
	def __init__(self, name):
		self.name = name
	
	def imprimir(ident):
		self.son1.imprimir(" " +  ident)

	def traducir(self):
		global txt
		id = incrementarCont()

		return id
    
