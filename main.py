from utils.pic import save_one_pic, read_pic, load_pic, get_pic
from utils.rectangle import get_rectangle, get_white

    
if __name__ == "__main__":
    # # 拍照
    # save_one_pic()
    
    # # 识别外细线框
    # img = load_pic('data/11.jpg')
    # get_white(img)
    
    
    # # 识别黑框
    img = load_pic('data/12.jpg')
    get_rectangle(img)
    