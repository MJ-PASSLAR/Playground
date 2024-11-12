import cv2 as cv
import qrcode as qr
import PIL
import numpy as np 

font = cv.FONT_HERSHEY_SIMPLEX 
names = open("Names.txt","r",encoding="utf8")
count = len(names.readlines())
names.close()
fontFace = cv.FONT_HERSHEY_SIMPLEX
fontScale = 3.75
fontColor = (0, 0, 0)
thickness = 14
qr_pos = [500,500]
names = open("Names.txt","r",encoding="utf8")
for i in range(count):
    name = names.readline().strip().title()
    qr_code = qr.make(name+" certificated @ Elementry_Academy_Course\n to check the certificate visit www.mositto.ir/certificates")
    
    pil_image = qr_code.convert('RGB')
    open_cv_image = np.array(pil_image)
    qr_code = open_cv_image[:, :, ::-1].copy()
    cv.imwrite("qr_code.jpg",qr_code)
    src = cv.imread("cer.tif")
    src[qr_pos[0]:qr_pos[0]+qr_code.shape[0],qr_pos[1]:qr_pos[1]+qr_code.shape[1]] = qr_code
    text_width, text_height = cv.getTextSize(name, fontFace, fontScale, thickness)[0]
    CenterCoordinates = (int(src.shape[1] / 2) - int(text_width / 2), int(src.shape[0] / 2) + int(text_height / 2))
    cv.putText(src, name, CenterCoordinates, fontFace, fontScale, fontColor, thickness)
    file_name = name+".jpg"
    cv.imwrite(file_name, src)
    print(name+"--> DONE")
names.close()






