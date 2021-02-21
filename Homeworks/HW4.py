import random as rnd


class Hangman:

    def __init__(self, wordlist):
        self.health = 5
        self.word_list = wordlist
        self.word = "_"
        self.inp = ""
        self.slc_word = ""
        self.dex = []
        self.slc_word = self.select_word()
        self.word *= len(self.slc_word)
        self.checking = 0

    def select_word(self):
        return self.word_list[rnd.randint(0, len(self.word_list) - 1)]

    def print_health(self):
        print("Your Health: {}".format(self.health))

    def game(self):
        while self.health > 0:
            print("Your Word:\n{}".format(self.word), sep="\n")
            self.inp = str(input("Please Enter Character: "))
            if len(self.inp) > 1:
                print("\nWrong Usage!!", sep="\n")
                self.wrong_disp()
                self.print_health()
                if self.health == 0:
                    print("GAME OVER!")
                    break
            else:
                self.dex = [pos for pos, char in enumerate(self.slc_word) if char == self.inp]
                if not self.dex:
                    print("Wrong Character!")
                    self.wrong_disp()
                    self.print_health()
                else:
                    for i in self.dex:
                        self.word = self.word[:i] + self.inp + self.word[i + 1:]
                        self.checking = self.word.find('_')

                        if self.checking == -1:
                            print("YOU WIN!!")
                            break
            if self.checking == -1:
                break

    def wrong_disp(self):
        stages = [
            """
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / \\
                       -
                       """, """
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     /
                       -
                       """,
            """
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |
                       -
                       """,
            """
                       --------
                       |      |
                       |      O
                       |
                       |
                       |
                       -
                     """,
            """
                       --------
                       |      |
                       |      
                       |
                       |
                       |
                       -
                       """

        ]
        print(stages[self.health - 1])
        self.health += -1
        if self.health == 0:
            print("YOU DIE!!")


wordList = ["adana", "mersin", "ankara", "bolu"]

hangman = Hangman(wordList)

hangman.game()
