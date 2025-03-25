class Persona():
    tipo= "Mamifero"
    def __init__(self ):
        self.__nombre =""
        self.__cedula =0
        self.__genero = ""
#Propiedades
    # Setters
    def asignarNombre(self,h):
        self.__nombre = h
    def asignarCedula(self,h):
        self.__cedula = h
    def asignarGenero(self,h):
        self.__genero = h

    # getters 
    def verNombre(self): 
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verGenero(self):
        return self.__genero
    
    #deleters
    def borrarNombre(self):
        del self.__nombre
    def borrarCedula(self):
        del self.__cedula
    def borrarGenero(self):
        del self.__genero
        
# Métodos adicionales segun la abstracción hecha 
    def caminar(self):        
        print(input("ingrese direccion: "))
    def comer(self):
        print(input("Ingrese la comida que desea: "))

class Paciente(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.__servicio = ""

    def asignarServicio(self, servicio):
        self.__servicio = servicio
    def verServicio(self):
        return self.__servicio

class Empleado_Hospital(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.__turno = ''

    def asignarTurno(self, turno):
        self.__turno = turno

    def verturno(self):
        return self.__turno

class Enfermera(Empleado_Hospital):
    def __init__(self):
        # Empleado_Hospital.__init__(self) # Invocando el constructor de la clase padre de la cual esta heredando 
        super().__init__() # Este metodo hace exactamente lo mismo que le anterior, invocar el constructor de la clase padre 
        self.__rango = ''

    def asignarRango(self, rango):
        self.__rango = rango
    def verRango(self):
        return self.__rango

class Medico(Empleado_Hospital):
    def __init__(self):
        Empleado_Hospital.__init__(self)
        
        self.__especialidad = ''
    
    def asignarEspecialidad(self, especialidad):
        self.__especialidad = ''
    def verEspecialidad(self):
        return self.__especialidad

class Sistema():
    def __init__(self):
        self.__lista_pacientes = []
    
    def ingresarPaciente(self, pac):
        self.__lista_pacientes.append(pac)
    
    def verDatosPaciente(self, c):
        # Voy a buscar paciente por paciente
        for p in self.__lista_pacientes:
            # Por cada paciente de la lista, le digo al paciente que me
            # retorne la cédula y la comparo con la ingresada por teclado
            if c == p.verCedula():
                return p  # Si encuentro el paciente lo retorno
    
    def verNumeroPacientes(self):
        print('En el sistema hay: ' + str(len(self.__lista_pacientes)) + ' pacientes')

def main():
    sis = Sistema()
    while True:
        print('\n--- Menú del Sistema Hospitalario ---')
        print('1. Ingresar nuevo paciente')
        print('2. Ver datos de un paciente')
        print('3. Ver número total de pacientes')
        print('0. Salir')
        
        try:
            opcion = int(input('Seleccione una opción: '))
        except ValueError:
            print('Por favor, ingrese un número válido.')
            continue
        
        if opcion == 1:
            # Ingreso pacientes
            print('A continuación se solicitarán los datos del paciente...')
            nombre = input('Ingrese el nombre: ')
            cedula = int(input('Ingrese la cédula: '))
            genero = input('Ingrese el género: ')
            servicio = input('Ingrese el servicio: ')
            
            pac = Paciente()
            pac.asignarNombre(nombre)
            pac.asignarCedula(cedula)
            pac.asignarGenero(genero)
            pac.asignarServicio(servicio)
            
            sis.ingresarPaciente(pac)
            print("Paciente ingresado exitosamente.")
        
        elif opcion == 2:
            # Ver datos de un paciente
            c = int(input('Ingrese la cédula del paciente a buscar: '))
            p = sis.verDatosPaciente(c)
            if p:
                print("Nombre: " + p.verNombre())
                print("Cédula: " + str(p.verCedula()))
                print("Género: " + p.verGenero())
                print("Servicio: " + p.verServicio())
            else:
                print("Paciente no encontrado.")
        
        elif opcion == 3:
            # Ver número total de pacientes
            sis.verNumeroPacientes()
        
        elif opcion == 0:
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

# Acá el Python descubre cuál es la función principal
if __name__ == '__main__':
    main()


