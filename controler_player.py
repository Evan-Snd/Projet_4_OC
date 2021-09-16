import player
from tinydb import TinyDB


class PlayerControler:

    def __init__(self):
        self.players = []  # List de Player
        self.load_players()

    def register_player(self, ind, last_name, first_name, date_birth, gender, classement):
        exist = self.verification_player(last_name, first_name)
        if exist:
            print("Ce joueur est déjà enregistré dans la base de données")
        else:
            p = player.Player(ind, last_name, first_name, date_birth, gender, classement)
            self.players.append(p)
            self.save_players()

    def delete_player(self, player_):
        self.players.remove(player_)

    def load_players(self):
        # Load data from DB
        db = TinyDB('player.json')
        players_table = db.table('players')
        serialized_players = players_table.all()

        # Save data in players
        for ind, ser_player in enumerate(serialized_players):
            self.players.append(
                player.Player(ser_player['Ind'], ser_player['Nom'], ser_player['Prenom'],
                              ser_player['Date de naissance'],
                              ser_player['Sexe'], ser_player['Classement']))

    def save_players(self):
        # serialize players
        serialized_players = []
        for player_ in self.players:
            ser_player = {
                'Ind': player_.ind,
                'Nom': player_.last_name,
                'Prenom': player_.first_name,
                'Date de naissance': player_.date_birth,
                'Sexe': player_.gender,
                'Classement': player_.classement
            }
            serialized_players.append(ser_player)
        # save serialized data
        db = TinyDB('player.json')
        players_table = db.table('players')
        players_table.truncate()  # clear the table first
        players_table.insert_multiple(serialized_players)

    def verification_player(self, last_name, first_name):
        res = False
        for player_ in self.players:
            if player_.last_name == last_name and player_.first_name == first_name:
                res_player = True
                if res_player:
                    res = res_player
                    break
                break
            else:
                continue
        return res

    def get_player(self, player_ind):
        for player_ in self.players:
            if player_.ind == player_ind:
                player_ind = player_
            else:
                continue
        return player_ind
