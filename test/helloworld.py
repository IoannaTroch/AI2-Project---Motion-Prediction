from ai4animation import AI4Animation


class Program:
    def __init__(self, variable):
        self.Variable = variable

    def Start(self):
        print(self.Variable)

    def Update(self):
        return

    def Draw(self):
        return

    def GUI(self):
        return


if __name__ == "__main__":
    AI4Animation(Program("Hello World"), mode=AI4Animation.Mode.STANDALONE)