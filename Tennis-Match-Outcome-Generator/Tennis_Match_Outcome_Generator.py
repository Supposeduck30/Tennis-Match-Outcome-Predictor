import random
import math

def serve_hold_prob(rank):
    # Base hold probability for rank 1 is ~85%
    # Probability decreases as rank increases, but not below 50%
    return max(0.5, 0.85 - (rank - 1) * 0.003)

def simulate_game(server_prob):
    # Server wins game with this probability
    return random.random() < server_prob

def play_set(rank1, rank2):
    p1_games, p2_games = 0, 0
    server = 1  # Player 1 serves first

    while True:
        if server == 1:
            if simulate_game(serve_hold_prob(rank1)):
                p1_games += 1
            else:
                p2_games += 1
            server = 2
        else:
            if simulate_game(serve_hold_prob(rank2)):
                p2_games += 1
            else:
                p1_games += 1
            server = 1

        # Check if set is over
        if (p1_games >= 6 or p2_games >= 6) and abs(p1_games - p2_games) >= 2:
            break
        if p1_games == 6 and p2_games == 6:
            # Tiebreak simulated as random winner of one game on serve of rank1
            if simulate_game(serve_hold_prob(rank1)):
                p1_games += 1
            else:
                p2_games += 1
            break

    return p1_games, p2_games

def simulate_match(player1, rank1, player2, rank2):
    print(f"\n {player1} (Rank {rank1}) vs {player2} (Rank {rank2}) ")

    p1_sets, p2_sets = 0, 0
    set_results = []

    while p1_sets < 2 and p2_sets < 2:
        s1, s2 = play_set(rank1, rank2)
        set_results.append((s1, s2))
        if s1 > s2:
            p1_sets += 1
        else:
            p2_sets += 1

    print("\nSet Scores:")
    for i, (g1, g2) in enumerate(set_results, 1):
        print(f"Set {i}: {player1} {g1} - {g2} {player2}")

    winner = player1 if p1_sets > p2_sets else player2
    print(f"\n🏆 Winner: {winner}")

# --- Run the simulation ---
player1 = input("Enter Player 1 name: ")
rank1 = int(input(f"Enter {player1}'s world ranking: "))

player2 = input("Enter Player 2 name: ")
rank2 = int(input(f"Enter {player2}'s world ranking: "))

simulate_match(player1, rank1, player2, rank2)
