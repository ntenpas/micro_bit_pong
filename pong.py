import radio
import microbit
from microbit import *

x = 0
bx = 0
by = 0
time = 0
# 0=NE, 1=SE, 2=SW, 3=NW
direction = 1

def paddleBounce(leftside):
  global direction
  if leftside == True:
    direction = 3
  else:
    direction = 0

def wallBounce():
  global bx,by,direction
  # move ball back to before wall crossing
  if direction == 0:
    bx-=1
    by+=1
  elif direction == 1:
    bx-=1
    by-=1
  elif direction == 2:
    bx+=1
    by-=1
  elif direction == 3:
    bx+=1
    by+=1
  direction = -1

def moveBall():
  global bx, by
  if by == 4:
    if bx == x:
      paddleBounce(True)
    elif bx == (x+1):
      paddleBounce(False)
  if bx < 0 or bx > 4 or by < 0 or by > 4:
    uart.write("wall")
    wallBounce()
    return
  uart.write("hi")
  # calculate next pos
  if direction == 0:
    bx+=1
    by-=1
  elif direction == 1:
    bx+=1
    by+=1
  elif direction == 2:
    bx-=1
    by+=1
  elif direction == 3:
    bx-=1
    by-=1

def drawBall():
  global time
  if time == 100:
    moveBall()
    time = 0
  display.set_pixel(bx,by,9)

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
while True:
  #uart.write(str(x) + "\r\n")
  x = getX()
  display.clear()
  drawPaddle(x)
  drawBall()
  time+=1
  if button_a.is_pressed():
    radio.send('msg')
    display.show(Image.HAPPY)
    break
