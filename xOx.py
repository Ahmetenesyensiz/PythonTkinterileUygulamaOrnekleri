import tkinter
import customtkinter as ctk

app = ctk.CTk()
app.title("XOX Game")
app.geometry("630x700")
app.resizable(False,False)
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

bc1 = True
bc2 = True
bc3 = True
bc4 = True
bc5 = True
bc6 = True
bc7 = True
bc8 = True
bc9 = True
state = "_"
bclick = True
WinCheck = False
Check = False
game = ["_","_","_",
        "_","_","_",
        "_","_","_"]

def Denetle():
    global game , WinCheck, Check, state
    if game[0] == "X" and game[1] == "X" and game[2] == "X":
        WinCheck = True
        state = "X"
    elif game[0] == "O" and game[1] == "O" and game[2] == "O":
        WinCheck = True
        state = "O"
    elif game[3] == "X" and game[4] == "X" and game[5] == "X":
        WinCheck = True
        state = "X"
    elif game[3] == "O" and game[4] == "O" and game[5] == "O":
        WinCheck = True
        state = "O"
    elif game[6] == "X" and game[7] == "X" and game[8] == "X":
        WinCheck = True
        state = "X"
    elif game[6] == "O" and game[7] == "O" and game[8] == "O":
        WinCheck = True
        state = "O"
    elif game[0] == "X" and game[3] == "X" and game[6] == "X":
        WinCheck = True
        state = "X"
        WinCheck = True
    elif game[0] == "O" and game[3] == "O" and game[6] == "O":
        WinCheck = True
        state = "O"
    elif game[1] == "X" and game[4] == "X" and game[7] == "X":
        WinCheck = True
        state = "X"
    elif game[1] == "O" and game[4] == "O" and game[7] == "O":
        WinCheck = True
        state = "O"
    elif game[2] == "X" and game[6] == "X" and game[8] == "X":
        WinCheck = True
        state = "X"
    elif game[2] == "O" and game[5] == "O" and game[8] == "O":
        WinCheck = True
        state = "O"
    elif game[0] == "X" and game[4] == "X" and game[8] == "X":
        WinCheck = True
        state = "X"
    elif game[0] == "O" and game[4] == "O" and game[8] == "O":
        WinCheck = True
        state = "O"
    elif game[2] == "X" and game[4] == "X" and game[6] == "X":
        WinCheck = True
        state = "X"
    elif game[2] == "O" and game[4] == "O" and game[7] == "O":
        WinCheck = True
        state = "O"
    elif bc1 == False and bc2 == False and bc3 == False and bc4 == False and bc5 == False and bc6 == False and bc7 == False and bc8 == False and bc9 == False:
        Check = True
def start():
    label1.destroy()
    button1.destroy()
    global Button1,Button2,Button3,Button4,Button5,Button6,Button7,Button8,Button9
    Button1 = ctk.CTkButton(master=app, text="", width=200, height=200,command=b1)
    Button1.place(x=5,y=65)
    Button2 = ctk.CTkButton(master=app, text="", width=200, height=200,command=b2)
    Button2.place(x=215,y=65)
    Button3 = ctk.CTkButton(master=app, text="", width=200, height=200,command=b3)
    Button3.place(x=425,y=65)

    Button4 = ctk.CTkButton(master=app, text="", width=200, height=200,command=b4)
    Button4.place(x=5,y=275)
    Button5 = ctk.CTkButton(master=app, text="", width=200, height=200,command=b5)
    Button5.place(x=215,y=275)
    Button6 = ctk.CTkButton(master=app, text="", width=200, height=200,command=b6)
    Button6.place(x=425,y=275)

    Button7 = ctk.CTkButton(master=app, text="", width=200, height=200,command=b7)
    Button7.place(x=5,y=485)
    Button8 = ctk.CTkButton(master=app, text="", width=200, height=200,command=b8)
    Button8.place(x=215,y=485)
    Button9 = ctk.CTkButton(master=app, text="", width=200, height=200,command=b9)
    Button9.place(x=425,y=485)
def clicked():
#    print("Berabere: ",Check)
#    print("Durum: "+state)
#    print(WinCheck)
#    print(bc1,bc2,bc3,bc4,bc5,bc6,bc7,bc8,bc9)
#    print(game[0:3],"\n",game[3:6],"\n",game[6:9])
    if WinCheck == True and state == "X":
        L1 = ctk.CTkLabel(master=app,text="X Kazandı!",font=("Roboto",30),width=200,anchor=tkinter.CENTER)
        L1.place(x=215, y=5)
    elif WinCheck == True and state == "O":
        L2 = ctk.CTkLabel(master=app,text="O Kazandı!",font=("Roboto",30),width=200,anchor=tkinter.CENTER)
        L2.place(x=215,y=5)
    elif WinCheck == False and Check == True:
        L3 = ctk.CTkLabel(master=app,text="Berabere Kalındı",font=("Roboto",30),width=200,anchor=tkinter.CENTER)
        L3.place(x=215,y=5)
def b1():
    global bclick,bc1,game
    if bclick == True and bc1 == True:

        f1 = ctk.CTkFrame(master=app, width=200, height=200, fg_color="blue")
        f1.place(x=5, y=65)
        Button1.destroy()
        bclick = False
        bc1 = False
        lf1 = ctk.CTkLabel(master=app, text="X", font=("Roboto", 50), width=200, height=50, fg_color="blue",
                           bg_color="blue")
        lf1.place(x=5, y=135)
        game[0] = "X"


        Denetle()
        clicked()
    elif bc1 == True and bclick == False:

        f1 = ctk.CTkFrame(master=app, width=200, height=200, fg_color="blue")
        f1.place(x=5, y=65)
        Button1.destroy()
        bclick = True
        b1 = False
        lf1 = ctk.CTkLabel(master=app, text="O", font=("Roboto", 50), width=200, height=50, fg_color="blue",
                           bg_color="blue")
        lf1.place(x=5, y=135)
        game[0]="O"
        Denetle()
        clicked()

def b2():
    global bclick, bc2,game
    if bclick == True and bc2 == True:

        f2 = ctk.CTkFrame(master=app, width=200, height=200, fg_color="blue")
        f2.place(x=215, y=65)
        Button2.destroy()
        bclick = False
        bc2 = False
        lf2 = ctk.CTkLabel(master=app, text="X", font=("Roboto", 50), width=200, height=50, fg_color="blue",
                           bg_color="blue")
        lf2.place(x=215, y=135)
        game[1] = "X"
        Denetle()
        clicked()

    elif bc2 == True and bclick == False:

        f2 = ctk.CTkFrame(master=app, width=200, height=200, fg_color="blue")
        f2.place(x=215, y=65)
        Button2.destroy()
        bclick = True
        bc2 = False
        lf2 = ctk.CTkLabel(master=app, text="O", font=("Roboto", 50), width=200, height=50, fg_color="blue",
                           bg_color="blue")
        lf2.place(x=215, y=135)
        game[1] = "O"
        Denetle()
        clicked()



def b3():
    global bclick, bc3,game
    if bclick == True and bc3 == True:

        f3 = ctk.CTkFrame(master=app, width=200, height=200, fg_color="blue")
        f3.place(x=425, y=65)
        Button3.destroy()
        bclick = False
        bc3 = False
        lf3 = ctk.CTkLabel(master=app, text="X", font=("Roboto", 50), width=200, height=50, fg_color="blue",
                           bg_color="blue")
        lf3.place(x=425, y=135)
        game[2] = "X"
        Denetle()
        clicked()

    elif bc3 == True and bclick == False:

        f3 = ctk.CTkFrame(master=app, width=200, height=200, fg_color="blue")
        f3.place(x=425, y=65)
        Button3.destroy()
        bclick = True
        bc3 = False
        lf3 = ctk.CTkLabel(master=app, text="O", font=("Roboto", 50), width=200, height=50, fg_color="blue",
                           bg_color="blue")
        lf3.place(x=425, y=135)
        game[2] = "O"
        Denetle()
        clicked()





def b4():
    global bclick, bc4,game
    if bclick == True and bc4 == True:

        f4 = ctk.CTkFrame(master=app, width=200, height=200, fg_color="blue")
        f4.place(x=5, y=275)
        Button4.destroy()
        bclick = False
        bc4 = False
        lf4 = ctk.CTkLabel(master=app, text="X", font=("Roboto", 50), width=200, height=50, fg_color="blue",
                           bg_color="blue")
        lf4.place(x=5, y=345)
        game[3] = "X"
        Denetle()
        clicked()

    elif bc4 == True and bclick == False:

        f4= ctk.CTkFrame(master=app, width=200, height=200, fg_color="blue")
        f4.place(x=5, y=275)
        Button4.destroy()
        bclick = True
        bc4 = False
        lf4 = ctk.CTkLabel(master=app, text="O", font=("Roboto", 50), width=200, height=50, fg_color="blue",
                           bg_color="blue")
        lf4.place(x=5, y=345)
        game[3] = "O"
        Denetle()
        clicked()


def b5():
    global bclick, bc5,game
    if bclick == True and bc5 == True:

        f5 = ctk.CTkFrame(master=app, width=200, height=200, fg_color="blue")
        f5.place(x=215, y=275)
        Button5.destroy()
        bclick = False
        bc5 = False
        lf5 = ctk.CTkLabel(master=app, text="X", font=("Roboto", 50), width=200, height=50, fg_color="blue",
                           bg_color="blue")
        lf5.place(x=215, y=345)
        game[4] = "X"
        Denetle()
        clicked()

    elif bc5 == True and bclick == False:

        f5 = ctk.CTkFrame(master=app, width=200, height=200, fg_color="blue")
        f5.place(x=215, y=275)
        Button5.destroy()
        bclick = True
        bc5 = False
        lf5 = ctk.CTkLabel(master=app, text="O", font=("Roboto", 50), width=200, height=50, fg_color="blue",
                           bg_color="blue")
        lf5.place(x=215, y=345)
        game[4] = "O"
        Denetle()
        clicked()

def b6():
    global bclick, bc6,game
    if bclick == True and bc6 == True:

        f6 = ctk.CTkFrame(master=app, width=200, height=200, fg_color="blue")
        f6.place(x=425, y=275)
        Button6.destroy()
        bclick = False
        bc6 = False
        lf6 = ctk.CTkLabel(master=app, text="X", font=("Roboto", 50), width=200, height=50, fg_color="blue",
                           bg_color="blue")
        lf6.place(x=425, y=345)
        game[5] = "X"
        Denetle()

        clicked()

    elif bc6 == True and bclick == False:

        f6 = ctk.CTkFrame(master=app, width=200, height=200, fg_color="blue")
        f6.place(x=425, y=275)
        Button6.destroy()
        bclick = True
        bc6 = False
        lf6 = ctk.CTkLabel(master=app, text="O", font=("Roboto", 50), width=200, height=50, fg_color="blue",
                           bg_color="blue")
        lf6.place(x=425, y=345)
        game[5] = "O"
        Denetle()
        clicked()


def b7():
    global bclick, bc7,game
    if bclick == True and bc7 == True:

        f7 = ctk.CTkFrame(master=app, width=200, height=200, fg_color="blue")
        f7.place(x=5, y=485)
        Button7.destroy()
        bclick = False
        bc7 = False
        lf7 = ctk.CTkLabel(master=app, text="X", font=("Roboto", 50), width=200, height=50, fg_color="blue",
                           bg_color="blue")
        lf7.place(x=5, y=555)
        game[6] = "X"
        Denetle()
        clicked()

    elif bc7 == True and bclick == False:

        f7 = ctk.CTkFrame(master=app, width=200, height=200, fg_color="blue")
        f7.place(x=5, y=485)
        Button7.destroy()
        bclick = True
        bc7 = False
        lf7 = ctk.CTkLabel(master=app, text="O", font=("Roboto", 50), width=200, height=50, fg_color="blue",
                           bg_color="blue")
        lf7.place(x=5, y=555)
        game[6] = "O"
        Denetle()
        clicked()


def b8():
    global bclick, bc8,game
    if bclick == True and bc8 == True:

        f8 = ctk.CTkFrame(master=app, width=200, height=200, fg_color="blue")
        f8.place(x=215, y=485)
        Button8.destroy()
        bclick = False
        bc8 = False
        lf8 = ctk.CTkLabel(master=app, text="X", font=("Roboto", 50), width=200, height=50, fg_color="blue",
                           bg_color="blue")
        lf8.place(x=215, y=555)
        game[7] = "X"
        Denetle()
        clicked()

    elif bc8 == True and bclick == False:

        f8 = ctk.CTkFrame(master=app, width=200, height=200, fg_color="blue")
        f8.place(x=215, y=485)
        Button8.destroy()
        bclick = True
        bc8 = False
        lf8 = ctk.CTkLabel(master=app, text="O", font=("Roboto", 50), width=200, height=50, fg_color="blue",
                          bg_color="blue")
        lf8.place(x=215, y=555)
        game[7] = "O"
        Denetle()
        clicked()



def b9():
    global bclick, bc9,game
    if bclick == True and bc9 == True:

        f9 = ctk.CTkFrame(master=app, width=200, height=200, fg_color="blue")
        f9.place(x=425, y=485)
        Button9.destroy()
        bclick = False
        bc9 = False
        lf9 = ctk.CTkLabel(master=app, text="X", font=("Roboto", 50), width=200, height=50, fg_color="blue",
                           bg_color="blue")
        lf9.place(x=425, y=555)
        game[8] = "X"
        Denetle()
        clicked()

    elif bc9 == True and bclick == False:

        f9 = ctk.CTkFrame(master=app, width=200, height=200, fg_color="blue")
        f9.place(x=425, y=485)
        Button9.destroy()
        bclick = True
        bc9 = False
        lf9 = ctk.CTkLabel(master=app, text="O", font=("Roboto", 50), width=200, height=50, fg_color="blue",
                           bg_color="blue")
        lf9.place(x=425, y=555)
        game[8] = "O"
        Denetle()
        clicked()





label1 = ctk.CTkLabel(master=app,text="XOX Oyununa Hoş Geldin",width=200,font=("Roboto", 20))
label1.place(x=200,y=30)
button1 = ctk.CTkButton(master=app,text="Oyna",width=200,command=start)
button1.place(x=200,y=200)



app.mainloop()