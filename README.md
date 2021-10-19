# Web Scraping
This project is a tournament software for chess games. This this for 8 players and this tournament use the swiss system. This software allows you to watch the tournament list with the players list, the rounds list and the matchs list. You can enregistrate a player in the data base.

# Intro
Create a folder and put all the file (all the .py, view_tournament.json,  README, requirement.txt) in this folder.

# Create environment (GitBash)
cd path_folder ( Go to the desired folder ) virtualenv nomEnv

# Activate environment (GitBash)
for windows : ". nomEnv/Scripts/Activate" or ". nomEnv/Scripts/activate"

# Install package
pip install -requirements.txt

# Generate Flake8 report (GitBash)
In the folder Flake8 on your PC, open "setup.py" or "default.py" and add your env like "envProjet4"(example for this project), in the exclude section. Then write 'flake8 --format=html --htmldir=flake-report' 

# Launch project
"python main.py" (GitBash)

# User Guide
Enter a number corresponding to the management of players or tournaments. Numbers are indicated on the left. Type "Enter" to validate your choice.
For the managementof the players :
- Enregistrate a player (Last name, first name, date of birth, gender and classement). Same principle : write and validate
- View of View of the list of players by ranking and alphabetical order
- Change player rank : Enter the first letter of the player last name, select the player with the index and then type the new rank of the player
- Delete a player : Enter the first letter of the player last name, select the player with the index

For the tournament :
- Create a tournament : enter the information of the tournament. Add 8 players with the same principe of "Delete player". When you have 8 players, create the first round. 4 matchs will be create. Select the match you want and then choose who win the match or if this is equality. When you have entered the result of the match, you can create the second round. At the end of the fourth round, you can view the final rank.
- View tournament list : Enter the first letter of the tournament, select the tournament with the index. Then you have 3 choice, view the player list, view round list and view the match list

When you are making a tournament, you can type "pause" for change the rank of a player. For return to the tournament, go to the tournament management and type the fourth option "Reprendre le tournoi en cours"

