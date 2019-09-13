import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600
Score = 0
Time = 0
Game_over = False

fox = Actor('fox')
fox.pos = 100,100
coin1 = Actor('coin')
coin2 = Actor('coin')
coin3 = Actor('coin')

def draw():
    screen.fill((151,255,255))
    fox.draw()
    coin1.draw()
    coin2.draw()
    coin3.draw()
    screen.draw.text('Score : '+str(Score),color='black',topleft=(10,10))
    screen.draw.text('Score : '+str(Time),color='black',topright=(770,10))
    if Game_over:
        screen.fill('pink')
        msg = "Time out,final score : " + str(Score)
        screen.draw.text(msg,topleft=(200,200),fontsize=50)
def update():
    global Score
    if keyboard.left and fox.left >= 0:
        fox.x = fox.x - 3
    if keyboard.right and fox.right <= WIDTH:
        fox.x = fox.x + 3
    if keyboard.up and fox.top >= 0:
        fox.y = fox.y - 3
    if keyboard.down and fox.bottom <= HEIGHT:
        fox.y = fox.y + 3
        
    coin_collected = fox.colliderect(coin1)
    if coin_collected:
        place_coin1()
        sounds.harp.play()
        Score += 1
    coin_collected = fox.colliderect(coin2)
    if coin_collected:
        place_coin2()
        sounds.harp.play()
        Score += 1
    coin_collected = fox.colliderect(coin3)
    if coin_collected:
        place_coin3()
        sounds.harp.play()
        Score += 1 
        
def place_coin1():
    x = randint(30,WIDTH - 30)
    y = randint(30,HEIGHT - 30)
    coin1.pos = (x,y)

def place_coin2():
    x = randint(30,WIDTH - 30)
    y = randint(30,HEIGHT - 30)
    coin2.pos = (x,y)

def place_coin3():
    x = randint(30,WIDTH - 30)
    y = randint(30,HEIGHT - 30)
    coin3.pos = (x,y)

def time_count():
    global Time
    Time += 1
    
def time_out():
    global Game_over
    Game_over = True

clock.schedule_interval(time_count,1.0)
clock.schedule(time_out,30.0)
place_coin1()
place_coin2()
place_coin3()
pgzrun.go()
