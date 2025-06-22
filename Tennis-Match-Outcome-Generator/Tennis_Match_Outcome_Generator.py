import random

def serve_hold_prob(rank):
    return max(0.5, 0.85 - (rank - 1) * 0.003)

def random_game_score(server_won, went_deuce):
    if went_deuce:
        return "40 - 40"
    else:
        return random.choice(["40 - Love", "40 - 15", "40 - 30"])

def simulate_game(rank_server, rank_receiver):
    base_prob = serve_hold_prob(rank_server)
    serve_prob = max(0.45, min(0.95, base_prob + random.uniform(-0.05, 0.05)))
    return random.random() < serve_prob

def play_tiebreak(rank1, rank2, player1, player2, starting_server):
    p1_points, p2_points = 0, 0
    server = starting_server
    point_number = 0


    while True:
        base_prob = serve_hold_prob(rank1) if server == 1 else serve_hold_prob(rank2)

        # Tiebreak serve probability is closer to 60%, with a small random variation
        # and reduced advantage to avoid blowouts
        serve_prob = base_prob - 0.08 + random.uniform(-0.04, 0.04)
        serve_prob = max(0.5, min(0.65, serve_prob))

        point_winner = 1 if random.random() < serve_prob else 2
        if point_winner == 1:
            p1_points += 1
        else:
            p2_points += 1

        point_number += 1

        # Switch server after first point, then every two points
        if point_number == 1 or (point_number > 1 and point_number % 2 == 1):
            server = 2 if server == 1 else 1

        # first to 7 with 2-point margin, but can go longer
        if (p1_points >= 7 or p2_points >= 7) and abs(p1_points - p2_points) >= 2:
            break

    return p1_points, p2_points

def play_set(rank1, rank2, starting_game_number, player1, player2):
    p1_games, p2_games = 0, 0
    game_number = starting_game_number

    while True:
        if p1_games == 6 and p2_games == 6:
            tiebreak_server = 1 if game_number % 2 == 0 else 2
            p1_tb_points, p2_tb_points = play_tiebreak(rank1, rank2, player1, player2, tiebreak_server)

            if p1_tb_points > p2_tb_points:
                p1_games += 1
            else:
                p2_games += 1

            print(f"Set Final Score: {player1} {p1_games}({p1_tb_points}) - {p2_games}({p2_tb_points}) {player2}")
            game_number += 1
            break

        server = 1 if game_number % 2 == 0 else 2
        server_name = player1 if server == 1 else player2
        rank_server = rank1 if server == 1 else rank2
        rank_receiver = rank2 if server == 1 else rank1

        adjusted_rank_server = rank_server + random.uniform(-2, 2)
        adjusted_rank_server = max(1, min(1000, adjusted_rank_server))

        server_won_game = simulate_game(adjusted_rank_server, rank_receiver)

        went_deuce = random.random() < 0.25
        game_score_str = random_game_score(server_won_game, went_deuce)

        if server_won_game:
            if server == 1:
                p1_games += 1
            else:
                p2_games += 1
        else:
            if server == 1:
                p2_games += 1
            else:
                p1_games += 1

        print(f"{player1} {p1_games} - {p2_games} {player2} ({game_score_str}, Server: {server_name})\n")

        game_number += 1

        if (p1_games >= 6 or p2_games >= 6) and abs(p1_games - p2_games) >= 2:
            break

    return p1_games, p2_games, game_number

def simulate_match(player1, rank1, player2, rank2):
    print(f"\n🎾 {player1} (Rank {rank1}) vs {player2} (Rank {rank2})")

    first_server = random.choice([1, 2])
    total_games_played = 0 if first_server == 1 else 1
    print(f"\n🪙 Coin Toss: {player1 if first_server == 1 else player2} will serve first.")

    p1_sets, p2_sets = 0, 0
    set_results = []

    while p1_sets < 2 and p2_sets < 2:
        print(f"\n--- Set {len(set_results) + 1} ---")
        s1, s2, total_games_played = play_set(rank1, rank2, total_games_played, player1, player2)
        set_results.append((s1, s2))

        if s1 > s2:
            p1_sets += 1
        else:
            p2_sets += 1

    print("\n📋 Set Scores:")
    for i, (g1, g2) in enumerate(set_results, 1):
        print(f"Set {i}: {player1} {g1} - {g2} {player2}")

    winner = player1 if p1_sets > p2_sets else player2
    print(f"\n🏆 Winner: {winner}")

player1 = input("Enter Player 1 name: ")
rank1 = int(input(f"Enter {player1}'s world ranking: "))

player2 = input("Enter Player 2 name: ")
rank2 = int(input(f"Enter {player2}'s world ranking: "))

simulate_match(player1, rank1, player2, rank2)
