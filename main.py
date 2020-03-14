import sys
from PIL import Image
from io import BytesIO
from point_by_addr import get_pos
from close_toponim import find_close
from get_map import get_map
from distance import lonlat_distance

TOPONIM_TYPE = "аптека"


def main():
    addr = ' '.join(sys.argv[1:])
    p1_pos = get_pos(addr)
    toponim_info = find_close(TOPONIM_TYPE, p1_pos)

    map = get_map(p1_pos, toponim_info["pos"])  # Map show
    toponim_info['distance'] = lonlat_distance(p1_pos, toponim_info['pos'])
    Image.open(BytesIO(
        map.content)).show()

    for k, i in toponim_info.items():
        print(f"{k}: \t {i}")


if __name__ == '__main__':
    main()
