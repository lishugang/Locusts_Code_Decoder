from Region_proposal import *
from Tag_decoder import *


if __name__ == "__main__":
    tag_decoder = Tag_decoder(1)
    region_proposal = Region_proposal()
    img_name = '202108181.bmp'
    print(img_name)
    img = cv2.imread(img_name)
    # The input image is 3 channel.
    regions = region_proposal.img_process(img)
    # tag_decoder.run(regions, img, i, True)
    tag_decoder.run(regions, img, 0, True)