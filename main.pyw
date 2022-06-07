from tkinter import Tk, Frame, Button, NORMAL, DISABLED

p = ' \u2007 '
sim, lst = [' x ', ' o '], []
coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
         (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def f(a):
    a.config(text=sim[0], state=DISABLED)
    sim.reverse()
    for crd in coord:
        if lst[crd[0]]['text'] == lst[crd[1]]['text'] == lst[crd[2]]['text'] != p:
            [lst[x].config(bg='red') for x in crd]
            [y.config(state=DISABLED) for y in lst]


def sym(e):
    tk.destroy() if e.keysym == 'Escape' else None
    if e.keysym == 'Return':
        [z.config(text=p, state=NORMAL, bg='white') for z in lst]
        sim[0], sim[1] = ' x ', ' o '


tk = Tk()
tk.overrideredirect(True)

fr = Frame(tk, bg='#6495ED', bd=4)
fr.pack()
for i in range(9):
    lst.append(Button(fr, text=p, font='arial 48', bg='white'))
    lst[i].grid(row=i // 3 + 1, column=i % 3, padx=1, pady=1, sticky='nsew')
    lst[i]['command'] = lambda j=i: f(lst[j])

tk.bind('<Key>', sym)
tk.eval('tk::PlaceWindow . center')
tk.mainloop()
