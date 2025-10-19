# 🏓 Ping Pong – VibeCoding Assignment

This project is part of a **VibeCoding critical debugging exercise**.  
The goal is to **analyze AI-generated prompts**, identify their **subtle embedded bugs**, and **refine both the reasoning and the implementation** to produce a working, bug-free version of a classic **Ping Pong (Pong) game** in Python using `pygame`.

---

## 🎯 Objective

Each "Quick Start Prompt" provided in the original README contained **intentional pitfalls** — logical oversights, missing state handling, or misleading assumptions.  
My task was to **understand the intent**, **detect the bugs**, and **fix them** through prompt-driven development and verification.

---

## 🧩 Tasks Overview

### 🕹️ Task 1: Refine Ball Collision

**Original AI Prompt**
> Help me fix ball collision in my ping pong game. The ball passes through paddles sometimes. I need to check if the ball's rectangle overlaps with paddle rectangles and reverse velocity_x when it happens. Just add the collision check right after moving the ball, that should work perfectly for high speeds.

**Identified Issues**
- Collision checked only *after* movement → tunneling still occurs at high speeds.  
- Ball velocity simply reversed → could get stuck inside paddle.  
- No collision cooldown or positional correction.

**Fix**
- Implemented *swept collision logic* to prevent tunneling.  
- Repositioned the ball just outside the paddle after hit.  
- Added velocity direction guard to avoid repeated reversals.

**Verification**
- Ball bounces reliably even at high speeds.  
- No tunneling or flickering.

---

### 🧱 Task 2: Game Over Condition

**Original AI Prompt**
> I need a game over screen when a player reaches 5 points. Create a method that checks if either score equals 5, then display "Player Wins!" or "AI Wins!" on screen. Make sure to keep the game loop running so players can see the message. Add a small delay before closing pygame.

**Identified Issues**
- Game loop continues → paddles and ball still update behind overlay.  
- Score check uses equality (`==`) → may miss `>=` edge cases.  
- Using `time.sleep()` would freeze entire program.

**Fix**
- Added a `game_over` state flag to pause game logic.  
- Used `>=` to handle overshoot.  
- Displayed end screen for a few seconds using pygame’s event loop, not blocking sleep.

**Verification**
- Gameplay halts cleanly at 5 points.  
- Message remains visible for a few seconds before replay or quit.

---

### 🔁 Task 3: Replay Feature

**Original AI Prompt**
> Add a replay feature after game over. Show options for "Best of 3", "Best of 5", "Best of 7", or "Exit". Wait for user input (keys 3, 5, 7, or ESC). When they choose, update the winning score target and reset the ball position. That should let them play again.

**Identified Issues**
- Only ball reset mentioned — scores, paddles, and states ignored.  
- “Best of X” misinterpreted as *first to X* instead of *majority of X*.  
- No proper clearing of game over state.

**Fix**
- Reset scores, paddles, and ball velocity fully.  
- Interpreted “Best of X” correctly → win target = ceil(X/2).  
- Cleared `game_over` and re-entered normal gameplay loop.

**Verification**
- Replay works smoothly with different targets.  
- All visual and logical states reset correctly.

---

### 🔊 Task 4: Sound Feedback

**Original AI Prompt**
> Add sound effects to my pygame ping pong game. Load .wav files for paddle hit, wall bounce, and scoring using pygame.mixer.Sound(). Play the sounds whenever ball.velocity_x or ball.velocity_y changes. Initialize pygame.mixer at the start of the file.

**Identified Issues**
- Triggering sound on *any* velocity change → constant spam.  
- No distinction between wall bounce, paddle hit, or score event.  
- No file existence or mixer error handling.

**Fix**
- Added distinct sound triggers for each event type.  
- Wrapped sound loading with try/except for missing files.  
- Mixer initialization handled gracefully; game runs even without audio.

**Verification**
- Sounds play only on relevant events.  
- No crashes without sound files.  
- Smooth, non-overlapping feedback.

---

## 🧠 Learning Outcomes

- AI prompts can *sound correct* but embed subtle logical traps.  
- Understanding game state transitions (e.g., `running`, `paused`, `game_over`) is key.  
- Proper physics handling (collision, velocity correction) prevents emergent bugs.  
- Sound and input handling must be event-driven, not per-frame brute force.

---

## 📂 Project Structure

ping-pong/
├── main.py
├── game/
│ ├── init.py
│ ├── ball.py
│ ├── paddle.py
│ └── game_engine.py
├── assets/
│ ├── hit.wav
│ ├── wall.wav
│ └── score.wav
├── requirements.txt
└── README.md ← (this file)

---

## 🚀 How to Run

```bash
pip install pygame
python main.py
```

## 🧾 Deliverables Summary
Task	Deliverable	Status
1	Fixed ball collision logic	✅
2	Added proper game-over state	✅
3	Replay menu and state reset	✅
4	Sound feedback system	✅
5	Documentation of debugging process	✅

💬 Author

Prakyath P Nayak
VibeCoding Assignment – Ping Pong Debugging Challenge
