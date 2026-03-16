# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game looked fine until you started pressing buttons, they do not work as intented
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. The new game button only gives you another secret number but it does not give you more attemps.
  2. Subsequently, the Submit button won't work because of the previous. Though the UI shows you have more attempts.
  3. The hints make no sense. The secret number stays the same.
  4. Attempts allowed when the game first loads is 1 less than it should be.
  it just shows the wrong number but it does give you the right amount of attempts.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Copilot and Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). Moving the business logic A.K.A get_range_for_difficulty, parse_guess, etc. Moving those functions from app.py to logic_utils.py actually made me understand how the app worked. Because before you had to go back and forth checking what functions called what in each file.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
For the time I wanteed to refactor and move the business logic. AI(Copilot) started giving me tremendous amount of code, it started perfecting the game and even adding unrequired logic and complexity to the UI. I tried to read through the changes it wanted to make but it could not fully explain me why he decided this and I could not understand it. Since I knew I only needed to change a few things not the whole app I decided to throw away that suggestion.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? 
I decided the bug of the of the hint was fixed when I tested thoroughly through playing the game and checking the state of the variables to see if it kept the score right.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  The first time I run pytest is when I realized the mess that was going on with the business logic in app.py. So, from there I started analyzing all the functions that did not belong there. 
- Did AI help you design or understand any tests? How?
AI help me understand how Pytest worked and it was really fun once it taught me I was creating Pytests everywhere. I asked Claude to create a few test and teach me how to use it and create my owns. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The code generated a new number every time you clicked something because its variable was not set with session state.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Reruns in Streamlit is pretty much like every time you press something the whole code runs again. And session state is like a variable that every time the code reruns its remembered and so it does not get overwritten. This allows to keep the count of how many tries you have left.
- What change did you make that finally gave the game a stable secret number?
Specifically adding this line in app.py st.session_state.secret = random.randint(low, high). Once when the code runs each time and another time when you hit New Game button.  

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? 
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  One habbit that will stick with me is that of first analyzing what possible bugs could there be. Then skimming through the code to figure out what function could be the cause and how many other depend on that function or variable. Then ask AI. Is a really nice and workable habit. For prompting, I would certainly open one agent for a specific task, that wat it does not get lost and it does not hallucinate.

- What is one thing you would do differently next time you work with AI on a coding task?
Definetely, I would make sure to use different agents. Because as I was iterating with only one agent for the most part. Later it became really hard for the Copilot to come up with good fixes.
- In one or two sentences, describe how this project changed the way you think about AI generated code. 
I have understood that AI is certainly a powerful tool. But it is still a tool. I still needed to guide it by first understanding the bugs and also checking every ouput it gave to me to make sure it was not going backwards. Also investigating the different tools.
