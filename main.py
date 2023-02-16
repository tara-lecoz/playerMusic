import os
from tkinter import *
import pygame
from pygame import mixer
from PIL import ImageTk, Image
from tkinter import filedialog

win = Tk()
win.geometry("700x500")
frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

playlist = ["son1.wav", "son2.wav", "son3.wav"]

song_frame = Frame(frame)
song_frame.pack()
label_songframe = Label(song_frame, text="Song Track")
label_songframe.pack(anchor='center')
listbox = Listbox(song_frame, height=4, width=35)
for song in playlist:
    listbox.insert(END,song)
listbox.pack()

img = ImageTk.PhotoImage(Image.open("img/img1.jpg"))
label = Label(frame, image = img)
label.pack()

def sound(event):
    pygame.mixer.music.set_volume(scale_sound.get())

scale_sound = Scale(frame, orient='horizontal', from_=0, to=7, resolution=0.1,command=sound)
scale_sound.set(0.7)
scale_sound.pack()

command_frame = Frame(frame, bg="white")
command_frame.pack(pady=3, anchor='center')

pygame.init()

index_song = 0

def play():
    global index_song
    current_song = listbox.get(listbox.curselection()[0])
    current_song = listbox.get(ACTIVE)
    pygame.mixer.music.load(current_song)
    pygame.mixer.music.play()
    index_song += 1
    if index_song >= len(playlist):
        index_song = 0 

def loop():
    pygame.mixer.music.play(-1,0,0) 

def pause():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
        
def previous_song():
    global index_song
    index_song -= 1
    if index_song < 0:
        index_song = len(playlist) - 1
    pygame.mixer.music.load(playlist[index_song])
    pygame.mixer.music.play()

def next_song():
    global index_song
    index_song += 1
    if index_song >= len(playlist) - 1:
        index_song = len(playlist) + 1
    if index_song >= len(playlist):
        index_song = 0
    pygame.mixer.music.load(playlist[index_song])
    pygame.mixer.music.play()
    
def stop():
    mixer.music.stop()
    listbox.selection_clear(ACTIVE)

def add_song():
    songs = filedialog.askopenfilename(initialdir=".", title="Sélectionner un fichier .wav", filetypes=(("fichiers wav", "*.wav"), ("tous les fichiers", "*.*")))
    listbox.insert(END,songs)

def remove_song():
    del_song=listbox.curselection()
    listbox.delete(del_song[0])

prev_image = PhotoImage(file="./img/prev.png")
prev_button = Button(frame, text="prev", image=prev_image, bg="white", command=previous_song)
prev_button.pack(in_=command_frame, side=LEFT)
play_image = PhotoImage(file="./img/play.png")
play_button = Button(frame, text="play", image=play_image, bg="white", command=play)
play_button.pack(in_=command_frame, side=LEFT)
pause_image = PhotoImage(file="./img/pause.png")
pause_button = Button(frame, text="pause", image=pause_image, bg="white", command=pause)
pause_button.pack(in_=command_frame, side=LEFT)
next_image = PhotoImage(file="./img/next.png")
next_button = Button(frame, text="next", image=next_image, bg="white", command=next_song)
next_button.pack(in_=command_frame, side=LEFT)
loop_image = PhotoImage(file="./img/loop.png")
loop_button = Button(frame, text="loop", image=loop_image, bg="white", command=loop)
loop_button.pack(in_=command_frame, side=LEFT)
stop_image = PhotoImage(file="./img/stop.png")
stop_button = Button(frame, text="stop", image=stop_image, bg="white", command=stop)
stop_button.pack(in_=command_frame, side=LEFT)
add_image = PhotoImage(file="./img/add.png")
add_button = Button(frame, text="add", image=add_image, bg="white", command=add_song)
add_button.pack(in_=command_frame, side=LEFT)
remove_image = PhotoImage(file="./img/remove.png")
remove_button = Button(frame, text="remove", image=remove_image, bg="white", command=remove_song)
remove_button.pack(in_=command_frame, side=LEFT)

win.mainloop()