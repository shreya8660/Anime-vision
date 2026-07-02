# 🎌 Anime Vision - AI Hand Gesture Anime Summoner

Anime Vision is a fun Computer Vision project built using **Python, OpenCV, MediaPipe, and Pygame**. It recognizes hand gestures in real-time through your webcam and instantly displays anime characters with their corresponding voice effects.

---

## 📸 Demo

Show a specific hand gesture in front of your webcam.

✨ Instantly:

- Displays the anime character image
- Plays the character voice
- Stops previous sound immediately when the gesture changes
- Removes image and sound when no gesture is detected

---

# 🎮 Supported Characters

## Right Hand

| Gesture | Character |
|----------|-----------|
| ☝️ Index Finger | Gojo |
| ✌️ Index + Middle | Naruto |
| 🖖 Index + Middle + Ring | Eren |
| 🖐️ Index + Middle + Ring + Pinky | Luffy |

---

## Left Hand

| Gesture | Character |
|----------|-----------|
| ☝️ Index Finger | Itachi |
| ✌️ Index + Middle | Tanjiro |
| 🖖 Index + Middle + Ring | Sukuna |
| 🖐️ Index + Middle + Ring + Pinky | Zenitsu |

---

# 🚀 Features

- 🎥 Real-time webcam detection
- 🤖 AI Hand Gesture Recognition using MediaPipe
- 🎭 8 Anime Characters
- 🔊 Instant Voice Effects
- 🖼️ Instant Character Images
- ⚡ Fast Image & Audio Switching
- 🎯 Stable Gesture Recognition
- 🖐️ Supports Left & Right Hand
- 💻 Built completely in Python

---

# 🛠️ Tech Stack

- Python
- OpenCV
- MediaPipe
- Pygame CE
- JSON

---

# 📂 Project Structure

```
Anime-Vision
│
├── app.py
├── gesture.py
│
├── data
│   └── characters.json
│
├── assets
│   ├── images
│   │   ├── gojo.png
│   │   ├── naruto.png
│   │   ├── eren.png
│   │   ├── luffy.png
│   │   ├── itachi.png
│   │   ├── tanjiro.png
│   │   ├── sukuna.png
│   │   └── zenitsu.png
│   │
│   └── audio
│       ├── gojo.mp3
│       ├── naruto.mp3
│       ├── eren.mp3
│       ├── luffy.mp3
│       ├── itachi.mp3
│       ├── tanjiro.mp3
│       ├── sukuna.mp3
│       └── zenitsu.mp3
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Anime-Vision.git
```

Go to the project

```bash
cd Anime-Vision
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python app.py
```

---

# 📦 Requirements

```
opencv-python
mediapipe==0.10.14
pygame-ce
numpy
```

---

# 🎯 How It Works

1. Webcam captures hand.
2. MediaPipe detects 21 hand landmarks.
3. GestureRecognizer identifies finger combinations.
4. Character data is loaded from `characters.json`.
5. Corresponding image is displayed.
6. Character voice is played instantly.
7. Previous audio stops automatically when gesture changes.

---

# 🔮 Future Improvements

- ✨ Anime Aura Effects
- ⚡ Domain Expansion Animation
- 🔥 Fire & Lightning Effects
- 🌊 Water Breathing Effects
- 🎵 Background Music
- 🤖 AI Custom Gesture Training
- 🥷 More Anime Characters
- 🌐 Web Version using React & Flask

---

# 👩‍💻 Author

**Shreya V**

Information Science & Engineering Student

Passionate about AI, Computer Vision, Web Development and UI/UX Design.

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub!
