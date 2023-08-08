import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hands_aa = {0: rock, 1: scissors, 2: paper}


def janken():
    """じゃんけんを実行する関数"""
    while True:
        hands = {0: 'グー', 1: 'チョキ', 2: 'パー'}

        # 手を選択
        while True:
            user_hand = input(f'じゃんけん！ {str(hands)}: ')
            try:
                user_hand = int(user_hand)
                if user_hand not in hands.keys():
                    raise ValueError
                break
            except ValueError:
                print('0, 1, 2のいずれかを入力してください。')

        # コンピュータの手を選択
        cpu_hand = random.choice(list(hands.keys()))

        # 手を表示
        print(f'あなた: {hands_aa[user_hand]}')
        print(f'コンピュータ: {hands_aa[cpu_hand]}')

        # 勝敗を表示
        result = judge(user_hand, cpu_hand)
        print(f"{result}\n")

        replay = input('もう一度勝負しますか (勝負する場合は y ): ').lower()
        if replay != 'y':
            print('またね！')
            break


def judge(user, cpu):
    """勝敗を判定する関数"""
    if user == cpu:
        return "あいこ"
    elif user == 0 and cpu == 1:
        return "勝ち"
    elif user == 1 and cpu == 2:
        return "勝ち"
    elif user == 2 and cpu == 0:
        return "勝ち"
    else:
        return "負け"


# じゃんけんを実行
if __name__ == '__main__':
    janken()
