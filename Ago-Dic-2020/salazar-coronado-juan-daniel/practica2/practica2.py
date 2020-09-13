class Estudiante():
    def __init__(self, nombre, edad, semestre, carrera):
        self.nombre = nombre
        self.edad = edad
        self.semestre = semestre
        self.carrera = carrera

    def presentacion(self):
        return "Soy " + self.nombre + ", tengo " + self.edad + " años y estoy en " + self.semestre + " semestre."

    def getCarrera(self):
        carreras = {
        'ISC': "Ing. En sistemas computacionales",
        'IIS': "Ing. Industrial y de sistemas",
        'IEC': "Ing. En electronica y comunicaciones",
        'ITC': "Ingeniero en tecnología y comunicaciones",
        'LSA': "Lic. En sistemas computacionales y administrativos",
        'IA': "Ingeniero automotriz"
        }
        return "Estudio la carrera de " + carreras.get(self.carrera)
    
    def MotivacionPromedio(self, promedio):
        if promedio >= 70 and promedio <= 79:
            return "necesito esforzarme más"
        elif promedio > 79 and promedio <= 89:
            return "lo estoy haciendo bien, pero puedo hacerlo mejor"
        elif promedio >= 90 and promedio <= 100:
            return "voy muy bien, debo seguir así"
        else:
            return "-> promedio fuera de los parametros normales <-"

class ServicioSocialYPracticas(Estudiante):
    def __init__(self, nombre, edad, semestre, carrera, servicio, practicas):
        Estudiante.__init__(self, nombre, edad, semestre, carrera)
        self.servicio = servicio
        self.practicas = practicas
        
    def Estado(self):
        if self.servicio == True and self.practicas == True:
            return "Ya realice el servicio social y las practicas profesionales"
        elif self.servicio == False and self.practicas == False:
            return "No he realizado el servicio social ni las practicas profesionales"
        elif self.servicio == True and self.practicas == False:
            return "Ya realice el servicio social pero no he realizado las practicas profesionales"
        elif self.servicio == False and self.practicas == True:
            return "No he realizado el servicio social pero ya realice las practicas profesionales"

    def ProgramasServicio(self):
        programas = ['Identidad institucional', 'Asistente de investigación', 'Pagina Web Sistemas']
        if self.servicio == False:
            print("Puedes realizar el servicio social en los siguientes programas: ")
            return programas

    def EmpresasPracticas(self):
        empresas = ['Banamex', 'Central de talento universitario SC', 'Tecno Profesionales Rubik']
        if self.practicas == False:
            print("Puedes realizar las practicas profesionales en las siguientes empresas: ")
            return empresas

estudiante1 = Estudiante("Daniel", "21", "Septimo", "ISC")

print(estudiante1.presentacion())
print(estudiante1.getCarrera())
print("En base a mi promedio " + estudiante1.MotivacionPromedio(88.34))

estudiante1ssyp = ServicioSocialYPracticas("Daniel", "21", "Septimo", "ISC", False, False)

print(estudiante1ssyp.Estado())
print(estudiante1ssyp.ProgramasServicio())
print(estudiante1ssyp.EmpresasPracticas())

