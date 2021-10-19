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
