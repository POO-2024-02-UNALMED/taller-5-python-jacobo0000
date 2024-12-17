from .animal import Animal

class Anfibio(Animal):
  ranas = 0
  salamandras = 0
  listado = []
  def __init__(self):
    self.__init__("",0,"","","",False)

  def __init__(self,nombre,edad,habitat,genero,colorPiel,venenoso):
    super().__init__(nombre,edad,habitat,genero)
    self.colorPiel = colorPiel
    self.venenoso = venenoso
    Anfibio.listado.append(self)
  
  @classmethod
  def cantidadAnfibios(cls):
    return len(cls.listado)
  
  def movimiento(self):
    return "saltar"
  
  @classmethod
  def crearRana(cls,nombre,edad,genero):
    a = cls(nombre,edad,"selva",genero,"rojo","true")
    cls.ranas += 1
    return a 
  @classmethod
  def crearSalamandra(cls,nombre,edad,genero):
    a =cls(nombre,edad,"negro y amarillo",genero,"rojo","false")
    cls.salamandras += 1
    return a