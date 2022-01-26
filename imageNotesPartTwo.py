Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import images
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import images
ModuleNotFoundError: No module named 'images'
>>> import os
>>> os.chdir("C:\\Users\\sharo\\OneDrive\\Documents\\CS Files")
>>> import images
>>> capys = images.Image(capycaras.gif)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    capys = images.Image(capycaras.gif)
NameError: name 'capycaras' is not defined
>>> capys = images.Image(capybaras.gif)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    capys = images.Image(capybaras.gif)
NameError: name 'capybaras' is not defined
>>> capys = images.Image("capybaras.gif")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    capys = images.Image("capybaras.gif")
  File "C:\Users\sharo\OneDrive\Documents\CS Files\images.py", line 86, in __init__
    raise Exception('File not in current directory')
Exception: File not in current directory
>>> capys = images.Image("capybara.gif")
>>> def grayscale(theImage):
	for colIndex in range(len(theImage.getWidth())):
		for rowIndex in range(len(theImage.getHeight())):
			pixelColor = theImage.getPixel(colIndex,rowIndex)
			channelAverage = (pixelColor[0] + pixelColor[1] + pixelColor[2] // 3)
			theImage.setPixel(colIndex,rowIndex,(channelAverage,channelAverage,channelAverage))

			
>>> capys = capys.clone()
>>> capysGrey = capys.clone()
>>> grayscale(capysGrey)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    grayscale(capysGrey)
  File "<pyshell#14>", line 2, in grayscale
    for colIndex in range(len(theImage.getWidth())):
TypeError: object of type 'int' has no len()
>>> def grayscale(theImage):
	for colIndex in range(theImage.getWidth()):
		for rowIndex in range(theImage.getHeight()):
			pixelColor = theImage.getPixel(colIndex,rowIndex)
			channelAverage = (pixelColor[0] + pixelColor[1] + pixelColor[2] // 3)
			theImage.setPixel(colIndex,rowIndex,(channelAverage,channelAverage,channelAverage))

			
>>> grayscale(capysGrey)

>>> capysGrey.draw()
>>> capysGrey.draw()
>>> def hFlip(theImage):
	newImage = images.Image(theImage.getWidth(), theImage.getHeight())
	for x in range(theImage.getWidth()):
		for y in range(theImage.getHeight()):
			pixelColor = theImage.getPixel(x,y)
			newImage.setPixel(newImage.getWidth()-x-1, y, pixelColor)
	return newImage

>>> hFlip(capysGrey)
<images.Image object at 0x00F3FCE8>
>>> flippedCapys = hFlip(capysGrey)
>>> flippedCapys.draw()
>>> greyCapys.draw()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    greyCapys.draw()
NameError: name 'greyCapys' is not defined
>>> capysGrey.draw()
>>> def copyFlip(theImage):
	newImage = images.Image(theImage.getWidth()*2, theImage.getHeight())
	for x in range(theImage.getWidth()):
		for y in range(theImage.getHeight()):
			pixelColor = theImage.getPixel(x,y)
			newImage.setPixel(x,y,pixelColor)
			newImage.setPixel(newimage.getWidth()-x-1,y,pixelColor)

			
>>> copyFlip = copyFlip(capys)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    copyFlip = copyFlip(capys)
  File "<pyshell#42>", line 7, in copyFlip
    newImage.setPixel(newimage.getWidth()-x-1,y,pixelColor)
NameError: name 'newimage' is not defined
>>> def copyFlip(theImage):
	newImage = images.Image(theImage.getWidth()*2, theImage.getHeight())
	for x in range(theImage.getWidth()):
		for y in range(theImage.getHeight()):
			pixelColor = theImage.getPixel(x,y)
			newImage.setPixel(x,y,pixelColor)
			newImage.setPixel(newImage.getWidth()-x-1,y,pixelColor)

			
>>> copyFlip = copyFlip(capys)
>>> def copyFlip(theImage):
	newImage = images.Image(theImage.getWidth()*2, theImage.getHeight())
	for x in range(theImage.getWidth()):
		for y in range(theImage.getHeight()):
			pixelColor = theImage.getPixel(x,y)
			newImage.setPixel(x,y,pixelColor)
			newImage.setPixel(newImage.getWidth()-x-1,y,pixelColor)
	return newImage

>>> copyFlip = copyFlip(capys)
>>> copyFlip.draw()
>>> def foo(x,y):
	def bar(a,b):
		return a+b+1
	return bar(x,y)+1
foo(2,3)
SyntaxError: invalid syntax
>>> foo(2,3)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    foo(2,3)
NameError: name 'foo' is not defined
>>> def average(triple):
	(r, g, b) = triple
	return (r+g+b)//3

>>> def detectEdges(theImage,amount):
	newImage = theImage.clone()
	for x in range(1,theImage.getWidth()):
		for y in range(theImage.getHeight()-1):
			oldPixel = theImage.getPixel(x,y)
			leftPixel = theImage.getPixel(x-1,y)
			bottomPixel = theImage.getPixel(x, y+1)
			oldLum = average(oldPixel)
			leftLum = average(leftPixel)
			bottomLum = average(bottomPixel)
			if abs(oldLum - leftLum) > amount or abs(oldLum - bottomLum) > amount:
				newImage.setPixel(x,y,(0,0,0))
			else:
				newImage.setPixel(x,y,(255,255,255))
	return newImage

>>> edgeCapy = detectEdges(capys,10)
>>> edgeCapys.draw()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    edgeCapys.draw()
NameError: name 'edgeCapys' is not defined
>>> edgeCapy.draw()
>>> edgeCapy = detectEdges(capys,5)
>>> edgeCapy.draw()
>>> edgeCapy = detectEdges(capys,25)
>>> edgeCapy.draw()
>>> 