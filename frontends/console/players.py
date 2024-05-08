import re
from typing import Union

from src.game.players import Player
from src.logic.exceptions import InvalidMove
from src.logic.models import GameState, Move

class ConsolePlayer(Player):
    def get_move(self, game_state: GameState) -> Union[Move, None]:
        while not game_state.game_over:
            try:
                index = grid_to_index(input(f"{self.mark}'s move: ").strip())
            except ValueError:
                print("Please provide coordinates in the form of A1 or 1A")
            else:
                try:
                    return game_state.make_move_to(index)
                except InvalidMove:
                    print("That cell is already occupied.")
        return None
    
def grid_to_index(grid: str) -> int:
    if re.match(r"[abcABC][123]", grid):
        col, row = grid
    elif re.match(r"[123][abcABC]", grid):
        row, col = grid
    else:
        raise ValueError("Invalid grid coordinates")
    return 3 * (int(row) - 1) + (ord(col.upper()) - ord("A"))