
import mediapipe as mp
from src.constants import cv, LANDMARKS, CARDS_IMG
from src.card_detect import CardDetect
from src.menu import Menu

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_styles = mp.solutions.drawing_styles

class TrucoDetect:
  def __init__(self):
    self.menu = Menu().get_thresholds()
    self.card_detect = CardDetect().get_detects()
  
  def process_frame(self, rgb) -> None :
    with mp_face_mesh.FaceMesh(
      max_num_faces=1,
      refine_landmarks=True,
      min_detection_confidence=0.5,
      min_tracking_confidence=0.5
    ) as face_mesh:
     
      results = face_mesh.process(rgb)
  
      if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
          points = {}
          for region, ids in LANDMARKS.items():
            points[region] = [(face_landmarks.landmark[i].x, face_landmarks.landmark[i].y) for i in ids]
  
        cards : list[str] = []
        for detect, threshold, card in zip(self.card_detect, self.menu, CARDS_IMG):
          if (detect(points, threshold())): cards.append(card)

        return points, cards
      
      return None, None
