import math
import random
import sys
import pygame as pg
import time

# global変数
WIDTH = 1600    # ウィンドウの横幅
HIGHT = 900     # ウィンドウの縦幅
txt_origin = ["攻撃","防御","魔法","回復","調教","逃走"]    # 勇者の行動選択肢のリスト
HP = 50         # 勇者のHP
MP = 10         # 勇者のMP
ENE_HP = 10     # 敵スライムのHP

class Button:
    """
    勇者の行動選択ボタンに関するクラス
    """
    def __init__(self, x, y, width, height, color, hover_color, text, text_color, action, num):
        """
        初期化メソッド
        x: ボタンのx座標
        y: ボタンのy座標
        width: ボタンの横幅
        height: ボタンの縦幅
        color: ボタンの色
        hover_color: マウスカーソルがボタンの上にある時のボタンの色
        text: 行動選択肢の文字
        text_color: 文字の色
        action: action関数
        num: index(0:攻撃, 1:防御, 2:魔法, 3:回復, 4:調教, 5:逃走)
        """
        self.rect = pg.Rect(x, y, width, height)    # rectを四角形を描画するsurfaceで初期化
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.text_color = text_color
        self.action = action
        self.num = num

    def draw(self,scr):
        """
        ボタンを描画するメソッド
        scr: display surface
        """
        pg.draw.rect(scr, self.color, self.rect)    # ボタンとなる四角形を描画
        font = pg.font.SysFont("hg正楷書体pro", 50)  # フォント指定
        text_surface = font.render(self.text, True, self.text_color)    # テキストsurface
        text_rect = text_surface.get_rect(center=self.rect.center)      # テキストの中心値指定
        scr.blit(text_surface, text_rect)   # ボタン描画

    def handle_event(self, event):
        """
        勇者の行動の切り替えメソッド
        event: event
        """
        # マウスボタンが押されたかつ左クリック(event.button == 1)の場合
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            # マウスの座標がボタンの範囲内にあれば
            if self.rect.collidepoint(event.pos):
                act = self.action(self.num)   # action関数を実行
                return act
        
def action(i):
    """
    勇者の行動に関する関数
    i: index (0:攻撃, 1:防御, 2:魔法, 3:回復, 4:調教, 5:逃走)
    """
    global HP, ENE_HP

    p = ["攻撃","防御","魔法","回復","調教","逃走"]
    print(p[i])

    # 攻撃処理
    fight_p = HP / 20       # 勇者の攻撃力
    if i == 0:              # 攻撃ボタンが押されたら
        ENE_HP -= fight_p   # スライムのHPを3減らす
    if ENE_HP <= 0:         # スライムのHPが0以下になったら
        ENE_HP = 0          # スライムのHPを0にする
    
    return i
        
def main():
    """
    main関数
    """
    global WIDTH, HIGHT, txt_origin, HP, ENE_HP    # global変数

    bg_image = "./ex05/fig/back.png"
    pg.display.set_caption("RPG of くそげー")   # ウィンドウの名前
    screen = pg.display.set_mode((WIDTH, HIGHT))    # 1600x900のdisplay surface
    clock  = pg.time.Clock()                        # 時間
    # surface
    # 背景
    bg_img = pg.image.load(bg_image)
    bg_img = pg.transform.scale(bg_img,(WIDTH,HIGHT))
    # 敵スライム
    ene_img = pg.image.load("./ex05/fig/ene.png")
    ene_rct = ene_img.get_rect()
    # 攻撃エフェクト
    toka = 0    # 攻撃エフェクトの透過度
    fight_img = pg.image.load("./ex05/fig/fight_effect.png")
    fight_img = pg.transform.scale(fight_img,(WIDTH,HIGHT))
    # テキストボックス
    win = pg.image.load("./ex05/fig/win.png")
    win = pg.transform.scale(win,(WIDTH/4,HIGHT/2))
    win2 = pg.transform.scale(win,(WIDTH-100,HIGHT/4))
    # フォント
    font1 = pg.font.SysFont("hg正楷書体pro", 100)
    font2 = pg.font.SysFont("hg正楷書体pro", 50)
    # テキスト
    text = "野生のスライムが現れた"
    fight_txt = "スライムを倒した！"
    txt = []    # 選択ボタンを描画するsurfaceのリスト
    # 勇者の行動選択ボタンを描画するsurfaceを作成しリストtxtに追加
    font3 = pg.font.SysFont(None, 200)
    die_text = "You died" # 死亡メッセージ

    for i,tx in enumerate(txt_origin):
        # インスタンス化
        if i%2==0:
            button = Button(125, 500+(i//2)*100, 100, 50, (50,50,50), (0,0,0), tx, (255,255,255), action, i)
        else:
            button = Button(275, 500+(i//2)*100, 100, 50, (50,50,50), (0,0,0), tx, (255,255,255), action, i)
        txt.append(button)

    # 繰り返し文    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return    # ×ボタンが押されたらプログラム終了

            for button in txt:                  # 勇者の行動処理
                act = button.handle_event(event)

                if act == 0:    # 勇者が攻撃したら
                    # 攻撃エフェクト
                    for i in range(25):
                        toka += 10
                        if toka > 255:
                            toka = 0
                        fight_img.set_alpha(toka)
                        screen.blit(fight_img,[200, 100])
                        pg.display.update()
                    time.sleep(0.1)

        screen.blit(bg_img,[0, 0])      # 背景描画
        screen.blit(ene_img,[WIDTH/2-ene_rct.width/2+100, HIGHT/2]) # 敵スライム描画
        screen.blit(win,[50, 400])      # テキストボックス描画
        screen.blit(win2,[50, 50])      # 行動選択のテキストボックス描画

        if ENE_HP <= 0:
            text = fight_txt
        x = 200
        for chr in text:
            rendered_text = font1.render(chr, True, (255, 255, 255))
            text_width = rendered_text.get_width()
            screen.blit(rendered_text,[x, 100])
            x += text_width
        for i in txt:
            i.draw(screen)  # ボタン描画
            if HP<=0: # HPが0になったら
                die_text2 = font3.render(die_text, True, (255, 0, 0))
                screen.blit(die_text2, (600, 450)) # 600, 450の位置に赤色で"You died"を表示する
                pg.display.update()
                time.sleep(3)
                pg.quit()

        text_surface1 = font2.render(f"HP:{HP} MP:{MP}", True, (255,255,255))   # 勇者のHP,MPのテキストsurface
        text_surface2 = font2.render(f"HP:{ENE_HP}", True, (255,255,255))       # 敵スライムのHPのテキストsurface
        screen.blit(text_surface1,[100, 350])   # 勇者のHP,MP表示
        screen.blit(text_surface2,[WIDTH/2-ene_rct.width/2+225, HIGHT/2-50])    # 敵スライムのHP表示
        
        # スライムを倒したら、画面を3秒止めてプログラム終了
        if ENE_HP <= 0:
            pg.display.update()
            time.sleep(3)
            sys.exit()

        pg.display.update()     # ディスプレイのアップデート
        clock.tick(100)         # 時間

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()