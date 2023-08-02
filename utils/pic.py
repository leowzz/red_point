import cv2
import numpy as np
from utils.util import get_now, get_uuid

capture_width = 1280
capture_height = 720
display_width = 1280
display_height = 720
framerate = 60
flip_method = 0

# 设置gstreamer管道参数
def gstreamer_pipeline(
    capture_width=1280, #摄像头预捕获的图像宽度
    capture_height=720, #摄像头预捕获的图像高度
    display_width=1280, #窗口显示的图像宽度
    display_height=720, #窗口显示的图像高度
    framerate=60,       #捕获帧率
    flip_method=0,      #是否旋转图像
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )


# 创建管道
print(gstreamer_pipeline(capture_width,capture_height,display_width,display_height,framerate,flip_method))

#管道与视频流绑定
cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
# cap = cv2.VideoCapture(0)

# if cap.isOpened():
#     window_handle = cv2.namedWindow("D435", cv2.WINDOW_AUTOSIZE)
    
def save_one_pic():
    ret, frame = cap.read()
    print(ret)
    if ret:
        # cv2.imshow("video", frame)
        cv2.imwrite(f'data/{get_now()}_{get_uuid()}.jpg', frame)
    
def load_pic(src: str) -> np.ndarray:
    return cv2.imread(src)

def read_pic() -> np.ndarray:
    ret, frame = cap.read()
    print(ret)
    if ret:
        return frame
    return False

def get_pic():
    ret, frame = cap.read()
    if ret:
        return frame
    return ret

if __name__ == "__main__":
    print(type(read_pic()))