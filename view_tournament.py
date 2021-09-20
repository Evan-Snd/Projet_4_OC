import sys
import controler


class Vue:

    def __init__(self):
        self.control = controler.Controler()

    @property
    def pcontrol(self):
        return self.control.player_controler

    @property
    def tcontrol(self):
        return self.control.tournament_controler

    # ******************************* MENU PRINCIPALE   *******************************

    def menu(self):
        # Display menu
        print('\n ******************** MENU PRINCIPALE ******************** \n\n'
              '1 - Gestion des joueurs \n'
              '2 - Gestion des tournois\n'
              '3 - Quitter le logiciel\n')
        response = input('Choix : ')

        if response == '1':
            self.menu_players()

        elif response == '2':
            self.menu_tournament()

        elif response == '3':
            x = 1 / 0
            print(x)

    # ******************************* MENU PLAYERS   *******************************

    def menu_players(self):
        print('\n ******************** GESTION DES JOUEURS ******************** \n\n'
              '1 - Enregistrer un joueur \n'
              '2 - Afficher la liste des joueurs \n'
              "3 - Changer le classement d'un joueur\n"
              '4 - Supprimer un joueur\n'
              '5 - Revenir au menu principale\n')

        response = input('Choix : ')
        if response == '1':
            self.insert_and_register_player_information()

        elif response == '2':
            players = self.pcontrol.players  # /!\
            self.view_player_list(players)
            self.menu_players()

        elif response == '3':
            self.change_player_ranking(self.pcontrol.players)
            self.menu_players()

        elif response == '4':
            self.delete_player_from_data_base()
            self.menu_players()

        elif response == '5':
            self.menu()

    # ******************************* MENU TOURNAMENT   *******************************

    def menu_tournament(self):
        print('\n ******************** GESTION DES TOURNOIS ******************** \n\n'
              '1 - Créer un tournoi \n'
              '2 - Afficher la liste des tournois \n'
              '3 - Revenir au menu principale \n')
        response = input('Choix : ')
        if response == '1':
            self.create_tournament()
            self.menu_tournament_2()

        if response == '2':
            # Afficher la liste des tournois
            print(
                '\n ******************* LISTE DES TOURNOIS ******************* ----- (Entrer 00 pour annulé)\n')
            list_tournament = self.tcontrol.tournament_list
            self.view_tournament_list(list_tournament)
            self.find_a_tournament()

        elif response == '3':
            self.menu()

        else:
            self.menu_tournament()

    # ******************************* MENU INITIALISATION TOURNOI  *******************************

    def menu_tournament_2(self):
        if self.tcontrol.status == 'Init':
            print('\n ******************** INITIALISATION DU TOURNOI ********************\n\n'
                  '1 - Ajouter des joueurs au tournoi courant \n'
                  '2 - Supprimer des joueurs du tournoi courant \n'
                  '3 - Créer un premier Round (possible que si 8 joueurs sont inscrits)\n')
            response = input('Choix : ')

            if response == '1':
                self.add_player_to_the_tournament()
                self.menu_tournament_2()

            if response == '2':
                self.delete_player_from_tournament()
                self.menu_tournament_2()

            if response == '3':
                if len(self.tcontrol.current_tournament.players_tournament_list) == 4:
                    print('\n ******************** CREATION DU PREMIER ROUND ********************\n')
                    self.method_create_first_round()
                    k = 0
                    self.menu_tournament_3(k)

                else:
                    print("Il n'y a pas assez de joueur pour créer un Round")
                    self.menu_tournament_2()
            else:
                self.menu_tournament_2()

    # ******************************* MENU ROUND 1   *******************************

    def menu_tournament_3(self, k):
        if self.tcontrol.status == 'Round 1':
            if k >= 2:
                print('\n\n ******************** SAISIE DES RESULTATS ********************\n\n'
                      '1 - Saisir les résultats du Match 1 \n'
                      '2 - Saisir les résultats du Match 2 \n'
                      '3 - Saisir les résultats du Match 3 (Pas programmer) \n'
                      '4 - Saisir les résultats du Match 4 (Pas programmer) \n'
                      '5 - Créer un deuxième round \n')
                response = input('Choix : ')
            else:
                print('\n\n ******************** SAISIE DES RESULTATS ********************\n\n'
                      '1 - Saisir les résultats du Match 1 \n'
                      '2 - Saisir les résultats du Match 2 \n'
                      '3 - Saisir les résultats du Match 3 (Pas programmer) \n'
                      '4 - Saisir les résultats du Match 4 (Pas programmer) \n')
                response = input('Choix : ')

            if response == '1':
                match = self.tcontrol.get_match(0)
                self.insert_result_of_the_match(match)
                k = k + 1
                print('\n\nRESULTAT DU MATCH 1 ENREGISTRE')

            elif response == '2':
                match2 = self.tcontrol.get_match(1)
                self.insert_result_of_the_match(match2)
                k = k + 1
                print('\n\nRESULTAT DU MATCH 2 ENREGISTRE')

            elif response == '3':
                pass

            elif response == '4':
                pass

            elif response == '5':
                if k >= 2:
                    print('\n ******************** CREATION DU DEUXIEME ROUND ********************\n')
                    self.method_create_new_round()
                    k = 0
                    self.menu_tournament_4(k)
                else:
                    print(
                        "Impossible de créer un nouveau round tant que les résultats de tous les matchs n'ont pas été saisies")

            else:
                self.menu_tournament_3(k)

            self.menu_tournament_3(k)

    # ******************************* MENU ROUND 2  *******************************

    def menu_tournament_4(self, k):
        if self.tcontrol.status == 'Round 2':
            if k >= 2:
                print('\n\n ******************** SAISIE DES RESULTATS ********************\n\n'
                      '1 - Saisir les résultats du Match 1 \n'
                      '2 - Saisir les résultats du Match 2 \n'
                      '3 - Saisir les résultats du Match 3 (Pas programmer) \n'
                      '4 - Saisir les résultats du Match 4 (Pas programmer) \n'
                      '5 - Créer un deuxième round \n')
                response = input('Choix : ')
            else:
                print('\n\n ******************** SAISIE DES RESULTATS ********************\n\n'
                      '1 - Saisir les résultats du Match 1 \n'
                      '2 - Saisir les résultats du Match 2 \n'
                      '3 - Saisir les résultats du Match 3 (Pas programmer) \n'
                      '4 - Saisir les résultats du Match 4 (Pas programmer) \n')
                response = input('Choix : ')

            if response == '1':
                match = self.tcontrol.get_match(0)
                self.insert_result_of_the_match(match)
                k = k + 1
                print('\n\nRESULTAT DU MATCH 1 ENREGISTRE')

            elif response == '2':
                match2 = self.tcontrol.get_match(1)
                self.insert_result_of_the_match(match2)
                k = k + 1
                print('\n\nRESULTAT DU MATCH 2 ENREGISTRE')

            elif response == '3':
                pass

            elif response == '4':
                pass

            elif response == '5':
                if k >= 2:
                    print('\n ******************** CREATION DU TROISIEME ROUND ********************\n')
                    self.method_create_new_round()
                    k = 0
                    self.menu_tournament_5(k)
                else:
                    print(
                        "Impossible de créer un nouveau round tant que les résultats de tous les matchs n'ont pas été saisies")
            else:
                self.menu_tournament_4(k)

            self.menu_tournament_4(k)

        # ******************************* MENU ROUND 3  *******************************

    def menu_tournament_5(self, k):
        if self.tcontrol.status == 'Round 3':
            if k >= 2:
                print('\n\n ******************** SAISIE DES RESULTATS ********************\n\n'
                      '1 - Saisir les résultats du Match 1 \n'
                      '2 - Saisir les résultats du Match 2 \n'
                      '3 - Saisir les résultats du Match 3 (Pas programmer) \n'
                      '4 - Saisir les résultats du Match 4 (Pas programmer) \n'
                      '5 - Créer un deuxième round \n')
                response = input('Choix : ')
            else:
                print('\n\n ******************** SAISIE DES RESULTATS ********************\n\n'
                      '1 - Saisir les résultats du Match 1 \n'
                      '2 - Saisir les résultats du Match 2 \n'
                      '3 - Saisir les résultats du Match 3 (Pas programmer) \n'
                      '4 - Saisir les résultats du Match 4 (Pas programmer) \n')
                response = input('Choix : ')

            if response == '1':
                match = self.tcontrol.get_match(0)
                self.insert_result_of_the_match(match)
                k = k + 1
                print('\n\nRESULTAT DU MATCH 1 ENREGISTRE')

            elif response == '2':
                match2 = self.tcontrol.get_match(1)
                self.insert_result_of_the_match(match2)
                k = k + 1
                print('\n\nRESULTAT DU MATCH 2 ENREGISTRE')

            elif response == '3':
                pass

            elif response == '4':
                pass

            elif response == '5':
                if k >= 2:
                    print('\n ******************** CREATION DU QUATRIEME ROUND ********************\n')
                    self.method_create_new_round()
                    k = 0
                    self.menu_tournament_6(k)
                else:
                    print(
                        "Impossible de créer un nouveau round tant que les résultats de tous les matchs n'ont pas été saisies")
            else:
                self.menu_tournament_5(k)

            self.menu_tournament_5(k)

        # ******************************* MENU ROUND 4  *******************************

    def menu_tournament_6(self, k):
        if self.tcontrol.status == 'Round 4':
            if k >= 2:
                print('\n\n ******************** SAISIE DES RESULTATS ********************\n\n'
                      '1 - Saisir les résultats du Match 1 \n'
                      '2 - Saisir les résultats du Match 2 \n'
                      '3 - Saisir les résultats du Match 3 (Pas programmer) \n'
                      '4 - Saisir les résultats du Match 4 (Pas programmer) \n'
                      '5 - Créer un deuxième round \n')
                response = input('Choix : ')
            else:
                print('\n\n ******************** SAISIE DES RESULTATS ********************\n\n'
                      '1 - Saisir les résultats du Match 1 \n'
                      '2 - Saisir les résultats du Match 2 \n'
                      '3 - Saisir les résultats du Match 3 (Pas programmer) \n'
                      '4 - Saisir les résultats du Match 4 (Pas programmer) \n')
                response = input('Choix : ')

            if response == '1':
                match = self.tcontrol.get_match(0)
                self.insert_result_of_the_match(match)
                k = k + 1
                print('\n\nRESULTAT DU MATCH 1 ENREGISTRE')

            elif response == '2':
                match2 = self.tcontrol.get_match(1)
                self.insert_result_of_the_match(match2)
                k = k + 1
                print('\n\nRESULTAT DU MATCH 2 ENREGISTRE')

            elif response == '3':
                pass

            elif response == '4':
                pass

            elif response == '5':
                if k >= 2:
                    self.menu_classement_final()
                else:
                    print(
                        "Impossible de créer un nouveau round tant que les résultats de tous les matchs n'ont pas été saisies")
            else:
                self.menu_tournament_6(k)

            self.menu_tournament_6(k)
            # def save_tournament

        # ******************************* MENU ROUND 4  *******************************

    def menu_classement_final(self):
        print('\n ******************** CLASSEMENT FINAL ********************\n')
        classement_after_round = self.tcontrol.sorting_player_classement_after_round
        self.view_classement_players(classement_after_round)
        self.control.save_all()
        print('\n1 - Revenir au menu principale \n'
              "2 - Changer le classement d'un joueur\n")
        response = input('Choix : ')
        if response == '1':
            self.menu()
        elif response == '2':
            # change player classement
            pass
        else:
            self.menu_classement_final()

    # change player classement

    # ******************************* INSERT RESULT OF THE MATCH *******************************

    def insert_result_of_the_match(self, match):
        print('\n ******************** RESULTAT DU MATCH ********************\n\n')
        self.view_match_versus(match)
        print('\n1 - Le joueur 1 a gagné \n'
              '2 - Le joueur 2 a gagné \n'
              '3 - Egalité \n')
        result = input('Choix : ')

        if result == '1':
            result_match = self.tcontrol.player1_win(match)
            self.view_result_of_the_match(result_match)

        elif result == '2':
            result_match = self.tcontrol.player2_win(match)
            self.view_result_of_the_match(result_match)

        elif result == '3':
            result_match = self.tcontrol.nobody_win(match)
            self.view_result_of_the_match(result_match)

    # ******************************* INSERT AND REGISTER PLAYER  *******************************

    def insert_and_register_player_information(self):
        ind = len(self.pcontrol.players) + 1
        last_name = input('\nEntrer un Nom (Majuscule au debut) : ')
        first_name = input('Entrer un Prénom (Majuscule au debut) : ')
        date_birth = input('Entrer une date de naissance (jj/mm/aaaa) : ')
        gender = input('Entre un genre (M/F) : ')
        classement = input('Entrer un classement :')
        self.pcontrol.register_player(ind, last_name, first_name, date_birth, gender, classement)

    # ******************************* METHODE VIEW  *******************************

    def view_player_list(self, players):
        msg_list = []
        for player in players:
            msg_player = "Ind: {} ; Nom: {} ; Prénom: {} ; Date de naissance: {} ; Sexe: {} ; Classement: {}".format(
                player.ind, player.last_name, player.first_name, player.date_birth, player.gender, player.classement)
            msg_list.append(msg_player)
        print("\n".join(msg_list))

    def view_match_versus(self, match):
        msg_versus_list = []
        i = 1
        for player_result in match:
            player = player_result[0]
            msg_player = "Joueur {} : {} {}".format(i, player.last_name, player.first_name)
            i = i + 1
            msg_versus_list.append(msg_player)
        print("\n".join(msg_versus_list))

    def view_result_of_the_match(self, match):
        msg_versus_list = []
        i = 0
        for player_result in match:
            player = player_result[0]
            msg_player = " {} ; {}".format(player.last_name, player.first_name) + ' ; Points : ' + str(match[i][1])
            i = i + 1
            msg_versus_list.append(msg_player)
        print("\n".join(msg_versus_list))

    def view_tournament_list(self, tournament_list):
        msg_list = []
        for tournament in tournament_list:
            msg_player = "\nIndex : {} \nNom du Tournoi : {} \nLieu du tournoi : {} \nDate du tournoi : {} \nDescription du tournoi : {}".format(
                tournament.index, tournament.name_tournament, tournament.location_tournament,
                tournament.date_tournament,
                tournament.description_tournament)
            msg_list.append(msg_player)
        print("\n".join(msg_list))

    def view_classement_players(self, players_points):
        msg_versus_list = []
        for i, player_result in enumerate(players_points):
            player = player_result[0]
            msg_player = "{} {} ; Classement : {}".format(player.last_name, player.first_name,
                                                          player.classement) + ' ; Points : ' + str(
                players_points[i][1])
            msg_versus_list.append(msg_player)
        print("\n".join(msg_versus_list))

    def view_round_list(self, round_list):
        msg_round_list = []
        for roundd in round_list:
            msg_round = "\nNom : {} \nDate de début : {} ; \nListe des matchs : {}".format(roundd.round_name,
                                                                                           roundd.start_date,
                                                                                           roundd.list_matches)
            msg_round_list.append(msg_round)
        print("\n".join(msg_round_list))

    def view_match_list(self, match_list):
        msg_match_list = []
        for k, match_round in enumerate(match_list):
            msg_match_list.append('\n******************** ROUND ' + str(k + 1) + ' ********************')
            for i, match in enumerate(match_round):
                msg_match_list.append('\nMatch ' + str(i + 1) + ':\n')
                for player_result in match:
                    player = self.tcontrol.load_player(player_result[0])
                    msg_match = " {} ".format(player.first_name + ' ' + player.last_name) + '  Points : ' + str(
                        match[i][1])
                    msg_match_list.append(msg_match)
        print("\n".join(msg_match_list))

    # ******************************* CREATE TOURNAMENT  *******************************

    def create_tournament_object(self):
        print('\n ******************** CREATION DU TOURNOI ********************\n'
              "Rentrez '00' si vous voulez revenir en arriere en cas d'erreur\n")
        index = len(self.tcontrol.tournament_list) + 1
        name_tournament = input('\nNom du tournoi (entre guillemets) : ')
        self.back_return(name_tournament)
        location_tournament = input('Lieu du tournoi : ')
        if location_tournament == '00':
            self.create_tournament_object()
        date_tournament = input('Date de début du tournoi :') + ' - ' + input('Date de fin du tournoi :')
        self.back_return(date_tournament)
        description_tournament = input('Description du tournoi :')
        self.back_return(description_tournament)
        tournament = self.tcontrol.create_tournament(index, name_tournament, location_tournament, date_tournament,
                                                     description_tournament)
        if (index or name_tournament or location_tournament or date_tournament or description_tournament) == '0':
            self.create_tournament()
        return tournament

    def back_return(self, information):
        if information == '00':
            self.create_tournament_object()

    def create_tournament(self):
        response = input('\nCréer un nouveau tournoi ? [oui/non] ')
        if response == 'oui':
            tournament = self.create_tournament_object()
            return tournament
        else:
            self.menu_tournament()

    # ******************************* GENERATE MATCH  *******************************

    def generate_one_match_by_ranking(self, player1, player2):
        return ([player1, None],
                [player2, None])

    def generate_four_match_by_ranking(self, players_by_ranking):
        print('\nListe des match pour le premier tour :')
        for i in range(0, 2):  # (0,4)
            player1 = players_by_ranking[i]
            player2 = players_by_ranking[i + 2]  # [i+4]
            match = self.generate_one_match_by_ranking(player1, player2)
            print('\nMatch ' + str(i + 1) + ':')
            self.view_match_versus(match)  # Afficher Joueur 1 vs Joueur 2
            self.tcontrol.add_match_to_current_round(match)

    def generate_four_match_by_points(self, player_by_points):
        res = []
        available_players = [pp[0] for pp in player_by_points]
        for i in range(2):
            player1 = available_players[0]
            player2 = self.__find_other_player_for_match(player1, available_players[1:])
            if player2 is None:
                player2 = available_players[1]
            # Create match
            match = self.generate_one_match_by_ranking(player1, player2)
            print('\nMATCH ' + str(i + 1) + ':')
            self.view_match_versus(match)  # Afficher Joueur 1 vs Joueur 2
            self.tcontrol.add_match_to_current_round(match)
            res.append(match)
            available_players.remove(player1)
            available_players.remove(player2)

        return res

    def __find_other_player_for_match(self, player1, other_players):
        """Return the player that will play with player1"""
        for player2 in other_players:
            if not self.__has_players_already_played(player1, player2):
                return player2

    def __has_players_already_played(self, player1, player2):
        """Return if player1 and player2 have already played"""
        for roundd in self.tcontrol.round_list:
            for match in roundd.list_matches:
                if (match[0][0] == player1 and match[1][0] == player2) or (
                        match[0][0] == player2 and match[1][0] == player1):
                    return True
        return False

    # ******************************* CREATE ROUND  *******************************

    def method_create_first_round(self):
        if len(self.tcontrol.current_tournament.players_tournament_list) == 4:  # (8 à la place de 4 normalement)
            roundd = self.tcontrol.create_new_round
            self.tcontrol.add_round_to_current_tournament(roundd)
            list_sorting_by_rankink = self.tcontrol.sorting_player_ranking
            # générer des 4 paires en fonction du classement pour le premier tour
            self.generate_four_match_by_ranking(list_sorting_by_rankink)
        else:
            print("Impossible de créer le premier round tant que les joueurs n'ont pas été ajoutés")

    def method_create_new_round(self):
        roundd = self.tcontrol.create_new_round
        self.tcontrol.add_round_to_current_tournament(roundd)
        classement_after_round = self.tcontrol.sorting_player_classement_after_round
        self.view_classement_players(classement_after_round)
        self.generate_four_match_by_points(classement_after_round)

    # ******************************* ADD PLAYER TO TOURNAMENT  *******************************

    def add_player_to_the_tournament(self):
        while len(self.tcontrol.current_tournament.players_tournament_list) <= 3:  # NORMALEMENT 7 A LA PLACE DE 3
            print("\n************************* AJOUT D'UN JOUEUR : *************************\n")
            print('\nNOMBRE DE JOUEURS INSCRITS AU TOURNOI : ' + str(
                len(self.tcontrol.current_tournament.players_tournament_list)))
            last_name = input('\nEntrer un Nom (Majuscule au debut) : ')
            player_find = self.control.find_players(last_name)
            print("\n************************* JOUEUR TROUVE : *************************\n")
            self.view_player_list(player_find)
            index = input("\nENTRER l'ID DU JOUEUR (00=cancel): ")
            for player in player_find:
                if player.ind == int(index):
                    self.tcontrol.add_player_to_current_tournament(player)
                    print("\nJOUEUR AJOUTE")
                    break
                elif index == '00':
                    # retour à la séléction de nom et prenom
                    self.add_player_to_the_tournament()
                else:
                    continue
        print('\nLISTE DES JOUEURS POUR LE TOURNOI :')
        self.view_player_list(self.tcontrol.current_tournament.players_tournament_list)

    # ******************************* DELETE A PLAYER FROM TOURNAMENT *******************************

    def delete_player_from_tournament(self):
        print("\n************************* SUPPRESSION D'UN JOUEUR DU TOURNOI : *************************\n")
        last_name = input('\nEntrer un Nom (Majuscule au début) : ')
        player_find = self.control.find_players_in_tournament(last_name)
        print("\n************************* JOUEUR TROUVE : *************************\n")
        self.view_player_list(player_find)
        index = input("\nENTRER l'ID DU JOUEUR (00=cancel): ")
        for player in player_find:
            if player.ind == int(index):
                self.tcontrol.delete_player_to_current_tournament(player)
                print("\nJOUEUR SUPPRIME")
                break
            elif index == '00':
                # retour à la séléction de nom et prenom
                self.menu_tournament_2()

        print('\nLISTE DES JOUEURS POUR LE TOURNOI :')
        self.view_player_list(self.tcontrol.current_tournament.players_tournament_list)

        # ******************************* DELETE A PLAYER FROM THE DATA BASE *******************************

    def delete_player_from_data_base(self):
        print("\n************************* SUPPRESSION D'UN JOUEUR DE LA BASE DE DONNEES : *************************\n")
        last_name = input('\nEntrer un Nom (Majuscule au debut) : ')
        player_find = self.control.find_players(last_name)
        print("\n************************* JOUEUR TROUVE : *************************\n")
        self.view_player_list(player_find)
        index = input("\nENTRER l'ID DU JOUEUR (00=cancel): ")
        for player in player_find:
            if player.ind == int(index):
                self.pcontrol.delete_player(player)
                print("\nJOUEUR SUPPRIME")
                break
            elif index == '00':
                # retour à la séléction de nom et prenom
                self.menu_tournament_2()
        self.pcontrol.save_players()

    # ******************************* FIND A TOURNAMENT  *******************************

    def find_a_tournament(self):
        name_tournament = input('\nEntrer le Nom du tournoi recherché (Majuscule au debut) :')
        if name_tournament == '00':
            self.menu_tournament()
        tournament_find = self.control.find_tournament(name_tournament)
        print("\n************************* TOURNOI TROUVE : *************************")
        self.view_tournament_list(tournament_find)
        index = input("\nENTRER l'INDEX DU TOURNOI (00=cancel): ")
        for tournament in tournament_find:
            if tournament.index == int(index):
                self.tcontrol.current_tournament = tournament
                round_list = self.tcontrol.round_list
                list_match = []
                for roundd in round_list:
                    list_match.append(self.tcontrol.list_match)
                list_players = self.tcontrol.players_list
                self.menu_view_tournoi_informations(round_list, list_match, list_players)
            elif tournament.index != int(index):
                print("L'indice rentré ne correspond a aucun Tournoi")
                self.find_a_tournament()
            elif index == '00':
                # retour à la séléction de nom et prenom
                self.find_a_tournament()
        self.find_a_tournament()

    # ******************************* CHANGE PLAYER RANKING  *******************************

    def change_player_ranking(self, players_list):
        last_name = input('\nEntrer un Nom (Majuscule au debut) : ')
        player_find = self.control.find_players(last_name)
        print("\n************************* JOUEUR TROUVE : *************************\n")
        self.view_player_list(player_find)
        index = input("\nENTRER l'ID DU JOUEUR (00=cancel): ")
        for player in player_find:
            if player.ind == int(index):
                print('\nJOUEUR SELECTIONNE :')
                print("\nInd: {} ; Nom: {} ; Prénom: {} ; Date de naissance: {} ; Classement: {}".format(
                    player.ind, player.last_name, player.first_name, player.date_birth,
                    player.classement))
                new_rank = input('\n Attribué le nouveau classement : ')
                player.classement = int(new_rank)
                for players in players_list:
                    if players == player:
                        continue
                    elif players.classement >= player.classement:
                        players.classement += 1
                    else:
                        continue
                break
            else:
                continue
        self.pcontrol.save_players()

    # ******************************* MENU VIEW TOURNAMENT INFORMATIONS  *******************************

    def menu_view_tournoi_informations(self, round_list, list_match, list_players):
        print("\n\n ******************** LISTE D'AFFICHAGE DU TOURNOI ********************\n\n"
              '1 - Afficher tous les joueurs du tournoi \n'
              '2 - Afficher tous les round du tournoi \n'
              '3 - Afficher tous les match du tournoi \n'
              '4 - Revenir a la gestion des tournois\n')
        response = input('Choix : ')

        if response == '1':
            self.menu_view_players_by_ranking_and_alphabetical_order(round_list, list_match, list_players)
        elif response == '2':
            self.view_round_list(round_list)
            self.menu_view_tournoi_informations(round_list, list_match, list_players)
        elif response == '3':
            self.view_match_list(list_match)
            self.menu_view_tournoi_informations(round_list, list_match, list_players)
        elif response == '4':
            self.menu_tournament()

    # ******************************* MENU VIEW PLAYERS IN THE TOURNAMENT  *******************************

    def menu_view_players_by_ranking_and_alphabetical_order(self, round_list, list_match, list_players):
        print("\n\n ******************** LISTE D'AFFICHAGE DES JOUEURS ********************\n\n"
              '1 - Afficher par ordre alphabétique \n'
              '2 - Afficher par ordre de classement \n'
              "3 - Revenir au menu d'affichage \n")
        response = input('Choix : ')

        if response == '1':
            print('\nListe des joueurs par ordre alphabétique : \n')
            all_players = sorted(list_players, key=lambda player: player.last_name)
            self.view_player_list(all_players)
        elif response == '2':
            print('\nListe des joueurs par ordre de classement : \n')
            all_players = sorted(list_players, key=lambda player: player.classement)
            self.view_player_list(all_players)
        elif response == '3':
            self.menu_view_tournoi_informations(round_list, list_match, list_players)
        self.menu_view_players_by_ranking_and_alphabetical_order(round_list, list_match, list_players)

    # ******************************* MAIN *******************************


if __name__ == "__main__":
    vue = Vue()
    try:
        while True:
            vue.menu()
    except ZeroDivisionError as exc:
        # print error
        pass
    finally:
        # save
        pass
    sys.exit(0)

# test = self.tcontrol.current_round
#         print(test)
