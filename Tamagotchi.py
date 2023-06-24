import PySimpleGUI as sg
import os
import textwrap
import pygame

def play_music():
    pygame.mixer.init() # mixerモジュールを初期化
    pygame.mixer.music.load("music/levelup.mp3") # 音楽ファイルの読み込み
    pygame.mixer.music.play() # 音楽の再生

class Tamagotchi:

    def __init__(self, name):
        self.name = name
        self.age = 0
        self.hunger = 5
        self.happiness = 5
        self.weight = 1
        self.stage = "start" # 進化を追跡する新しいプロパティを追加
        print(f"{self.name}が孵化しました！")

    def eat(self):
        print(f"{self.name}にご飯を与えました")
        print("もぐもぐ!")
        self.age += 0
        self.hunger = min(100, self.hunger + 5)
        self.happiness = min(100, self.happiness + 5)
        self.weight += 2
        self.check_game_over()
        self.check_growth()

    def sleep(self):
        print(f"{self.name}は眠りにつきました")
        print("ぐーぐー…")
        self.age += 0
        self.hunger = max(0, self.hunger - 1)
        self.happiness = min(100, self.happiness + 1)
        self.weight += 0
        self.check_game_over()
        self.check_growth()

    def play(self):
        print(f"{self.name}は遊びました")
        print("わいわい!!")
        self.age += 0
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(100, self.happiness + 1)
        self.weight = max(0, self.weight - 1)
        self.check_game_over()
        self.check_growth()

    def update_time(self, hour):
        print(f"{hour}時間経過しました")
        self.age += 1 * hour
        self.hunger = max(0, self.hunger - (2 * hour))
        self.happiness = max(0, self.happiness - (3 * hour))
        self.weight += 1 * hour
        self.check_game_over()
        self.check_growth()

    def check_game_over(self):
        if self.hunger <= 0 or self.happiness <= 0:
            print(f"{self.name}は餓死してしまいました。ゲームオーバー")
            self.__init__(self.name)

    # 進化のチェック
    def check_growth(self):
        current_name = self.name
        new_name = self.name

        if self.age >= 60 and self.weight >= 50 and self.name == "ますくっち" and self.stage == "senior":
            new_name = "おやじっち"
            self.__class__ = Adult # Adultクラスを参照する

        elif self.age >= 18 and self.stage == "adult":
            if self.hunger >= 80 and self.happiness >= 80:
                new_name = "まめっち"
                self.stage = "senior"
            elif self.hunger >= 70 and self.happiness >= 70:
                new_name = "ぎんじろっち"
                self.stage = "senior"
            elif self.hunger >= 65 and self.happiness >= 65:
                new_name = "くちぱっち"
                self.stage = "senior"
            elif self.hunger >= 60 and self.happiness >= 60:
                new_name = "にょろっち"
                self.stage = "senior"
            elif self.hunger >= 55 and self.happiness >= 55:
                new_name = "ますくっち"
                self.stage = "senior"
            elif self.hunger >= 50 and self.happiness >= 50 and self.name == "くちたまっち":
                new_name = "たらこっち"
                self.stage = "senior"

        elif self.age >= 10 and self.stage == "child":
            if self.hunger >= 30 and self.happiness >= 30:
                new_name = "たまっち"
                self.stage = "adult"
            else:
                new_name = "くちたまっち"
                self.stage = "adult"

        elif self.age >= 5 and self.hunger >= 10 and self.happiness >= 10 and self.stage == "baby":
            new_name = "まるっち"
            self.stage = "child"

        elif self.age >= 2 and self.stage == "egg":
            new_name = "べびっち"
            self.__class__ = Baby # Babyクラスを参照する
            self.stage = "baby"

        elif self.age >= 0 and self.stage == "start":
            new_name = "たまご"
            self.stage = "egg"

        if new_name == "たまご":
            self.name = new_name
            print("ようこそたまごっちゲームへ！！\nたまごを孵化させるために、まずは時間経過のボタンを押してみてね😊")

        elif current_name != new_name:
            self.name = new_name
            print(f"おめでとう！{self.name}に進化しました！")
            play_music()  # 進化時に音楽を再生

    def __str__(self):
        self.status = textwrap.dedent(
            f"""名前:{self.name}\n年齢:{self.age}\n満腹度:{self.hunger}\n幸福度:{self.happiness}\n体重:{self.weight}"""
        )
        return self.status

# Tamagotchiクラスを継承
class Baby(Tamagotchi):
    def cry(self):
        print(f"{self.name}が泣いているよ")
        print("おんぎゃー!!!!")
        self.age += 0
        self.hunger -= 1
        self.happiness -= 1
        self.weight += 0

# Tamagotchiクラスをオーバーライド
class Adult(Tamagotchi):
    def __init__(self, name):
        self.name = name
        self.age = 18
        self.hunger = 5
        self.happiness = 5
        self.weight = 50
        print(f"大人になり{self.name}になりました")

    def drink_alcohol(self):
        print(f"{self.name}は飲んだくれています")
        print("酒持ってこーい!")
        self.age += 0
        self.hunger += 3
        self.happiness += 3
        self.weight += 3

def main():
    tama = Tamagotchi("たまごっち")

    print(tama)

    # ユーザーコマンド入力を追加
    while True:
        print("■コマンド一覧")
        print("1. ごはんをあげる")
        print("2. 寝かせる")
        print("3. 遊ぶ")
        print("4. 時間を進める")
        print("5. ステータスを確認")
        print("6. 終了")

        choice = input("何をしますか？（1-6から選んで数字を入力してください）: ")

        if choice == "1":
            tama.eat()
        elif choice == "2":
            tama.sleep()
        elif choice == "3":
            tama.play()
        elif choice == "4":
            hour = int(input("何時間経過させますか？（時間を数字で入力してください）： "))
            tama.update_time(hour)
        elif choice == "5":
            print(tama)
        elif choice == "6":
            break
        else:
            print("無効な選択です。もう一度お試しください。")
        print("\n")
        print("-" * 50)


def gui():
    sg.theme("Dark Blue15")

    # GUI layout を定義します
    layout = [
        # メイン画面と進化図の画面をタブで作成
        [sg.TabGroup([[sg.Tab("メイン",[[sg.Image(
                                    filename=os.path.join("img", "たまごっち.png"),
                                    key="-IMAGE-",)]],),
                    sg.Tab("進化図",[[sg.Image(
                                    filename=os.path.join("img", "進化図.png"),
                                    )]],),]])],
        [sg.Button("食べる", size=(8, 1)), sg.Button("眠る", size=(8, 1)), sg.Button("遊ぶ", size=(8, 1)),sg.Text(" "),
         sg.Text("時間経過:", size=(8, 1)),
         sg.Input(default_text="1", size=(5, 1), key="-HOURS-"),
         sg.Button("時間経過"),
         # 隠しボタンを追加
        ],
        [sg.Button("泣く", size=(8, 1), key="-CRY-", visible=False), sg.Button("飲んだくれる", size=(8, 1), key="-DRINK-", visible=False),],
        [
            sg.Text(
                "たまごっちゲームへようこそ！！\n"
                "初代たまごっちのキャラクターは全部で11種類\n"
                "「おやじっち」を目指して頑張って育ててあげよう！\n"
                "まずは時間経過のボタンを押してみてね😊", size=(40, 5), key="-STATUS-", font=("Helvetica", 20), text_color="red"
            ),
        ],
        [sg.Output(size=(95, 10))],
    ]

    # ウィンドウを作成します
    window = sg.Window("たまごっち", layout)

    # インスタンスを作成します
    tama = Tamagotchi("たまごっち")

    while True:
        # イベントを読み込みます
        event, values = window.read()

        # 閉じるボタンが押された場合、またはウィンドウが閉じられた場合、終了します
        if event == sg.WINDOW_CLOSED or event == "閉じる":
            break

        # 各ボタンに応じて、対応するたまごっちのアクションを実行します
        elif event == "食べる":
            tama.eat()
        elif event == "眠る":
            tama.sleep()
        elif event == "遊ぶ":
            tama.play()
        elif event == "時間経過":
            hour = int(values["-HOURS-"])
            tama.update_time(hour)
        elif event == "-CRY-" and isinstance(tama, Baby):
            tama.cry()
        elif event == "-DRINK-" and isinstance(tama, Adult):
            tama.drink_alcohol()

        # ステータスを更新します
        window["-STATUS-"].update(str(tama))

        # たまごっちの名前と画像を更新します
        window["-IMAGE-"].update(filename=os.path.join("img", f"{tama.name}.png"))

        # 隠しボタンの可視化
        window['-CRY-'].update(visible=isinstance(tama, Baby))
        window['-DRINK-'].update(visible=isinstance(tama, Adult))

    # ウィンドウを閉じます
    window.close()


# ユーザーがコマンドラインで "python3 Tamagotchi.py console" と入力するとテキストベースのインタラクションが起動します
# ユーザーが "python3 Tamagotchi.py gui" と入力すると GUI ベースのインタラクションが起動します
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "console":
        main()
    elif len(sys.argv) > 1 and sys.argv[1] == "gui":
        gui()
    else:
        print("コマンドは次のいずれかを入力してください: python3 Tamagotchi.py console | python3 Tamagotchi.py gui")
