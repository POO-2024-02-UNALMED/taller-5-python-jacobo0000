class Zona:
  def __init__(self):
    self.__init__("",None)

  def __init__(self,nombre, zoo = None):
    self.nombre = nombre
    self.zoo = zoo 
    self.animales = []
  
  def agregarAnimales(self,animalNuevo):
    self.animales.append(animalNuevo)

  def cantidadAnimales(self):
    return len(self.animales)
