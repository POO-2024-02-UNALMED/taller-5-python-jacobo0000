from zooAnimales.animal import Animal

class Mamifero(Animal):
  listado = []
  caballos = 0
  leones= 0

  def __init__(self):
    self.__init__("",0,"","",False, 0)

  def __init__(self,nombre,edad,habitat,genero,pelaje,patas):
    super().__init__(nombre,edad,habitat,genero)
    self.pelaje = pelaje
    self.patas = patas
    Mamifero.listado.append(self)
  
  @classmethod
  def cantidadMamiferos(cls):
    return len(cls.listado)
  
  def crearCaballo(cls,nombre,edad,genero):
    a = cls.__init__(nombre,edad,"pradera",genero,"true","4")
    cls.caballos += 1
    return a
  
  def crearLeon(cls,nombre,edad,genero):
    a = cls.__init__(nombre,edad,"selva",genero,"true","4")
    cls.leones += 1
    return a