import numpy as np

from utils.pic import save_one_pic, read_pic, load_pic
import cv2
# save_one_pic()
# print(type(read_pic("data/2023-08-02_07:18:00_3d26.jpg")))

def get_rectangle(img: np.ndarray):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('data/out/01.jpg', img)
    ret, img = cv2.threshold(img, 100, 220, cv2.THRESH_BINARY)
    cv2.imwrite('data/out/02.jpg', img)
    contours, hier = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:  #遍历轮廓
        rect = cv2.minAreaRect(c)  #生成最小外接矩形
        box_ = cv2.boxPoints(rect)
        h = abs(box_[3, 1] - box_[1, 1])
        w = abs(box_[3, 0] - box_[1, 0])
        print("宽，高",w,h)
        #只保留需要的轮廓
        if (h > 3000 or w > 2200):
            continue
        if (h < 2500 or w < 1500):
            continue
        box = cv2.boxPoints(rect)  # 计算最小面积矩形的坐标
        box = np.int0(box)  # 将坐标规范化为整数
        angle = rect[2]  #获取矩形相对于水平面的角度
        if angle > 0:
            if abs(angle) > 45:
                angle = 90 - abs(angle)
        else:
            if abs(angle) > 45:
                angle = (90 - abs(angle))
        # 绘制矩形
        cv2.drawContours(img, [box], 0, (255, 0, 255), 3)
    print("轮廓数量", len(contours))
    cv2.imwrite('data/out/03.jpg', img)
    
if __name__ == "__main__":
    # save_one_pic()
    img = load_pic('data/01.jpg')
    get_rectangle(img)