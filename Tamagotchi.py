import textwrap


class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.hunger = 5
        self.happiness = 5
        self.weight = 1
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
            exit(0)

    def check_growth(self):
        current_name = self.name
        new_name = self.name

        if self.age >= 60 and self.weight >= 50:
            new_name = "おやじっち"
        elif self.age >= 18 and self.hunger >= 60 and self.happiness >= 60:
            new_name = "まめっち"
        elif self.age >= 4 and self.hunger >= 10 and self.happiness >= 10:
            if self.hunger >= 30 and self.happiness >= 30:
                new_name = "たまっち"
            else:
                new_name = "くちたっち"
        elif self.age >= 2 and self.hunger >= 1 and self.happiness >= 1:
            new_name = "まるっち"

        if current_name != new_name:
            self.name = new_name
            print(f"{self.name}に進化しました")

    def __str__(self):
        self.status = textwrap.dedent(
            f"""名前:{self.name}\n年齢:{self.age}\n満腹度:{self.hunger}\n幸福度:{self.happiness}\n体重:{self.weight}\n{'-' * 50}
    """
        )
        return self.status


class Baby(Tamagotchi):
    # Tamagotchiクラスを継承
    def cry(self):
        print(f"{self.name}が泣いているよ")
        print("おんぎゃー!!!!")
        self.age += 0
        self.hunger -= 1
        self.happiness -= 1
        self.weight += 0


class Adult(Tamagotchi):
    # オーバーライド
    def __init__(self, name):
        self.name = name
        self.age = 18
        self.hunger = 5
        self.happiness = 5
        self.weight = 50
        self.drunkness = 0
        print(f"大人になり{self.name}になりました")

    def drink_alchol(self):
        print(f"{self.name}は飲んだくれています")
        print("酒持ってこーい!")
        self.age += 0
        self.hunger += 3
        self.happiness += 3
        self.weight += 3
        self.drunkness += 20

    def __str__(self):
        self.status = textwrap.dedent(
            f"""名前:{self.name}\n年齢:{self.age}\n満腹度:{self.hunger}\n幸福度:{self.happiness}\n体重:{self.weight}\n酔度{self.drunkness}\n{'-' * 50}
    """
        )
        return self.status


def main():
    tama = Tamagotchi("たまごっち")
    print(tama)

    # ユーザーインタラクションを追加
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


if __name__ == "__main__":
    main()
