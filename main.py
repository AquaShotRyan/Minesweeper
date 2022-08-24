import pygame,sys,time,random

def write_text(screen,text, x, y, c, font): #function that writes text on the screen
    font = pygame.font.SysFont(None, font)
    img = font.render(text, True, c)
    screen.blit(img, (x, y))

def reset_flags(): #resets all the flags placed to blanks
    flags = [""] * 100
    return flags

def center_number_X(board,position): #centers numbers on board to make it look nice
    centeringx = 0
    if 0 <= board[position] <= 9:
        centeringx = 12
    if board[position] >= 10:
        centeringx = 2
    return centeringx

def center_number_Y(board,position): #centers numbers on board to make it look nice
    centeringy = 0
    if 0 <= board[position] <= 9:
        centeringy = 8
    if board[position] >= 10:
        centeringy = 8
    return centeringy

def find_colour(display,position): #changes colour of the number
    #colours
    gray = (200, 200, 200)
    light_gray = (170, 170, 170)
    black = (0, 0, 0)
    white = (250, 250, 250)
    red = (255, 0, 0)
    green = (57, 168, 23)
    blue = (30, 60, 183)
    purple = (71, 19, 139)
    if display[position] == 0:
        colour = light_gray
    elif display[position] == 1:
        colour = blue
    elif display[position] == 2:
        colour = green
    elif display[position] == 3:
        colour = red
    elif display[position] == 4:
        colour = purple
    else:
        colour = black
    return colour

def draw_board(screen,display,flags,gameover,flag,board,mine):
    FLAG = "|"  # a flag to keep track of discovered mines
    MINE = 10  # the "mine"
    for y in range(10):
        for x in range(10):
            position = x + y * 10
            colour = find_colour(display,position)
            centeringx = center_number_X(board,position)
            centeringy = center_number_Y(board,position)

            pygame.draw.rect(screen, (200, 200, 200), [x * 50, y * 50, 45, 45])  # draws gray rectangles to form grid
            write_text(screen,str(display[position]), x * 50 + centeringx, y * 50 + centeringy, colour,50)  # places blank spaces across grid

            if flags[position] == FLAG:  # displays placed flags
                screen.blit(flag, (x * 50, y * 50))
            if gameover == True:  # displays the mines after gameover
                if board[position] == MINE:
                    screen.blit(mine, (x * 50, y * 50))

def which_square(x, y): #gives the position of the square clicked
    xpos = x // 50
    ypos = y // 50
    result = xpos + (ypos * 10)
    if 0 <= xpos <= 10 - 1 and 0 <= ypos <= 10 - 1:
        return result
    else:
        return -100

def setup_display():
    display = [""] * 100
    return display

def make_board():#makes the data for the board and sets it up
    MINE = 10  # the "mine"
    EMPTY = 0  # the non-mine spaces
    board = [MINE] * 12 + [EMPTY] * 88
    random.shuffle(board)
    return create_numbers(board,MINE)

def create_numbers(board,MINE):
    for i in range(len(board)):
        column = i % 10 #numbers coloumn on the grid from 0 to 9
        row = i // 10 #numbers row on the grid from 0 to 9
        if board[i] < MINE:
            if row > 0 and column > 0 and board[i - 11] == MINE:#ensures squares are truly adjacent
                board[i] += 1
            if row > 0 and board[i - 10] == MINE:
                board[i] += 1
            if row > 0 and column < 9 and board[i - 9] == MINE:
                board[i] += 1
            if column > 0 and board[i - 1] == MINE:
                board[i] += 1
            if column < 9 and board[i + 1] == MINE:
                board[i] += 1
            if column > 0 and row < 9 and board[i + 9] == MINE:
                board[i] += 1
            if row < 9 and board[i + 10] == MINE:
                board[i] += 1
            if row < 9 and column < 9 and board[i + 11] == MINE:
                board[i] += 1
        if board[i] >= 10:
            board[i] = 10
    return board

def main():
    # colours
    black = (0, 0, 0)
    white = (250, 250, 250)
    red = (255, 0, 0)
    green = (57, 168, 23)
    MINE = 10  # the "mine"
    FLAG = "|"  # a flag to keep track of discovered mines

    #intialize window and intialize pygame
    pygame.init()
    window_width = 500  # dimensions of window
    window_height = 700
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Minesweeper")

    mine = pygame.image.load("mine_minesweeper.jpg").convert_alpha()  # mine image
    mine = pygame.transform.scale(mine, (45, 45))

    flag = pygame.image.load("mine_flag.png").convert_alpha()  # flag image
    flag = pygame.transform.scale(flag, (45, 45))

    flags = reset_flags()
    display = setup_display()
    board = make_board()

    gameover = False
    safe_spaces = 0
    start_ticks = pygame.time.get_ticks()

    while gameover == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pygame.mouse.get_pos()  # gets position of mouse click
                square = which_square(x, y)
                if display[square] != board[square]:  # only lets user interact with the square if not already interacted with
                    display[square] = board[square]
                    flags[square] = board[square]
                    if display[square] < 10:  # if user clicks on a non-mine, safe_spaces goes up by one
                        safe_spaces += 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    (x, y) = pygame.mouse.get_pos()
                    square = which_square(x, y)
                    if flags[square] == "":  # lets the user freely place and remove flags
                        flags[square] = FLAG
                    elif flags[square] == FLAG:
                        flags[square] = ""
                draw_board(screen,display,flags,gameover,flag,board,mine)
                pygame.display.flip()

            seconds = (pygame.time.get_ticks() - start_ticks) // 1000  # keeps track and displays time on screen
            pygame.draw.rect(screen, black, [0, 505, 500, 200])
            write_text(screen,"Time: " + str(seconds), 20, 510, white, 70)

            for i in display:  # looks for mines to see if player has lost
                if i == MINE:
                    gameover = True

                    pygame.draw.rect(screen, black, [0, 505, 500, 200])# displays loss screen if lost
                    write_text(screen, "You exploded!", 85, 600, red, 70)
                    write_text(screen, "Time: " + str(seconds), 20, 510, white, 70)

            if safe_spaces == 88:  # displays win screen if won
                gameover = True
                pygame.draw.rect(screen, black, [0, 505, 500, 200])
                write_text(screen,"You win!", 150, 600, green, 70)
                write_text(screen,"Time: " + str(seconds), 20, 510, white, 70)

            draw_board(screen,display,flags,gameover,flag,board,mine)
            pygame.display.flip()
main()
time.sleep(5)