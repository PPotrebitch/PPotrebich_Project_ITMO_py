import tkinter as tk
import pygame
from Keygen import key_gen

def close():
    window.destroy()

def play_music():
    pygame.mixer.music.load('melody_game.mp3')
    pygame.mixer.music.play(loops=0)

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    window.after(100, update, ind)

def gen():
    lbl_gen.configure(text=key_gen())

pygame.mixer.init()

window = tk.Tk()
window.geometry("1920x982")
bg_img = tk.PhotoImage(file='GAME_art.png')

frameCnt = 15
frames = [tk.PhotoImage(file='AU.gif', format='gif -index %i' %(i)) for i in range(frameCnt)]

play_music()

gif_label = tk.Label(window, image="")
gif_label.pack()

lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.35, anchor='center')

lbl_toc = tk.Label(frame, text='Keygen for game "Among us"', font=('Arial', 30), bg='black', fg='white')
lbl_toc.grid(column=0, row=2, padx=5, pady=5)

lbl_gen = tk.Button(frame, text='Generate key', font=('Arial',20), command=gen, fg='green')
lbl_gen.grid(column=0, row=6, padx=10, pady=15)

btn_exit = tk.Button(frame, text='Cancel', font=('Arial', 20), command=close, fg='red')
btn_exit.grid(column=0, row=9, padx=10, pady=15)
label = tk.Label(window)

label.pack(anchor='nw')
window.after(0, update,0)

window.mainloop()
