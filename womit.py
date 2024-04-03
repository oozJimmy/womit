import curses
from random import random
from art import text2art

def vomiter(screen):
    WIN_BACKSPACE = 8
    input_word = ""
    words = {}

    key = screen.getch(0, len(input_word))
    while True:
        height, width = screen.getmaxyx()
        screen.clear()

        if chr(key) in [" ", "\n"]:
            random_y = int(random() * height)
            random_x = int(random() * width)
            words[input_word] = (random_y, random_x)
            input_word = ""
        elif key == curses.KEY_BACKSPACE or key == WIN_BACKSPACE:
            input_word = input_word[0:len(input_word) - 1]
        else:
            input_word = input_word + chr(key)
        
        for word, (y, x) in words.items():
            screen.addstr(y, x, word, curses.A_REVERSE)

        screen.addstr(0, 0, input_word)

        key = screen.getch(0, len(input_word))

def title_screen(screen):
    key = ""
    count = 0 

    while key != " ":
        height, width = screen.getmaxyx()
        screen.clear()
        screen.addstr(text2art("womiter").center(width))
        if count % 18 == 0 or count % 40 == 0:
            screen.addstr(height - 1, 0, "Press Spacebar to continue", curses.A_REVERSE)
        else:
            screen.addstr(height - 1, 0, " " * width, curses.A_REVERSE)
            
        key = screen.getkey()
    screen.clear()

def main():
    curses.wrapper(title_screen)
    curses.wrapper(vomiter)

if __name__ == "__main__":
    main()