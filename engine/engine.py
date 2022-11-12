import numpy as np
import re

class Game():
    GUESSING_BOARD = 4
    def __init__(self,size):
        try:
            assert size >= self.GUESSING_BOARD
            self.size = size
            print("GUESS THE COMBINATION, NUMBERS FROM 0 TO {}".format(self.size-1))
            self.generate_solution()
            self.turn = 1
            self.results = {} # dict for {turn:{in,in_place}}
        except AssertionError:
            print("The size of the game must be at least {}".format(self.GUESSING_BOARD))

    def generate_solution(self):
        values = np.arange(self.size)
        self.solution = np.random.choice(values,replace=False,size=self.GUESSING_BOARD)
    
    def ask(self):
        continue_loop = True
        while continue_loop:
            user_combination = []
            combination = input("Turn {}. Insert combination (a1 a2 ... a{}): ".format(self.turn,self.GUESSING_BOARD))
            combination_split = re.split("\s",combination)
            if len(combination_split) == self.GUESSING_BOARD:
                for cipher in combination_split:
                    try:
                        user_combination.append(int(cipher))
                    except ValueError:
                        break
            if len(user_combination) == self.GUESSING_BOARD:
                self.user_combination = user_combination
                continue_loop = False

    def count(self):
        solution = set(self.solution)
        found = {'in_place':0,'in':0}
        for u_cipher,s_cipher in zip(self.user_combination,self.solution):
            if u_cipher in solution:
                if u_cipher == s_cipher:
                    found["in_place"] += 1
                else:
                    found["in"] += 1
        self.results[self.turn] = found

    def show_results(self):
        this_result = self.results[self.turn]
        str_show = "✅: {} | 🆗: {}".format(this_result['in_place'],this_result['in'])
        print(str_show)

    def execute(self):
        not_finished = True
        while not_finished:
            self.ask()
            self.count()
            self.show_results()
            if self.results[self.turn]["in_place"] == self.GUESSING_BOARD:
                not_finished = False
            self.turn += 1
        print("YOU WON!")
                 

if __name__ == "__main__":
    new_game = Game(4)
    new_game.execute()
