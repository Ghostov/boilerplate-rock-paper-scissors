# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 3:
        # Start with a random choice for the first few moves
        return random.choice(["R", "P", "S"])

    # Create a dictionary to count the occurrences of each move following every possible move
    last_three = "".join(opponent_history[-3:])
    if last_three not in transition_matrix:
        transition_matrix[last_three] = {"R": 0, "P": 0, "S": 0}
    if prev_play:
        transition_matrix[last_three][prev_play] += 1

    # Predict the opponent's next move based on the transition matrix
    possible_moves = transition_matrix[last_three]
    predicted_move = max(possible_moves, key=possible_moves.get)

    # Choose the move that beats the predicted move
    if predicted_move == "R":
        return "P"
    elif predicted_move == "P":
        return "S"
    else:
        return "R"

# A transition matrix to track the opponent's moves
transition_matrix = {}

if __name__ == "__main__":
    # Example of running the player function
    import random

    def simulate_game():
        moves = ["R", "P", "S"]
        opponent_moves = [random.choice(moves) for _ in range(100)]
        my_moves = []
        prev_play = ""

        for move in opponent_moves:
            my_move = player(prev_play)
            my_moves.append(my_move)
            prev_play = move

        return my_moves, opponent_moves

    my_moves, opponent_moves = simulate_game()
    print("My moves:", my_moves)
    print("Opponent's moves:", opponent_moves)

