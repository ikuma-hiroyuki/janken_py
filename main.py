import player
from hands import winning_combinations


def play_game():
    """じゃんけんを実行する関数"""

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
        result = judge(user, cpu)
        print(f"{result}\n")

        replay = input('もう一度勝負しますか？ (勝負する場合は y ): ').lower()
        if replay != 'y':
            user.score.show()
            print('またね！')
            break


def judge(user, cpu):
    """
    じゃんけんの勝敗を判定する関数
    :param user: ユーザーのインスタンス
    :param cpu: コンピュータのインスタンス
    :return: 勝敗の結果
    """

    if user.hand == cpu.hand:
        user.score.increment_draw()
        return "あいこ"
    elif winning_combinations[user.hand.name] == cpu.hand.name:
        user.score.increment_win()
        return "勝ち！"
    else:
        user.score.increment_lose()
        return "負け"


# じゃんけんを実行
if __name__ == '__main__':
    play_game()
