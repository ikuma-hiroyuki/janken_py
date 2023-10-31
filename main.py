import player
from score import Score
from hands import winning_combinations


def janken():
    """じゃんけんを実行する関数"""

    score = Score()
    user = player.User()
    cpu = player.CPU()

    while True:
        # 手を選択
        user.choice_hand()
        cpu.choice_hand()

        # 手を表示
        print(f'あなた: {user.hand.art}')
        print(f'コンピュータ: {cpu.hand.art}')

        # 勝敗を表示
        result = judge(user, cpu, score)
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
    :return: 勝敗の結果
    """

    if user.hand == cpu.hand:
        score.increment_draw()
        return "あいこ"
    elif winning_combinations[user.hand.name] == cpu.hand.name:
        score.increment_win()
        return "勝ち！"
    else:
        score.increment_loss()
        return "負け"


# じゃんけんを実行
if __name__ == '__main__':
    janken()
