# Pygameで横スクロールアクションを作ろう!!

import pygame
import sys


# main関数
def main():

  # -------------------------
  #
  # 初期化する
  #

  # Pygameの初期化する
  pygame.init()

  # スクリーンのサイズを決める
  screen_width = 800  # スクリーンの幅
  screen_height = 600  # スクリーンの高さ

  # ゲームウィンドウの作成する
  # 作成するときにスクリーンの幅と高さを設定する
  screen = pygame.display.set_mode((screen_width, screen_height))

  # -------------------------
  #
  # 更新する
  #

  # ゲームループ
  running = True
  while running:  # runningがTrueの間、回し続ける

    # イベントを処理する
    for event in pygame.event.get():

      # 終了イベントならば
      if event.type == pygame.QUIT:
        # runningをFalseにする
        running = False

    # for event はここまで

    # ゲームのロジックをここに追加

    # ゲーム画面を更新する
    pygame.display.flip()

  # while running はここまで

  # -------------------------
  #
  # 終了する
  #

  # Pygameを終了する
  pygame.quit()

  # アプリケーションを終了する
  sys.exit()


# mainはここまで

if __name__ == '__main__':

  # mainを呼び出す
  main()
