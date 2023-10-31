import random

from hands import rock, paper, scissors
from score import Score

# プレイヤーが出せる手
hands_asset = {
    'g': rock,
    'c': scissors,
    'p': paper
}


class Player:
    def __init__(self):
        self.hand = None  # Hand クラスのインスタンス

    def choice_hand(self):
        pass


class User(Player):
    def __init__(self):
        super().__init__()
        self.score = Score()

    def choice_hand(self):
        """
        ユーザーの手を選択するためのメソッド。
        ユーザーに手を入力してもらい、妥当な手が選択されるまでループします。
        """

        print("あなたの手をアルファベットで入力してください。\n")
        choices = "".join(f'{key}: {hand.name}\n' for key, hand in hands_asset.items())
        choice = ''
        while choice not in hands_asset:
            choice = input(f'じゃんけん！\n{choices}').lower()
            if choice not in hands_asset:
                print(f'{" ".join(hands_asset)} のいずれかを入力してください。\n')
        self.hand = hands_asset[choice]


class CPU(Player):
    def choice_hand(self):
        """ コンピュータの手をランダムに選択するためのメソッド。 """
        self.hand = random.choice(list(hands_asset.values()))
