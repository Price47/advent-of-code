from core import DefaultLogger, AOCBase


log = DefaultLogger().get_log()


class Diagnostic(AOCBase):

    def column_bits(self, data, col):
        digits = [row[col] for row in data]
        ones = sum([1 for i in digits if i == '1'])
        zeros = len(digits) - ones

        return ones, zeros

    def most_common_bit(self, data, col):
        ones, zeros = self.column_bits(data, col)
        return "1" if ones > zeros or ones == zeros else "0"

    def least_common_bit(self, data, col):
        ones, zeros = self.column_bits(data, col)
        return "0" if zeros < ones or ones == zeros else "1"

    def gamma(self, data):
        data = data or self.read_input()
        gamma_str = "".join([self.most_common_bit(data, i) for i in range(len(data[0]))])

        return gamma_str

    def epsilon(self, gamma):
        epsilon_str = "".join([str(abs(int(c)-1)) for c in list(gamma)])
        return epsilon_str

    def get_power_consumption(self, data):
        gama = self.gamma(data)
        epsilon = self.epsilon(gama)

        return (int(gama, 2) * int(epsilon, 2))

    def get_gas_rating(self, fn, data, i=0):
        significant_bit = fn(data, i)
        new_data = [d for d in data if d[i] == significant_bit]
        if len(new_data) == 1:
            return new_data[0]
        else:
            return self.get_gas_rating(fn, new_data, i + 1)

    def get_life_support_rating(self, data):
        O2 = self.get_gas_rating(self.most_common_bit, data)
        C02 = self.get_gas_rating(self.least_common_bit, data)

        return int(O2, 2) * int(C02, 2)

    def run(self, data=None):
        data = data or self.read_input()

        power_consumption = self.get_power_consumption(data)
        log.info(f"Power Consumption {power_consumption}")
        life_support_rating = self.get_life_support_rating(data)
        log.info(f"Life Support Rating {life_support_rating}")






