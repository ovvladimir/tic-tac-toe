from tkinter import Tk, Frame, Button, NORMAL, DISABLED, E, W, S, N

p = ' \u2007 '
sim = [' x ', ' o ']
ls = ('b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9')
s = E + W + S + N
lst = []
coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
         (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def check(lt):
    for crd in coord:
        if lt[crd[0]] == lt[crd[1]] == lt[crd[2]]:
            for g, h in enumerate(ls):
                if g in {crd[0], crd[1], crd[2]}:
                    fr.nametowidget(h)['bg'] = 'red'
            return True
    return False


def f(a):
    lst.clear()
    a.config(text=sim[0], state=DISABLED)
    sim.reverse()
    for n, m in enumerate(ls):
        z = fr.nametowidget(m)
        lst.append(n) if z['text'] == p else lst.append(z['text'])
    if check(lst):
        for k in ls:
            fr.nametowidget(k)['state'] = DISABLED


def sym(e):
    tk.destroy() if e.keysym == 'Escape' else None
    if e.keysym == 'Return':
        for k in ls:
            u = fr.nametowidget(k)
            u.config(text=p, state=NORMAL, bg='white')
        sim[0], sim[1] = ' x ', ' o '


tk = Tk()
tk.overrideredirect(True)

fr = Frame(tk, bg='#6495ED', bd=4)
fr.pack()
[Button(
    fr, text=p, font='arial 50', bg='white', name=j, command=lambda r=j: f(fr.nametowidget(r))
).grid(row=i // 3 + 1, column=i % 3, padx=1, pady=1, sticky=s) for i, j in enumerate(ls)]
# tk.nametowidget(j) если нет Frame
"""
def f(e):
    e.widget.config(text=sim[0])
    sim.reverse()

[Button(fr, {'text': j, 'font': 'arial 50', 'bg': 'white', Grid: {
    'row': i // 3 + 1, 'column': i % 3, 'padx': 1, 'pady': 1}}).bind(
        '<Button-1>', f) for i, j in enumerate(ls)]
"""
tk.bind('<Key>', sym)
tk.eval('tk::PlaceWindow . center')
tk.mainloop()
