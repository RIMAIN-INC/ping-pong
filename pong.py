#Author: Richmond Nartey Kwalah Tettey
#Course: CS1
#Date: 10/12/2024
#Purpose: Pong CS labs 1

from graphics import *



#Keys to Start and End Game
START_KEY = " "
END_KEY = "q"

#to set the background color once
first_background = True

#window sizes
WINDOW_X = 600
WINDOW_Y = 400

#constant height and width of square graphics
SQUARE_WIDTH = 20
SQUARE_HEIGHT = 80


#The amount that a paddle moves when it moves
PADDLE_RATE = 10



#Initial constant ball rate
BALL_RATE_X = 10
BALL_RATE_Y = 10

ball_rate_x = BALL_RATE_X
ball_rate_y = BALL_RATE_Y

#record players score
p1_score = 0
p2_score = 0

#record number of rounds
rounds = 0
MAX_ROUNDS = 5

#Constant Variable for position of two square graphics
PLAYER_X_1 = 0
PLAYER_X_2 = WINDOW_X - SQUARE_WIDTH

#to change movement of square between up and bottom
player_y_1 = 0

player_y_2 = WINDOW_Y - SQUARE_HEIGHT

#to check the keys pressed
is_a_pressed = False
is_z_pressed = False
is_k_pressed = False
is_m_pressed = False
is_space_pressed = False
is_q_pressed = False
is_s_pressed = False

#boolean to check if game has started
in_progress = False


#Ball Properties
BALL_SIZE = 10
BALL_COLOR = [252/255,213/255,40/255]


#Functions for Ball Attributes
circle_x = WINDOW_X/2
circle_y = WINDOW_Y/2

#function to draw ball object
def draw_ball():
    global circle_x, circle_y
    set_stroke_color(BALL_COLOR[0], BALL_COLOR[1], BALL_COLOR[2])
    set_fill_color(BALL_COLOR[0], BALL_COLOR[1], BALL_COLOR[2])
    draw_circle(circle_x,circle_y,BALL_SIZE)

#to make the ball move
def update_ball_position():
    global circle_x, circle_y,ball_rate_x,ball_rate_y
    circle_x -= ball_rate_x
    circle_y -= ball_rate_y

    if collide_inner_face():
        ball_rate_x = -ball_rate_x

    if collide_with_floor_ceiling():
        ball_rate_y = -ball_rate_y


#to set field boundaries
def draw_boundary():
    set_stroke_color(1,1,1)
    set_stroke_width(3)
    draw_line(int(WINDOW_X/2),0,int(WINDOW_X/2),int(WINDOW_Y))

#to bounce ball when it hits the pedal
def collide_inner_face():
    global circle_x,circle_y,player_y_2,player_y_1

    if PLAYER_X_2 <= circle_x + BALL_SIZE <= PLAYER_X_2 + SQUARE_WIDTH:
        if player_y_2 <= circle_y <= player_y_2 + SQUARE_HEIGHT:
            circle_x -= 5
            return True

    #returns true if ball position is equal to the pedal of player 1 (left)
    # if PLAYER_X_1 <= circle_x - BALL_SIZE <= PLAYER_X_1 + SQUARE_WIDTH:
    #     if player_y_1 <= circle_y <= player_y_1 + SQUARE_HEIGHT:
    #         return True

    if circle_x - BALL_SIZE <= PLAYER_X_1 + SQUARE_WIDTH:
        if player_y_1 <= circle_y + BALL_SIZE <= player_y_1 + SQUARE_HEIGHT:
            circle_x += 5
            return True

    return False

#to bounce off when hits with floor ceiling
def collide_with_floor_ceiling():

    #condition to check if ball hits the floor or ceiling
    if circle_y + BALL_SIZE >= WINDOW_Y or circle_y - BALL_SIZE <= 0:
        return True

    return False

#to end game when the ball hits the vertical walls
def collide_with_vertical_walls():
    global in_progress, p1_score, p2_score, rounds
    if circle_x + BALL_SIZE >= WINDOW_X or circle_x - BALL_SIZE <= 0: #increase rounds
        rounds += 1
        in_progress = False

    if circle_x + BALL_SIZE >= WINDOW_X: #increase score of red pedals
        p1_score += 1

    if  circle_x - BALL_SIZE <= 0: #increase score of blue pedals
        p2_score += 1

    return False



#draw square graphics
def draw_mysquare(my_x, my_y,r,g,b):
    global SQUARE_WIDTH, SQUARE_HEIGHT
    set_stroke_color(r,g,b)
    set_fill_color(r,g,b) #to change color of square
    draw_rectangle(my_x,my_y,SQUARE_WIDTH,SQUARE_HEIGHT) #to draw the rectangle function

#draw first and second player
my_first_player = draw_mysquare
my_second_player = draw_mysquare

# a function to change positions of square graphics
def change_position():
    global player_y_1, player_y_2, PADDLE_RATE

    #PLAYER 1 - to check if a is pressed to move square graphics withing the boundaries
    if is_a_pressed and player_y_1 > 0:
        player_y_1 -= PADDLE_RATE

    if is_z_pressed and player_y_1 < 400 - SQUARE_HEIGHT:
        player_y_1 += PADDLE_RATE

    #PLAYER 2 - to check if a is pressed to move square graphics withing the boundaries
    if is_k_pressed and player_y_2 > 0:
        player_y_2 -= PADDLE_RATE

    if is_m_pressed and player_y_2 < 400 - SQUARE_HEIGHT:
        player_y_2 += PADDLE_RATE


#function to display scores
def draw_score_board():
    global p1_score, p2_score
    set_stroke_color(1,1,1)
    set_fill_color(104/255,103/255,175/255)
    draw_rectangle(int(WINDOW_X/2) - int(WINDOW_X/5/2),0,int(WINDOW_X/5),int(WINDOW_Y/18))

    draw_text(str(p1_score),int(WINDOW_X/2)-int(WINDOW_X/20),int(WINDOW_Y/36)+5)
    draw_text(str(p2_score),int(WINDOW_X/2)+int(WINDOW_X/20),int(WINDOW_Y/36)+5)



#function to display game over text and an option to quit or rematch
def new_match():
    global p1_score, p2_score
    set_stroke_color(77/255,81/255,87/255)
    set_fill_color(77/255,81/255,87/255)
    # set_clear_color(62/255,143/255,82/255)

    draw_rectangle(int(WINDOW_X/5.5),int(WINDOW_Y/4), 400, 200)

    reset_game()

    p1_score = 0
    p2_score = 0


def draw_borders():
    set_stroke_color(1,1,1)
    set_stroke_width(6)
    draw_line(0,0,WINDOW_X,0)
    draw_line(WINDOW_X,0,WINDOW_X,WINDOW_Y)
    draw_line(0,WINDOW_Y,WINDOW_X,WINDOW_Y)
    draw_line(0,0,0,WINDOW_Y)


# Function to check if game is over
def check_game_over():
    global rounds, in_progress

    if rounds >= MAX_ROUNDS:
        in_progress = False
        draw_game_over_box()
        return True

    return False

# Function to display "Game Over" box
def draw_game_over_box():
    global p1_score, p2_score
    set_stroke_color(1, 1, 1)  # White border for the box
    set_fill_color(0, 0, 0)  # Black fill for the box
    draw_rectangle(0,0, int(WINDOW_X), int(WINDOW_Y))  # Box dimensions
    set_stroke_color(1, 1, 1)  # White text color

    first_player = ""
    if p2_score > p1_score:
        first_player = "Blue Wins!"
    elif p1_score > p2_score:
        first_player = "Red Wins!"
    else:
        first_player = "It was a Tier!"

    # Centered text
    draw_text(first_player, int(WINDOW_X / 2 -55)+ 20, int(WINDOW_Y / 2 - 30))
    draw_text("Press q to Quit", int(WINDOW_X / 2 - 100) + 20, int(WINDOW_Y / 2 + 5))
    draw_text("Press s For New Match", int(WINDOW_X / 2 - 100) + 20, int(WINDOW_Y / 2 + 20))

# Reset game and start a new match after Game Over
def new_match():
    global p1_score, p2_score, rounds, in_progress
    p1_score = 0
    p2_score = 0
    rounds = 0
    in_progress = False
    reset_game()



#function to reset positions of objects in the game
def reset_game():
    global player_y_1,player_y_2, circle_y, circle_x,ball_rate_y,ball_rate_x

    # to change movement of square between up and bottom
    player_y_1 = 0

    player_y_2 = WINDOW_Y - SQUARE_HEIGHT

    # variables for Ball Attributes
    circle_x = WINDOW_X / 2
    circle_y = WINDOW_Y / 2

    #change
    ball_rate_x = BALL_RATE_X
    ball_rate_y = BALL_RATE_Y


#A draw function to draw graphics
def draw():
    global PLAYER_X_1,PLAYER_X_2, player_y_1, player_y_2, my_first_player,my_second_player, is_space_pressed,circle_y,circle_x, rounds,first_background
    if first_background:
        set_clear_color(104/255,103/255,175/255)
        clear()


    #calling first and second player functions
    my_first_player(PLAYER_X_1,player_y_1, 1,0,0)
    my_first_player(PLAYER_X_2,player_y_2, 0,0,1)

    #drawing border lines of table
    draw_borders()

    #draw boundary line
    draw_boundary()
    draw_score_board()

    #calling draw circle function
    draw_ball()

    # Check if the game is over
    if check_game_over():
        if is_q_pressed:
            cs1_quit()
        if is_s_pressed:
            new_match()

    #To quit at any time when ball is not moving
    if not in_progress:
     if is_q_pressed:
         cs1_quit()

    # Game in progress
    if is_space_pressed and not in_progress:
        if is_q_pressed: #to quit the game
            cs1_quit()

        if rounds < MAX_ROUNDS:
            reset_game()  #to move on to next round
            is_space_pressed = False




    #to call functions when game starts
    if in_progress:
        # calling draw circle function
        draw_ball()
        # calling the function to move square graphics
        collide_inner_face()
        collide_with_vertical_walls()
        change_position()
        update_ball_position()



#to confirm the letters pressed
def my_key_press(value):
    global is_a_pressed, is_k_pressed, is_z_pressed , is_m_pressed, is_q_pressed, is_space_pressed,in_progress, is_s_pressed
    if value == "a":
        is_a_pressed = True
    if value == "z":
        is_z_pressed = True
    if value == "k":
        is_k_pressed = True
    if value == "m":
        is_m_pressed = True
    if value == " ":
        is_space_pressed = True
        in_progress = True
    if value == "q":
        is_q_pressed = True
    if value == "s":
        is_s_pressed = True

#to confirm the letters released
def my_key_release(value):
    global is_a_pressed, is_k_pressed, is_z_pressed, is_m_pressed, is_q_pressed, is_space_pressed, is_s_pressed
    if value == "a":
        is_a_pressed = False
    if value == "k":
        is_k_pressed = False
    if value == "z":
        is_z_pressed = False
    if value == "k":
        is_k_pressed = False
    if value == "m":
        is_m_pressed = False
    if value == "q":
        is_q_pressed = False
    if value == "s":
        is_s_pressed = False



start_graphics(draw, key_press=my_key_press, key_release=my_key_release, width=WINDOW_X, height=WINDOW_Y)