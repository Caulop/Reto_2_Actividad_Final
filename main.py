from abc import ABC, abstractmethod

class Movible (ABC):
    
    @abstractmethod
    def mover(self):
        pass
    
# Clase Motor (composicion)
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
            
# Clase abstracta Vehiculo
class Vehiculo(Movible):
    
    def __init__(self,placa):
        self.placa = placa
        self.motor = Motor ("Gasolina") # Composicion
        self.conductor = None # Agergacion
        
    def asignar_conductor(self, conductor):
        self.conductor = conductor
        print(f"conductor: {conductor.nombre} asignado Vehiculo con placa: {self.placa}")
    
    @abstractmethod
    def iniciar_jornada(self):
        pass

class Moto(Vehiculo):

    def __init__(self, placa, casco):
        super().__init__(placa)
        self.casco = casco

    def mover(self):
        print("La moto se está moviendo")

    def iniciar_jornada(self):
        if self.casco:
            print("Jornada iniciada para la moto")
        else:
            print("No puede iniciar: casco obligatorio")
    
class Carro(Vehiculo):
    
    def __init__(self, placa, revision_tecnica):
        super().__init__(placa)
        self.revision_tecnica = revision_tecnica
    
    def mover(self):
        print("El carro se esta moviendo")
        
    def iniciar_jornada(self):
        if self.revision_tecnica:
            print("Jornada iniciada por el carro")
        else:
            print("No puede iniciar jornada: Revision tecnica vencida")
            
class Camion(Vehiculo):
    
    def __init__(self, placa, planilla_carga, peso):
        super().__init__(placa)
        self.planilla_carga = planilla_carga
        self.peso = peso
        self.peso_maximo = 10000
    
    def mover(self):
        print("El camion se esta moviendo")
    
    def iniciar_jornada(self):
        if self.planilla_carga and self.peso <= self.peso_maximo:
            print("Jornada iniciada para el camion")
        else:
            print("No puede iniciar jornada: problemas con la carga o el peso")

# Clase conductor

class Conductor:
    
    def __init__(self, nombre, documento, licencia):
        self.nombre = nombre
        self.documento = documento
        self.licencia = licencia

if __name__=="__main__":
    
    Conductor1 = Conductor("Carlos", 41003744, "A2")
    Conductor2 = Conductor("Andres", 75462025, "B1")
    Conductor3 = Conductor("Jose", 41907178, "C2") 
    
    moto = Moto("ABC, 123", casco = False)
    carro = Carro ("XYZ, 567", revision_tecnica = True)
    camion = Camion("CAM, 457", planilla_carga = False, peso = 10000)
    
    moto.asignar_conductor(Conductor1)
    moto.iniciar_jornada()
    carro.asignar_conductor(Conductor2)
    carro.iniciar_jornada()
    camion.asignar_conductor(Conductor3)
    camion.iniciar_jornada() 