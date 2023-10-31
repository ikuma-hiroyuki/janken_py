class Score:
    def __init__(self):
        self.win = 0
        self.draw = 0
        self.lose = 0

    def increment_win(self):
        self.win += 1

    def increment_loss(self):
        self.lose += 1

    def increment_draw(self):
        self.draw += 1

    def show(self):
        print(f'あなたの成績は {self.win}勝 {self.lose}敗 {self.draw}分 でした')
