from tkinter import Tk, Frame, Button, NORMAL, DISABLED, Toplevel, BOTH, Canvas

p, dt, c = ' ', 40, 'red'
sim, lst = ['X', 'O'], []


def play(a):
    a.config(text=sim[0], state=DISABLED)
    sim.reverse()
    for key, val in coord.items():
        if lst[key[0]]['text'] == lst[key[1]]['text'] == lst[key[2]]['text'] != p:
            # [lst[x].config(disabledforeground=c) for x in key]
            [y.config(state=DISABLED) for y in lst]
            tl.attributes('-topmost', 1)
            cnv.create_line(val, width=4, fill=c)


def back(e):
    tk.destroy() if e.keysym == 'Escape' else ...
    if e.keysym == 'Return':
        [z.config(text=p, state=NORMAL) for z in lst]
        sim[0], sim[1] = 'X', 'O'
        tk.attributes('-topmost', 1)
        cnv.delete('all')


tk = Tk()
tl = Toplevel()
tk.attributes('-topmost', 1)
tl.attributes('-transparentcolor', '#6495ED')
tk.overrideredirect(True)
tl.overrideredirect(True)

fr = Frame(tk, bg='#6495ED', bd=4)
fr.pack()

for i in range(9):
    lst.append(Button(fr, text=p, font='arial 72', width=3, disabledforeground='black'))
    lst[i].grid(row=i // 3 + 1, column=i % 3, padx=1, pady=1, sticky='nsew')
    lst[i]['command'] = lambda j=i: play(lst[j])

cnv = Canvas(tl, bg='#6495ED')
cnv.pack(expand=1, fill=BOTH)

tk.bind('<Key>', back)
tk.eval('tk::PlaceWindow . center')

w, h = tk.winfo_width(), tk.winfo_height()
tl.geometry(f'{w}x{h}+{(tk.winfo_screenwidth()-w) // 2}'
            f'+{(tk.winfo_screenheight()-h) // 2}')

coord = {
    (0, 1, 2): (dt, h // 6, w - dt, h // 6), (3, 4, 5): (dt, h * .5, w - dt, h * .5),
    (6, 7, 8): (dt, h * .82, w - dt, h * .82), (0, 3, 6): (w // 6, dt, w // 6, h - dt),
    (1, 4, 7): (w * .5, dt, w * .5, h - dt), (2, 5, 8): (w * .83, dt, w * .83, h - dt),
    (0, 4, 8): (dt, dt, w - dt, h - dt), (2, 4, 6): (w - dt, dt, dt, h - dt)}

tk.mainloop()
