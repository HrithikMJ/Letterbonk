import pgzrun #pgzrun to play the game
import sqlite3 #sqlite3 to manage database
from time import sleep #sleep module for a better feel while using console
import csv#to manage log
import os # for getting os name in screen_clear()
from random import choice,randint # to randomise values for more fun
from string import ascii_letters# to get letter string
import pygame
#sql connection
conn = sqlite3.connect('score_1.db')
c = conn.cursor()
#declaring variables
WIDTH=800
HEIGHT=700
letter = {'a':'' , 'x':0 , 'y':20 }
sc_letters=[]
scoreg=0
scoreb=0
name_list=[]

#to create tables if they dont EXISTS
c.execute("CREATE TABLE IF NOT EXISTS names (names text NOT NULL PRIMARY KEY);")
c.execute("CREATE TABLE IF NOT EXISTS scores (name text NOT NULL PRIMARY KEY, tier text, correct int, wrong int);")

def screen_clear():  #to clear screen
   # for mac and linux
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def loadingsc():#to make a minimalist loading screen
   flag = 1
   while flag < 4:
    print("\rin" + ("." * flag), end=" ")
    sleep(1)
    flag = flag + 1

def menu():#The main menu
    print("********************************************************************")
    print("\033[96m"+"\033[1m"+"\t\t\tLetter Bonk   v0.6"+"\033[0m", flush=False)
    print("********************************************************************")
    print(" \n")
    print("\tSelect one of the options below or press any other key to exit\n")
    print("1. Play")
    print("2. Display Highscores")
    print("3. DELETE specific value ")
    print("4. DELETE all HIGHSCORES")
    choice = input("Please enter your choice:")
    print(" \n")
    screen_clear()

    return choice

def draw(): #draw function of pgzrun
    global scoreg,scoreb,i,colour,colour1,lvl
    leveler()
    pygame.mixer.init()
    if not music.is_playing('bgm') :
         music.play('bgm')


    screen.fill(colour)
    screen.draw.text(lvl,((WIDTH//2)-50,20),fontsize=50,color='white')

    for letter in sc_letters:
         screen.draw.text(letter['a'],(letter['x'],letter['y']),fontname="mono",fontsize=50,color=colour1)

    screen.draw.text("Correct:"+str(scoreg),(WIDTH-80,0),fontsize=20,color=(1,1,1))
    screen.draw.text("Wrong:"+str(scoreb),(WIDTH-80,20),fontsize=20,color=(1,1,1))
    r=[i,scoreg,scoreb]
 #NICE:)))))
    csv_logger(r)


def csv_logger(r): #log
    filename = "log.csv"
    fields=['Velocity','correct','wrong']
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)

        csvwriter.writerow(r)


def update():#update function of pgzrun
    global scoreb,i,scoreg
    leveler()
    r=[i,scoreg,scoreb]
    csv_logger(r)
    for letter in sc_letters:
      letter['y']+=i
      if  letter['y'] > HEIGHT :
        randomiser()
        sc_letters.remove(letter)
        sounds.win.play()
        scoreb+=1

    while len(sc_letters) < 4 :
        randomiser()


def randomiser():#to randomise values
    letter={}
    letter['a'] = choice(ascii_letters)
    letter['x'] = randint(10,WIDTH-30)
    letter['y'] = 20
    sc_letters.append(letter)


def leveler(): #to add levels
    global scoreg,scoreb,temp_1,i,colour,colour1,lvl
    i=0
    lvl="GG"
    colour=(252 , 161, 146)
    colour1=(153, 47, 29)

    if scoreg>0 and scoreg<10:
        i=1
        colour=(252 , 161, 146)
        colour1=(153, 47, 29)
        lvl="Tin Tier"

    elif scoreg>=10 and scoreg<30:
        i=1.1
        colour=(154, 189, 245)
        colour1=(13, 57, 128)
        lvl="Silver Tier"


    elif scoreg>=30 and scoreg < 50:
        i=1.4
        colour=(37, 12, 118)
        colour1=(163, 141, 235)
        lvl="Gold Tier"


    elif scoreg>=50 and scoreg< 100:
        i=1.7
        colour=(131, 17, 135)
        colour1=(229, 144, 232)
        lvl="Platinum Tier"


    elif scoreg>=100 and scoreg< 150:
        i=2
        colour=(140, 0, 17)
        colour1=(235, 141, 152)
        lvl="Diamond Tier"

    elif scoreg>=150 and scoreg < 1000:
        i=3
        colour=(10, 6, 7)
        colour1=(217, 0, 255)
        lvl="God Tier"

    else:
        i=1

def username_checker(a):#this function checks username and is divided into 2 parts

    if a== 1:#part 1: this is to check whether a entered username is unique

        n=input("\033[1m" + "Enter your Username: "+ "\033[0m" )
        n.lower()
        c.execute("SELECT * FROM names" )
        record = c.fetchall()
        try:
           c.execute('INSERT INTO names VALUES (?)', (n,))
           conn.commit()
           tot=(n,lvl,scoreg,scoreb)
           print("\n\n\n")
           print("\033[1m" + "\t\t\t------------------------" + "\033[0m" )
           print("\033[1m" + "\t\t\t         SCORE" + "\033[0m" )
           print("\033[1m" + "\t\t\t------------------------" + "\033[0m" )
           print("\n")
           print("\033[91m"+"\033[1m" + "Wrong and missed Letters : " +str(scoreb)+ "\033[0m")
           print("\033[94m"+"\033[1m" + "Correct Letters          : " +str(scoreg)+ "\033[0m")
           if lvl!="GG":
              print("\033[95m"+"\033[1m" + "\n\nCongratulations "+"\033[4m"+"\033[1m"+n+"\033[0m" +" on reaching "+"\033[0m"+"\033[4m"+"\033[1m"+lvl+"\033[0m"  )
              print("\033[95m"+"\033[1m" + "\n\tGG"+"\033[0m")
           else:
                print("\033[1m" + "TRY TYPING THE LETTERS AS THEY APPEAR ON SCREEN" + "\033[0m" )

           try:
                 c.execute('INSERT INTO scores VALUES (?,?,?,?)', tot)
                 conn.commit()

           except:
                 print("Something went wrong:(())")



        except:
            print("\033[91m"+"\033[1m" + "Username alredy exist"  + "\033[0m")
            print("Try again")
            username_checker(1)


    elif a== 2:#part2: to check whether a username exists
        print("THE FOLLOWING WILL BE DISPLAYED IN ['name','tier','correct','wrong'] ")
        c.execute("SELECT name FROM scores" )
        record = c.fetchall()
        name_view=input("Enter username of player to be viewed : ")
        name_view.lower()

        if name_view in record:
            c.execute("SELECT * FROM scores WHERE name=?;", (name_view,) )
            print(c.fetchall())
            sleep(2)
            print("\n\n")
            print("\033[91m"+"\033[1m" + "DONE!!"  + "\033[0m")

        else:
             print("\033[91m"+"\033[1m" + "Username doesnt exist"  + "\033[0m")
             print("Try again")
             username_checker(2)

def on_key_down(unicode): #keydown function of pgzrun
#this function detects key presses
    global scoreb,scoreg

    if unicode:
       for letter in sc_letters:
        if unicode == letter['a'] :
          randomiser()
          sc_letters.remove(letter)
          scoreg+=1
          break
       else :
          scoreb+=1
          sounds.negative.play()



#start of main function

randomiser()
#start of while loop
while True:
    ch = menu()
    if ch == '1':

         pgzrun.go()
         username_checker(1)



    elif ch == '2':
        print("THE FOLLOWING WILL BE DISPLAYED IN ['name','tier','correct','wrong'] ")
        c.execute("SELECT * FROM scores ORDER BY correct DESC;")
        sleep(1)
        print(c.fetchall())

    elif ch == '3':

        c.execute("SELECT * FROM scores ;")
        print(c.fetchall())
        name_del=input("Enter name to be deleted : ")
        name_del.lower()
        k=input("\033[91m"+"\033[1m" + "ARE YOU SURE?........type 'YeS' to confirm or press anyother key to quit "  + "\033[0m")
        if k=='YeS':
            loadingsc()
            c.execute("DELETE FROM scores WHERE name=?", (name_del,))
            c.execute("DELETE FROM names WHERE names=?", (name_del,))
        else:
            sleep(3)
            screen_clear()

    #elif ch== '5' :

            #username_checker(2)



    elif ch== '4' :
        k=input("\033[91m"+"\033[1m" + "ARE YOU SURE?........type 'YeS' to confirm "  + "\033[0m")
        if k=='YeS':
            loadingsc()
            c.execute("DELETE FROM scores")
            c.execute("DELETE FROM names")
            conn.commit()
            screen_clear()
            print("\033[91m"+"\033[1m" + "DONE!!"  + "\033[0m")

        else:
            conn.close()
            sleep(5)
            screen_clear()
            break

    else:

       conn.close()
       print("\033[91m"+"\033[1m" + "CIAO!!"  + "\033[0m")
       sleep(2)
       screen_clear()
       break
