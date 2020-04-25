from src.hdr import *
import os
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage:  python run.py [input_folder] [output_folder]")
        sys.exit()
    # Read image from file
    HDR_Filter = FakeHDR(True)
    for idir , _ , image_list in os.walk(sys.argv[1]):
        for img_fl in image_list:
            image = cv2.imread(os.path.join(idir, img_fl), -1)
            output_image = HDR_Filter.process(image)
            cv2.imwrite(os.path.join(sys.argv[2], img_fl.split('.')[0]+'_hdr_result.jpg'), 255 * output_image)

