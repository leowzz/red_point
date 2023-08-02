import numpy as np
from loguru import logger
from utils.pic import save_one_pic, read_pic, load_pic
import cv2
# save_one_pic()
# print(type(read_pic("data/2023-08-02_07:18:00_3d26.jpg")))


def get_rectangle(img: np.ndarray):
    img = img[50:800, 250:1000] 
    cai = img
    # 转灰度
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('data/out/01.jpg', img)
    # 二值化
    # ret, img = cv2.threshold(img, 50, 220, cv2.THRESH_BINARY)
    img = cv2.Canny(img, 50, 220)
    cv2.imwrite('data/out/02.jpg', img)
    # 轮廓检测，获取最外层矩形框的偏转角度angle
    contours, hier = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:  #遍历轮廓
        # 近似轮廓为直边四边形
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        print(approx)
        # 如果近似的轮廓有四个顶点，认为是矩形
        if len(approx) == 4:
            # 计算矩形的旋转角度
            rect = cv2.minAreaRect(contour)
            angle = rect[2]
            # 在图像中绘制检测到的矩形
            cv2.drawContours(cai, [contour], 0, (0, 0, 255), 2)
        # box_ = cv2.boxPoints(rect)
        # h = abs(box_[3, 1] - box_[1, 1])
        # w = abs(box_[3, 0] - box_[1, 0])
        # print("宽，高",w,h)
        # box = cv2.boxPoints(rect)  # 计算最小面积矩形的坐标
        # box = np.int0(box)  # 将坐标规范化为整数
        # angle = rect[2]  #获取矩形相对于水平面的角度
        # cv2.drawContours(cut, [box], 0, (255, 0, 255), 3)
        
    print("轮廓数量", len(contours))
    cv2.imwrite('data/out/05.jpg', cai)
    
    
def get_white(img: np.ndarray):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img = cv2.threshold(gray, 90, 210, cv2.THRESH_BINARY)
    cv2.imwrite('data/out/thre.jpg', img)
    # # 图像腐蚀操作
    kernel = np.ones((3, 1), np.uint8)
    # cv2.imwrite('data/out/kernel.jpg', kernel)
    # 图像膨胀操作
    dilation = cv2.dilate(img, kernel, iterations=5)
    cv2.imwrite('data/out/dilation.jpg', dilation)
    
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite('data/out/closing.jpg', closing)
    
    cv2.imwrite('data/out/02.jpg', img)
    
    
if __name__ == "__main__":
    # save_one_pic()
    
    img = load_pic('data/02.jpg')
    get_rectangle(img)
    
    # img = load_pic('data/01.jpg')
    # get_white(img)