from tkinter import Tk, Frame, Button, Toplevel, Canvas, PhotoImage, \
    CENTER, BOTH, NORMAL, DISABLED
from time import sleep
from random import choice

p, dt, color = ' ', 40, '#6495ED'
sim, lst, elem_keys = ['X', 'O'], [], [0]


def check() -> None:
    for key, val in coord.items():
        if lst[key[0]]['text'] == lst[key[1]]['text'] == lst[key[2]]['text'] != p:
            [y.config(state=DISABLED) for y in lst]
            tl.attributes('-topmost', 1)
            cnv.create_line(val, width=4, fill='red')
    sim.reverse()
    tk.update_idletasks()
    sleep(.5)


def computer(ind) -> None:
    lst_bool = [x['state'] == NORMAL for x in lst]

    for keys in coord_keys:
        [keys.remove(el) for el in keys if el == ind]
        if len(keys) == 1 and lst_bool[keys[0]] is True:
            elem_keys[0] = keys[0]
            coord_keys.remove(keys)

    ls1 = [t for t in coord.keys() if ind in t]
    ls2 = set(sum((ls1), ()))
    ls2.remove(ind)
    ls3 = set(g for g, w in enumerate([r['state'] == NORMAL for r in lst]) if w is True)
    ls4 = list(ls2 & ls3)
    if len(ls4) == 0:
        ls4 = list(ls3)
    if len(ls4) != 0:
        if lst_bool[elem_keys[0]] is True:
            element = elem_keys[0]
        else:
            element = choice(ls4)
        lst[element].config(text=sim[0], state=DISABLED)
        check()


def player(a) -> None:
    a.config(text=sim[0], state=DISABLED)
    check()
    computer(lst.index(a))


def back(e) -> None:
    tk.destroy() if e.keysym == 'Escape' else ...
    if e.keysym == 'Return':
        [z.config(text=p, state=NORMAL) for z in lst]
        sim[0], sim[1] = 'X', 'O'
        tk.attributes('-topmost', 1)
        cnv.delete('all')
        coord_keys[:] = [*map(list, list(coord.keys()))]


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

cnv = Canvas(tl, bg=color)
cnv.pack(expand=1, fill=BOTH)

tk.bind('<Key>', back)
tk.eval('tk::PlaceWindow . center')

w, h = tk.winfo_width(), tk.winfo_height()
tl.geometry(tk.geometry())

coord = {
    (0, 1, 2): (dt, h / 6., w - dt, h / 6.), (3, 4, 5): (dt, h * .5, w - dt, h * .5),
    (6, 7, 8): (dt, h * .83, w - dt, h * .83), (0, 3, 6): (w / 6., dt, w / 6., h - dt),
    (1, 4, 7): (w * .5, dt, w * .5, h - dt), (2, 5, 8): (w * .83, dt, w * .83, h - dt),
    (0, 4, 8): (dt, dt, w - dt, h - dt), (2, 4, 6): (w - dt, dt, dt, h - dt)}
coord_keys = [*map(list, list(coord.keys()))]

tk.mainloop()
