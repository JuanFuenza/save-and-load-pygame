import pygame
import json

pygame.init()

WIDTH = 800
HEIGHT = 600
ds = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Save and load")

font = pygame.font.SysFont("Arial", 32)

data = {
    'red': 0,
    'blue': 0
}

try:
    with open("clicker_score.txt") as score_file:
        data = json.load(score_file)
except:
    print("Not file created yet")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('clicker_score.txt', 'w') as score_file:
                json.dump(data, score_file)
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if rect1.collidepoint(mouse_pos):
                data['red'] += 1
            if rect2.collidepoint(mouse_pos):
                data['blue'] += 1
        
    ds.fill((220, 220, 220))

    rect1_rect = pygame.Rect(WIDTH//3, HEIGHT//2, 200, 200)
    rect1_rect.center = (WIDTH//4, HEIGHT//2)
    rect1 = pygame.draw.rect(ds, "red", rect1_rect)

    rect2_rect = pygame.Rect(WIDTH//3, HEIGHT//2, 200, 200)
    rect2_rect.center = (3*WIDTH//4, HEIGHT//2)
    rect2 = pygame.draw.rect(ds, "blue", rect2_rect)

    score1_text = font.render(f"Clicks: {data['red']}", True, "black")
    score1_rect = score1_text.get_rect(topleft = (WIDTH - 750, 50))
    ds.blit(score1_text, score1_rect)

    score2_text = font.render(f"Clicks: {data['blue']}", True, "black")
    score2_rect = score2_text.get_rect(topleft = (WIDTH - 150, 50))
    ds.blit(score2_text, score2_rect)

    pygame.display.update()

pygame.quit()