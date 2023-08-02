import cv2
import numpy as np

def get_rectangle(img: np.ndarray):
    # 获取黑色矩形靶
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
        # 如果近似的轮廓有四个顶点，认为是矩形
        if len(approx) == 4:
            # 计算矩形的旋转角度
            rect = cv2.minAreaRect(contour)
            angle = rect[2]
            # 在图像中绘制检测到的矩形
            cv2.drawContours(cai, [contour], 0, (0, 0, 255), 2)
            # 4个边角
            print([list(i[0]) for i in approx])
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
    """
    获取细小边界
    """
    img = img[50:800, 250:1000] 
    cai = img
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 只保留图像中的黑线
    ret, gray = cv2.threshold(gray, 80, 210, cv2.THRESH_BINARY_INV)
    cv2.imwrite('data/out/gray.jpg', gray)
    # 霍夫变换
    lines = cv2.HoughLinesP(gray, 100, np.pi / 20,
                            threshold=0,
                            minLineLength=100,
                            maxLineGap=10 )
    """
    增加minLineLength参数：增加minLineLength参数的值可以过滤掉较短的线段，从而减少一些断点的影响。通过逐渐增加minLineLength的值，你可以选择保留长度适中的直线段。
    霍夫变换的阈值参数用于控制检测到的直线的数量。具体来说，它定义了在霍夫空间中曲线交点的最小投票数，投票数低于该阈值的直线将被忽略。
    较低的阈值将导致更多的直线被检测出来，包括一些噪声和不准确的线段。较高的阈值将筛选掉较少的直线，只保留较强和较明显的线段。
    """
    if  lines is None:
        print("line not found !!!!!!!!!!! ")
        return
    print(len(lines))
    for line in lines:
        x1 = line[0][0]
        y1 = line[0][1]
        x2 = line[0][2]
        y2 = line[0][3]
        cv2.line(cai, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
    cv2.imwrite('data/out/lines.jpg', cai)
    