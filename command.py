class Command:
    def __init__(self, args):
        self.args = args

    def parse(self):
        if self.args.install is True:
            self.install()

    def install(self):
        # do with sally