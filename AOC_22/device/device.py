from collections import defaultdict
from typing import List

from core import DefaultLogger

log = DefaultLogger().get_log()

class dirNode:
    def __init__(self):
        self.dirs = []
        self.files = []
        self.size = 0


    def add_dir(self, dir):
        self.dirs.append(dir)

    def add_file(self, file):
        self.files.append(file)
        self.size += file[0]

    def add_size(self, size: int):
        self.size += size

    def set_size(self, size: int):
        self.size = size

class fileSystem:
    def __init__(self):
        self.tree = defaultdict(dirNode)
        self.cur_dir = "/"

    def add_file(self, file):
        log.info(f"Updating files for {self.cur_dir}")
        self.tree[self.cur_dir].add_file(file)

    def add_dir(self, dir):
        log.info(f"Updating dirs for {self.cur_dir}")
        self.tree[self.cur_dir].add_dir(dir)

    def set_dir(self, dir):
        log.info(f"setting dir to {dir}")
        self.cur_dir = dir

    def _traverse_director_files(self, dir_name, size):
        node = self.tree[dir_name]
        dirs = node.dirs
        log.info(node)
        log.warning(f"{node.dirs}")
        if not dirs:
            return node.size
        else:
            for dir_name in dirs:
               size += self._traverse_director_files(dir_name, size)

        return size


    def directory_file_sizes(self):
        for dir_name, node in self.tree.items():
            node.set_size(self._traverse_director_files(dir_name, node.size))


    def get_files_by_size(self, limit=100000):
        self.directory_file_sizes()
        for node in self.tree.values():
            print(node.size)
        return sum([node.size for node in self.tree.values() if node.size <= limit])


class Device:
    file_system = fileSystem()

    def __init__(self, data_stream: str = None, terminal_input: List[str] = None):
        self.data_stream = data_stream
        self.terminal_input = terminal_input

    def _command(self, line: str):
        return line[1::].strip() if line[0] == "$" else None

    def _dir(self, line: str):
        return line[3::].strip() if line[:3] == "dir" else None

    def _file(self, line: str):
        file_size, file_name = line.split(" ")
        return int(file_size), file_name.strip()

    def file_info(self, line: str):
        if dir_name := self._dir(line):
            self.file_system.add_dir(dir_name)
        else:
            self.file_system.add_file(self._file(line))

    def command(self, line: str) -> bool:
        cmd_map = {
            "cd": lambda x: self.file_system.set_dir(x),
            "ls": lambda x: log.info(f"Listing directory files...")
        }

        if cmd_info := self._command(line):
            cmd = cmd_info.split(" ")
            cmd_map[cmd[0]](cmd[-1])

            return True

        return False

    def system_info(self):
        for line in self.terminal_input:
            log.info(line)
            if not self.command(line):
                self.file_info(line)

    def _find_marker(self, n):
        for i in range(len(self.data_stream) - (n-1)):
            if len(set([c for c in self.data_stream[i:i + n]])) == n:
                return i + n

    def start_of_packet_marker(self) -> int:
        return self._find_marker(14)

    def start_of_message_marker(self) -> int:
        return self._find_marker(4)

    def parse_terminal_screen(self):
        self.system_info()
        log.info(self.file_system.get_files_by_size())


