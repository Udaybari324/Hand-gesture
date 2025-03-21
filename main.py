import cv2
import mediapipe as mp

# Initialize Mediapipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# Function to recognize a basic gesture
def recognize_gesture(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    victory_threshold = index_finger_tip.y < middle_finger_tip.y < thumb_tip.y
    stop_threshold = all(
        finger_tip.y > thumb_tip.y
        for finger_tip in [index_finger_tip, middle_finger_tip, ring_finger_tip, pinky_finger_tip]
    )
    fist_threshold = all(
        finger_tip.y > thumb_tip.y
        for finger_tip in [index_finger_tip, middle_finger_tip, ring_finger_tip, pinky_finger_tip]
    )
    pointing_threshold = index_finger_tip.x < thumb_tip.x
    rock_sign_threshold = all(
        finger_tip.y > thumb_tip.y for finger_tip in [index_finger_tip, middle_finger_tip]
    ) and all(
        finger_tip.x > thumb_tip.x for finger_tip in [index_finger_tip, middle_finger_tip]
    )
    thumbs_up_threshold = thumb_tip.y < index_finger_tip.y
    thumbs_down_threshold = thumb_tip.y > index_finger_tip.y
    ok_sign_threshold = all(
        finger_tip.y > thumb_tip.y for finger_tip in [index_finger_tip, ring_finger_tip]
    ) and all(
        finger_tip.x > thumb_tip.x for finger_tip in [index_finger_tip, ring_finger_tip]
    )

    if victory_threshold:
        return "Victory"
    elif stop_threshold:
        return "Stop"
    elif fist_threshold:
        return "Fist"
    elif pointing_threshold:
        return "Pointing"
    elif rock_sign_threshold:
        return "Rock Sign"
    elif thumbs_up_threshold:
        return "Thumbs Up"
    elif thumbs_down_threshold:
        return "Thumbs Down"
    elif ok_sign_threshold:
        return "OK Sign"
    else:
        return "No Gesture Detected"

# Open the webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    
    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame for hand detection
    result = hands.process(rgb_frame)
    
    # Draw hand landmarks and recognize gesture
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = recognize_gesture(hand_landmarks)
            cv2.putText(
                frame, gesture, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA
            )
    
    # Display the resulting frame
    cv2.imshow('Hand Gesture Recognition', frame)
    
    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
