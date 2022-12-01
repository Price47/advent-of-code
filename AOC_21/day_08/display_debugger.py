from core import DefaultLogger, AOCBase
from .display import Display

log = DefaultLogger().get_log()


class DisplayDebugger(AOCBase):

    def check_uniq_code_values(self, data):
        uniq_digit_instances = sum([Display(d, True).check_segment_wires() for d in data])
        log.info(f"Instances of unique display values {uniq_digit_instances}")

    def get_display_segments(self, data):
        summed_segments = sum([Display(d).decode_segments() for d in data])
        log.info(f"Summed Dislpay debugging output {summed_segments}")

    def run(self, data=None):
        data = data or self.read_input()
        self.check_uniq_code_values(data)
        self.get_display_segments(data)



