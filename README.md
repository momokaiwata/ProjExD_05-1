# ゲーム のタイトル
* 「RPG of くそげー」
## 実行環境の必要条件
* python >= 3.10
* pygame >= 2.1

## ゲームの概要
* RPGの戦闘シーン、敵のスライムと戦闘をする
* 攻撃をクリック: スライムに攻撃
* 防御をクリック: 防御
* 回復をクリック: HPを回復
* 調教をクリック: スライムが仲間になる
* スライムを倒すとゲームクリア
* HPが0になると死亡、ゲームオーバー

## ゲームの実装
### 共通基本機能
#### global変数
* WIDTH: ウィンドウの横幅
* HIGHT: ウィンドウの縦幅
* txt_origin: 勇者の行動選択の文字列のリスト ["攻撃","防御","魔法","回復","調教","逃走"]
* HP: 勇者のヒットポイント
* MP: 勇者のマジックポイント
* ENE_HP: 敵のヒットポイント
#### Buttonクラス
* 勇者の行動を選択するためのボタンに関するクラス
##### 初期化メソッド:
* 引数:
+ x: ボタンのx座標
+ y: ボタンのy座標
+ width: ボタンの横幅
+ height: ボタンの縦幅
+ color: ボタンの色
+ hover_color: ？
+ text: 行動選択肢の文字
+ text_color: 文字の色
+ action: 行動
+ num: ？
##### drawメソッド:
* 勇者の行動選択肢のボタンを描画するメソッド
* 引数:
+ scr: screen
##### handle_eventメソッド:
*
#### action関数
*
#### main関数
*
### 画像fig
* back.png: 背景画像
* breiv.png: 4人パーティーの画像
* ene.png: 敵スライムの画像
* haikei.jpg: サブ背景
* win.png: テキストボックス

### 担当追加機能
* 戦闘: サクライ
* 防御: イワタ
* 回復: ママタ
* 死亡: コヤマ
* 仲間: イハラ
### ToDo
- [ ] 攻撃の選択をしたら敵のHPを減らす
- [ ] 攻撃の選択をしたら攻撃モーションを追加
- [ ] スライムを倒したらゲームクリアの表示
- [ ] 攻撃に合わせたテキストをテキストボックスに表示
### メモ
* 