class LineServiceBasic:
    def __init__(self, filepath='odyssey.txt'):
        self.filepath = filepath
        try:
            f = open(self.filepath, "r")
            self.lines = f.readlines()
            f.close()
        except OSError:
            self.lines = []

    def get_lines(self):
        return self.lines

    def get_line(self, line_id):
        return self.lines[line_id]



