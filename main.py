import pgzrun
import sqlite3
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


def draw():
    global scoreg,scoreb,i,colour,colour1,lvl
    leveler()

    screen.fill(colour)
    screen.draw.text(lvl,((WIDTH//2)-50,20),fontsize=50,color='white')
    for letter in sc_letters:
         screen.draw.text(letter['a'],(letter['x'],letter['y']),fontname="mono",fontsize=50,color=colour1)

    screen.draw.text("Correct:"+str(scoreg),(WIDTH-80,0),fontsize=20,color=(1,1,1))
    screen.draw.text("Wrong:"+str(scoreb),(WIDTH-80,20),fontsize=20,color=(1,1,1))
    print("velocity:",i)




def update():
    global scoreb,velocity,i
    leveler()
    for letter in sc_letters:
      letter['y']+=i
      if  letter['y'] > HEIGHT :
        randomiser()
        sc_letters.remove(letter)
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
    print('correct:',scoreg)
    if scoreg>0 and scoreg<10:
        i=1
        colour=(252 , 161, 146)
        colour1=(153, 47, 29)
        lvl="Tin Tier"
        print('correct:',scoreg)


    elif scoreg>=10 and scoreg<30:
        i=1.1
        colour=(154, 189, 245)
        colour1=(13, 57, 128)                          #nice:))
        lvl="Silver Tier"
        print('correct:',scoreg)

    elif scoreg>=30 and scoreg < 50:
        i=1.4
        colour=(37, 12, 118)
        colour1=(163, 141, 235)
        lvl="Gold Tier"
        print('correct:',scoreg)

    elif scoreg>=50 and scoreg< 100:
        i=1.7
        colour=(131, 17, 135)
        colour1=(229, 144, 232)
        lvl="Platinum Tier"
        print('correct:',scoreg)

    elif scoreg>=100 and scoreg< 150:
        i=2
        colour=(140, 0, 17)
        colour1=(235, 141, 152)
        lvl="Diamond Tier"
        print('correct:',scoreg)

    elif scoreg>=150 and scoreg < 1000:
        i=3
        colour=(10, 6, 7)
        colour1=(217, 0, 255)
        lvl="God Tier"
        print('correct:',scoreg)

    else:
        i=1
        print("GG")



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

print("\033[91m"+"\033[1m" + "LOG:"  + "\033[0m")
music.play('bgm')
pgzrun.go()
n=input("\033[1m" + "Enter your Username: "+ "\033[0m" )
tot=(n,lvl,scoreg,scoreb)
c.execute('INSERT INTO scores VALUES (?,?,?,?)', tot)
conn.commit()
conn.close()
print("\n\n\n")
print("\033[1m" + "\t\t\t------------------------" + "\033[0m" )
print("\033[1m" + "\t\t\t         SCORE" + "\033[0m" )
print("\033[1m" + "\t\t\t------------------------" + "\033[0m" )
print("\n\n")
print("\033[91m"+"\033[1m" + "Wrong and missed Letters : " +str(scoreb)+ "\033[0m")
print("\033[94m"+"\033[1m" + "Correct Letters          : " +str(scoreg)+ "\033[0m")
print("\033[95m"+"\033[1m" + "\n\nCongratulations "+"\033[4m"+"\033[1m"+n+"\033[0m" +" on reaching "+"\033[0m"+"\033[4m"+"\033[1m"+lvl+"\033[0m"  )
print("\033[95m"+"\033[1m" + "\n\tGG"+"\033[0m")
