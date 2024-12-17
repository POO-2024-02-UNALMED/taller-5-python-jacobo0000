class Zoologico:
  def __init__(self):
    self.__init__("","")

  def __init__(self, nombre, ubicacion):
    self.nombre = nombre
    self. ubicacion = ubicacion
    self.zonas = []

  def cantidadTotalAnimales(self):
    cantidadTotal = 0
    for zona in self.zonas:
      cantidadTotal += zona.cantidadAnimales()
    return cantidadTotal
  
  def agregarZonas(self,zonaNueva):
    self.zonas.append(zonaNueva)
  
