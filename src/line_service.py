import pylru

from out_of_range_exception import OutOfRangeException


class LineService:
    def __init__(self, filepath='odyssey.txt', cachesize=100000):
        self.filepath = filepath
        self.index = pylru.lrucache(cachesize)
        self.index_file()

    def get_line_slow(self, line_id):
        fp = open(self.filepath, "r")

        line = fp.readline()

        if line_id == 0:
            return [0, line]

        line_counter = 0
        pos_counter = len(line)

        while line_counter < line_id and line:
            line = fp.readline()
            line_counter += 1
            pos_counter += len(line)

        fp.close()

        if line_counter == line_id:
            return [pos_counter, line]
        else:
            raise OutOfRangeException("Line %d is out of range" % line_id)

    def get_line_fast(self, pos):
        f = open(self.filepath, "r")
        f.seek(pos, 0)
        line = f.readline()
        f.close()
        return line

    def index_file(self):
        fp = open(self.filepath, "r")

        line = fp.readline()
        pos_counter = len(line)
        line_id = 0
        self.index[line_id] = 0

        while line:
            line_id += 1
            self.index[line_id] = pos_counter
            line = fp.readline()
            pos_counter += len(line)

        fp.close()

    def get_line(self, line_id):
        if line_id not in self.index:
            [pos, line] = self.get_line_slow(line_id)
            self.index[line_id] = pos
            return line

        return self.get_line_fast(self.index[line_id])



