import tkinter as tk
from tkinter import messagebox


class Game:
    def __init__(self):
        self.grid = [' ' for i in range(9)]
        self.turn = 'X'

    def win(self):
        won = [(0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6)]
        for combinations in won:
            if self.grid[combinations[0]] == self.grid[combinations[1]] == self.grid[combinations[2]] != ' ':
                return self.grid[combinations[0]]
        if ' ' not in self.grid:
            return 'Tie'
        return False

    def input(self, move):
        if self.grid[move] == ' ':
            self.grid[move] = self.turn
            return True
        return False

    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'


class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe!")
        self.game = Game()
        self.buttons = []

        for i in range(9):
            button = tk.Button(self.root, text=" ", width=10, height=3, font=("Arial", 30), command=lambda i=i: self.click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        self.turn_label = tk.Label(self.root, text="Player X's turn", font=("Arial", 14))
        self.turn_label.grid(row=3, column=0, columnspan=3)

        self.restart_button = tk.Button(self.root, text="Restart", width=10, command=self.restart)
        self.restart_button.grid(row=4, column=0, columnspan=3)

    def click(self, index):
        if self.game.input(index):
            self.buttons[index].config(text=self.game.turn)
            result = self.game.win()
            if result:
                if result == 'Tie':
                    messagebox.showinfo("Game Over", "It's a tie!")
                    self.restart()
                else:
                    messagebox.showinfo("Game Over", f"The winner is {result}!")
                    self.restart()
            else:
                self.game.switch_turn()
                self.turn_label.config(text=f"Player {self.game.turn}'s turn")

    def restart(self):
        self.game = Game()
        for button in self.buttons:
            button.config(text=" ", state=tk.NORMAL)
        self.turn_label.config(text="Player X's turn")


def main():
    root = tk.Tk()
    game_gui = GameGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
