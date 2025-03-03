import pygame,sys,time,random
LIGHT_GRAY = (170, 170, 170)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (57, 168, 23)
BLUE = (30, 60, 183)
PURPLE = (71, 19, 139)
WHITE = (250, 250, 250)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 700

from classes.minesweeper_board_class import MinesweeperBoard

# writes text on the screen
def write_text(screen,text, x, y, c, font): 
    font = pygame.font.SysFont(None, font)
    img = font.render(text, True, c)
    screen.blit(img, (x, y))

# horizontally centers numbers on board
def center_number_X(board,position): 
    centeringx = 0
    if 0 <= board[position] <= 9:
        centeringx = 12
    if board[position] >= 10:
        centeringx = 2
    return centeringx

# vertically centers numbers on board
def center_number_Y(board,position):
    centeringy = 0
    if 0 <= board[position] <= 9:
        centeringy = 8
    if board[position] >= 10:
        centeringy = 8
    return centeringy

# colors numbers on the board
def getColor(number): 
    displayPos = number
    match displayPos:
        case 0:
            return LIGHT_GRAY
        case 1:
            return BLUE
        case 2:
            return GREEN
        case 3:
            return RED
        case 4:
            return PURPLE
        case _:
            return BLACK

# draw graphical interface of current state of board
def draw_board(screen, board: MinesweeperBoard, flagImg, mineImg):
    DISPLAY = board.getDisplayBoard()
    MINEBOARD = board.getMineBoard()
    SIZE = board.getSize()
    FLAG = board.getFlag()
    MINE = board.getMine()
    for row in range(SIZE):
        for col in range(SIZE):
            tileValue = DISPLAY.get(row, col)

            if tileValue == FLAG:
                screen.blit(flagImg, (row * 50, col * 50))
            elif board.isGameOver() and MINEBOARD.get(row, col) == MINE:
                screen.blit(mineImg, (row * 50, col * 50))
            else:
                colour = getColor(tileValue)
                pygame.draw.rect(screen, (200, 200, 200), [row * 50, col * 50, 45, 45])  # draws gray rectangles to form grid
                write_text(screen,str(tileValue), row * 50, col * 50, colour,50)  # places blank spaces across grid
        
# returns (row, col) index of clicked square
def convertMouseClick(x, y, boardSize): 
    row = x // 50
    col = y // 50
    if 0 <= row <= boardSize - 1 and 0 <= col <= boardSize - 1:
        return row, col
    else:
        return None, None

def main():
    # intialize window and pygame
    pygame.init()
    
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Minesweeper")
    start_ticks = pygame.time.get_ticks()

    # set up images
    # mine image
    mineImg = pygame.image.load("mine_minesweeper.jpg").convert_alpha()
    mineImg = pygame.transform.scale(mineImg, (45, 45))  
    # flag image
    flagImg = pygame.image.load("mine_flag.png").convert_alpha()
    flagImg = pygame.transform.scale(flagImg, (45, 45))

    # create minesweeper board
    board = MinesweeperBoard(10)
    
    # main game loop
    while board.isWin() == False and board.isGameOver() == False:
        for event in pygame.event.get():

            (x, y) = pygame.mouse.get_pos()  # gets position of mouse click
            row, col = convertMouseClick(x, y, board.getSize())

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if row != None and col != None:
                    board.clickTile(row, col)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_f: # place flags with F key
                if row != None and col != None:
                    board.placeFlag(row, col)

        # keep track and display time on screen
        seconds = (pygame.time.get_ticks() - start_ticks) // 1000  
        pygame.draw.rect(screen, BLACK, [0, 505, 500, 200])
        write_text(screen, f"Time: {str(seconds)}", 20, 510, WHITE, 70)

        if board.isGameOver():
            pygame.draw.rect(screen, BLACK, [0, 505, 500, 200])# displays loss screen if lost
            write_text(screen, "You exploded!", 85, 600, RED, 70)
            write_text(screen, f"Time: {str(seconds)}", 20, 510, WHITE, 70)

        if board.isWin():  # displays win screen if won
            pygame.draw.rect(screen, BLACK, [0, 505, 500, 200])
            write_text(screen,"You win!", 150, 600, GREEN, 70)
            write_text(screen, f"Time: {str(seconds)}", 20, 510, WHITE, 70)

        draw_board(screen, board, flagImg, mineImg)
        pygame.display.flip()
main()
time.sleep(5)