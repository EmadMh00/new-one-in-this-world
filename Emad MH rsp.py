from tkinter import*
from random import randint
from tkinter import ttk

root = Tk()
root.title('Emad_Mh RSP')
root.iconbitmap()
root.geometry("700x800")
#pas zamine ra be sefid taghiir midahim.
root.config(bg="white")

#tasavir ra taarif mikonim
rock = PhotoImage(file='C:\\Users\\TS\\Downloads\\rock.png')
paper = PhotoImage(file='C:\\Users\\TS\\Downloads\\Paper.png')
scissors = PhotoImage(file='C:\\Users\\TS\\Downloads\\Scissors.png')

#tasavir ro be list azafe mikonim
image_list = [rock, paper, scissors]

#yek Adad random beyn 0 va 2 entekhab mikonim
pick_number = randint(0,2)

image_Label = Label(root, image=image_list[pick_number], bd=0)
image_Label.pack(pady=20)

#Function charkhesh ijad mikonim
def spin():
    #entekhab random adad
    pick_number = randint(0,2)
    #neshan dadan tasvir
    image_Label.config(image=image_list[pick_number])

    # 0 = Rock
    # 1 = Paper
    # 2 = Scissors

    #entekhab haro be adad tabdil mikonim
    if user_choice.get() == "Rock":
        user_choice_value = 0
    elif user_choice.get() == "Paper":
        user_choice_value = 1
    elif user_choice.get() == "Scissors":
        user_choice_value = 2


        # taiin chegonegiye bord va bakht
        # Agar karbar Sang ro entekhab konad
    if user_choice_value == 0 : #Rock
        if pick_number == 0 :
            win_lose_Label.config(text=" Mosavi shod dobare emtehan konid...")
        elif pick_number == 1 : #Paper
            win_lose_Label.config(text=" kaghaz Sang ro miposhone !! Shoma Bakhtid...")
        elif pick_number == 2 : #Scissors
            win_lose_Label.config(text=" sang Gheychi ro khord mikone !! Shoma Barande Shodid...")

    
        # Agar karbar kaghaz ro entekhab konad
    if user_choice_value == 1 : #Paper
        if pick_number == 1 :
            win_lose_Label.config(text=" Mosavi shod dobare emtehan konid...")
        elif pick_number == 0 : #Rock
            win_lose_Label.config(text=" kaghaz Sang ro miposhone !! Shoma Barande Shodid...")
        elif pick_number == 2 : #Scissors
            win_lose_Label.config(text=" Gheychi kaghaz ro Miboorad !! Shoma Bakhtid...")


        # Agar karbar Gheychi ro entekhab konad
    if user_choice_value == 2 : #Scissors
        if pick_number == 2 :
            win_lose_Label.config(text=" Mosavi shod dobare emtehan konid...")
        elif pick_number == 0 : #Rock
            win_lose_Label.config(text=" sang Gheychi ro khord mikone !! Shoma Bakhtid...")
        elif pick_number == 1 : #Paper
            win_lose_Label.config(text=" Gheychi kaghaz ro Miboorad !! Shoma Barande Shodid...")


    
#sakht panel entekhab
user_choice = ttk.Combobox(root, value=("Rock", "Paper", "Scissors"))
user_choice.current(0)
user_choice.pack(pady=20)

#sakht dokme charkhesh
spin_button = Button(root, text="Spin!", command=spin)
spin_button.pack(pady=10)

#Label baraye moshakhas karde bord va bakht
win_lose_Label = Label(root,text="",font=("helvetica",18),bg="white")
win_lose_Label.pack(pady=50)

root.mainloop()
