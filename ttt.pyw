from tkinter import Tk, Frame, Button, Toplevel, Canvas, PhotoImage, \
    CENTER, BOTH, NORMAL, DISABLED
from time import sleep
from random import choice

p, dt, color = ' ', 40, '#6495ED'
sim, lst = ['X', 'O'], []


def check() -> None:
    for key, val in coord.items():
        if lst[key[0]]['text'] == lst[key[1]]['text'] == lst[key[2]]['text'] != p:
            [y.config(state=DISABLED) for y in lst]
            tl.attributes('-topmost', 1)
            cnv.create_line(val, width=4, fill='red')
    sim.reverse()
    tk.update_idletasks()
    sleep(.5)


def change(move_xo, queue) -> int or None:
    for keys in coord_keys:
        for el in keys:
            if el == move_xo and queue == 1:
                keys[keys.index(el)] = 'X'
            if el == move_xo and queue == 2:
                keys[keys.index(el)] = 'O'
    for keys in coord_keys:
        if keys.count('X') == 2 or keys.count('O') == 2:
            for xo in keys:
                if type(xo) == int:
                    coord_keys.remove(keys)
                    return xo
    return None


def computer(x_move) -> None:
    lst_bool = [x['state'] == NORMAL for x in lst]
    lst_ind = [g for g, t in enumerate(lst_bool) if t is True]
    if len(lst_ind) != 0:
        if o_move[0] is not None and o_move[0] != len(lst) and lst_bool[o_move[0]] is True:
            move = o_move[0]
        elif x_move is not None and lst_bool[x_move] is True:
            move = x_move
        else:
            move = choice(lst_ind)
        lst[move].config(text=sim[0], state=DISABLED)
        o_move[0] = change(move, 2)
        check()


def player(a) -> None:
    a.config(text=sim[0], state=DISABLED)
    move_x = change(lst.index(a), 1)
    check()
    computer(move_x)


def back(e) -> None:
    tk.destroy() if e.keysym == 'Escape' else ...
    if e.keysym == 'Return':
        [z.config(text=p, state=NORMAL) for z in lst]
        sim[0], sim[1] = 'X', 'O'
        tk.attributes('-topmost', 1)
        cnv.delete('all')
        coord_keys[:] = [*map(list, list(coord.keys()))]
        o_move[0] = len(lst)


tk = Tk()
tl = Toplevel()
tk.attributes('-topmost', 1)
tl.attributes('-transparentcolor', color)
tk.overrideredirect(True)
tl.overrideredirect(True)

fr = Frame(tk, bg=color, bd=4)
fr.pack()

pixelVirtual = PhotoImage(width=1, height=1)

for i in range(9):
    lst.append(Button(
        fr, text=p, image=pixelVirtual, font='arial 72',
        width=200, height=200, compound=CENTER, disabledforeground='black'))
    lst[i].grid(row=i // 3 + 1, column=i % 3, padx=1, pady=1)
    lst[i]['command'] = lambda j=i: player(lst[j])
o_move = [len(lst)]

cnv = Canvas(tl, bg=color)
cnv.pack(expand=1, fill=BOTH)

tk.bind('<Key>', back)
tk.eval('tk::PlaceWindow . center')

w, h = tk.winfo_width(), tk.winfo_height()
tl.geometry(tk.geometry())

coord = {
    (0, 1, 2): (dt, h * .17, w - dt, h * .17), (3, 4, 5): (dt, h * .5, w - dt, h * .5),
    (6, 7, 8): (dt, h * .83, w - dt, h * .83), (0, 3, 6): (w * .17, dt, w * .17, h - dt),
    (1, 4, 7): (w * .5, dt, w * .5, h - dt), (2, 5, 8): (w * .83, dt, w * .83, h - dt),
    (0, 4, 8): (dt, dt, w - dt, h - dt), (2, 4, 6): (w - dt, dt, dt, h - dt)}

# coord_keys = [list(i) for i in list(coord.keys())]
coord_keys = [*map(list, list(coord.keys()))]

tk.mainloop()
