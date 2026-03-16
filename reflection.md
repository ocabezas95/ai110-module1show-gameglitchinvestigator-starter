# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

# Answer: 
1. Enter key input doesnt work even if its prompting in the text box.
2. The game stops after the first win, and the New Game button doesn’t work.
3. the logic of the game when the secret number should be higher, it says lower. 
4. calculation in the attempts is wrong. play 5 times wrongly, the game print out 2 
5. Input validation the game allows user to input outside of the range
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

1. Copilot
2. The score points was buggy, even after few intents AI could not solve it, so I had to use a different AI model to look into and solve it.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
1. I use the actually game to verify if the bug was fixed
2. I ran pytest and all 22 passed
3. Yes, AI wrote the tests. I just verified run it manually. 

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

The secret number kept changing because Streamlit reruns the script every time the user interacts with the app, and the secret number was being reset on each rerun. Without using Streamlit's session state to store the secret number, it gets re-generated every time, instead of staying the same throughout the game session.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns the whole script every time you interact with the app, like clicking a button or entering text. This means any variables reset unless you use session state. Session state lets you store values (like the secret number) so they stay the same between reruns, making your app behave consistently for the user.

- What change did you make that finally gave the game a stable secret number?


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

