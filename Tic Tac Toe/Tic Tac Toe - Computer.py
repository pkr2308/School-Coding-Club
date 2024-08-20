'''
Tic Tac Toe - Computer
'''
import pygame
import sys
import random
pygame.init() # Initialising pygame

pygame.display.set_caption("Tic Tac Toe")
screen = pygame.display.set_mode((600, 650))

spaces = [['','',''],['','',''],['','','']]

font = pygame.font.Font('freesansbold.ttf', 32)

black = (0,0,0)
currentplayer = 'X'
winner = ''
player = ''
computer = ''


def draw_board():
    for i in range(0, 4):
        pygame.draw.line(screen, black, (i * 150 + 75, 125), (i * 150 + 75, 575), 3)
        pygame.draw.line(screen, black, (75, i * 150 + 125), (525, i * 150 + 125), 3)

def set_players():
    text = font.render("Do you want to start?", True, black)
    textRect = text.get_rect()
    textRect.center = (300, 45)
    screen.blit(text, textRect)

    text = font.render("Yes", True, black)
    textRect = text.get_rect()
    textRect.center = (200, 90)
    screen.blit(text, textRect)

    text = font.render("No", True, black)
    textRect = text.get_rect()
    textRect.center = (400, 90)
    screen.blit(text, textRect)

    pygame.display.flip()

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
def minimax_score():
    for i in range(0, 3):
        if spaces[i][0] == spaces[i][1] == spaces[i][2] and spaces[i][0] != '':
            return spaces[i][0]
        if spaces[0][i] == spaces[1][i] == spaces[2][i] and spaces[0][i] != '':
            return spaces[0][i]
    if spaces[0][0] == spaces[1][1] == spaces[2][2] and spaces[0][0] != '':
        return spaces[0][0]
    if spaces[0][2] == spaces[1][1] == spaces[2][0] and spaces[0][2] != '':
        return spaces[0][2]
    if all([spaces[i][j] != '' for i in range(0, 3) for j in range(0, 3)]):
        return '-'
    return ''

def declare_winner(winner):
    if (winner == 'X' and player == 'X') or (winner == 'O' and player == 'O'): 
        winner = 'You'
        text = font.render(f'{winner} win!', True, black)
    elif (winner == 'X' and computer == 'X') or (winner == 'O' and computer == 'O'):
        winner = 'Computer'
        text = font.render(f'{winner} wins!', True, black)
    elif winner == '-':
        text = font.render('Draw!', True, black)
    if winner != '': 
        textRect = text.get_rect()
        textRect.center = (300, 50)
        screen.blit(text, textRect)
    check_score()

def display_screen():
    screen.fill((255,182,193))
    draw_board()
    if (computer != '' and player != ''):
        if(winner == ''):
            if currentplayer == computer:
                text = font.render("Computer's chance", True, black)
            if currentplayer == player:
                text = font.render("Your chance", True, black)
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

def minimax(spaces, depth, isMaximizing):
    score = minimax_score()
    if score != '':
        if score == computer: score = 10
        if score == player: score = -10
        if score == '-': score = 0
    if isMaximizing:
        bestscore = -1000
        for i in range(0, 3):
            for j in range(0, 3):
                if spaces[i][j] == '':
                    spaces[i][j] = computer
                    score = minimax(spaces, depth + 1, False)
                    spaces[i][j] = ''
                    bestscore = max(score, bestscore)
        return bestscore
    else:
        bestscore = 1000
        for i in range(0, 3):
            for j in range(0, 3):
                if spaces[i][j] == '':
                    spaces[i][j] = player
                    score = minimax(spaces, depth + 1, True)
                    spaces[i][j] = ''
                    bestscore = min(score, bestscore)
        return bestscore

def computer_move():
    move = []
    bestscore = -1000
    moves = []
    for i in range(0, 3):
        for j in range(0, 3):
            if spaces[i][j] == '':
                spaces[i][j] = computer
                score = minimax(spaces, 0, False)
                spaces[i][j] = ''
                if score > bestscore:
                    bestscore = score
                    move = [i, j]
                    moves = []
                    moves.append(move)
                elif score == bestscore:
                    move = [i, j]
                    moves.append(move)
    if len(moves) > 0:
        move = moves[random.randint(0, len(moves) - 1)]
    spaces[move[0]][move[1]] = computer


display_screen()
set_players()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and winner == '':
            if player == '':
                x,y = pygame.mouse.get_pos()
                if x > 150 and x < 250 and y > 65 and y < 115: player = 'X'
                if x > 350 and x < 450 and y > 65 and y < 115: player = 'O'
                if player != '':
                    if player == 'X': computer = 'O'
                    else: computer = 'X'
                    currentplayer = 'X'
                    display_screen()
            elif player != '' and currentplayer == player:        
                x,y = pygame.mouse.get_pos()
                row = (y - 125) // 150
                col = (x - 75) // 150
                if spaces[row][col] == '': spaces[row][col] = currentplayer
                if currentplayer == 'X': currentplayer = 'O'
                else: currentplayer = 'X'
    if currentplayer == computer and computer != '':
        computer_move()
        currentplayer = player
    display_screen()
    if player == '' or computer == '': set_players()
    winner = check_score()
    if winner != '': declare_winner(winner)