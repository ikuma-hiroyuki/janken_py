import player
from referee import Referee


def play_game():
    """じゃんけんを実行する関数"""

    user = player.User()
    cpu = player.CPU()
    referee = Referee()

    while True:
        print("\nじゃんけん！")

        # 決着がつくまで繰り返す
        while not referee.game_decided:
            user.choice_hand()
            cpu.choice_hand()

            # 手を表示
            print(f'あなた: {user.hand.art}')
            print(f'コンピュータ: {cpu.hand.art}')

            # 勝敗を表示
            referee.judge(user, cpu)
            print(f"{referee.judgment}\n")

        is_replay = input('再戦する場合は何か入力してエンターキーを押してください: ').lower()

        if not is_replay:
            user.score.show()
            print('またね！')
            break
        else:
            referee.game_decided = False


# じゃんけんを実行
if __name__ == '__main__':
    play_game()
