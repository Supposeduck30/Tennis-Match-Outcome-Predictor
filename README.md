# Tennis Match Simulator in Python
## A fully functional tennis match simulator in python made from scratch which simulates a realistic best of 3 set tennis match point by point
This project was built with no external libraries at all, and it simulates the game purely off of math and randomness. This project:
- Asks for player names and their world ranking
- Simulates points, games, and sets with randomness weighted by player ranking
- Prints out a game by game report and a match result

## 🚀 How to run this project 
1. Ensure Python is installed on your device (You can verify this by running the command python --version in your terminal/command prompt)

2. Download the script
   - If you have git installed, run "clone https://github.com/Supposeduck30/tennis-match-simulator.git" in terminal/command prompt
   - Or, download the zip file and extract it

3. Navigate to the directory containing the script

4. Run it by inputting into the command prompt/terminal "python Tennis_Match_Outcome_Generator.py"

5. ALTERNATIVE - Paste the code into an online python compiler
#### THE CODE IS IN THE .py FILE INSIDE OF THE FOLDER

## 🕓 Version History 
### 1.0.0 
- Terminal based
- Asks for ranks and names of players
- Simulates the match game by game randomly weighted towards rank
- Outputs the score of each set

### 1.2.0
- Asks for ranks and names of players
- Simulates the match point by point
- Outputs a game by game summary with the score of each game
- Incorporates serving logic (who serves first, alternating serves, person is more likely to win their service game)

## 🔧 How to tweak the project for your own uses 
1. Fork the repository

2. Clone the fork

3. Make your changes to the code

4. Commit and push your changes to the fork

5. OPTIONAL - Create a pull request if you want the main repository to change the code with what you changed

## 📊 How it works 
- With the input of the ranks, it then simulates each game, randomizing who serves first and alternating from there
- A higher ranked player is mlre likely to win their service game
- It outputs the score of each game and who won
- The randomness makes it so the higher ranked is more likely to win, but there can be upsets
- The higher the difference in rank, the more likely it is for the higher ranked person to win

## Screenshots
## ![image](https://github.com/user-attachments/assets/1dbaccb8-5f5e-421f-b8be-6670cc2caafc)

## ![image](https://github.com/user-attachments/assets/6083996c-2ecc-4896-8b23-dbc0d9a0213b)

## ⚠️ Known issues 
- If both players are inputted with the same rankings, it still works 
- This simulator may oversimply the effects of rankings on match outcomes 

## ⚖️ License
### MIT License