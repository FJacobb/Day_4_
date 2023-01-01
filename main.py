from tkinter import *
import random
from playsound import playsound
def user_statement():
    global hand
    if user_answer.get().lower() == "0" or user_answer.get().lower() == "r":
        hand =canves.create_image(60,450, image=urock)
    elif user_answer.get().lower() == "1" or user_answer.get().lower() == "p":
        hand =canves.create_image(60, 450, image=upaper)
    elif user_answer.get().lower() == "2" or user_answer.get().lower() == "s":
        hand =canves.create_image(60, 450, image=uscissors)
    return

def comp_statement():
    global chand
    if computer_choose == 0:
        chand = canves.create_image(280,450, image=crock)
    elif computer_choose == 1:
        chand = canves.create_image(280, 450, image=cpaper)
    elif computer_choose == 2 :
        chand = canves.create_image(280, 450, image=cscissors)
    return
def result():
    global tx, ur, cp, score
    if str(computer_choose) == user_answer.get().lower():
        tx =canves.create_text(180,100, text="YOU HAD A DRAW GAME",font=("Franklin Gothic Demi Cond", 10, "bold"), fill="#ffffff" )
    elif computer_choose == 0 and (user_answer.get().lower() == "1" or user_answer.get().lower() == "p"):
        tx =canves.create_text(180, 100, text="YOU HAD A WIN GAME", font=("Franklin Gothic Demi Cond", 10, "bold"),
            fill="#ffffff")
        ur +=1
    elif computer_choose == 1 and (user_answer.get().lower() == "2" or user_answer.get().lower() == "2"):
        tx =canves.create_text(180, 100, text="YOU HAD A WIN GAME", font=("Franklin Gothic Demi Cond", 10, "bold"),
            fill="#ffffff")
        ur += 1
    elif computer_choose == 2 and (user_answer.get().lower() == "0" or user_answer.get().lower() == "r"):
        tx =canves.create_text(180, 100, text="YOU HAD A WIN GAME", font=("Franklin Gothic Demi Cond", 10, "bold"),
            fill="#ffffff")
        ur += 1
    else:
        tx =canves.create_text(180, 100, text="YOU HAVE LOST A GAME", font=("Franklin Gothic Demi Cond", 10, "bold"),
            fill="#ffffff")
        cp += 1
    canves.delete(score)
    score = canves.create_text(230, 20, text=f"User - {ur}:{cp} - Computer", font=("arel", 15, "bold"), fill="#ffffff")
    return
def command():
    global count, computer_choose

    computer_choose = random.randrange(0, 3)
    if user_answer.get().lower() == "end":
        home.destroy()
    else:
        if count == 0:
            user_statement()
            comp_statement()
            result()
        else:
            canves.delete(hand, chand, tx, score)
            user_statement()
            comp_statement()
            result()
        playsound("music/mixkit-arcade-retro-jump-223.wav")
        count+=1
    return count
home = Tk()
home.title("Rock-Paper-Scissors")
home.geometry("250x450")
img = PhotoImage(file="image/Rock+Paper+Scissors+Logo.png")
home.geometry("346x600")
bg= PhotoImage(file="image/background.png")
crock= PhotoImage(file="image/comp_rock.png")
cscissors= PhotoImage(file="image/comp_sic.png")
cpaper= PhotoImage(file="image/COMP_PAPPER.png")
urock= PhotoImage(file="image/USER_ROCK.png")
uscissors= PhotoImage(file="image/USER_SIC.png")
upaper= PhotoImage(file="image/USER_PAPER.png")
read_box = PhotoImage(file="image/Layer 2.png")
score_box = PhotoImage(file="image/Layer 3.png")
canves = Canvas(width=346,height=600)
canves.create_image(173,300, image=bg)
canves.create_image(205,20, image=score_box)
ur = 0
cp = 0
score = canves.create_text(230,20, text=f"User - {ur}:{cp} - Computer", font=("arel", 15, "bold"), fill="#ffffff")
canves.create_text(170,140, text=f"GAME ON", font=("arel", 50, "bold"), fill="#ffffff")
canves.place(x=-2,y=-1)
canves.create_image(145,275, image=read_box)
canves.create_text(145,275, justify=CENTER, text="What do you choose? type 0 or R for Rock,\n1 or P for Paper, or 2 or S for scissors.\nTo end the game type 'end'", font=("arel", 10, "bold"), fill="#ffffff" )
user_answer = Entry(home, width=25, fg="#ffffff", bg="green")
user_answer.place(y=570, x=85)

count = 0
Button(home, text="Play", fg="#ffffff", bg="green", command=command).place(y=565, x=265)
home.mainloop()
