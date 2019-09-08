import pygame
import random

pygame.init()

row, column =600, 600
size = (row, column)
end, run = True, True
white = (255, 255, 255)
xaxis, yaxis = 75, 0
x, y, z, a = 0, 1, 1, 1
o = 0
back_color = (0, 0, 0)

wind = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")
list_disp = [(0, 0), (25, 0), (50, 0), (75, 0)]
result = 0


def fill_board():

    global column, row, white, wind, o, back_color

    if o % 2 == 1:
        back_color = (120, 120, 150)

    wind.fill(back_color)

    for j in range(0, column - 1, 25):
        pygame.draw.lines(wind, white, False, [(0, j), (column, j)])
    pygame.draw.lines(wind, (125, 25, 170), False, [(0, column - 1), (column, column - 1)], 6)
    pygame.draw.lines(wind, (125, 25, 170), False, [(0, 0), (0, column)], 6)

    for i in range(25, row - 1, 25):
        pygame.draw.lines(wind, white, True, [(i, 0), (i, row)])
    pygame.draw.lines(wind, (125, 25, 170), False, [(row - 1, 0), (row - 1, row)], 6)
    pygame.draw.lines(wind, (125, 25, 170), False, [(0, 0), (column , 0)], 6)


def exit_game(end):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = False
            pygame.display.quit()
    return end


def lost_game(run, xaxis, yaxis):

    if xaxis > row - 1 or yaxis > column-1 or xaxis < 0 or yaxis < 0:
        run = False
        wind.fill((0, 0, 0))
        pygame.display.update()
    return run


def check_keys():

    global xaxis, yaxis, x,  y, z, a, run, list_disp, result
    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN]:
        if y != 0 and z != 0:
            y, x, z, a = 0, 1, 1, 1
    if keys[pygame.K_UP]:
        if y != 0 and z != 0:
            y, x, z, a = 1, 1, 0, 1
    if keys[pygame.K_RIGHT]:
        if x != 0 and a != 0:
            y, x, z, a = 1, 0, 1, 1
    if keys[pygame.K_LEFT]:
        if x != 0 and a != 0:
            y, x, z, a = 1, 1, 1, 0
    if keys[pygame.K_SPACE]:
        if run == True:
            return xaxis, yaxis, x, y, z, a, run, list_disp, result

        run = True
        xaxis, yaxis = 75, 0
        x, y, z, a = 0, 1, 1, 1
        list_disp = [(0, 0), (25, 0), (50, 0), (75, 0)]
        result = 0


def random_food():
    i = random.randint(0, 600/25-1)
    j = random.randint(0, 600/25-1)
    return i*25, j*25


def main():

    global row, column, xaxis, x, y, yaxis, z, a, end, run, o, result, list_disp

    i, j = random_food()

    while end:
        pygame.time.delay(100)

        if run:
            fill_board()
            check_keys()
            if x == 0:
                xaxis += 25
            if y == 0:
                yaxis += 25
            if z == 0:
                yaxis -= 25
            if a == 0:
                xaxis -= 25
            run = lost_game(run, xaxis, yaxis)

            if not run :
                continue
            if (xaxis, yaxis) in list_disp:
                run = False
                continue

            if (xaxis, yaxis) == (i, j):
                i, j = random_food()
                o += 1
                result += 1
            else:
                list_disp.pop(0)

            list_disp.append((xaxis, yaxis))

            for r, t in list_disp:
                pygame.draw.rect(wind, (255, 255, 0), pygame.Rect(r, t, 25, 25))
            r, t = list_disp[len(list_disp)-1]

            pygame.draw.rect(wind, (0, 0, 0), pygame.Rect(r+17, t+7, 3, 3))
            pygame.draw.rect(wind, (0, 0, 0), pygame.Rect(r+17, t+17, 3, 3))

            pygame.draw.circle(wind, (255, 0, 0), (i + 25 // 2 + 1, j + 25 // 2 + 1), 10)
            pygame.display.update()

            end = exit_game(end)

        else:
            wind.fill((255, 255, 255))

            basicfont = pygame.font.SysFont(None, 48)
            text = basicfont.render(f' YOUR SCORE IS ', True, (255, 0, 0), (255, 255, 255))

            basicfont3 = pygame.font.SysFont(None, 60)
            text3 = basicfont3.render(f' {result} ', True, (255, 0, 0), (255, 255, 255))

            basicfont2 = pygame.font.SysFont(None, 24)
            text2 = basicfont2.render(f' press space to retry ', True, (255, 0, 0), (255, 255, 255))
            wind.blit(text2, (430, 450))
            wind.blit(text3, (290, 230))
            wind.blit(text, (170, 190))
            pygame.display.update()
            check_keys()
            end = exit_game(end)

main()
pygame.quit()
