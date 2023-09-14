import pygame
import sys

# pygameの初期化
pygame.init()

# ゲームウィンドウのサイズ
screen_width = 800
screen_height = 600

# ゲームウィンドウの作成
screen = pygame.display.set_mode((screen_width, screen_height))

# ゲームループ
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # ゲームのロジックをここに追加

  # ゲーム画面を更新
  pygame.display.flip()

# Pygameの終了
pygame.quit()
sys.exit()
