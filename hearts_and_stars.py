"""Приветствие и правила игры."""
print("Добро пожаловать в игру сердечки-звёздочки!")
print("Игрок 1 - ♡ Игрок 2 - ☆")
print("Игровое поле пронумеровано следующим образом:")
print(" 1 | 2 | 3 ")
print("-----------")
print(" 4 | 5 | 6 ")
print("-----------")
print(" 7 | 8 | 9 ")
start = input("начать игру?(да/нет)")
if start == "нет":
    print("до свидания!")
else:
    def print_board(board):
        """Функция для отображения игрового поля."""
        for row in board:
            print(" | ".join(row))
            print("-" * 9)

    def check_winner(board):
        """Функция для проверки завершенности игры."""
        # строки
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != " ":
                return row[0]
        # столбцы
        for col in range(3):
            if (board[0][col] == board[1][col] == board[2][col] and
                    board[0][col] != " "):
                return board[0][col]
        # диагонали
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
            return board[0][2]
        # Проверка на ничью
        if all(cell != " " for row in board for cell in row):
            return "ничья"
        return None

    def is_valid_input(board, position):
        """Функция для проверки корректности ввода."""
        if position.isdigit():
            pos = int(position) - 1
            row, col = divmod(pos, 3)
            return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "
        return False

    def hearts_and_stars():
        """Основная функция игры."""
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "♡"
        while True:
            print_board(board)
            position = input(f"Игрок {current_player},"
                             f" введите номер клетки (1-9): ")

            if not is_valid_input(board, position):
                print("Эта клетка уже занята. Попробуйте ещё раз!")
                continue

            pos = int(position) - 1
            row, col = divmod(pos, 3)
            board[row][col] = current_player

            winner = check_winner(board)
            if winner:
                print_board(board)
                if winner == "ничья":
                    print("Ничья!")
                else:
                    print(f"Игра завершилась! Победил игрок {winner}!")
                break

            current_player = "☆" if current_player == "♡" else "♡"
    if __name__ == "__main__":
        hearts_and_stars()
