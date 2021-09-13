import player_obj
from tinydb import TinyDB


class PlayerControler:

    def __init__(self):
        self.players = []  # List de Player
        self.load_players()

    def register_player(self, ind, last_name, first_name, date_birth, gender, classement):
        exist = self.verification_player(last_name, first_name)
        if exist:
            print("Ce joueur est deja enregistre dans la base de donnees")
        else:
            player = player_obj.Player(ind, last_name, first_name, date_birth, gender, classement)
            self.players.append(player)
        # save players

    def load_players(self):
        # Load data from DB
        db = TinyDB('player.json')
        players_table = db.table('players')
        serialized_players = players_table.all()

        # Save data in players
        for ind, ser_player in enumerate(serialized_players):
            self.players.append(
                player_obj.Player(ser_player['Ind'], ser_player['Nom'], ser_player['Prenom'],
                                  ser_player['Date de naissance'],
                                  ser_player['Sexe'], ser_player['Classement']))

    def save_players(self):
        # serialize players
        serialized_players = []
        for player in self.players:
            ser_player = {
                'Ind': player.ind,
                'Nom': player.last_name,
                'Prenom': player.first_name,
                'Date de naissance': player.date_birth,
                'Sexe': player.gender,
                'Classement': player.classement
            }
            serialized_players.append(ser_player)
        # save serialized data
        db = TinyDB('player.json')
        players_table = db.table('players')
        players_table.truncate()  # clear the table first
        players_table.insert_multiple(serialized_players)

    def verification_player(self, last_name, first_name):
        res = False
        for player in self.players:
            if player.last_name == last_name and player.first_name == first_name:
                res_player = True
                if res_player:
                    res = res_player
                    break
                break
            else:
                continue
        return res

    def get_player(self, player_ind):
        for player in self.players:
            if player.ind == player_ind:
                player_ind = player
            else:
                continue
        return player_ind
