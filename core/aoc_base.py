import sys

# Built-in namespace
import builtins

# Extended subclass
class AOCStr(str):
    def strip_split(self, split_val=","):
        if self:
            return self.strip().split(split_val)
        else:
            return ''


class AOCBase:
    def __init__(self, data=None):
        self.data = data or self.read_input()

    def read_input(self, type_cast=None):
        file_path = sys.argv[0]
        dir_root = '/'.join(file_path.split('/')[:-1])

        with open(f'{dir_root}/input.txt') as f:
            content = f.read()
            lines = content.splitlines()

        if type_cast:
            lines = [type_cast(line) for line in lines]

        return lines

    def highlight(self, s, il, ih=None):
        highlighter = "\x1b[31;1m"
        reset = "\x1b[0m"

        if not ih:
            ih = il

        s = f'{s[:il]}{highlighter}{s[il:ih+1]}{reset}{s[ih+1:]}'
        print(s)

    def split_indices(self, d):
        return [i for i in range(len(d)) if d[i] == '']

    def is_int(self, char, return_cast=int):
        try:
            return return_cast(int(char))
        except ValueError:
            pass


if __name__ == '__main__':
    AOCBase().read_input()