from hands import rock, paper, scissors


class Referee:
    """勝敗を判定するクラス"""

    # 勝敗の組み合わせ
    winning_combinations = {
        # 勝ち手: 負け手
        rock.name: scissors.name,
        scissors.name: paper.name,
        paper.name: rock.name
    }

    def __init__(self):
        self.game_decided = False
        self.judgment_result = ""

    @staticmethod
    def _is_user_win(user_hand_name, computer_hand_name):
        return Referee.winning_combinations[user_hand_name] == computer_hand_name

    def evaluate_judge(self, user, cpu):
        """
        じゃんけんの勝敗を判定する
        :param user: ユーザーのインスタンス
        :param cpu: コンピュータのインスタンス
        :return: 勝敗の結果
        """

        if user.hand == cpu.hand:
            user.score.increment_draw()
            self.game_decided = False
            self.judgment_result = "あいこ"
        elif Referee._is_user_win(user.hand.name, cpu.hand.name):
            user.score.increment_win()
            self.game_decided = True
            self.judgment_result = "勝ち！"
        else:
            user.score.increment_lose()
            self.game_decided = True
            self.judgment_result = "負け"
