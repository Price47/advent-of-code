class Display:
    digit_segments = [
        'abcefg', #0
        'cf', #1
        'acdeg', #2
        'acdfg', #3
        'bcdf', #4
        'abdfg', #5
        'abdefg', #6
        'acf',  #7
        'abcdefg', #8
        'abcdfg' #9
    ]

    uniq_digits = {
        2: 1,
        3: 7,
        4: 4,
        7: 8
    }

    def __init__(self, display_line, check_code=False):
        self.check_code = check_code
        self.uniq_digit_instances = 0
        self.display_units = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set(),
            9: set()
        }
        self.wire_translation = {
            'a': set(),
            'b': set(),
            'c': set(),
            'd': set(),
            'e': set(),
            'f': set(),
            'g': set(),
        }

        segments, code = display_line.split(' | ')
        self.segments = segments.strip().split(' ')
        self.code = code.strip().split(' ')

    def _condensed_segments(self):
        return {list(translation)[0]: wire for wire, translation in self.wire_translation.items()}

    def _check_uniq_display_values(self):
        wires = self.code if self.check_code else self.segments
        for w in wires:
            if display_number := self.uniq_digits.get(len(w)):
                self.uniq_digit_instances += 1
                self.display_units[display_number].update(w)

    def _four_one_diff(self):
        return self.display_units[4].difference(self.display_units[1])

    def _eight_four_a_diff(self):
        return (

        )

    def _decipher_6_segment_digit(self):
        digits = [s for s in self.segments if len(s) == 6]
        for d in digits:
            d_set = set(d)
            if self.display_units[4].issubset(d_set):
                self.display_units[9] = d_set
            else:
                if (self.display_units[8] - d_set).issubset(self.display_units[1]):
                    self.display_units[6] = d_set
                    self.wire_translation['c'] = self.display_units[8] - d_set
                else:
                    self.display_units[0] = d_set
                    self.wire_translation['d'] = self.display_units[8] - d_set


    def translate_wires(self):
        self.wire_translation['a'] = self.display_units[7] - self.display_units[1]
        self._decipher_6_segment_digit()
        self.wire_translation['f'] = self.display_units[1] - self.wire_translation['c']
        self.wire_translation['e'] = self.display_units[8] - self.display_units[9]
        self.wire_translation['g'] = (
                self.display_units[8]
                - self.display_units[4]
                - self.wire_translation['a']
                - self.wire_translation['e']
        )
        self.wire_translation['b'] = (
            self.display_units[4]
                - self.wire_translation['c']
                - self.wire_translation['d']
                - self.wire_translation['f']
        )


    def find_segment_val(self, segment):
        for idx, digit in enumerate(self.digit_segments):
            if sorted(digit) == sorted(segment):
                return str(idx)

    def decipher_code(self):
        wire_translation = self._condensed_segments()
        segments = [''.join([wire_translation[s] for s in c]) for c in self.code]
        code_vals = int("".join([self.find_segment_val(segment) for segment in segments]))
        return code_vals

    def check_segment_wires(self):
        self._check_uniq_display_values()
        return self.uniq_digit_instances

    def decode_segments(self):
        self._check_uniq_display_values()
        self.translate_wires()
        return self.decipher_code()

