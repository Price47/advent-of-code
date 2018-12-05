from input import CLAIMS
import re

def _read_claim(claim):
    claim = claim.replace(' ','')
    _, id, offset, area  = re.split(r'#|@|:', claim)
    offset = offset.split(',')
    area = area.split('x')
    return id, int(offset[0]), int(offset[1]), int(area[0]), int(area[1])

def _get_fabric_overlaps(claims):
    fabric_coordinates = {}
    for claim in claims:
        claimId, offsetX, offsetY, areaX, areaY = _read_claim(claim)
        for x in range(offsetX, areaX + offsetX):
            for y in range(offsetY, areaY + offsetY):
                try:
                    fabric_coordinates[x, y].append(claimId)
                except KeyError:
                    fabric_coordinates[x, y] = [claimId]

    return fabric_coordinates

def day_3_part_1(claims):
    fabric_coordinates = _get_fabric_overlaps(claims)
    overlaps = [claims for coordinates, claims in fabric_coordinates.items() if len(claims) > 1]
    return len(overlaps)

def day_3_part_2(claims):
    claimIds = set(re.findall(r'(?<=#)\d+', ''.join(claims)))
    fabric_overlaps = _get_fabric_overlaps(claims)
    overlapping_claims = [claims for coordinates, claims in fabric_overlaps.items() if len(claims) > 1]
    overlapping_claim_ids = set([claim for claims in overlapping_claims for claim in claims])
    non_overlapping_claim_ids = claimIds - overlapping_claim_ids
    if len(non_overlapping_claim_ids) == 1:
        return non_overlapping_claim_ids.pop()
    else:
        raise Exception("Multiple claim ids found")


def main():
    print("Overlapping Fabric (in square inches): {} ".format(day_3_part_1(CLAIMS)))
    print("None overlapping claim id: {}".format(day_3_part_2(CLAIMS)))

if __name__ == '__main__':
    main()
