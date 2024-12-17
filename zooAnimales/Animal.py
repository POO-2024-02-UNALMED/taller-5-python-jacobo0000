from zooAnimales import Mamifero, Anfibio, Ave, Pez, Reptil

class Animal:
  totalAnimales = 0
  def __init__(self):
    self.__init__("",0,"","")

  def __init__(self,nombre,edad,habitat,genero):
    self.nombre = nombre
    self.edad = edad
    self.habitat = habitat
    self.genero = genero
    self.zona = None

  def totalPortipo(self):
    return f"Mamiferos : {Mamifero.cantidadMamiferos()}\nAves : {Ave.cantidadAnfibios()}\nReptiles : {Reptil.cantidadReptiles()}\nPeces : {Pez.cantidadPeces()}\nAnfibios : {Anfibio.cantidadAnfibios()}"

  def toString(self):
    if self.zona == None:
      return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi genero es {self.genero}"
    else:
      return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi genero es {self.genero}, la zona en la que me ubico es {self.zona}, en el zoo {self.zona.zoo}"
    
  def movimiento(self):
    return "desplazarse"
  
  def getNombre(self):
    return self.nombre
  
  def getEdad(self):
    return self.edad
  
  def getHabitat(self):
    return self.habitat
  
  def getGenero(self):
    return self.genero
  
  @classmethod
  def getTotalAnimales(cls):
    return cls.totalAnimales
  
  def setNombre(self,nombre):
    self.nombre = nombre

  def setEdad(self,edad):
    self.edad = edad

  def setHabitat(self,habitat):
    self.habitat = habitat

  def setGenero(self,genero):
    self.genero = genero