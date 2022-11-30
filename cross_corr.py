import cv2

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED',
           'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
# TM_CCORR or TM_CCOEFF
result = []
images = []
for i in range(10):
    images.append(cv2.imread(f"images/im{i}.png"))

def cross_correlate(template, imgs):
    for img in imgs:
        # for i in range(len(methods)):
        result.append(cv2.matchTemplate(img, template, i)) #,methods[i]
        cv2.mean(template)
            # print ("Method {}  : Result{}").format(methods[i], result[i])
        # print(result)

cross_correlate(images[0], images[1:])
print(cv2.mean(images[0]))