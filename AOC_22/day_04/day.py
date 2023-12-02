from core import DefaultLogger, AOCBase


log = DefaultLogger().get_log()


class day(AOCBase):
    def _parse_sections(self):
        return [
            [
                [int(str_val) for str_val in x.split("-")] for x in d.split(",")
            ] for d in self.data
        ]

    def sections_contained(self, elf_sections):
        first_elf_sections, second_elf_sections = elf_sections

        return (
            ( first_elf_sections[0] >= second_elf_sections[0] and first_elf_sections[1] <= second_elf_sections[1])
            or
            ( second_elf_sections[0] >= first_elf_sections[0] and second_elf_sections[1] <= first_elf_sections[1])
        )

    def sections_overlap(self, elf_sections):
        first_elf_start, first_elf_end = elf_sections[0]
        second_elf_start, second_elf_end = elf_sections[1]

        return len(set(
            [i for i in range(first_elf_start, first_elf_end + 1)]
        ).intersection(
            [i for i in range(second_elf_start, second_elf_end + 1)]
        )) > 0

    def check_elf_pair_sections_fully_contained(self):
        log.info(
            f"{sum(1 for elf_sections in self._parse_sections() if self.sections_contained(elf_sections))}"
            f" sections are fully contained"
        )

    def check_elf_pair_sections_overlap(self):
        log.info(
            f"{sum(1 for elf_sections in self._parse_sections() if self.sections_overlap(elf_sections))}"
            f" sections are fully contained"
        )


    def run(self):
        self.check_elf_pair_sections_fully_contained()
        self.check_elf_pair_sections_overlap()