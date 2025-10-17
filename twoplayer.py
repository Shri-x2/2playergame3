import pyautogui, pygame, time, random
pygame.init()
w, h = pyautogui.size()
spacewar = pygame.display.set_mode((w, h))
bullets = []
pygame.display.set_caption("Space War")
space = pygame.image.load("spacebg1.png")
space = pygame.transform.scale(space, (w, h))
ship1 = pygame.image.load("spaceship.png")
ship1 = pygame.transform.scale(pygame.transform.rotate(ship1, 90), (60, 60))
ship2 = pygame.image.load("spaceship2.png")
ship2 = pygame.transform.scale(pygame.transform.rotate(ship2, -90), (60, 60))
border = pygame.Rect(w//2 - 10, 0, 20, h)

def draw(red, orange, bulletred, bulletorange):
    spacewar.blit(space, (0, 0))
    pygame.draw.rect(spacewar, (255, 0, 0), red)
    pygame.draw.rect(spacewar, (255, 165, 0), orange)
    spacewar.blit(ship1, (red.x, red.y))
    spacewar.blit(ship2, (orange.x, orange.y))
    pygame.draw.rect(spacewar, ("white"), border)
    for i in bulletred:
        pygame.draw.rect(spacewar, ("red"), i)
    for i in bulletorange:
        pygame.draw.rect(spacewar, ("orange"), i)
    pygame.display.update()
def handlebullets(red, orange, bulletred, bulletorange):
    
    for i in bulletred:
        i.x += 1
        print(i.x)
        for j in bulletorange:
            if i.colliderect(j):
                print("HEllo")
                bulletred.remove(i)
                bulletorange.remove(j)
                break
        if i.x >= w:
            bulletred.remove(i)
        if i.colliderect(orange):
            bulletred.remove(i)
            print("collided orange")
    for i in bulletorange:
        i.x -= 10
        if i.x <= 0:
            bulletorange.remove(i)
        if i.colliderect(red):
            bulletorange.remove(i)
            print("Collide red")            
def shipmove(keypressed, red, orange):
    if keypressed[pygame.K_UP] and red.y > 0:
        red.y -= 10
    if keypressed[pygame.K_DOWN] and red.y < h - red.height:
        red.y += 10
    if keypressed[pygame.K_LEFT] and red.x > 0:
        red.x -= 10
    if keypressed[pygame.K_RIGHT] and red.x < border.x - red.width:
        red.x += 10
    if keypressed[pygame.K_w] and orange.y > 0:
        orange.y -= 10
    if keypressed[pygame.K_s] and orange.y < h - orange.height:
        orange.y += 10
    if keypressed[pygame.K_a] and orange.x > border.x + 20:
        orange.x -= 10
    if keypressed[pygame.K_d] and orange.x < w - orange.width:
        orange.x += 10
def main():   
    red = pygame.Rect(100, h//2, 60, 60)
    orange = pygame.Rect(w-160, h//2, 60, 60)
    bulletsred = bulletsorange = []
    print(bulletsred, bulletsorange)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RCTRL:
                    bullet = pygame.Rect(orange.x, orange.y + orange.height // 2, 20, 8)
                    bulletsorange.append(bullet)
                    # pygame.display.update()
                if e.key == pygame.K_LCTRL:
                    bullet = pygame.Rect(red.x + red.width, red.y + red.height // 2, 20, 8)
                    print(bullet.x)
                    bulletsred.append(bullet)
                    #pygame.display.update()
        keypressed = pygame.key.get_pressed()
        shipmove(keypressed, red, orange)
        draw(red, orange, bulletsred, bulletsorange)
        handlebullets(red, orange, bulletsred, bulletsorange)

        pygame.display.update()
main()
       

