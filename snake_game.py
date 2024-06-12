
import time
import random
import turtle as turt


score = 0
#speed of the snake will be controlled by this variable
delay = 0.03
head = turt.Turtle()
init_board = turt.Turtle()
ts = turt.Screen()
prey = turt.Turtle()

def display_screen():
    ts.setup(width=600, height=600)
    ts.bgcolor("tan")
    ts.title('Snake Game by Team')
    ts.tracer(0)

def initial_board():
    init_board.speed(0)
    init_board.shape('square')
    init_board.color('black')
    init_board.penup()
    init_board.hideturtle()
    init_board.goto(100, 220)
    init_board.write('Score: 0', font = ('Georgia', 20, 'bold'))
    init_board.penup()

def settingup_playing_field():
    field = turt.Turtle()
    field.speed(0)
    field.shape('square')
    field.color('black')
    field.fillcolor('light blue')
    field.penup()
    field.hideturtle()
    field.goto(220,220)
    field.pendown()
    field.goto(-220,220)
    field.goto(-220,-220)
    field.goto(220,-220)
    field.goto(220,220)
    field.penup()


def snake_head():
    head.speed(-100)
    head.shape("square")
    head.color('black')
    head.penup()
    head.goto(0,0)
    head.direction = 'stop'

def snake_prey():
    prey.speed(0) 
    prey.shape("turtle")
    prey.color('green')
    prey.penup()
    prey.goto(0,100)

pieces = []

def update_score(score):
    init_board.clear()
    init_board.write('Score: {}'.format(score), font = ('Georgia', 20, 'bold'))

def up():
    if head.direction != 'down':
        head.direction = 'up' 
        
def down():
    if head.direction != 'up':
        head.direction = 'down'
def left():
    if head.direction != 'right':
        head.direction = 'left'
def right():
    if head.direction != 'left':
        head.direction = 'right'


def move():
    for i in range(len(pieces)-1, 0, -1):
        x = pieces[i-1].xcor()
        y = pieces[i-1].ycor()
        pieces[i].goto(x,y)
    if len(pieces) > 0:
        x = head.xcor()
        y = head.ycor()
        pieces[0].goto(x,y)
    if head.direction == 'up':
        head.sety(head.ycor() + 5)
    if head.direction == 'down':
        head.sety(head.ycor() - 5)
    if head.direction == 'left':
        head.setx(head.xcor() - 5)
    if head.direction == 'right':
        head.setx(head.xcor() + 5)

def crash():
    score = 0
    time.sleep(0.1)
    head.goto(0,0)
    head.direction = 'stop'
    update_score(score)
    for segment in pieces:
        segment.hideturtle()
    pieces.clear()


def keyboard_binding():
    ts.listen()
    try:
        ts.onkeypress(right, 'Right')
        ts.onkeypress(up, 'Up')
        ts.onkeypress(left, 'Left')
        ts.onkeypress(down, 'Down')
    except:
        print('Use the right keys!')
        
    
    

display_screen()
settingup_playing_field()
snake_head()
snake_prey()
initial_board()
keyboard_binding()


while True:
    ts.update()

    if head.xcor()>200 or head.xcor()<-200 or head.ycor()>200 or head.ycor()<-200:
        crash()
    

    if head.distance(prey) < 20:
        prey.goto(random.randint(-200,200),random.randint(-200,200))
        new_segment = turt.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color("brown")
        new_segment.penup()
        pieces.append(new_segment)
        score += 1
        update_score(score)

    move()

    for segment in pieces:
        if segment.distance(head) < 5:
            crash()
    time.sleep(delay)
ts.mainloop()
