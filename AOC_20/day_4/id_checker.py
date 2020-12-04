from core import DefaultLogger, AOCBase
import re


log = DefaultLogger.get_log()


class IdChecker(AOCBase):
    """
    https://adventofcode.com/2020/day/4

    """

    def reread_data(self):
        """
        messy and not that pretty but gets the job done
        :return:
        """
        reorganized_data = []
        data = self.read_input()
        data1 = []
        for d in data:
            if d == '':
                data1.append('\n ')
            else:
                data1.append(d)

        new_input = ' '.join(data1).splitlines()
        input_val_dicts = [i.split(' ') for i in new_input]
        for i in input_val_dicts:
            vals = {}
            for pair in i:
                if pair:
                    key, value = pair.split(':')
                    vals[key] = value

            reorganized_data.append(vals)

        return reorganized_data

    def _valid_height(self, h):
        if re.match(r'\d+cm|\d+in', h):
            if 'cm' in h:
                val = h.replace('cm', '')
                return 150 <= int(val) <= 193
            if 'in' in h:
                val = h.replace('in', '')
                return 59 <= int(val) <= 76

    def validate(self, i):
        """
            byr (Birth Year) - four digits; at least 1920 and at most 2002.
            iyr (Issue Year) - four digits; at least 2010 and at most 2020.
            eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
            hgt (Height) - a number followed by either cm or in:
                            If cm, the number must be at least 150 and at most 193.
                            If in, the number must be at least 59 and at most 76.
            hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
            ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
            pid (Passport ID) - a nine-digit number, including leading zeroes.
            cid (Country ID) - ignored, missing or not.
        """

        validation_fns = [
            lambda i: len(i.get('byr', 0)) == 4 and 1920 <= int(i.get('byr'), 0) <= 2002,
            lambda i: len(i.get('iyr', '')) == 4 and 2010 <= int(i.get('iyr', 0)) <= 2020,
            lambda i: len(i.get('eyr', '')) == 4 and 2020 <= int(i.get('eyr', 0)) <= 2030,
            lambda i: self._valid_height(i.get('hgt')),
            lambda i: re.match(r'#[a-f0-9]{6}', i.get('hcl')),
            lambda i: i.get('ecl') in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
            lambda i: re.match(r'^[0-9]{9}$', i.get('pid'))
        ]

        return all(valid_fn(i) for valid_fn in validation_fns)

    def valid_ids(self, all_ids):
        required_keys =  ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        validish_ids = [i for i in all_ids if all(elem in i.keys()  for elem in required_keys)]
        validated_ids = [validish_id for validish_id in validish_ids if self.validate(validish_id)]

        return validated_ids

    def main(self):
        data = self.reread_data()
        valid_ids = self.valid_ids(data)

        log.info(f'{len(valid_ids)} valid ids found in batch')
