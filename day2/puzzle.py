# Common.
from enum import IntEnum

def input(file):
    return [line.split() for line in open("day2/" + file + ".txt", "r")]
    
class Move(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def translate_player_1(move):
    match move:
        case "A": return Move.ROCK
        case "B": return Move.PAPER
        case "C": return Move.SCISSORS

def game_score(move_player_1, move_player_2):
    if move_player_2 == move_player_1:
        return 3
    match move_player_2:
        case Move.ROCK: return 6 if move_player_1 == Move.SCISSORS else 0
        case Move.PAPER: return 6 if move_player_1 == Move.ROCK else 0
        case Move.SCISSORS: return 6 if move_player_1 == Move.PAPER else 0

def game_scores(file, translator_player_2):
    game_moves = [[translate_player_1(moves[0]), translator_player_2(moves[0], moves[1])] for moves in input(file)]
    return [moves[1] + game_score(moves[0], moves[1]) for moves in game_moves]

# Part 1
def translate_player_2(move1, move2):
    match move2:
        case "X": return Move.ROCK
        case "Y": return Move.PAPER
        case "Z": return Move.SCISSORS

print("example  1: ", sum(game_scores("example", translate_player_2)))
print("part 1: ", sum(game_scores("input", translate_player_2)))

# Part 2
def strategy_player_2(move1, move2):
    move1 = translate_player_1(move1)
    if move2 == "Y":
        return move1
    match move1:
        case Move.ROCK: return Move.SCISSORS if move2 == "X" else Move.PAPER
        case Move.PAPER: return Move.ROCK if move2 == "X" else Move.SCISSORS
        case Move.SCISSORS: return Move.PAPER if move2 == "X" else Move.ROCK

print("example  2: ", sum(game_scores("example", strategy_player_2)))
print("part 2: ", sum(game_scores("input", strategy_player_2)))