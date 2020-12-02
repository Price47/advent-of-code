import os
from core import DefaultLogger

log = DefaultLogger.get_log()

class PasswordScrubber:

    def _parse_policy(self, p):
        limits, value = p.split(' ')
        lower_limit, upper_limit = limits.split('-')

        return [lower_limit, upper_limit, value]

    def _parse_input(self, s):
        policy, password = s.split(':')
        password_policies = self._parse_policy(policy)

        return [password.strip()] + password_policies


    def read_input(self):
        with open(f'{os.getcwd()}/day_2/input.txt') as f:
            content = f.read()
            passwords = content.splitlines()

        return passwords

    def check_sled_company_passwords(self, passwords):
        """
        Check password policies (password, upper_limit, lower_limit, value) that are
        invalid

        :param passwords:
        :return:
        """
        sled_company_policy = lambda p, l, u, v: int(l) <= p.count(v) <= int(u)
        password_policies = [self._parse_input(p) for p in passwords]

        valid_passwords = [(p, l, u, v) for (p, l, u, v) in password_policies if sled_company_policy(p, l, u, v)]

        return valid_passwords

    def _toboggan_policy_check(self, password, index_1, index_2, value):
        val_1 = password[int(index_1) - 1]
        val_2 = password[int(index_2) - 1]

        check_vals = [
            lambda v1, v2: v1 != v2,
            lambda v1, v2: v1 == value or v2 == value
        ]

        return all([check_val(val_1, val_2) for check_val in check_vals])

    def check_toboggan_company_passwords(self, passwords):
        """
        Check password policies (password, upper_limit, lower_limit, value) that are
        invalid

        :param passwords:
        :return:
        """
        password_policies = [self._parse_input(p) for p in passwords]

        valid_passwords = [
            (p, i1, i2, v) for (p, i1, i2, v) in password_policies if self._toboggan_policy_check(p, i1, i2, v)
        ]

        return valid_passwords


    def check_valid_passwords(self):
        passwords = self.read_input()
        valid_sled_passwords = self.check_sled_company_passwords((passwords))
        valid_tobbogan_passwords = self.check_toboggan_company_passwords(passwords)

        log.info(f'{len(valid_sled_passwords)} valid sled co passwords')
        log.info(f'{len(valid_tobbogan_passwords)} valid toboggan co passwords')

