"""" i tried really hard to put it in LAN but i couldn't until now, i think i might keep trying
it would resolve some problems of the game, i couldn't also, hide the cards of the players from 
other players, cause to do that i needed to have a Lan game working, or not, im not sure
"""

import random


def howtoplay():
    print("""
    The "dirty deck" of 40 cards is used, but the manilhas are not fixed. After the cards have been dealt, the top card of the remaining deck is turned face up: this card is known as the "vira" (turned card). The manilhas for this hand are the four cards of the rank immediately above the vira in the cyclic order [4]-3-2-A-K-J-Q-7-6-5-4-[3]. For example if the vira is a Five, the manilhas are the Sixes, if the vira is a Seven the manilhas are the Queens (remember that Queens normally rank below Jacks in this game), and if the vira is a Three (the highest rank), the manilhas are the Fours (the lowest). The four manilhas rank according to their suits in descending order Clubs > Hearts > Spades > Diamonds. This system is sometimes known as manilha nova (new manilha), while the fixed manilhas in Truco Mineiro are known as manilha velha (old manilha). Note that the suit order of the manilhas in Truco Paulista is the same as the suit order of the fixed manilhas in Truco Mineiro. The other cards rank in the normal Truco order 3-2-A-K-J-Q-7-6-5-4, missing out the manilha rank.

Example: if the vira is a Jack, the cards rank from high to low: clubK - heartK - spadeK - diamondK - 3's - 2's - A's - J's - Q's - 7's - 6's - 5's - 4's

Gustavo Schafaschek reports that in his states of origin - Paraná and Santa Catarina, in the south - the manilhas are known as Gato (clubs), Copas (hearts), Espadilha (spades) and Mole or Salmoura (diamonds). The rules of play in Truco Paulista differ from Truco Miniero as follows:

The deal is one card at a time, in counter-clockwise order, normally from the bottom of the deck. There is no opportunity to pass or burn cards - everyone plays with the three cards they are dealt.
A call of truco is a bet on winning the hand according to the usual criteria: winning two tricks or the first trick won in case of ties - not just a bet on who will win the current trick.
When a trick is tied, the same player who led to the tied trick leads to the next trick.
As usual the first bet, if accepted, raises the stake of the hand from 1 to 3 points. If it is accepted, the play continues as usual, up to the third trick if necessary, to determine the result. If the opponents wish to raise the stake to 6, they do not have to do this immediately. They can continue the play and interrupt it later to call vale 6, and the first team must reply before play continues again. Subsequent bets by alternate teams raising the stake to 9 and 12 are also possible.
Immediately after truco is called, the opponents can look at each other's hands by passing all cards face down to each other and discuss whether to accept the call. Similarly, if the opposing team decides to call 6 later on (or immediately), the Truco-calling team can also look at each other's hands before deciding if they accept the raise to 6 or decline.
When one team has 11 points the cards are dealt as usual (one at a time from the bottom of the deck). No truco calls are allowed. Before play begins, the members of the team with 11 points can look at each other's hands by passing their cards to each other face down across the table, and must then decide whether to give up for 1 point or play for 3 points.
When both teams have 11 points an iron hand (mão de ferro) is played: the cards are dealt as usual but players must not look at their cards. Instead they play to the tricks by simply turning over their top card, and the winners of the deal win the game.
When one or both of the teams has 11 points, calling truco automatically gives the victory to the opposing team - that is, the opposing team wins the entire game, not only the hand! This is a very harsh rule and very easy to fall for, so one needs to be very careful to not say truco when one of the teams has 11 points.

    """)


def help(a):
    if "--help" in trying or "--help" in a:
        howtoplay()
        stop = input("Write --resume to go on with the game: ")
        if "--resume" in stop:
            pass


def createDeck():
    Deck = []
    letters = ["A", "Q", "J", "K"]
    for card in range(2, 8):
        Deck.append(str(card) + "h")
        Deck.append(str(card) + "s")
        Deck.append(str(card) + "d")
        Deck.append(str(card) + "c")

    for card in letters:
        Deck.append(str(card) + "h")
        Deck.append(str(card) + "s")
        Deck.append(str(card) + "d")
        Deck.append(str(card) + "c")
    random.shuffle(Deck)
    return Deck


deck = createDeck()

if len(deck) <= 500:
    deck = createDeck()


class game:

    def __init__(self):
        self.manilha = createDeck().pop()
        self.dic = []

    def vira(self):
        self.mani = createDeck().pop()
        self.dic = []
        cardsdict = [{"Ah": 22, "As": 21, "Ad": 20, "Ac": 23}, {"2h": 22, "2c": 23, "2d": 20, "2s": 21},
                     {"3h": 22, "3s": 21, "3d": 20, "3c": 23}, {"4h": 22, "4s": 21, "4d": 20, "4c": 23},
                     {"5h": 22, "5s": 21, "5c": 23, "5d": 20}, {"6h": 22, "6s": 21, "6d": 20, "6c": 23},
                     {"7h": 22, "7s": 21, "7d": 20, "7c": 23}, {"Qh": 22, "Qs": 21, "Qd": 20, "Qc": 23},
                     {"Jh": 22, "Js": 21, "Jd": 20, "Jc": 23}, {"Kh": 22, "Ks": 21, "Kd": 20, "Kc": 23}
                     ]
        for cards in cardsdict:
            if self.manilha in cards:
                self.dic += cards
        return self.dic

    def outrovira(self):
        if self.manilha in self.dic:
            self.manilha = createDeck().pop()
            return

    def samegame(self):
        self.vira()
        print("The manilhas of the game are", self.vira())



point = 1

tru = False
mo6 = False
mo9 = False
mo12 = False
moa = False
nomtru = ""
trunom = ""


def turco(name):
    global point, tru, mo6, mo9, mo12, moa, trunom, nomtru
    def falsotruco():
        tru = False
        mo6 = False
        mo9 = False
        mo12 = False
        moa = False
        nomtru = ""
        trunom = ""
        return tru, mo6, mo9, mo12, moa, nomtru, trunom
    if tru == False:
        truco = input("The player " + name + " asked for truco. ")
        if Player1.name == name:
            trunom = Player2.name
            nomtru = Player1.name
        elif Player2.name == name:
            trunom = Player1.name
            nomtru = Player2.name
    else:
        truco = input("You wanna more: (6), (9), (12)?: ")
    try:
        while (True):
            if (truco == "yes" or truco == "y" or truco == "Y" or truco == "YES" or truco == "Yes" or truco == "PODE VIRA POHA") and tru == False:
                point = 3
                tru = True
                print("The player", trunom, "accepted the truco.\n")
                nam = input("put your name (in-game): ")
                if nam == trunom:
                    truco = input("do you "+ trunom+ " wanna ask for 6? (6): ")
                    if truco == "n" or truco == "N":
                        point = 3
                        break
                    elif truco == "y" or truco == "Y" or truco == "YES" or truco == "yes" or truco == "Yes":
                        truco = input("Ther player "+ trunom + " asked for 6, do you wanna go 6? y/n: ")
                        continue
                else:
                    print("pass to the other player, the other player should type 6 to 6 and no to just go on with the truco")
                    return turco(Player)
            elif (truco == "não" or truco == "nao" or truco == "n" or truco == "NÃO" or truco == "N" or truco == "Não") and tru == False:
                point = 1
                if name == Player1.name:
                    Player1.score = 2
                elif name == Player2.name:
                    Player2.score = 2
                win()
            elif truco == "6" and tru == True and mo6 == False:
                truco = input("Ther player "+ trunom + " asked for 6, do you wanna go 6? y/n: ")
                continue
            elif (truco == "y" or truco == "Y") and tru == True and mo6 == False:
                mo6 = True
                print("The player", nomtru, "accepted the 6.\n")
                point = 6
                nam = input("put your name (in-game): ")
                if nam == nomtru:
                    truco = input("do you "+ nomtru+ " wanna ask for 9? (9): ")
                    if truco == "n" or truco == "N":
                        point = 6
                        break
                    elif truco == "y" or truco == "Y":
                        truco = input("Ther player " + nomtru + " asked for 9, do you wanna go 9? y/n: ")
                        continue
                else:
                    print("pass to the other player, the other player should type 9 to 9 and no to just go on with the truco")
                    return turco(Player)
            elif (truco == "não" or truco == "nao" or truco == "n" or truco == "NÃO" or truco == "N" or truco == "Não") and tru == True and mo6 == False:
                point = 3
                if name == Player1.name:
                    Player2.score = 2
                elif name == Player2.name:
                    Player1.score = 2
                win()
            elif truco == "9" and mo6 == True and mo9 == False:
                truco = input("Ther player " + nomtru + " asked for 9, do you wanna go 9? y/n: ")
                continue
            elif (truco == "y" or truco == "Y") and mo6 == True and mo9 == False:
                point = 9
                mo9 = True
                nam = input("put your name: ")
                if nam == trunom:
                    truco = input("do you "+ trunom+ " wanna ask for 12? (y): ")
                    if truco == "n" or truco == "N":
                        point = 9
                        break
                    elif truco == "y" or truco == "Y":
                        truco = input("Ther player " + trunom + " asked for 12, do you wanna go 12? y/n: ")
                        continue
                else:
                    print("pass to the other player, the other player should type 12 to 12 and no to just go on with the truco")
                    return turco(Player)
            elif truco == "12" and mo9 == True and mo12 == False:
                truco = input("Ther player " + trunom + " asked for 12, do you wanna go 12? y/n: ")
                continue
            if truco == "y" or truco == "Y":
                point = 12
                mo12 = True
                break
            elif (truco == "não" or truco == "nao" or truco == "n" or truco == "NÃO" or truco == "N" or truco == "Não") and mo9 == True and mo12 == False:
                point = 9
                if name == Player1.name:
                    Player1.score = 2
                elif name == Player2.name:
                    Player2.score = 2
                win()
            elif mo12 == True:
                break
            else:
                inp = input("you should choose one more than the previous one, truco, 6, 9 or 12: ")
                if inp == "ok" or inp == "OK" or inp == "Ok" or inp == "Y" or inp == "Y":
                    turco(Player)
                elif inp == "n" or inp == "não" or inp == "no" or inp == "nao" or inp == "Não" or inp == "N" or inp == "NÃO" or inp == "NAO":
                    break
    except:
        pass

class Player(game):

    def __init__(self, name="none", hand=[]):
        game.__init__(self)
        self.name = name
        self.hand = hand
        self.score = 0
        self.card = ""
        self.turn = 0
        self.gamescore = 0

    def __str__(self):
        name = input("are you " + self.name + " ?")
        cards = ""
        for card in self.hand:
            cards += str(card) + " "
        player = "Your cards " + self.name + ": " + cards + "\nScore " + str(self.score)
        try:
            if name == "yes" or name == "y" or name == "Y" or name == "YES" or name == "Yes":
                help(name)
                return player
            elif name == "truco" or name == "TRUCO" or name == "Truco" or name == "tRUCO" or name == "6" or name == "9" or name == "12":
                turco(self.name)
                return player
            else:
                self.__str__()
                return player
        except:
            return Player



    def desce(self):
        try:
            card = int(input("with witch card (1, 2, 3) do you wanna go: "))
        except:
            card = str()
            helpp = input("Type --help or truco: ")
            if helpp == "truco" or helpp == "TRUCO" or helpp == "Truco" or helpp == "tRUCO" or helpp == "6" or helpp == "9" or helpp == "12":
                turco(self.name)
            help(helpp)
            return self.desce()
        if -1 < card < 4:
            if card == 1:
                help(str(card))
                self.card = self.hand[0]
                del self.hand[0]
            elif card == 2:
                help(str(card))
                self.card = self.hand[1]
                del self.hand[1]
            elif card == 3:
                help(str(card))
                self.card = self.hand[2]
                del self.hand[2]
        else:
            print("You must have put the wrong card")
            return self.desce()
        return self.card

    def setPontuation(self):
        cardsdict = {"Ah": 11, "As": 11, "Ad": 11, "Ac": 11, "2h": 12, "2c": 12, "2d": 12, "2s": 12,
                     "3h": 13, "3s": 13, "3d": 13, "3c": 13, "4h": 4, "4s": 4, "4d": 4, "4c": 4, "5h": 5,
                     "5s": 5, "5c": 5, "5d": 5, "6h": 6, "6s": 6, "6d": 6, "6c": 6, "7h": 7, "7s": 7, "7d": 7,
                     "7c": 7, "Qh": 8, "Qs": 8, "Qd": 8, "Qc": 8, "Jh": 9, "Js": 9, "Jda": 9, "Jc": 9,
                     "Kh": 10, "Ks": 10, "Kd": 10, "Kc": 10
                     }
        if self.card in cardsdict and self.card not in Firstgame.dic:
            self.turn = int(cardsdict[self.card])
        elif self.card in Firstgame.dic:
            cardmanilha = {"Ah": 22, "As": 21, "Ad": 20, "Ac": 23, "2h": 22, "2c": 23, "2d": 20, "2s": 21,
                           "3h": 22, "3s": 21, "3d": 20, "3c": 23, "4h": 22, "4s": 21, "4d": 20, "4c": 23,
                           "5h": 22, "5s": 21, "5c": 23, "5d": 20, "6h": 22, "6s": 21, "6d": 20, "6c": 23,
                           "7h": 22, "7s": 21, "7d": 20, "7c": 23, "Qh": 22, "Qs": 21, "Qd": 20, "Qc": 23,
                           "Jh": 22, "Js": 21, "Jd": 20, "Jc": 23, "Kh": 22, "Ks": 21, "Kd": 20, "Kc": 23
                           }
            self.turn = int(cardmanilha[self.card])
        return self.turn

    def game(self):
        if self.gamescore >= 12:
            print(self.name, "won the game")
            breakpoint()
        elif self.gamescore <= 11:
            self.hand = [createDeck().pop(), createDeck().pop(), createDeck().pop()]


empardou = 0


def win():
    if Player1.score == 1 and Player2.score == 1:
        print(Player1)
        Player1.desce()
        Player1.setPontuation()
        print(Player2)
        Player2.desce()
        Player2.setPontuation()
        if Player1.turn > Player2.turn:
            print("Player one won the round")
            Player1.score = 0
            Player2.score = 0
            Player1.gamescore += point
            print("The", Player1.name, "has", Player1.gamescore, "points")
            Firstgame.outrovira()
            Firstgame.samegame()
            Player1.game()
            Player2.game()
            jogo()

        elif Player2.turn > Player1.turn:
            print("Player two won the round")
            Player2.gamescore += point
            Player1.score = 0
            Player2.score = 0
            print("The", Player2.name, "has", Player2.gamescore, "points")
            Firstgame.outrovira()
            Firstgame.samegame()
            Player2.game()
            Player1.game()
            jogo()

        else:
            print("The game has tied")
            Firstgame.outrovira()
            Firstgame.samegame()
            Player1.score = 0
            Player2.score = 0
            Player1.game()
            Player2.game()
            jogo()
    elif Player1.score == 2:
        print("Player one has won the round")
        Player1.score = 0
        Player2.score = 0
        Player1.gamescore += point
        print("The", Player1.name, "has", Player1.gamescore, "points")
        Firstgame.outrovira()
        Firstgame.samegame()
        Player1.game()
        Player2.game()
        jogo()
    elif Player2.score == 2:
        print("Player two has won the round")
        Player1.score = 0
        Player2.score = 0
        Player2.gamescore += point
        print("The", Player2.name, "has", Player2.gamescore, "points")
        Firstgame.outrovira()
        Firstgame.samegame()
        Player2.game()
        Player1.game()
        jogo()


def round():
    if Player1.turn > Player2.turn:
        print(Player1.turn)
        print("Player one won this turn")
        Player1.score += 1

    elif Player2.turn > Player1.turn:
        print(Player2.turn)
        print("Player two won this turn")
        Player2.score += 1

    else:
        print("Empardou")
        global empardou
        Player1.score += 1
        Player2.score += 1
        empardou += 1
        return


while True:
    Firstgame = game()
    deck = createDeck()
    firsthand = [deck.pop(), deck.pop(), deck.pop()]
    secondhand = [deck.pop(), deck.pop(), deck.pop()]
    print("The manilhas of the game are", Firstgame.vira())
    name1 = input("What's your name?")
    pass
    if name1 == "--help":
        howtoplay()
        stop = input("Write --resume to go on with the game: ")
        name1 = input("Put your name again (Player 1)")
        if stop == "--resume":
            pass
    name2 = input("What's your name?")
    pass
    if name2 == "--help":
        howtoplay()
        stop = input("Write --resume to go on with the game: ")
        name2 = input("Put your name again (Player 2)")
        if stop == "--resume":
            pass
        else:
            breakpoint()
    Player1 = Player(name1, firsthand)
    Player2 = Player(name2, secondhand)

    trying = [name1, name2, Player1.turn, Player2.turn, Player1, Player2]


    def jogo():
        try:
            for a in range(3):
                Firstgame.vira()
                print(Player1)
                Player1.desce()
                Player1.setPontuation()
                print(Player2)
                Player2.desce()
                Player2.setPontuation()
                round()
                win()
        except:
            pass



    jogo()
