import os
from src.constants import cv
from src.truco_detect import TrucoDetect

def draw_cards(imWebcam, cards : dict):
  x, y, offset = 10, 10, 10
  for idx, carta in enumerate(cards):
    x_pos = x + idx * (carta.shape[1] + offset)
    h, w = carta.shape[:2]

    if carta.shape[2] == 4:
      alpha = carta[:, :, 3:] / 255.0
      roi = imWebcam[y:y+h, x_pos:x_pos+w]
      imWebcam[y:y+h, x_pos:x_pos+w] = (1 - alpha) * roi + alpha * carta[:, :, :3]
    else:
      imWebcam[y:y+h, x_pos:x_pos+w] = carta

def draw_points(imWebcam, points):
  h, w, _ = imWebcam.shape
  for region_points in points.values():
    for x, y in region_points:
      cx, cy = int(x * w), int(y * h)
      cv.circle(imWebcam, (cx, cy), 3, (155, 255, 155), -1)

if os.name == "nt":
  webcam= cv.VideoCapture(0, cv.CAP_DSHOW) # WINDOWS
elif os.name == "posix":
  webcam = cv.VideoCapture(0) # LINUX / OS

td = TrucoDetect()

while True:
  ret, imWebcam = webcam.read()

  if not ret: break

  rgb = cv.cvtColor(imWebcam, cv.COLOR_BGR2RGB)

  points, cards = td.process_frame(rgb)

  if points: draw_points(imWebcam, points)
  if cards: draw_cards(imWebcam, cards)

  cv.imshow('webcam', imWebcam)
  
  if cv.waitKey(30) & 0xFF == ord('q'): break


webcam.release()
cv.destroyAllWindows()