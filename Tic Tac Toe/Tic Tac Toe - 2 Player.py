import pygame
import sys

pygame.init()

pygame.display.set_caption("Tic Tac Toe")
screen = pygame.display.set_mode((600, 650))

spaces = [['','',''],['','',''],['','','']]

font = pygame.font.Font('freesansbold.ttf', 32)

black = (0,0,0)
currentplayer = 'X'
winner = ''

def draw_board():
    for i in range(0, 4):
        pygame.draw.line(screen, black, (i * 150 + 75, 125), (i * 150 + 75, 575), 3)
        pygame.draw.line(screen, black, (75, i * 150 + 125), (525, i * 150 + 125), 3)

def check_score():
    for i in range(0, 3):
        if spaces[i][0] == spaces[i][1] == spaces[i][2] and spaces[i][0] != '':
            pygame.draw.line(screen, black, (150, i * 150 + 200), (450, i * 150 + 200), 3)
            pygame.display.flip()
            return spaces[i][0]
        if spaces[0][i] == spaces[1][i] == spaces[2][i] and spaces[0][i] != '':
            pygame.draw.line(screen, black, (i * 150 + 150, 200), (i * 150 + 150, 500), 2)
            pygame.display.flip()
            return spaces[0][i]
    if spaces[0][0] == spaces[1][1] == spaces[2][2] and spaces[0][0] != '':
        pygame.draw.line(screen, black, (150, 200), (450, 500), 2)
        pygame.display.flip()
        return spaces[0][0]
    if spaces[0][2] == spaces[1][1] == spaces[2][0] and spaces[0][2] != '':
        pygame.draw.line(screen, black, (450, 200), (150, 500), 2)
        pygame.display.flip()
        return spaces[0][2]
    if all([spaces[i][j] != '' for i in range(0, 3) for j in range(0, 3)]):
        return '-'
    return ''

def declare_winner(winner):
    if winner == 'X' or winner == 'O' :
        text = font.render(f'{winner} wins!', True, black)
        textRect = text.get_rect()
        textRect.center = (300, 50)
        screen.blit(text, textRect)
    elif winner == '-':
        text = font.render('Draw!', True, black)
        textRect = text.get_rect()
        textRect.center = (300, 50)
        screen.blit(text, textRect)

def display_screen():
    screen.fill((255,182,193))
    draw_board()
    if(winner == ''):
        text = font.render(f"{currentplayer}'s chance", True, black)
        textRect = text.get_rect()
        textRect.center = (300, 50)
        screen.blit(text, textRect)
    else:
        declare_winner(winner)
        
    for i in range(0, 3):
        for j in range(0, 3):
            if spaces[i][j] == 'X':
                text = font.render('X', True, black)
                textRect = text.get_rect()
                textRect.center = (j * 150 + 150, i * 150 + 200)
                screen.blit(text, textRect)
            if spaces[i][j] == 'O':
                text = font.render('O', True, black)
                textRect = text.get_rect()
                textRect.center = (j * 150 + 150, i * 150 + 200)
                screen.blit(text, textRect)
    pygame.display.flip()

display_screen()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and winner == '':
            x,y = pygame.mouse.get_pos()
            row = (y - 125) // 150
            col = (x - 75) // 150
            if spaces[row][col] == '': spaces[row][col] = currentplayer
            if currentplayer == 'X': currentplayer = 'O'
            else: currentplayer = 'X'
    
    display_screen()
    winner = check_score()
    if winner != '': declare_winner(winner)