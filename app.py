import cv2
import mediapipe as mp
import pygame
import json
import time
from gesture import GestureRecognizer

# -----------------------------
# Initialize Audio
# -----------------------------
pygame.mixer.init()

# -----------------------------
# Load Character Database
# -----------------------------
with open("data/characters.json", "r") as f:
    characters = json.load(f)

# -----------------------------
# Preload Images & Sounds
# -----------------------------
for key in characters:

    img = cv2.imread(characters[key]["image"])

    if img is not None:
        img = cv2.resize(img, (220, 320))

    characters[key]["image_data"] = img

    characters[key]["sound_data"] = pygame.mixer.Sound(
        characters[key]["audio"]
    )

# -----------------------------
# MediaPipe
# -----------------------------
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.85,
    min_tracking_confidence=0.85
)

gesture = GestureRecognizer()

# -----------------------------
# Webcam
# -----------------------------
cap = cv2.VideoCapture(0)

current_character = None
current_image = None
current_sound = None

last_gesture = None

candidate_gesture = None
candidate_time = 0

STABLE_TIME = 0.20

# -----------------------------
# Main Loop
# -----------------------------
while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    detected_gesture = None

    if results.multi_hand_landmarks and results.multi_handedness:

        for hand_landmarks, handedness in zip(
            results.multi_hand_landmarks,
            results.multi_handedness
        ):

            hand_label = handedness.classification[0].label

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            gesture_name = gesture.recognize(
                hand_landmarks.landmark,
                hand_label
            )

            if gesture_name is not None:
                detected_gesture = gesture_name
                break
                # ---------------------------------
    # Stable Gesture Recognition
    # ---------------------------------

    if detected_gesture is None:

        if current_sound is not None:
            pygame.mixer.stop()

        current_character = None
        current_image = None
        current_sound = None

        last_gesture = None
        candidate_gesture = None
        candidate_time = 0

    else:

        if detected_gesture != candidate_gesture:

            candidate_gesture = detected_gesture
            candidate_time = time.time()

        elif (
            time.time() - candidate_time >= STABLE_TIME
            and candidate_gesture != last_gesture
        ):

            # Stop previous sound
            pygame.mixer.stop()

            last_gesture = candidate_gesture

            current_character = characters[last_gesture]

            current_image = current_character["image_data"]

            current_sound = current_character["sound_data"]

            current_sound.play()

    # ---------------------------------
    # Draw Character Image
    # ---------------------------------

    if current_image is not None:

        h, w = current_image.shape[:2]

        x = frame.shape[1] - w - 20
        y = 40

        if (
            x >= 0
            and y >= 0
            and x + w <= frame.shape[1]
            and y + h <= frame.shape[0]
        ):
            frame[y:y+h, x:x+w] = current_image

    # ---------------------------------
    # Display Character Name
    # ---------------------------------

    if current_character is not None:

        cv2.putText(
            frame,
            current_character["name"],
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 255),
            2
        )
            # ---------------------------------
    # FPS (Optional)
    # ---------------------------------
    cv2.putText(
        frame,
        "Anime Vision v2",
        (20, frame.shape[0] - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    # ---------------------------------
    # Show Window
    # ---------------------------------
    cv2.imshow("Anime Vision", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

# ---------------------------------
# Cleanup
# ---------------------------------
pygame.mixer.stop()
cap.release()
cv2.destroyAllWindows()


