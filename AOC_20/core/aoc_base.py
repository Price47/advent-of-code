import sys


class AOCBase:

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

if __name__ == '__main__':
    AOCBase().read_input()