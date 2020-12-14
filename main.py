import pgzrun
from random import choice,randint
from string import ascii_letters
WIDTH=800
HEIGHT=600
colour=(252, 161, 146)
letter = {'a':'' , 'x':0 , 'y':20 }
sc_letters=[]
scoreg=0
scoreb=0

def draw():
    global scoreg,scoreb,i
  
    screen.fill(colour)
    for letter in sc_letters:
         screen.draw.text(letter['a'],(letter['x'],letter['y']),fontsize=50,color=(153, 47, 29))

    screen.draw.text("Correct:"+str(scoreg),(WIDTH-80,0),fontsize=20,color=(1,1,1))
    screen.draw.text("Wrong:"+str(scoreb),(WIDTH-80,20),fontsize=20,color=(1,1,1))
    print("velocity:",i)    
    

    

def update():
    global scoreb,velocity
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
    global scoreg,scoreb,temp_1,i
    i=0
    print('correct:',scoreg)
    if scoreg>0 and scoreg<10:
        i=1
        print('correct:',scoreg)

    elif scoreg>=10 and scoreg<30:
        i=1.1
        print('correct:',scoreg)

        
    elif scoreg>=30 and scoreg < 50:
        i=1.4
        print('correct:',scoreg)
        
    elif scoreg>=50 and scoreg< 100:
        i=1.7
        print('correct:',scoreg)
        
    elif scoreg>=100 and scoreg< 150:
        i=2          
        print('correct:',scoreg)                                                                  

    elif scoreg>=150 and scoreg < 1000:
        i=3 
        print('correct:',scoreg)
        
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


def randomiser_color():
  global j,colour1
  j=0
  while j==0:
    colour1 = (randint(0,255),randint(0,255),randint(0,255))  
    j+=1  
   

def checker(): #this function is not called and needs correction 
    global i,j,colour1
    if scoreg != 0 and scoreg%10==0:
        i+=0.5
        
                                                                            

randomiser()
print("\033[91m"+"\033[1m" + "LOG:"  + "\033[0m")  
music.play('bgm')
pgzrun.go()
