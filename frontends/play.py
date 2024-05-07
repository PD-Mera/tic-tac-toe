import sys
sys.path.append("/home/data/dongtrinh/tic-tac-toe-ai")

from src.game.engine import TicTacToe
from src.game.players import RandomComputerPlayer
from src.logic.models import Mark

from console.renderers import ConsoleRenderer

player1 = RandomComputerPlayer(Mark("X"))
player2 = RandomComputerPlayer(Mark("O"))

TicTacToe(player1, player2, ConsoleRenderer()).play()