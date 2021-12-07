class Fish:

    def __init__(self, timer=8):
        self.timer = timer

    def spawn(self):
        pass

    def age(self):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            return True

        return False

    def __repr__(self):
        return f"Fish with age {self.timer}"