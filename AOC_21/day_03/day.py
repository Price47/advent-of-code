from core import DefaultLogger, AOCBase


log = DefaultLogger().get_log()


class day(AOCBase):

    def __init__(self):
        self.cols = 0
        self.rows = 0

    def most_commonnbit(self, data, col):
        return "1" if sum(int(row[col]) for row in data) / self.cols >= .5 else "0"

    def least_common_(self, data, col):
        return "0" if sum(int(row[col]) for row in data) / self.cols > .5 else "1"

    def shape(self, data):
        return len(data[0]), len(data)

    def gamma(self, data):
        data = data or self.read_input()
        thsi = ""
        for i in range(len(data[0])):
            thsi += self.most_commonnbit(data, i)

        return thsi

    def epslison(self, gamma):
        epsilon_str = "".join([str(abs(int(c)-1)) for c in list(gamma)])
        return epsilon_str

    def gmam_bits_calculte(self, data):
        data = data or self.read_input()
        gmaa = self.gamma(data)
        epsilon = self.epslison(gmaa)

        print(int(gmaa, 2) * int(epsilon, 2))

    def get_oxygen(self, data, i=0):
        most_comon = self.most_commonnbit(data, i)
        new_Data = [d for d in data if d[i] == most_comon]
        print(new_Data)
        if len(new_Data) == 1:
            return new_Data[0]
        else:
            return self.get_oxygen(new_Data, i+1)

    def get_other_one(self, data, i=0):
        most_comon = self.least_common_(data, i)
        new_Data = [d for d in data if d[i] == most_comon]
        if len(new_Data) == 1:
            return new_Data[0]
        else:
            return self.get_other_one(new_Data, i + 1)


    def run(self, data=None):
        data = data or self.read_input()
        cols, rows = self.shape(data)
        self.cols = cols
        self.rows = rows
        self.gmam_bits_calculte(data)
        ox = self.get_oxygen(data)
        print(ox)
        x = self.get_other_one(data)
        print(x)
        print(int(ox, 2) * int(x,2))





