import abc
import random
import time
from typing import Union

from src.logic.exceptions import InvalidMove
from src.logic.minimax import find_best_move
from src.logic.models import GameState, Mark, Move

class Player(metaclass=abc.ABCMeta):
    def __init__(self, mark: Mark) -> None:
        self.mark = mark

    def make_move(self, game_state: GameState) -> GameState:
        if self.mark is game_state.current_mark:
            if move := self.get_move(game_state):
                return move.after_state
            raise InvalidMove("No more possible moves")
        else:
            raise InvalidMove("It's the other player's turn")

    @abc.abstractmethod
    def get_move(self, game_state: GameState) -> Union[Move, None]:
        """Return the current player's move in the given game state."""

class ComputerPlayer(Player, metaclass=abc.ABCMeta):
    def __init__(self, mark: Mark, delay_seconds: float = 0.25) -> None:
        super().__init__(mark)
        self.delay_seconds = delay_seconds

    def get_move(self, game_state: GameState) -> Union[Move, None]:
        time.sleep(self.delay_seconds)
        return self.get_computer_move(game_state)

    @abc.abstractmethod
    def get_computer_move(self, game_state: GameState) -> Union[Move, None]:
        """Return the computer's move in the given game state."""

class RandomComputerPlayer(ComputerPlayer):
    def get_computer_move(self, game_state: GameState) -> Union[Move, None]:
        return game_state.make_random_move()
        
class MinimaxComputerPlayer(ComputerPlayer):
    def get_computer_move(self, game_state: GameState) -> Union[Move, None]:
        if game_state.game_not_started:
            return game_state.make_random_move()
        else:
            return find_best_move(game_state)