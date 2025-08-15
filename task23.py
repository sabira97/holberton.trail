from abc import ABC, abstractmethod

class Sport (ABC):
    @abstractmethod
    def play(self):
        pass
class Football(Sport):
    def play(self):
        print("Playing football :soccer:")
class Chess(Sport):
    def play(self):
        print("Playing chess :chess_pawn:")
Football().play()
Chess().play()