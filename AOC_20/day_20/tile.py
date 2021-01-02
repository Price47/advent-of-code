class Tile:

    def __init__(self, t):
        self.tile_id = t[0].replace(':', '')
        self.tile = t[1:]

    def top(self):
        return self.tile[0]

    def right(self):
        return ''.join([row[len(row) - 1] for row in self.tile])

    def bottom(self):
        return self.tile[len(self.tile) - 1]

    def left(self):
        return ''.join([row[0] for row in self.tile])

    def flip_horizontal(self):
        max_row = len(self.tile) - 1
        for i in range(max_row // 2):
            x = self.tile[max_row - i]
            self.tile[max_row - i] = self.tile[i]
            self.tile[i] = x

    def flip_vertical(self):
        for i in range(len(self.tile) - 1):
            self.tile[i] = self.tile[i][::-1]

    def rotate(self):
        rotated_list = list(zip(*self.tile[::-1]))
        self.tile = ["".join(r) for r in rotated_list]

    def get_tile(self):
        return self.tile

    def equals(self, t2):
        for l1, fn in [('top', self.top), ('right', self.right), ('bottom', self.bottom), ('left', self.left)]:
            for l2, fn2 in [('top', t2.top), ('right', t2.right), ('bottom', t2.bottom), ('left', t2.left)]:
                if fn() == fn2():
                    if l1 == 'right':
                        return [self, t2]
                    if l1 == 'left':
                        return [t2, self]
                    if l1 == 'top':
                        return [[t2], [self]]
                    if l1 == 'bottom':
                        return [[self], [t2]]

        return False

    def __repr__(self):
        return self.tile_id

    def __str__(self):
        tile = "\n".join(self.tile)
        return f'\n{self.tile_id}\n{tile}'

    def __eq__(self, t2):
        return self.equals(t2)