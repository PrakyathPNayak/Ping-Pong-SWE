🏓 Real-Time Ping Pong Game (Fixed & Enhanced)

A lightweight real-time Ping Pong (Pong) clone built with Python + Pygame, featuring smooth delta-time movement, robust paddle-ball collision, adjustable difficulty, game-over states, replay options, and optional sound effects.


---

🚀 Features

✅ Smooth, time-based physics – consistent speed across devices
✅ Accurate collisions – no tunneling or paddle-pass bugs
✅ Progressive ball speed-up for higher challenge
✅ AI opponent with adjustable difficulty
✅ Game-over screen when someone wins
✅ Replay options – choose Best of 3/5/7 or exit
✅ Optional sound effects for hits, bounces, and scoring
✅ Clean modular design – easy to extend and learn from


---

🧱 Project Structure

ping-pong/
├── main.py
├── requirements.txt
├── README.md
└── game/
    ├── __init__.py
    ├── ball.py
    ├── paddle.py
    └── game_engine.py

Optional sound files (place in project root):

hit.wav      # Paddle hit sound
bounce.wav   # Wall bounce sound
score.wav    # Scoring sound


---

🧩 Installation & Setup

1️⃣ Clone the repository

git clone https://github.com/<your-username>/ping-pong.git
cd ping-pong

2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣ Run the game

python main.py


---

🎮 Controls

Key	Action

W	Move paddle up
S	Move paddle down
ESC	Quit game / Exit replay menu
3 / 5 / 7	Select Best-of-3/5/7 when match ends



---

🧠 Gameplay Details

Scoring: Each time an opponent misses, the other player scores.

Winning condition: First to reach target score wins (default = 5).

AI movement: Tracks the ball with ~95 % accuracy for a fair challenge.

Replay system: After a win, press 3, 5, or 7 to start a new match.



---

🔊 Sound Effects (Optional)

You can drop in any short .wav files in the project root named:

Filename	Trigger

hit.wav	When ball hits paddle
bounce.wav	When ball bounces off top/bottom wall
score.wav	When a player scores


If these files are missing, the game runs silently (no crashes).


---

🛠️ Technical Notes

Built with Pygame 2.1+

Uses delta-time updates (dt = clock.tick(60)/1000) for consistent frame-independent movement

Collision uses rect-based detection with position correction to prevent tunneling

Clean OOP architecture: Ball, Paddle, and GameEngine separated for readability

Runs at a steady 60 FPS



---

🌟 Future Improvements

Power-ups (speed boost, slow-ball, etc.)

Multiplayer over LAN

Visual effects (trails, glow, etc.)

Menu system for settings and difficulty

Mobile-friendly touch controls



---

📷 Screenshots (optional section)

(Add images here once you run the game and take screenshots)
Example:

![Gameplay Screenshot](assets/gameplay.png)


---

🧑‍💻 Author

V S Vishwas (original repo)
Modified & Fixed by: Your Name Here

📚 Licensed under the MIT License


---

Would you like me to make a shorter “student-friendly” version (for a GitHub profile or project submission) — or keep this detailed one for documentation?

