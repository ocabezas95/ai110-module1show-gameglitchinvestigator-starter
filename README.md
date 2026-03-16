# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
  - The game is a number guessing game where the player tries to guess a secret number, receiving hints after each guess.
- [x] Detail which bugs you found.
  - The secret number resets on every button click due to improper state management in Streamlit.
  - The hints for "Higher/Lower" were incorrect and misleading.
- [x] Explain what fixes you applied.
  - Used Streamlit's session state to persist the secret number across interactions.
  - Corrected the logic for hints so they accurately reflect whether the guess should be higher or lower.

## 📸 Demo
![alt text](<Screenshot 2026-03-15 at 11.31.02 PM.png>)
![alt text](<Screenshot 2026-03-15 at 11.31.15 PM.png>)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
