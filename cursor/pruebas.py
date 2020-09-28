import curses
import time


## se puede hacer con wrapper ! 
#stdscr = curses.initscr()
#
##no hacer echo en la terminal 
#curses.noecho() 
#
## no esperar a que presionen enter
#curses.cbreak() 
#
##no quiero un blinking cursor
#curses.curs_set(0)
##special keys, special values
#stdscr.keypad(True)
#
#curses.echo()
#curses.nocbreak() 
#curses.curs_set(1)
#stdscr.keypad(False)
#curses.endwin()

def main(stdscr):
    curses.curs_set(0)
    stdscr.addstr(15,5, "Hello")
    stdscr.refresh()
    time.sleep(3)

curses.wrapper(main)



