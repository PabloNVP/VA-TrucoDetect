from src.constants import cv
import math

class CardDetect:
  def __init__(self) -> None :
    self.detects : list[function] = [
      self.detect_uno_espada,
      self.detect_uno_basto,
      self.detect_siete_espada,
      self.detect_siete_oro,
      self.detect_dos
    ]

  def get_detects(self):
    return self.detects
  
  @staticmethod
  def distance(punto_a : dict, punto_b : dict) -> float :
    return math.sqrt((punto_a[0] - punto_b[0])**2 + (punto_a[1] - punto_b[1])**2)
  
  def detect_uno_espada(self, points : dict, threshold : float) -> bool :
    return (self.distance(points["ojo_izq"][0], points["ceja_izq"][0]) > threshold and
            self.distance(points["ojo_der"][0], points["ceja_der"][0]) > threshold)

  def detect_uno_basto(self, points : dict, threshold : float) -> bool :
    return (self.distance(points["ojo_der"][1], points["ojo_der"][0]) < threshold and
            self.distance(points["ojo_izq"][1], points["ojo_izq"][0]) > threshold)

  def detect_siete_espada(self, points : dict, threshold : float) -> bool :
    return (self.distance(points["boca"][3], points["boca"][0]) > threshold)

  def detect_siete_oro(self, points : dict, threshold : float) -> bool :
    return (self.distance(points["boca"][2], points["boca"][0]) > threshold)

  def detect_dos(self, points : dict, threshold_int : float, threshold_ext : float = 0.1) -> bool :
    return (self.distance(points["boca"][0], points["boca"][1]) < threshold_int and 
            self.distance(points["boca"][3], points["boca"][2]) < threshold_ext)