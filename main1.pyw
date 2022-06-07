from tkinter import Tk, Frame, Button, NORMAL, DISABLED

sim = [' x ', ' o ']
lst, ls = [], []


def check(lt):
    coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
             (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for crd in coord:
        if lt[crd[0]] == lt[crd[1]] == lt[crd[2]]:
            [lst[g].config(bg='red') for g in crd]
            [d.config(state=DISABLED) for d in lst]


def f(a):
    ls.clear()
    a.config(text=sim[0], state=DISABLED)
    sim.reverse()
    for n, m in enumerate(lst):
        ls.append(n) if m['text'] == ' \u2007 ' else ls.append(m['text'])
    check(ls)


def sym(e):
    tk.destroy() if e.keysym == 'Escape' else None
    if e.keysym == 'Return':
        [k.config(text=' \u2007 ', state=NORMAL, bg='white') for k in lst]
        sim[0], sim[1] = ' x ', ' o '


tk = Tk()
tk.overrideredirect(True)

fr = Frame(tk, bg='#6495ED', bd=4)
fr.pack()
for i in range(9):
    lst.append(Button(fr, text=' \u2007 ', font='arial 50', bg='white'))
    lst[i].grid(row=i // 3 + 1, column=i % 3, padx=1, pady=1, sticky='nsew')
    lst[i]['command'] = lambda i=i: f(lst[i])

tk.bind('<Key>', sym)
tk.eval('tk::PlaceWindow . center')
tk.mainloop()
