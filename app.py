import main 
import curses
import webbrowser

noticias = [
    'El tiempo',
    'El espectador'
    ]

def limits(noticias, max_y): 
    leaps = max_y//len(noticias)
    completo = ''
    limites = []
    soft_limit = 0
    for i in noticias: 
        if len(i) > leaps: 
            completo += i[0:leaps] + ' ' 
        else: 
            completo += i + ' ' * (leaps - len(i))


        limites.append([soft_limit, soft_limit + leaps])
        soft_limit += leaps

    return (limites, completo)


news = [
    main.el_tiempo(),
    main.el_espectador()
]


def print_et(stdscr, current_row, news,inicio, fin, completo, limites, c_n):
    fin -= 1
    stdscr.clear()
    for c, i in enumerate(limites):
        if c == c_n:
            stdscr.addstr(0,i[0],completo[i[0]:i[1]+1], curses.A_STANDOUT)
        else: 
            stdscr.addstr(0,i[0],completo[i[0]:i[1]+1])

    for idx, row in enumerate(news.titulares[inicio:fin+1]):
        y = idx + 1 
        if idx == (current_row - inicio):
            #stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, 0, row['titular'], curses.A_STANDOUT)
            #stdscr.attroff(curses.color_pair(1))
        else: 
            stdscr.addstr(y,0, row['titular'])




def principal(stdscr):
    curses.curs_set(0)
    current_row = -1
    inicio = 0
    h, w = stdscr.getmaxyx()
    limites, completo = limits(noticias, w)
    fin = int(h)-2
    c_n = 0
    print_et(stdscr, current_row, news[c_n], inicio, fin, completo, limites, c_n)
    stdscr.refresh()

    while 1 : 
        key = stdscr.getch()

        stdscr.clear()

        if key == curses.KEY_UP and current_row > 0:
            if current_row == inicio:
                fin -= 1
                inicio -= 1 
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(news[c_n].titulares) - 1 : 
            if current_row == fin-1:
                fin += 1
                inicio += 1 
            current_row += 1 
        elif (key == curses.KEY_ENTER or key in [10,13]) and current_row >= 0:
            webbrowser.open(news[c_n].titulares[current_row]['href'])
        elif key == curses.KEY_LEFT and c_n > 0:
            c_n -= 1
        elif key == curses.KEY_RIGHT and c_n < len(noticias) -1 :
            c_n += 1

        print_et(stdscr, current_row, news[c_n], inicio, fin, completo, limites, c_n)

        stdscr.refresh()



curses.wrapper(principal)