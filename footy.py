import pygame, time, random, pyautogui
pygame.init()
w, h = pyautogui.size()
footy = pygame.display.set_mode((w, h))
direction1 = 1
pygame.display.set_caption("Football")
field = pygame.image.load("footyfield.png")
field = pygame.transform.scale(field, (w, h))
player1 = pygame.image.load("footballer.png")
player1 = pygame.transform.scale(pygame.transform.rotate(player1, 90), (60, 60))
player2 = pygame.image.load("footballer2.png")
player2 = pygame.transform.scale(pygame.transform.rotate(player2, -90), (60, 60))
ball = pygame.image.load("goldball.png")
ball = pygame.transform.scale(ball, (30, 30))
ball2 = pygame.image.load("goldball2.png")
ball2 = pygame.transform.scale(ball2, (30, 30))
border = pygame.Rect(w//2 - 10, 0, 20, h)
def draw(red, orange, ballpos):
    footy.blit(field, (0, 0))
    pygame.draw.rect(footy, ("white"), border)
    # pygame.draw.rect(footy, (255, 0, 0), red)
    # pygame.draw.rect(footy, (255, 165, 0), orange)
    footy.blit(player1, (red.x, red.y))
    footy.blit(player2, (orange.x, orange.y))
    footy.blit(ball, (ballpos.x, ballpos.y))
    
def playermove(keypressed, red, orange, ballpos):
    global direction1
    if keypressed[pygame.K_UP] and red.y > 0:
        red.y -= 10
    if keypressed[pygame.K_DOWN] and red.y < h - red.height:
        red.y += 10
    if keypressed[pygame.K_LEFT] and red.x > 0:
        red.x -= 10
    if keypressed[pygame.K_RIGHT] and red.x < w - border.x - red.width:
        red.x += 10
    if keypressed[pygame.K_w] and orange.y > 0:
        orange.y -= 10
    if keypressed[pygame.K_s] and orange.y < h - red.height:
        orange.y += 10
    if keypressed[pygame.K_a] and orange.x > border.x + 20:
        orange.x -= 10
    if keypressed[pygame.K_d] and orange.x < w - orange.width:
        orange.x += 10
    # ballpos.x += 1
    # ballpos.y += 1
    ballpos.x += 10 * direction1
    if ballpos.x <= border.x + 5 and ballpos.x >= w - 30:
        direction1 = direction1 * (-1)
    # if ballpos.x < w - 30:
    #     ballpos.x -=1
    if ballpos.y > 0:
        ballpos.y -= 1
    if ballpos.y < h - 30:
        ballpos.y += 1
    
     
def main():
    red = pygame.Rect(100, h//2, 60, 60)
    orange = pygame.Rect(w-160, h//2, 60, 60)
    ballpos = pygame.draw.circle(footy, ("yellow"), (w//2 + 30, h//2), 15)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
        keypressed = pygame.key.get_pressed()
        playermove(keypressed, red, orange, ballpos)
        draw(red, orange, ballpos)
        pygame.display.update()
main()    