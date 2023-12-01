from core import DefaultLogger, AOCBase
from AOC_22.device import Device

log = DefaultLogger().get_log()



class day(AOCBase):
    def __init__(self, data=None):
        self.data = data or self.read_input()

    def run(self):
        d = Device(data_stream=self.data[0])

        log.info(f"Start of packet marker: {d.start_of_packet_marker()}")
        log.info(f"Start of message marker: {d.start_of_message_marker()}")