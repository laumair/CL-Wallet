class Settings:
    def __init__(self, account):
        self.account = account
        self.keep_alive = False

    def initialize(self):
        self.keep_alive = True