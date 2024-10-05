import random
from tkinter import *
from tkinter import messagebox
import pygame

# Initialize Pygame
pygame.init()  # Initialize all Pygame modules

# Set up Pygame display
pygame_display = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame + Tkinter Example")

def play_music():
    try:
        pygame.mixer.init()  # Initialize Pygame mixer
        music_file = "Fluffing_a_Duck.mp3"  # Ensure the file path is correct
        pygame.mixer.music.load(music_file)  # Load the music
        pygame.mixer.music.play()  # Play the music
    except pygame.error as e:
        print(f"Error initializing mixer: {e}")

# Pause music function
def pause_music():
    pygame.mixer.music.pause()

# Pygame main loop
playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

run = True
score = 0
# main loop
while run:
    global root
    root = Tk()
    root.geometry('900x500+400+150')
    root.title('HANG MAN')
    root.config(bg = '#FFFFB5')
    count = 0
    win_count = 0

    # Create Tkinter buttons
    PLAY = PhotoImage(file = "button (9).png")
    play_button =Button(root, image=PLAY, command=play_music,bg ='#FFFFB5',activebackground = "#FFFFB5")
    play_button.place(x = 350, y = 10)
    OFF = PhotoImage(file = "button (10).png")
    pause_button =Button(root, image = OFF, command=pause_music, bg = '#FFFFB5' , activebackground = "#FFFFB5")
    pause_button.place(x = 420, y = 10)
    

    index9 = random.randint(0,25)
    file = open('sports.txt','r')
    l = file.readlines()
    selected_word = l[index9].strip('\n')
    
    # creation of word dashes variables
    x = 2
    for i in range(0,len(selected_word)):
        x += 35
        exec('d{}=Label(root,text="_",bg="#FFFFB5",font=("arial",30))'.format(i))
        exec('d{}.place(x={},y={})'.format(i,x,150))
        
    #letters icon
    al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for let in al:
        exec('{}=PhotoImage(file="{}.png")'.format(let,let))
        
    # hangman images
    h123 = ['h1','h2','h3','h4','h5','h6','h7']
    for hangman in h123:
        exec('{}=PhotoImage(file="{}.png")'.format(hangman,hangman))
        
    #letters placement
    button = [['b1','a',0,350],['b2','b',50,350],['b3','c',100,350],['b4','d',149,350],['b5','e',202,350],['b6','f',250,350],['b7','g',298,350],['b8','h',350,350],['b9','i',402,350],['b10','j',0,400],['b11','k',45,400],['b12','l',95,400],['b13','m',142,400],['b14','n',198,400],['b15','o',250,400],['b16','p',302,400],['b17','q',352,400],['b18','r',405,400],['b19','s',0,450],['b20','t',48,450],['b21','u',97,450],['b22','v',150,450],['b23','w',200,450],['b24','x',260,450],['b25','y',310,450],['b26','z',360,450]]

    for q1 in button:
        exec('{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="#FFFFB5",activebackground="#FFFFB5",font=10,image={})'.format(q1[0],q1[1],q1[0],q1[1]))
        exec('{}.place(x={},y={})'.format(q1[0],q1[2],q1[3]))
        
    #hangman placement
    han = [['c1','h1'],['c2','h2'],['c3','h3'],['c4','h4'],['c5','h5'],['c6','h6'],['c7','h7']]
    for p1 in han:
        exec('{}=Label(root,bg="#FFFFB5",image={})'.format(p1[0],p1[1]))

    # placement of first hangman image
    c1.place(x =500,y =-50)
    #high score
    def load_high_score():
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0


    # exit buton and score
    def close():
        global run
        answer = messagebox.askyesno('ALERT','YOU WANT TO EXIT THE GAME?')
        if answer == True:
            run = False
            root.destroy()
            
    e1 = PhotoImage(file = 'exit.png')
    ex = Button(root,bd = 0,command = close,bg="#FFFFB5",activebackground = "#FFFFB5",font = 10,image = e1)
    ex.place(x=770,y=10)
    score_label = Label(root, text="", font=("Helvetica", 20) , bg = "#FFFFB5")
    score_label.pack(pady=5)
    score_label.config(text=f"Score: {score}")
    score_label.place(x = 10, y = 10)
    high_score = load_high_score()
    high_score_label = Label(root, text="High Score: {}".format(high_score), font=("Helvetica", 20) , bg = "#FFFFB5")
    high_score_label.pack(pady=5)
    high_score_label.place(x = 10,y = 50)
    def update_high_score():
        global high_score
        if score > high_score:
            high_score = score
            high_score_label.config(text="High Score: {}".format(high_score))
            with open("high_score.txt", "w") as file:
                file.write(str(high_score))

    update_high_score()

    # button press check function
    def check(letter,button):
        global count,win_count,run,score
        exec('{}.destroy()'.format(button))
        if letter in selected_word:
            for i in range(0,len(selected_word)):
                if selected_word[i] == letter:
                    win_count += 1
                    exec('d{}.config(text="{}")'.format(i,letter.upper()))
            if win_count == len(selected_word):
                score += 1
                update_high_score()
                answer = messagebox.askyesno('GAME OVER','YOU WON!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    root.destroy()   
                else:
                    run = False
                    root.destroy()
        else:
            count += 1
            exec('c{}.destroy()'.format(count))
            exec('c{}.place(x={},y={})'.format(count+1,470,-50))
            if count == 6:
                answer = messagebox.askyesno('GAME OVER','YOU LOST!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    root.destroy()
                else:
                    run = False
                    root.destroy()         
    root.mainloop()
    pygame.quit()
