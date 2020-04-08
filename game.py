import pyautogui as gui
import time
from PIL import Image, ImageDraw

def draw(image, box, color):
    img = ImageDraw.Draw(image)
    img.rectangle(box, outline=color)
    del img
    image.save('Image_' + str(time.time()) + '.png')


jumps = 0
# sleeping_time = 0.05
while True:
    img = gui.screenshot()
    # draw = ImageDraw.Draw(img)
    c = [420,360,530,380]
    vertical = c[3] - c[1]
    horizontal = c[2] - c[0]
    crop_img = img.crop(c)
    pixel_img = crop_img.load()
    found = False

    for i in range(horizontal-1,-1,-1):
        for j in range(vertical):
            if pixel_img[i,j][1]==83:
                gui.press('space')
                jumps += 1
                print('space',i,j,pixel_img[i,j]) 
                
                draw(img, c, (0,0,0,0))
                
                # time.sleep(sleeping_time-0.001*jumps) 
                found = True
                break
        if found:
            break

'''
link to website
https://elgoog.im/t-rex/
'''