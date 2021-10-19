import tournament.round_obj as tround
import tournament.tournament as tournament_
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
        Tournament = tournament_.Tournament(index, name_tounament, location_tournament, date_tournament,
                                            description_tournament)
        self.tournament_list.append(Tournament)
        self.current_tournament = Tournament
        return Tournament

    def validate_date(self, date_text):
        try:
            datetime.datetime.strptime(date_text, '%d-%m-%Y')
            res = True
        except ValueError:
            print("Incorrect date format, should be JJ-MM-AAAA")
            res = False
        return res

    def end_date(self):
        mydatetime = datetime.datetime.now()
        tround.Round.end_date = mydatetime.strftime('%d-%m-%Y %H:%M:%S')

    @property
    def create_new_round(self):
        mydatetime = datetime.datetime.now()
        date = mydatetime.strftime('%d-%m-%Y %H:%M:%S')
        name = self.create_new_round_name
        roundd = tround.Round(name, date)  # créer un round
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
        db = TinyDB('view_tournament.json')
        tournament_table = db.table('tournament')
        serialized_tournament = tournament_table.all()

        for ind, ser_tournament in enumerate(serialized_tournament):
            Tournament = tournament_.Tournament(ser_tournament['Ind'], ser_tournament['Nom'], ser_tournament['Lieu'],
                                                ser_tournament['Date'], ser_tournament['Description'])
            self.load_rounds(Tournament, ser_tournament['Liste des rounds'])
            self.load_tournament_players(Tournament, ser_tournament['Liste des joueurs'])
            self.tournament_list.append(Tournament)

    def load_rounds(self, tournament1, serialized_rounds):
        for ser_round in serialized_rounds:
            round = self.load_round(ser_round)
            tournament1.add_round(round)

    def load_round(self, serialized_round):
        res = tround.Round(serialized_round['Nom'], serialized_round['Date de début'])
        res.end_date = serialized_round['Date de fin']
        self.load_matches(res, serialized_round['Matches'])
        return res

    def load_matches(self, round, serialized_matches):
        for ser_match in serialized_matches:
            match = self.load_match(ser_match)
            round.add_match(match)

    def load_match(self, serialized_match):
        ser_p1 = serialized_match['J1']  # ser_p1 = [1, 0.5]
        player1 = self.load_player(ser_p1[0])
        p1_score = [player1, ser_p1[1]]  # p1_score = [{object player 1}, 0.5]

        ser_p2 = serialized_match['J2']  # ser_p1 = [1, 0.5]
        player2 = self.load_player(ser_p2[0])
        p2_score = [player2, ser_p2[1]]  # p1_score = [{object player 1}, 0.5]

        res = (p1_score, p2_score)
        return res

    def load_tournament_players(self, tournament1, serialized_players):
        for player_ind in serialized_players:
            player = self.load_player(player_ind)
            tournament1.add_player(player)

    def load_player(self, player_ind):
        return self.__root_controler.player_controler.get_player(player_ind)

    def save_all_tournaments(self):
        # serialize players
        serialized_tournaments = []
        for tournament1 in self.tournament_list:
            ser_tournament = self.serialize_tournament(tournament1)
            serialized_tournaments.append(ser_tournament)

        # save serialized data
        db = TinyDB('view_tournament.json')
        tournament_table = db.table('tournament')
        tournament_table.truncate()  # clear the table first
        tournament_table.insert_multiple(serialized_tournaments)

    def serialize_tournament(self, tournament1):
        return {
            'Ind': tournament1.index,
            'Nom': tournament1.name_tournament,
            'Lieu': tournament1.location_tournament,
            'Date': tournament1.date_tournament,
            'Description': tournament1.description_tournament,
            'Liste des rounds': self.serialize_rounds(tournament1),
            'Liste des joueurs': [p.ind for p in tournament1.players_tournament_list],
        }

    def serialize_rounds(self, tournament1):
        res = []
        for round in tournament1.rounds_list:
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
