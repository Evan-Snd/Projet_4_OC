class Tournament:

    def __init__(self, index, name_tournament, location_tournament, date_tournament, description_tournament):
        self.__index = index
        self.__name_tournament = name_tournament
        self.__location_tournament = location_tournament
        self.__date_tournament = date_tournament
        self.__description_tournament = description_tournament
        self.__players_tournament = []
        self.__round_list = []

    @property
    def status(self):
        if len(self.__round_list) < 1:  # normalement 8 à la place de 4
            return 'Init'
        elif len(self.__round_list) == 1:
            return 'Round 1'
        elif len(self.__round_list) == 2:
            return 'Round 2'
        elif len(self.__round_list) == 3:
            return 'Round 3'
        elif len(self.__round_list) == 4:
            return 'Round 4'
        else:
            raise Exception("Unexpected case")

    @property
    def current_round(self):
        if len(self.__round_list) > 0:
            return self.__round_list[-1]
        else:
            return None

    @property
    def name_tournament(self):
        return self.__name_tournament

    @property
    def location_tournament(self):
        return self.__location_tournament

    @property
    def date_tournament(self):
        return self.__date_tournament

    @property
    def description_tournament(self):
        return self.__description_tournament

    @property
    def index(self):
        return self.__index

    @property
    def rounds_list(self):
        return list(self.__round_list)

    @property
    def players_tournament_list(self):
        return list(self.__players_tournament)

    @property
    def all_match_list(self):
        res = []
        for round in self.__round_list:
            res.append(round.list_matches)
        return res

    @property
    def back_players_points(self):
        total_points_by_player = {}
        for roundd in self.__round_list:
            for match in roundd.list_matches:
                if match[0][0] not in total_points_by_player:
                    total_points_by_player[match[0][0]] = 0
                    total_points_by_player[match[0][0]] += match[0][1]
                    if match[1][0] not in total_points_by_player:
                        total_points_by_player[match[1][0]] = 0
                        total_points_by_player[match[1][0]] += match[1][1]

                elif match[0][0] in total_points_by_player:
                    total_points_by_player[match[0][0]] += match[0][1]

                    if match[1][0] in total_points_by_player:
                        total_points_by_player[match[1][0]] += match[1][1]

        myList = total_points_by_player.items()
        players_points = list(myList)
        return players_points

    def add_player(self, player):
        self.__players_tournament.append(player)

    def delete_player(self, player):
        self.__players_tournament.remove(player)

    def add_round(self, roundd):
        self.__round_list.append(roundd)
