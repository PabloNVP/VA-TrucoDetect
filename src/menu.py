
from src.constants import cv, THRESHOLDS

class Menu:
  def __init__(self):
    cv.namedWindow("webcam")
    cv.createTrackbar("uno_espada", "webcam", int(THRESHOLDS["uno_espada"]*1000), 1000, self.none)
    cv.createTrackbar("uno_basto", "webcam", int(THRESHOLDS["uno_basto"]*1000), 1000, self.none)
    cv.createTrackbar("siete_espada", "webcam", int(THRESHOLDS["siete_espada"]*1000), 1000, self.none)
    cv.createTrackbar("siete_oro", "webcam", int(THRESHOLDS["siete_oro"]*1000), 1000, self.none)
    cv.createTrackbar("dos", "webcam", int(THRESHOLDS["dos"]*1000), 1000, self.none)

  def get_thresholds(self):
    return [
      self.get_threshold_uno_espada,
      self.get_threshold_uno_basto,
      self.get_threshold_siete_espada,
      self.get_threshold_siete_oro,
      self.get_threshold_dos
    ]

  def none(self, val):
    pass

  def get_threshold_uno_espada(self) -> float:
    return cv.getTrackbarPos("uno_espada", "webcam") / 1000

  def get_threshold_uno_basto(self) -> float:
    return cv.getTrackbarPos("uno_basto", "webcam") / 1000
  
  def get_threshold_siete_espada(self) -> float:
    return cv.getTrackbarPos("siete_espada", "webcam") / 1000
  
  def get_threshold_siete_oro(self) -> float:
    return cv.getTrackbarPos("siete_oro", "webcam") / 1000
  
  def get_threshold_dos(self) -> float:
    return cv.getTrackbarPos("dos", "webcam") / 1000
