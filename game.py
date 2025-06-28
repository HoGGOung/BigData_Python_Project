import pygame
import random
import sys

# 게임 설정
WIDTH = 480
HEIGHT = 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 초기화
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("똥 피하기 게임")
clock = pygame.time.Clock()

# 플레이어 설정
player_img = pygame.image.load("player.png")
player_rect = player_img.get_rect()
player_rect.centerx = WIDTH // 2
player_rect.bottom = HEIGHT - 10

# 똥 이미지 및 설정
enemy_img = pygame.image.load("enemy.png")
enemy_width = enemy_img.get_width()
enemy_count = 3

# 똥 클래스 정의
class Enemy:
    def __init__(self):
        self.rect = enemy_img.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-300, -40)  # 서로 다른 높이에서 시작
        self.speed = random.randint(3, 7)        # 서로 다른 속도

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-300, -40)
            self.speed = random.randint(3, 7)

# 똥 3개 생성
enemies = [Enemy() for _ in range(enemy_count)]

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5

    # 게임 로직
    for enemy in enemies:
        enemy.update()

    # 충돌 검사
    for enemy in enemies:
        if player_rect.colliderect(enemy.rect):
            running = False

    # 그리기
    screen.fill(BLACK)
    screen.blit(player_img, player_rect)
    for enemy in enemies:
        screen.blit(enemy_img, enemy.rect)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
