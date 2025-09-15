import cv2 as cv

SIZE_IMAGE = (114, 184)

THRESHOLDS = {
  "uno_espada": 0.215,
  "uno_basto": 0.015,
  "siete_espada": 0.065,
  "siete_oro": 0.062,
  "dos": 0.10
}

LANDMARKS = {
  "frente": [10],
  "ceja_izq": [105],
  "ceja_der": [334],
  "ojo_der": [159, 145],
  "ojo_izq": [386, 374],
  "boca": [13, 14, 78, 308],
  "barbilla": [152]
}

CARDS_IMG = [
  cv.resize(cv.imread("./assets/uno_espada.png", cv.IMREAD_UNCHANGED), SIZE_IMAGE),
  cv.resize(cv.imread("./assets/uno_basto.png", cv.IMREAD_UNCHANGED), SIZE_IMAGE),
  cv.resize(cv.imread("./assets/siete_espada.png", cv.IMREAD_UNCHANGED), SIZE_IMAGE),
  cv.resize(cv.imread("./assets/siete_oro.png", cv.IMREAD_UNCHANGED), SIZE_IMAGE),
  #cv.resize(cv.imread("./assets/tres_copas.png", cv.IMREAD_UNCHANGED), SIZE_IMAGE),
  cv.resize(cv.imread("./assets/dos_basto.png", cv.IMREAD_UNCHANGED), SIZE_IMAGE)
]