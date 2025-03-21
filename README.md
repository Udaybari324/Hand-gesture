# Hand Gesture Recognition using MediaPipe🖐️

This Python project utilizes the [MediaPipe](https://mediapipe.dev/) library and [OpenCV](https://opencv.org/) to perform real-time hand gesture recognition. With this code, you can control your computer's cursor and keyboard using hand gestures.

## Features

- Detects and tracks hand landmarks in real time.
- Recognizes left and right-hand gestures for mouse and keyboard control.
- Control the mouse cursor and perform keyboard actions (e.g., move, click, swipe) using hand gestures.
- Easily customizable for different hand gestures and actions.

## Prerequisites

Before running the code, make sure you have the following dependencies installed:

- Python 3.x
- OpenCV (`pip install opencv-python`)
- MediaPipe (`pip install mediapipe`)

## How to Use

1. Clone this repository:

   ```bash
   git clone https://github.com/Udaybari324/Hand-gesture.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Hand-gesture
   ```

3. Run the code:

   ```bash
   python main.py
   ```

4. A window will open showing the webcam feed. Move your hand in front of the camera to control the cursor and perform gestures.

5. To exit the program, press 'q' in the OpenCV window.

## Hand Gestures and Actions
This project leverages OpenCV and MediaPipe to detect and recognize hand gestures in real time using a webcam. It processes hand landmarks and classifies them into predefined gestures based on the positions and distances between key points.

 ## Supported Gestures
   1. **Thumbs Up 👍** – Thumb is raised while other fingers are curled downward, indicating approval or agreement.
   2. **Thumbs Down 👎** – Thumb is pointing downward, representing disapproval or a negative response.
   3. **OK Sign 👌** – Thumb and index finger form a circle while other fingers remain extended, signaling "OK" or "perfect."
   4. **Victory ✌️** – Index and middle fingers are raised, forming a "V" shape, often used as a sign of victory or peace.
   5. **Stop ✋** – All fingers are extended and spread apart, resembling a stop signal to indicate a halt or warning.

## Customization

You can customize this code to recognize additional hand gestures and map them to different actions. Modify the code to add your own gestures and actions.

## Acknowledgments

This project uses the [MediaPipe](https://mediapipe.dev/) library for hand landmark detection and tracking.

## License

This project is licensed under the MIT License.

## Author

- Uday Bari 
- GitHub: [Udaybari324](https://github.com/udaybari324)

Feel free to contribute to this project and make it even more awesome! If you have any questions or suggestions, please open an issue or pull request.

Enjoy controlling your computer with hand gestures! 🖐️🖥️
