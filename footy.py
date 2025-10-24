import pygame, pyautogui
pygame.init()

w, h = pyautogui.size()
footy = pygame.display.set_mode((w, h))
pygame.display.set_caption("Football")
clock = pygame.time.Clock()

# Assets
field = pygame.transform.scale(pygame.image.load("footyfield.png"), (w, h))
player1 = pygame.transform.scale(pygame.transform.rotate(pygame.image.load("footballer.png"), 90), (60, 60))
player2 = pygame.transform.scale(pygame.transform.rotate(pygame.image.load("footballer2.png"), -90), (60, 60))
ball_img = pygame.transform.scale(pygame.image.load("goldball.png"), (30, 30))
# ball2_img = pygame.transform.scale(pygame.image.load("goldball2.png"), (30, 30))  # unused for now

border = pygame.Rect(w // 2 - 10, 0, 20, h)

def draw(red, orange, ball_rect):
    footy.blit(field, (0, 0))
    pygame.draw.rect(footy, "white", border)
    footy.blit(player1, (red.x, red.y))
    footy.blit(player2, (orange.x, orange.y))
    footy.blit(ball_img, (ball_rect.x, ball_rect.y))
    pygame.display.update()

def playermove(keys, red, orange):
    # Red on LEFT half
    if keys[pygame.K_UP] and red.y > 0:
        red.y -= 10
    if keys[pygame.K_DOWN] and red.y < h - red.height:
        red.y += 10
    if keys[pygame.K_LEFT] and red.x > 0:
        red.x -= 10
    if keys[pygame.K_RIGHT] and red.x < border.x - red.width:
        red.x += 10

    # Orange on RIGHT half
    if keys[pygame.K_w] and orange.y > 0:
        orange.y -= 10
    if keys[pygame.K_s] and orange.y < h - orange.height:  # fixed bound
        orange.y += 10
    if keys[pygame.K_a] and orange.x > border.x + border.width:
        orange.x -= 10
    if keys[pygame.K_d] and orange.x < w - orange.width:
        orange.x += 10

def move_ball(ball_rect, vel):
    # Move
    ball_rect.x += vel[0]
    ball_rect.y += vel[1]

    # Bounce on vertical boundaries
    if ball_rect.left <= 0 or ball_rect.right >= w:
        vel[0] *= -1
        # clamp inside screen
        ball_rect.left = max(ball_rect.left, 0)
        ball_rect.right = min(ball_rect.right, w)

    # Bounce on horizontal boundaries (top/bottom)
    if ball_rect.top <= 0 or ball_rect.bottom >= h:
        vel[1] *= -1
        ball_rect.top = max(ball_rect.top, 0)
        ball_rect.bottom = min(ball_rect.bottom, h)

    # Bounce on center border
    if ball_rect.colliderect(border):
        # If coming from left/right, flip X; otherwise flip Y
        # Simple approach: flip X
        vel[0] *= -1
        # Nudge out of border to avoid sticking
        if ball_rect.centerx < border.centerx:
            ball_rect.right = border.left
        else:
            ball_rect.left = border.right

def main():
    red = pygame.Rect(100, h // 2, 60, 60)
    orange = pygame.Rect(w - 160, h // 2, 60, 60)

    # Ball rect from image, centered mid-field
    ball_rect = ball_img.get_rect(center=(w // 2, h // 2))
    ball_vel = [8, 5]  # vx, vy

    running = True
    while running:
        clock.tick(60)  # cap FPS
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        playermove(keys, red, orange)
        move_ball(ball_rect, ball_vel)
        draw(red, orange, ball_rect)

    pygame.quit()

if __name__ == "__main__":
    main()
