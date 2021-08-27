from Region_proposal import *
from Tag_decoder import *
from tqdm import tqdm

def takeSecond(elem):
    length = len(elem)
    num = elem[5:length-4]
    return int(num)

if __name__ == "__main__":
    # img_set = 'image_set'
    img_set = 'E:/20210818-5fps-10min'
    img_list = os.listdir(img_set)
    img_list.sort(key=takeSecond)
    total_frames = len(img_list)
    region_proposal = Region_proposal()
    tag_decoder = Tag_decoder(total_frames)
    for i in tqdm(range(total_frames)):
        img_name = img_list[i].split('.')[0]
        # print(img_name)
        img_file = img_set + "/" + img_name + ".bmp"
        img = cv2.imread(img_file)
        # The input image is 3 channel.
        regions = region_proposal.img_process(img)
        # tag_decoder.run(regions, img, i, True)
        tag_decoder.run(regions, img, i)
    tag_decoder.save_result_dict()
