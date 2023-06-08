from multiprocessing.connection import wait
import cv2 as cv
import pytesseract 
import YB_Pcb_Car
import time
car = YB_Pcb_Car.YB_Pcb_Car()
#x = input('type a random number from a to five ')
#y = x+'.png'
#img = cv.imread(y)
cap = cv.VideoCapture(0)

def get_ocr(img):
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    return pytesseract.image_to_string(img_rgb)


'''
while True:
    hehe , frame = cap.read()

    cv.imshow('Final', frame)
    k = cv.waitKey(1)
    if k % 256 == 27:
        print("ESC...")
        break
    elif k % 256 == 32:
        text_ocr = get_ocr(frame)
        print(text_ocr)
        if "Sad" in text_ocr:
            car.Ctrl_Servo(1, 90)
            car.Ctrl_Servo(1, 90)
'''
car.Ctrl_Servo(1, 90)
car.Ctrl_Servo(1, 1)
time.sleep(1)
car.Ctrl_Servo(1, 90)
car.Ctrl_Servo(1, 1)