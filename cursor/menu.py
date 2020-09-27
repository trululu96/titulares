#### altura y ancho
import curses
import time


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_YELLOW)


    h,w = stdscr.getmaxyx()
    text = 'hello'
    y = h//2
    x = w//2 - len(text)//2

    while 1: 
        key = stdscr.getch()
        stdscr.clear()
        if key == curses.KEY_UP: 
            stdscr.addstr(0,0, "up")
        elif key == curses.KEY_DOWN: 
            stdscr.addstr(0,0, "down")
        elif key == curses.KEY_ENTER or key in [10,13]:
            stdscr.addstr(0,0,"enter") 

    #stdscr.attron(curses.color_pair(1))
    #stdscr.addstr(y, x, text)
    #stdscr.attroff(curses.color_pair(1))
    #stdscr.refresh()
    #time.sleep(3)

curses.wrapper(main)
