from .animal import Animal

class Pez(Animal):
  listado = []
  salmones = 0
  bacalaos = 0

  def __init__(self):
    self.__init__("",0,"","","",0)

  def __init__(self,nombre,edad,habitat,genero,colorEscamas,cantidadAletas):
    super().__init__(nombre,edad,habitat,genero)
    self.colorEscamas = colorEscamas
    self.cantidadAletas = cantidadAletas
    Pez.listado.append(self)
  
  def movimiento(self):
    return "nadar"
  
  @classmethod
  def cantidadPeces(cls):
    return len(cls.listado)
  @classmethod
  def crearSalmon(cls,nombre,edad,genero):
    a = cls(nombre,edad,"oceano",genero,"rojo","6")
    cls.salmones += 1
    return a
  @classmethod
  def crearBacalao(cls,nombre,edad,genero):
    a = cls(nombre,edad,"oceano",genero,"gris","6")
    cls.bacalaos += 1
    return a
  
  def getColorEscamas(self):
    return self.colorEscamas
  
  def getCantidadAletas(self):
    return self.cantidadAletas