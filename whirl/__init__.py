import os
import vlc
import webbrowser
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def BrowseFile():
    global music
    global Music_Name
    opened = []
    opened.append(music.audio_get_track())
    file = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("mp3 files","*.mp3")])
    base, ext = os.path.basename(file).split(".")
    music_name.set(base)
    music.play()
    music.set_media(file)
    print(base, " + ", ext)

def pauseplay():
    if music.play() == True:
        music.pause()
    elif music.pause() == True:
        music.play()
def musicstop():
    music.stop()
    
def musicrestart():
    music.stop()
    music.play()  

        
music = vlc.MediaPlayer()

whirl = Tk()
whirl.title("Whirl")
whirl.geometry('300x200')
whirl.config(bg = "#0084FF")

Menubar = Menu(whirl, activebackground ="#0084FF", activeforeground = "#FFFFFF",bg = "#FFFFFF", fg = "#0084FF" ,font = "Segoe")

Filemenu = Menu(Menubar, tearoff = 0)
Filemenu.add_command(label="Open", command=BrowseFile)
Filemenu.add_separator()
Filemenu.add_command(label="Exit", command=whirl.destroy)
Menubar.add_cascade(label="File", menu=Filemenu)

Helpmenu = Menu(Menubar, tearoff = 0)
Helpmenu.add_command(label = "Website", command=lambda:webbrowser.open("http://www.github.com/Whirlpool-Programmer/Whirl"))
Helpmenu.add_separator()
Helpmenu.add_command(label = "Changelog", command=None)
Helpmenu.add_command(label = "About",command = None)
Menubar.add_cascade(label = "Help", menu=Helpmenu)

pause_btn = PhotoImage(file = "icons/pause.png", master = whirl) .subsample(12,12)
play0_btn = PhotoImage(file = "icons/play.png", master = whirl) .subsample(12,12)
stop0_btn = PhotoImage(file = "icons/stop.png", master = whirl) .subsample(12,12)
add00_btn = PhotoImage(file = "icons/add.png", master = whirl) .subsample(12,12)

music_name = StringVar()
music_name.set("Whirl 0.5")

Music_Name = Label(whirl, textvariable = music_name,borderwidth=1, relief="flat", bg = "#0084FF", fg = "white")
Browserfile = Button(whirl,  image = add00_btn,bg = "#0084FF", borderwidth = 0, command = lambda:BrowseFile())
Play = Button(whirl, image = pause_btn,bg = "#0084FF",borderwidth = 0,command = lambda:pauseplay())
stop = Button(whirl, image = stop0_btn,bg = "#0084FF", borderwidth = 0,command = lambda:musicstop())
restart = Button(whirl,image = play0_btn,bg = "#0084FF",borderwidth = 0, command = lambda:musicrestart())

Music_Name.place(x = 10,y = 130)#(row = 0,column=0)#columnspan=1,ipadx=100
Browserfile.place(x = 260,y = 130)#row = 0, column = 1
Play.place(x = 50, y = 150)
restart.place(x = 10, y = 150)
stop.place(x = 90, y = 150)

whirl.config(menu = Menubar)
whirl.mainloop()
music.stop()
