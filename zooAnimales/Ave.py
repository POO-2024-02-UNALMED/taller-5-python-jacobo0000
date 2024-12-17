import Animal

class Ave(Animal):
  listado = []
  halcones = 0
  aguilas = 0

  def __init__(self):
    self.__init__("",0,"","","")

  def __init__(self,nombre,edad,habitat,genero,colorPlumas):
    super().__init__(nombre,edad,habitat,genero)
    self.colorPlumas = colorPlumas
    Ave.listado.append(self)
  
  @classmethod
  def cantidadAves(cls):
    return len(cls.listado)
  
  def movimiento(self):
    return "volar"
  
  @classmethod
  def crearHalcon(cls,nombre,edad,genero):
    a = cls.__init__(nombre,edad,"montañas",genero,"cafe glorioso")
    cls.halcones += 1
    return a 
  
  def crearAguila(cls,nombre,edad,genero):
    a = cls.__init__(nombre,edad,"montañas",genero,"blanco y amarillo")
    cls.aguilas += 1
    return a