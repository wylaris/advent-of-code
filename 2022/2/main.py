def get_rounds(filename):
    rounds = []
    with open(filename) as file:
        for line in file:
            parts = line.strip().split(" ")
            rounds.append((parts[0], parts[1]))
    return rounds

def day_one(moves, rounds):
    score = 0
    for round in rounds:
        opponent = round[0]
        mine = round[1]
        # print(opponent, mine)
        # Tie
        if (opponent == "A" and mine == "X") or (opponent == "B" and mine == "Y") or (opponent == "C" and mine == "Z"):
            score += 3 + moves[mine]
        # Win
        elif (opponent == "A" and mine == "Y") or (opponent == "B" and mine == "Z") or (opponent == "C" and mine == "X"):
            score += 6 + moves[mine]
        # Lose
        elif (opponent == "A" and mine == "Z") or (opponent == "B" and mine == "X") or (opponent == "C" and mine == "Y"):
            score += moves[mine]
    print(score)

def day_two(moves, rounds):
    score = 0
    wins = {"A": 2, "B": 3, "C": 1}
    loss = {"A": 3, "B": 1, "C": 2}
    tie = {"A": 1, "B": 2, "C": 3}
    for round in rounds:
        opponent = round[0]
        win_lose = round[1]
        # Lose
        if win_lose == "X":
            score += loss[opponent]
        # Tie
        elif win_lose == "Y":
            score += 3 + tie[opponent]
        # Win
        elif win_lose == "Z":
            score += 6 + wins[opponent] 
    print(score)

def main():
    moves = {"X": 1, "Y": 2, "Z": 3}
    rounds = get_rounds("in.txt")
    day_one(moves, rounds)
    day_two(moves, rounds)

if __name__ == "__main__":
    main()