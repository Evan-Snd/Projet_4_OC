import round_obj
import tournament_obj
import datetime
from tinydb import TinyDB
from operator import itemgetter


class TournamentControler:

    def __init__(self, root_controler):
        self.__root_controler = root_controler
        self.tournament_list = []  # List of Tournoi
        self.current_tournament = None  # Instance of current Tournoi
        self.load_all_tournaments()

    @property
    def current_round(self):
        return self.current_tournament.current_round

    def delete_player_to_current_tournament(self, player):
        self.current_tournament.delete_player(player)

    def add_player_to_current_tournament(self, player):
        """Add player in current tournament"""
        self.current_tournament.add_player(player)

    def add_match_to_current_round(self, match):
        self.current_round.add_match_to_list_match(match)

    def add_round_to_current_tournament(self, roundd):
        self.current_tournament.add_round(roundd)

    @property
    def sorting_player_ranking(self):
        new_list = sorted(self.current_tournament.players_tournament_list, key=lambda player: player.classement)
        return new_list

    @property
    def sorting_player_classement_after_round(self):
        lst = self.player_points
        classement_point = sorted(lst, key=itemgetter(1), reverse=True)
        list_points = sorted(list(set([p[1] for p in classement_point])), reverse=True)
        players_sorted = []
        for point in list_points:
            pp_point = [p for p in classement_point if p[1] == point]
            pp_sorted = sorted(pp_point, key=lambda p: p[0].classement)
            players_sorted.extend(pp_sorted)
        return players_sorted

    def create_tournament(self, index, name_tounament, location_tournament, date_tournament, description_tournament):
        tournament = tournament_obj.Tournament(index, name_tounament, location_tournament, date_tournament,
                                               description_tournament)
        self.tournament_list.append(tournament)
        self.current_tournament = tournament
        return tournament

    def end_date(self):
        mydatetime = datetime.datetime.now()
        round_obj.Round.end_date = mydatetime.strftime('%Y-%m-%d %H:%M:%S')

    @property
    def create_new_round(self):
        mydatetime = datetime.datetime.now()
        date = mydatetime.strftime('%Y-%m-%d %H:%M:%S')
        name = self.create_new_round_name
        roundd = round_obj.Round(name, date)  # créer un round
        return roundd

    @property
    def create_new_round_name(self):
        roundd = 'ROUND ' + str(len(self.round_list) + 1)
        return roundd

    @property
    def status(self):
        return self.current_tournament.status

    @property
    def list_match(self):
        return self.current_round.list_matches

    @property
    def round_list(self):
        return self.current_tournament.rounds_list

    @property
    def players_list(self):
        return self.current_tournament.players_tournament_list

    @property
    def player_points(self):
        return self.current_tournament.back_players_points

    def get_match(self, index):
        return self.current_round.get_match(index)

    def player1_win(self, match):
        return self.current_round.player1_win(match)

    def player2_win(self, match):
        return self.current_round.player2_win(match)

    def nobody_win(self, match):
        return self.current_round.nobody_win(match)

    def load_all_tournaments(self):
        # Load data from DB
        db = TinyDB('tournament.json')
        tournament_table = db.table('tournament')
        serialized_tournament = tournament_table.all()

        for ind, ser_tournament in enumerate(serialized_tournament):
            tournament = tournament_obj.Tournament(ser_tournament['Ind'], ser_tournament['Nom'], ser_tournament['Lieu'],
                                                   ser_tournament['Date'], ser_tournament['Description'])
            self.load_rounds(tournament, ser_tournament['Liste des rounds'])
            self.load_tournament_players(tournament, ser_tournament['Liste des joueurs'])
            self.tournament_list.append(tournament)

    def load_rounds(self, tournament, serialized_rounds):
        for ser_round in serialized_rounds:
            round = self.load_round(ser_round)
            tournament.add_round(round)

    def load_round(self, serialized_round):
        res = round_obj.Round(serialized_round['Nom'], serialized_round['Date de début'])
        res.end_date = serialized_round['Date de fin']
        self.load_matches(res, serialized_round['Matches'])
        return res

    def load_matches(self, round, serialized_matches):
        for ser_match in serialized_matches:
            match = self.load_match(ser_match)
            round.add_match(match)

    def load_match(self, serialized_match):
        res = (serialized_match['J1'], serialized_match['J2'])
        return res

    def load_tournament_players(self, tournament, serialized_players):
        for player_ind in serialized_players:
            player = self.load_player(player_ind)
            tournament.add_player(player)

    def load_player(self, player_ind):
        return self.__root_controler.player_controler.get_player(player_ind)

    def save_all_tournaments(self):
        # serialize players
        serialized_tournaments = []
        for tournament in self.tournament_list:
            ser_tournament = self.serialize_tournament(tournament)
            serialized_tournaments.append(ser_tournament)

        # save serialized data
        db = TinyDB('tournament.json')
        tournament_table = db.table('tournament')
        tournament_table.truncate()  # clear the table first
        tournament_table.insert_multiple(serialized_tournaments)

    def serialize_tournament(self, tournament):
        return {
            'Ind': tournament.index,
            'Nom': tournament.name_tournament,
            'Lieu': tournament.location_tournament,
            'Date': tournament.date_tournament,
            'Description': tournament.description_tournament,
            'Liste des rounds': self.serialize_rounds(tournament),
            'Liste des joueurs': [p.ind for p in tournament.players_tournament_list],
        }

    def serialize_rounds(self, tournament):
        res = []
        for round in tournament.rounds_list:
            ser_round = self.serialize_round(round)
            res.append(ser_round)
        return res

    def serialize_round(self, round):
        return {
            'Nom': round.round_name,
            'Date de début': round.start_date,
            'Date de fin': round.end_date,
            'Matches': self.serialize_matches(round.list_matches)
        }

    def serialize_matches(self, matches):
        res = []
        for match in matches:
            ser_match = TournamentControler.serialize_match(match)
            res.append(ser_match)
        return res

    @staticmethod
    def serialize_match(match):
        if isinstance(match[0][0], int):
            return {
                'J1': [match[0][0], match[0][1]],
                'J2': [match[1][0], match[1][1]]
                }
        else:
            return {
                'J1': [match[0][0].ind, match[0][1]],
                'J2': [match[1][0].ind, match[1][1]]
                }

    @staticmethod
    def serialized_one_player_for_match(player):
        ser_player = {player.last_name}
        return ser_player

    def current_tournament_none(self):
        self.current_tournament = None
        return self.current_tournament
