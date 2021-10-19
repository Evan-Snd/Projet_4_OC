from tournament import tournament_controler
from player import controler_player


class Controler(object):

    def __init__(self):
        self.player_controler = controler_player.PlayerControler()
        self.tournament_controler = tournament_controler.TournamentControler(self)

    def find_players(self, last_name):
        res = []
        for player in self.player_controler.players:
            if player.last_name.startswith(last_name):
                res.append(player)
        return res

    def find_players_in_tournament(self, last_name):
        res = []
        for player in self.tournament_controler.current_tournament.players_tournament_list:
            if player.last_name.startswith(last_name):
                res.append(player)
        return res

    def find_tournament(self, name_tournament):
        res = []
        for tournament in self.tournament_controler.tournament_list:
            if tournament.name_tournament.startswith(name_tournament):
                res.append(tournament)
        return res

    def save_all(self):
        self.player_controler.save_players()
        self.tournament_controler.save_all_tournaments()
