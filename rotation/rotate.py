import PIL
from PIL import Image
im = Image.open("moving_delay.jpg")

ans = True
var = 1
while ans == True:
 im.rotate(var).show()
 var += 1
