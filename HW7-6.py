class Logger:
    def __init__(self, file):
        self.file = file
        self.file1 = open(file, 'a')

    def write_log(self, log):
        self.file1.write(log)
