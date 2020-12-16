import pgzrun
import sqlite3
import time
import csv
from random import choice,randint
from string import ascii_letters
conn = sqlite3.connect('score_1.db')
c = conn.cursor()
WIDTH=800
HEIGHT=700
letter = {'a':'' , 'x':0 , 'y':20 }
sc_letters=[]
scoreg=0
scoreb=0

def loadingsc():
   flag = 1
   while flag < 4:
    print("\rin" + ("." * flag), end=" ")
    time.sleep(1)
    flag = flag + 1

def menu():
    print(" \n")
    print("\tSelect one of the below options...UwU\n")
    print("1. Play")
    print("2. Display Highscores")
    print("3. Exit Game")
    print("4. DELETE all HIGHSCORES")
    choice = int(input("Please enter your choice:"))
    print(" \n")

    return choice

def draw():
    global scoreg,scoreb,i,colour,colour1,lvl
    leveler()

    screen.fill(colour)
    screen.draw.text(lvl,((WIDTH//2)-50,20),fontsize=50,color='white')
    for letter in sc_letters:
         screen.draw.text(letter['a'],(letter['x'],letter['y']),fontname="mono",fontsize=50,color=colour1)

    screen.draw.text("Correct:"+str(scoreg),(WIDTH-80,0),fontsize=20,color=(1,1,1))
    screen.draw.text("Wrong:"+str(scoreb),(WIDTH-80,20),fontsize=20,color=(1,1,1))
    r=[i,scoreg,scoreb]
    csv_logger(r)


def csv_logger(r):
    filename = "log.csv"
    fields=['Velocity','correct','wrong']
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerow(r)



def update():
    global scoreb,i,scoreg
    leveler()
    r=[i,scoreg,scoreb]
    csv_logger(r)
    for letter in sc_letters:
      letter['y']+=i
      if  letter['y'] > HEIGHT :
        randomiser()
        sc_letters.remove(letter)                                               #NICE:)))))
        sounds.win.play()
        scoreb+=1

    while len(sc_letters) < 4 :
        randomiser()


def randomiser():
    letter={}
    letter['a'] = choice(ascii_letters)
    letter['x'] = randint(10,WIDTH-30)
    letter['y'] = 20
    sc_letters.append(letter)

def leveler():
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




def on_key_down(unicode):
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




randomiser()
print("********************************************************************")
print("\t\t\tLetter Bonk", flush=False)
print("********************************************************************")
while True:
    ch = menu()
    if ch == 1:
        music.play('bgm')
        pgzrun.go()
        n=input("\033[1m" + "Enter your Username: "+ "\033[0m" )
        tot=(n,lvl,scoreg,scoreb)
        c.execute('INSERT INTO scores VALUES (?,?,?,?)', tot)
        conn.commit()

        print("\n\n\n")
        print("\033[1m" + "\t\t\t------------------------" + "\033[0m" )
        print("\033[1m" + "\t\t\t         SCORE" + "\033[0m" )
        print("\033[1m" + "\t\t\t------------------------" + "\033[0m" )
        print("\n\n")
        print("\033[91m"+"\033[1m" + "Wrong and missed Letters : " +str(scoreb)+ "\033[0m")
        print("\033[94m"+"\033[1m" + "Correct Letters          : " +str(scoreg)+ "\033[0m")
        print("\033[95m"+"\033[1m" + "\n\nCongratulations "+"\033[4m"+"\033[1m"+n+"\033[0m" +" on reaching "+"\033[0m"+"\033[4m"+"\033[1m"+lvl+"\033[0m"  )
        print("\033[95m"+"\033[1m" + "\n\tGG"+"\033[0m")
        conn.close()
        break

    elif ch == 2:
        c.execute("SELECT * FROM scores ;")
        print(c.fetchall())

    elif ch == 3:
        conn.close()
        break

    elif ch==4 :
        k=input("\033[91m"+"\033[1m" + "ARE YOU SURE?........type 'YeS' to confirm "  + "\033[0m")
        if k=='YeS':
            loadingsc()
            c.execute("DELETE FROM scores")
            conn.commit()
            print("\033[91m"+"\033[1m" + "DONE!!"  + "\033[0m")

        else:
            conn.close()
            break



    else:
        print("\033[91m"+"\033[1m" + "INVALID INPUT"  + "\033[0m")
        print("Try again")
        loadingsc
        conn.close()
