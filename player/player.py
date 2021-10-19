class Player:

    def __init__(self, ind, last_name, first_name, date_birth, gender, classement):
        self.__ind = ind
        self.__last_name = last_name
        self.__first_name = first_name
        self.__date_birth = date_birth
        self.__gender = gender
        self.__classement = classement

    @property
    def last_name(self):
        return self.__last_name

    @property
    def first_name(self):
        return self.__first_name

    @property
    def date_birth(self):
        return self.__date_birth

    @property
    def gender(self):
        return self.__gender

    @property
    def classement(self):
        return self.__classement

    @classement.setter
    def classement(self, classement):
        if type(classement) != int:
            raise Exception("The classment must be an integer")
        self.__classement = classement

    @property
    def ind(self):
        return self.__ind
