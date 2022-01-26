Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import images
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import images
ModuleNotFoundError: No module named 'images'
>>> import is
SyntaxError: invalid syntax
>>> import os
>>> os.chdir("C:\\Users\\sharo\\OneDrive\\Documents\\CS Files")
>>> import images
>>> capys = images.Image("capybara.gif")
>>> capys.draw()
>>> capys.getWidth()
800
>>> capys.getHeight()
558
>>> capys.getPixel(0, 0)
(212, 236, 148)
>>> capys.draw()
>>> capys.setPixel(0, 0, (255, 0, 0))
>>> capys.draw()
>>> blank = images.Image(400, 400)
>>> blank.draw()
>>> blank.getPixel(0, 0)
(0, 0, 0)
>>> def paintRow(theImage, rowIndex, theColor):
	for colIndex in range(theImage.getWidth()):
		theImage.setPixel(colIndex, rowIndex, theColor)

		
>>> red = (255,0,0)
>>> paintRow(blank,10, red)
>>> paintRow(blank, 11,red)
>>> paintRow(blank,12,red)
>>> blank.draw()
>>> def paintSquare(theImage, x, y, height, width, theColor):
	for i in range(width):
		for j in range(height)
		
SyntaxError: invalid syntax
>>> def paintSquare(theImage, x, y, height, width, theColor):
	for i in range(width):
		for j in range(height):
			theImage.setPixel(x+i, y+j, theColor)

			
>>> paintSquare(blank,100,100,200,200,red)
>>> blank.draw()
>>> def blackAndWhite(theImage):
	for y in range(image.getHeight()):
		for x in range(image.getWidth()):
			oldColor = image.getPixel(x, y)
			oldRed = oldColor[]
			
SyntaxError: invalid syntax
>>> def blackAndWhite(theImage):
	for y in range(image.getHeight()):
		for x in range(image.getWidth()):
			oldColor = image.getPixel(x, y)
			oldRed = oldColor[0]
			oldGreen = oldColor[1]
			oldBlue = oldColor[2]
			average = (oldRed+oldGreen+oldBlue)//3
			if average < 128:
				image.setPixel(x, y, (0, 0, 0))
			else:
				image.setPixel(x, y, (255,255,255))

				
>>> capycopy = capys.clone()
>>> blackAndWhite(capycopy)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    blackAndWhite(capycopy)
  File "<pyshell#47>", line 2, in blackAndWhite
    for y in range(image.getHeight()):
NameError: name 'image' is not defined
>>> def blackAndWhite(theImage):
	for y in range(theImage.getHeight()):
		for x in range(image.getWidth()):
			oldColor = theImage.getPixel(x, y)
			oldRed = oldColor[0]
			oldGreen = oldColor[1]
			oldBlue = oldColor[2]
			average = (oldRed+oldGreen+oldBlue)//3
			if average < 128:
				theImage.setPixel(x, y, (0, 0, 0))
			else:
				theImage.setPixel(x, y, (255,255,255))

				
>>> blackandWhite(capycopy)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    blackandWhite(capycopy)
NameError: name 'blackandWhite' is not defined
>>> blackAndWhite(capycopy)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    blackAndWhite(capycopy)
  File "<pyshell#51>", line 3, in blackAndWhite
    for x in range(image.getWidth()):
NameError: name 'image' is not defined
>>> def blackAndWhite(theImage):
	for y in range(theImage.getHeight()):
		for x in range(theImage.getWidth()):
			oldColor = theImage.getPixel(x, y)
			oldRed = oldColor[0]
			oldGreen = oldColor[1]
			oldBlue = oldColor[2]
			average = (oldRed+oldGreen+oldBlue)//3
			if average < 128:
				theImage.setPixel(x, y, (0, 0, 0))
			else:
				theImage.setPixel(x, y, (255,255,255))

				
>>> blackAndWhite(capycopy)
>>> capycopy.draw()
>>> 