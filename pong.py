import radio
import microbit
from microbit import *

def drawPaddle(x):
  display.set_pixel(x,4,9)
  display.set_pixel(x+1,4,9)

def getX():
  acx = accelerometer.get_x()
  if acx < -500:
    return 0
  elif acx >= -500 and acx < 0:
    return 1
  elif acx >= 0 and acx < 500:
    return 2
  elif acx >= 500:
    return 3
  return 0

display.on()
display.clear()
radio.on()
x = 0
while True:
  uart.write(str(x) + "\r\n")
  x = getX()
  display.clear()
  drawPaddle(x)
  if button_a.is_pressed():
    radio.send('msg')
    display.show(Image.HAPPY)
    break
