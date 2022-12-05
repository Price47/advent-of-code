from collections import defaultdict

from core import DefaultLogger, AOCBase


log = DefaultLogger().get_log()


class day(AOCBase):
    def __init__(self, data=None):
        self.data = data or self.read_input()

    def parse_input(self):
        input_commands_index = 0

        stacks = defaultdict(list)
        for idx, row in enumerate(self.data):
            stack = 0
            if not row:
                input_commands_index = idx + 1
                break
            for i in range(0, len(row), 4):
                crate = "".join(row[i:i + 4]).strip(" ").replace("[", "").replace("]", "")
                if not crate.isdigit() and crate:
                    stacks[stack+1].append(crate)
                stack += 1

        commands = [
            [int(c) for c in d.replace("move", "").replace("to", "").replace("from", "").split(" ") if c]
            for d in self.data[input_commands_index::]
        ]

        return {k: [item for item in v[::-1]] for k,v in stacks.items()}, commands

    def list_top_crates(self, stacks):
        return_str = ""

        for k in range(len(stacks.keys())):
            try:
                return_str += stacks[k + 1].pop()
            except IndexError:
                continue

        return return_str

    def crate_mover_9000_ordering(self):
        stacks, commands = self.parse_input()

        for command in commands:
            move_boxes, from_stack, to_stack = command
            for _ in range(move_boxes):
                crate = stacks[from_stack].pop()
                stacks[to_stack].append(crate)

        log.info(f"CrateMover 9000 stack order: {self.list_top_crates(stacks)}")

    def crate_mover_9001_ordering(self):
        stacks, commands = self.parse_input()

        for command in commands:
            move_boxes, from_stack, to_stack = command
            crates = stacks[from_stack][-move_boxes::]
            stacks[from_stack] = stacks[from_stack][0:-move_boxes]
            stacks[to_stack].extend(crates)

        log.info(f"CrateMover 9001 stack order: {self.list_top_crates(stacks)}")

    def run(self):
        self.crate_mover_9000_ordering()
        self.crate_mover_9001_ordering()
