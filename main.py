import random

from hands_resource import hands_asset
from score import Score


def input_user_hand_number():
    """ユーザーの手を入力させる関数"""

    print("あなたの手をアルファベットで入力してください。\n")
    explanation = [f'{key}: {value["name"]}\n' for key, value in hands_asset.items()]
    while True:
        user_hand = input(f'じゃんけん！\n{"".join(explanation)}').lower()
        all_hands = list(hands_asset.keys())
        if user_hand not in all_hands:
            print(f'{" ".join(all_hands)} のいずれかを入力してください。\n')
            continue
        return user_hand


def janken():
    """じゃんけんを実行する関数"""

    score = Score()
    while True:
        # 手を選択
        user_hand = input_user_hand_number()

        # コンピュータの手を選択
        cpu_hand = random.choice(list(hands_asset.keys()))

        # 手を表示
        print(f'あなた: {hands_asset[user_hand]["art"]}')
        print(f'コンピュータ: {hands_asset[cpu_hand]["art"]}')

        # 勝敗を表示
        result = judge(user_hand, cpu_hand, score)
        print(f"{result}\n")

        replay = input('もう一度勝負しますか (勝負する場合は y ): ').lower()
        if replay != 'y':
            score.show()
            print('またね！')
            break


def judge(user, cpu, score):
    """
    じゃんけんの勝敗を判定する関数
    :param user: ユーザーの手
    :param cpu: コンピュータの手
    :param score: 勝敗の記録
    """

    if user == cpu:
        score.increment_draw()
        return "あいこ"
    elif any([user == 'g' and cpu == 'c', user == 'c' and cpu == 'p', user == 'p' and cpu == 'g']):
        score.increment_win()
        return "勝ち！"
    else:
        score.increment_loss()
        return "負け"


# じゃんけんを実行
if __name__ == '__main__':
    janken()
