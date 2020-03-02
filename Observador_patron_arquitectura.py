class observador:
     def __init__(self, nombre, sujeto):
         self.nombre = nombre
         sujeto.registro(self)

     def notificar(self, evento):
         print (self.nombre, "se recibe un evento", evento)

class sujeto:
     def __init__(self):
         self.observadores = []
 
     def registro(self, observador):
         self.observadores.append(observador)
 
     def baja(self, observador):
         self.observadores.remove(observador)
 
     def notificar_a_observadores(self, evento):
         for observador in self.observadores:
             observador.notificar(evento)

sujeto = sujeto()
observadorA = observador("<Observador A>", sujeto)
observadorB = observador("<Observador B>", sujeto)
print (sujeto.notificar_a_observadores("< hola se modifico algo desde la local>"))

