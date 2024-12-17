import zooAnimales.animals as animals

class Pez(animals):
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
  
  def crearSalmon(cls,nombre,edad,genero):
    a = cls.__init__(nombre,edad,"oceano",genero,"rojo","6")
    cls.salmones += 1
    return a
  
  def crearBacalao(cls,nombre,edad,genero):
    a = cls.__init__(nombre,edad,"oceano",genero,"gris","6")
    cls.bacalaos += 1
    return a