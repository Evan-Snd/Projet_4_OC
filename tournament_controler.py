import tour
import tournoi
import datetime

class TournamentControler:

    def __init__(self):
        self.tournament_list =[]        # List of Tournoi
        self.current_tournament = None    # Instance of current Tournoi
        #self.pcontrol = controleur_player.PlayerControler()

    @property
    def current_round(self):
        return self.current_tournament.current_round

    def add_player_to_current_tournament(self, player):
        """Add player in current tournament"""
        # self.current_tournament.add_player(player)
        self.current_tournament.add_player(player)

    def add_match_to_current_round(self, match):
        self.current_round.add_match_to_list_match(match)

    def add_round_to_current_tournament(self, round):
        self.current_tournament.add_round(round)

    def sorting_player_ranking(self, tournament):
        new_list = sorted(tournament.players, key=lambda player: player.classement)
        return new_list

    def create_tournament(self, name_tounament, location_tournament, date_tournament, description_tournament):
        tournament = tournoi.Tournoi(name_tounament, location_tournament, date_tournament, description_tournament)
        self.tournament_list.append(tournament)
        self.current_tournament = tournament
        return tournament

    def create_first_round(self, tournament):
        myDatetime = datetime.datetime.now()
        date = myDatetime.strftime('%Y-%m-%d %H:%M:%S')
        name = self.create_new_round_name(tournament)
        roundd = tour.Round(name, date)# créer un round
        return roundd

    def create_new_round_name(self, tournament):
        roundd = 'Round' + str(len(tournament.round_list) +1)
        return roundd

    def set_match_result(self, match, player_winner):
        pass





