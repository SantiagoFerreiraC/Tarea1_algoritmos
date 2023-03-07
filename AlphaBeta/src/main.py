from alphabeta import TicTacToe
from alphabeta import alpha_beta_value


def play(state):
    """Makes turn and prints the result of it until the game is over
    :param state: The initial state of the game (TicTacToe)
    """
    def play(state):
        while not state.is_end_state():
         if state.is_max_node():
            print("It is crosses turn (X)")
         else:
            print("It is noughts turn (O)")

        value, row, col = alpha_beta_value(state)
        if state.is_max_node():
            state = TicTacToe(state.state[:row * 3 + col] + 'x' + state.state[row * 3 + col + 1:], False)
        else:
            state = TicTacToe(state.state[:row * 3 + col] + 'o' + state.state[row * 3 + col + 1:], True)

        print(state)

    score = state.value()
    if score == 0:
        print("Draw!")
    elif score == 1:
        print("Crosses (X) won!")
    else:
        print("Noughts (O) won!")


def main():
    """
    You need to implement the following functions/methods:
    play(state): makes turn and prints the result of it until the game is over
    value() in TicTacToe class: returns the current score of the game
    generate_children() in TicTacToe class: returns a list of all possible states after this turn
    alpha_beta_value(node): implements the MinMax algorithm with alpha-beta pruning
    max_value(node, alpha, beta): implements the MinMax algorithm with alpha-beta pruning
    min_value(node, alpha, beta):implements the MinMax algorithm with alpha-beta pruning
    """
    empty_board = 3 * '???'
    state = TicTacToe(empty_board, True)
    print(state)
    play(state)


if __name__ == '__main__':
    main()
