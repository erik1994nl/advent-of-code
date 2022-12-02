from abc import ABC, abstractmethod
from pathlib import Path
from typing import Tuple
from typing_extensions import Literal

rps_file_path = f"{Path(__file__).parent.parent}\\data\\02_rockpaperscissor.txt"


class Strategy(ABC):
    move_score = {
        'X': 1,  # Rock
        'Y': 2,  # Paper
        'Z': 3,  # Scissor
    }

    @abstractmethod
    def get_score(self, they: str, you: str):
        raise NotImplementedError("Not implemented!")


class Strategy1(Strategy):
    # In this strategy 'your' move means rock/paper/scissor
    @staticmethod
    def get_outcome(moves: Tuple[str, str]) -> int:
        win = [('A', 'Y'), ('B', 'Z'), ('C', 'X')]
        draw = [('A', 'X'), ('B', 'Y'), ('C', 'Z')]

        if moves in win:
            return 6
        elif moves in draw:
            return 3
        else:
            return 0

    def get_score(self, they: str, you: str) -> int:
        return Strategy1.get_outcome((they, you)) + Strategy.move_score.get(you, 0)


class Strategy2(Strategy):
    # In this strategy 'your' move means win/draw/lose
    def __init__(self):
        self.outcome = {
            'X': 0,  # Lose
            'Y': 3,  # Draw
            'Z': 6,  # Win
        }

    @staticmethod
    def get_move(info: Tuple[str, str]) -> str:
        rock = [('A', 'Y'), ('B', 'X'), ('C', 'Z')]
        paper = [('A', 'Z'), ('B', 'Y'), ('C', 'X')]
        if info in rock:
            return 'X'
        elif info in paper:
            return 'Y'
        else:
            return 'Z'

    def get_score(self, they: str, you: str):
        return self.outcome.get(you) + Strategy.move_score.get(Strategy2.get_move((they, you)), 0)


def strategy_factory(strat):
    if strat == 1:
        return Strategy1()
    elif strat == 2:
        return Strategy2()
    else:
        raise ValueError('Unknown strategy')


with open(rps_file_path, 'r') as f:
    rps_rounds = f.read().splitlines()

    strategy_number: Literal[1, 2] = 2

    chosen_strategy = strategy_factory(strategy_number)
    total_score = 0
    for opponent_move, _, your_move in rps_rounds:
        round_score = chosen_strategy.get_score(opponent_move, your_move)
        total_score += round_score

    print(f"Total score for strategy {strategy_number} is: {total_score}")
