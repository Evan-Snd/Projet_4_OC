class Round:

    def __init__(self, round_name, start_date):
        self.__round_name = round_name
        self.__start_date = start_date
        self.__end_date = None
        self.__list_match = []

    @property
    def round_name(self):
        return self.__round_name

    @property
    def start_date(self):
        return self.__start_date

    @property
    def end_date(self):
        return self.__end_date

    @end_date.setter
    def end_date(self, end_date):
        self.__end_date = end_date

    @property
    def list_matches(self):
        return self.__list_match

    def add_match_to_list_match(self, match):
        if len(self.__list_match) == 4:
            raise Exception("The round has already 4 matches")
        self.__list_match.append(match)

    def get_match(self, index):
        return self.__list_match[index]

    def player1_win(self, match):
        match[0][1] = 1
        match[1][1] = 0
        return match

    def player2_win(self, match):
        match[0][1] = 0
        match[1][1] = 1
        return match

    def nobody_win(self, match):
        match[0][1] = 1/2
        match[1][1] = 1/2
        return match

    def add_match(self, match):
        self.__list_match.append(match)
