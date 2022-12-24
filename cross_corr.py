import cv2
from matplotlib import pyplot as plt
import numpy as np

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED,
           cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

# use TM_CCORR:2 or TM_CCOEFF:4

results = []
max_vals = []

images1 = []
images_ones = []
images_twos = []
images_threes = []

images1.append(cv2.imread(f"images/template1.png", 0))
for i in range(9):
    images1.append(cv2.imread(f"images/im{i}.png", 0))

images_ones.append(cv2.imread(f"images2/Ones/template.png", 0))
for i in range(1, 6):
    images_ones.append(cv2.imread(f"images2/Ones/im{i}.png", 0))

# images_twos.append(cv2.imread(f"images2/Twos/template.png", 0))
for i in range(1, 4):
    images_twos.append(cv2.imread(f"images2/Twos/im{i}.png", 0))

images_threes.append(cv2.imread(f"images2/Threes/template.png", 0))
for i in range(1, 9):
    images_threes.append(cv2.imread(f"images2/Threes/im{i}.png", 0))


def cross_correlate(template, imgs):

    for idx, img in enumerate(imgs):
        img = img.copy()

        # res = cv2.matchTemplate(img, template, cv2.TM_CCORR)
        
        method = cv2.TM_CCORR_NORMED
        # method = cv2.TM_CCOEFF_NORMED
        # method = cv2.TM_SQDIFF_NORMED

        res = cv2.matchTemplate(img, template, method)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        results.append(res)
        max_vals.append(max_val)
        print(max_val)
        w, h = template.shape[::-1]

        bottom_right = (top_left[0] + w, top_left[1] + h)

        cv2.rectangle(img, top_left, bottom_right, 255, 2)
        plt.subplot(131), plt.imshow(res, cmap='gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(132), plt.imshow(img, cmap='gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.subplot(133), plt.imshow(template, cmap='gray')
        plt.title('Template Image'), plt.xticks([]), plt.yticks([])
        # print('template shape', template.shape)
        # print('image shape', img.shape)
        # print('result shape', res.shape)
        # plt.subplot(1,1,1), plt.plot(res.flatten())
        # plt.title('Cross Correlations')
        plt.show()


cross_correlate(images_threes[0], images_threes[:])
        
print("Mean:", np.mean(max_vals))
print("Std:", np.std(max_vals))
