
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

listapacientes={}

def menupacientes():
    while True:
        print('1. Ingresar un paciente')
        print('2. Ver lista de pacientes')
        print('3. Salir')
        opcion = int(input('Ingrese una opción: '))

        if opcion == 1:
            p1 = Paciente()
            p1.asignarNombre(input('Ingrese el nombre del paciente: '))
            p1.asignarCedula(input('Ingrese la cedula del paciente: '))
            p1.asignarGenero(input('Ingrese el genero del paciente: '))
            p1.asignarServicio(input('Ingrese el servicio que requiere el paciente: '))
            listapacientes[p1.verCedula()] = p1

        elif opcion == 2:
            for cedula, paciente in listapacientes.items():
                print(f'Nombre: {paciente.verNombre()}')
                print(f'Cedula: {paciente.verCedula()}')
                print(f'Genero: {paciente.verGenero()}')
                print(f'Servicio: {paciente.verServicio()}')
                print()

        elif opcion == 3:
            print('Saliendo...')
            break


listaempleados={}

def menuempleados():
    while True:
        print('1. Ingresar un empleado')
        print('2. Ver lista de empleados')
        print('3. Salir')
        opcion = int(input('Ingrese una opción: '))

        if opcion == 1:
            e1 = Empleado_Hospital()
            e1.asignarNombre(input('Ingrese el nombre del empleado: '))
            e1.asignarCedula(input('Ingrese la cedula del empleado: '))
            e1.asignarGenero(input('Ingrese el genero del empleado: '))
            e1.asignarTurno(input('Ingrese el turno del empleado: '))
            listaempleados[e1.verCedula()] = e1

        elif opcion == 2:
            for cedula, empleado in listaempleados.items():
                print(f'Nombre: {empleado.verNombre()}')
                print(f'Cedula: {empleado.verCedula()}')
                print(f'Genero: {empleado.verGenero()}')
                print(f'Turno: {empleado.verturno()}')
                print()

        elif opcion == 3:
            print('Saliendo...')
            break

listaenfermeras={}

def menuenfermeras():
    while True:
        print('1. Ingresar una enfermera')
        print('2. Ver lista de enfermeras') 
        print('3. Salir')

        opcion = int(input('Ingrese una opción: '))

        if opcion == 1:
            en1 = Enfermera()
            en1.asignarNombre(input('Ingrese el nombre de la enfermera: '))
            en1.asignarCedula(input('Ingrese la cedula de la enfermera: '))
            en1.asignarGenero(input('Ingrese el genero de la enfermera: '))
            en1.asignarTurno(input('Ingrese el turno de la enfermera: '))
            en1.asignarRango(input('Ingrese el rango de la enfermera: '))
            listaenfermeras[en1.verCedula()] = en1

        elif opcion == 2:
            for cedula, enfermera in listaenfermeras.items():
                print(f'Nombre: {enfermera.verNombre()}')
                print(f'Cedula: {enfermera.verCedula()}')
                print(f'Genero: {enfermera.verGenero()}')
                print(f'Turno: {enfermera.verturno()}')
                print(f'Rango: {enfermera.verRango()}')

        elif opcion == 3:
            print('Saliendo...')    
            break


listamedicos={}

def menumedicos():
    while True:
        print('1. Ingresar un medico')
        print('2. Ver lista de medicos')
        print('3. Salir')

        opcion = int(input('Ingrese una opción: '))

        if opcion == 1:
            m1 = Medico()
            m1.asignarNombre(input('Ingrese el nombre del medico: '))
            m1.asignarCedula(input('Ingrese la cedula del medico: '))
            m1.asignarGenero(input('Ingrese el genero del medico: '))
            m1.asignarTurno(input('Ingrese el turno del medico: '))
            m1.asignarEspecialidad(input('Ingrese la especialidad del medico: '))
            listamedicos[m1.verCedula()] = m1   

        elif opcion == 2:
            for cedula, medico in listamedicos.items():
                print(f'Nombre: {medico.verNombre()}')
                print(f'Cedula: {medico.verCedula()}')
                print(f'Genero: {medico.verGenero()}')
                print(f'Turno: {medico.verturno()}')
                print(f'Especialidad: {medico.verEspecialidad()}')

        elif opcion == 3:
            print('Saliendo...')
            break

def menuhospital():
    while True:
        print('1. Ver menu de pacientes')
        print('2. Ver menu de empleados')
        print('3. Ver menu de enfermeras')
        print('4. Ver menu de medicos')
        print('5. Salir')

        opcion = int(input('Ingrese una opción: '))

        if opcion == 1:
            menupacientes()
        elif opcion == 2: 
            menuempleados()
        elif opcion == 3:
            menuenfermeras()
        elif opcion == 4:
            menumedicos()
        elif opcion == 5:  
            print('Saliendo...')
            break

menuhospital()




          