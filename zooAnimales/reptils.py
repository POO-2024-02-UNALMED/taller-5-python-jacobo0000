import zooAnimales.animals as animals

class Reptil(animals):
  listado = []
  iguanas = 0
  serpientes = 0

  def __init__(self):
    self.__init__("",0,"","","",0)

  def __init__(self,nombre,edad,habitat,genero,colorEscamas,largoCola):
    super().__init__(nombre,edad,habitat,genero)
    self.colorEscamas = colorEscamas
    self.largoCola  = largoCola
    Reptil.listado.append(self)
  
  def movimiento(self):
    return "reptar"
  
  @classmethod
  def cantidadReptiles(cls):
    return len(cls.listado)
  
  def crearIguana(cls,nombre,edad,genero):
    a = cls.__init__(nombre,edad,"humedal",genero,"verde","3")
    cls.iguanas += 1
    return a
  
  def crearSerpiente(cls,nombre,edad,genero):
    a = cls.__init__(nombre,edad,"jungla",genero,"blanco","1")
    cls.serpientes += 1
    return a