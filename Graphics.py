# Graphics.py

# This version of the <Graphics> library
# was written by Mr. John Schram 10/3/18
# for use in first year Computer Science 1
# or Computer Science 1-Honors / PreAPCS.

# While built on "Turtle Graphics", the
# procedures and functions below allow
# graphics programming with more traditional
# graphics commands for greater convenience.

# It was inspired by a similar graphics
# library created by Mr. Leon Schram and
# is designed to operate in a manner
# similar to that of the <Expo> class 
# that we created for "Exposure Java".

# This code is free software.
# You can redistribute it and/or modify it under 
# the terms of the GNU General Public License as 
# published by the Free Software Foundation. This 
# code is distributed in the hope that it will be 
# useful, but WITHOUT ANY WARRANTY; without even 
# the implied warranty of MERCHANTABILITY or 
# FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU General Public License for more details. 


###########################################
# Warning for students in APCS-Principles #
# --------------------------------------- #
# While this file may look similar to     #
# something that you need to create for   #
# one of your labs, it is actually quite  #
# different.  Do not make the mistake     #
# of simply copying this code.  If you    #
# do, it will be painfully obvious that   #
# you have cheated.                       #
###########################################


from turtle import *
from math import *
from time import sleep
from random import randint
import inspect
import turtle    # Necessary to make the <circle> procedure work


# Translates the x-coordinate from Traditional Graphics to Turtle Graphics.
def getX(x): 
   centerX = window_width() / 2 
   return int(x - centerX + 1)


# Translates the y-coordinate from Traditional Graphics to Turtle Graphics.
def getY(y):
   centerY = window_height() / 2 
   return int(centerY - y - 1)
   

# Translates the x-coordinate from Turtle Graphics to Traditional Graphics.
def actualX(x): 
   centerX = window_width() / 2 
   return int(x + centerX - 1)


# Translates the y-coordinate from Turtle Graphics to Traditional Graphics.
# Note: Technically, this function is identical to <getY>.
def actualY(y):
   centerY = window_height() / 2 
   return int(centerY - y - 1) 
   
   
# Translates the (x,y)-coordinate from Traditional Graphics to Turtle Graphics.
def turtleXY(x,y):
   return getX(x), getY(y)    
   
   
# Translates the (x,y)-coordinate from Turtle Graphics to Traditional Graphics.
def traditionalXY(x,y):
   return actualX(x), actualY(y)      


# Sets the dimensions of the graphics window 
# and sets the graphics mode to instant display
# and also hides the turtle.   
def beginGrfx(x,y):
   setup(x+10,y+10)
   tracer(0,0)
   hideturtle()
   

# Updates the graphics window to make sure the last
# thing drawn displays and keeps the graphics window 
# open until the user chooses to close it.  
def endGrfx():
   hideturtle()
   update() 
   done()
       
       
# Draws a single pixel
# which may be too small to see.
def drawPixel(x,y):
   x = getX(x)
   y = getY(y)
   penup()
   goto(x,y)
   pendown()
   goto(x+1,y)
   
   
# Draws a "point" which is really a 5 x 5 square
def drawPoint(x,y):
   x = getX(x)
   y = getY(y)
   penup()
   goto(x-2,y-2)
   pendown()
   begin_fill()
   goto(x+2,y-2)
   goto(x+2,y+2)
   goto(x-2,y+2)
   goto(x-2,y-2)
   end_fill()
    

# Draws a line from (x1,y1) to (x2,y2)   
def drawLine(x1,y1,x2,y2):
   x1 = getX(x1)
   y1 = getY(y1)
   x2 = getX(x2)
   y2 = getY(y2)
   penup()
   goto(x1,y1)
   pendown()
   goto(x2,y2) 
   
   
# Draws a rectangle from top-left (x1,y1) 
# to bottom-right (x2,y2)   
def drawRectangle(x1,y1,x2,y2):
   drawLine(x1,y1,x2,y1)
   drawLine(x2,y1,x2,y2)
   drawLine(x2,y2,x1,y2)
   drawLine(x1,y2,x1,y1) 
   
   
# Fills a rectangle from top-left (x1,y1) 
# to bottom-right (x2,y2)   
def fillRectangle(x1,y1,x2,y2):
   begin_fill()
   drawRectangle(x1,y1,x2,y2)
   end_fill()
   #update()
      
   
# Draws a rectangle from top-left (x,y) 
# with width(w) and height(h)  
def drawRect(x,y,w,h):
   drawRectangle(x,y,x+w,y+h)
   

# Fills a rectangle from top-left (x,y) 
# with width(w) and height(h)  
def fillRect(x,y,w,h):
   fillRectangle(x,y,x+w,y+h)   


# Draws a circle with center (centerX,centerY) 
# and radius (r).
# This procedure uses lines to draw a circle.
# It concludes by drawing a line from the last 
# point in the circle to the first point, 
# thereby "closing" the circle. 
def drawCircle(centerX,centerY,r):
   x = getX(centerX)
   y = getY(centerY)
   setheading(0)
   penup()
   goto(x,y-r)
   pendown()
   turtle.circle(r)
         

# Fills a circle with center (centerX,centerY) 
# and radius (r).
def fillCircle(centerX,centerY,r):
   begin_fill()
   drawCircle(centerX,centerY,r)
   end_fill()  
   #update()    


# Displays text on the graphics screen at the (x,y)
# position with the <face>, <font> and <style> if specified.
# If not specified, the default font is used.  
def drawString(output,x,y,face="Arial",size=10,style="normal"):
   if style.lower() == "plain":
      style = "normal"  
   if style.lower() in ["bold&italic","bold+italic","both"]:
      style = ("bold","italic")      
   penup()
   setpos(getX(x),getY(y))
   write(output,font=(face,size,style)) 


# Draws an oval with center (centerX,centerY), 
# horizontal radius (hr) and vertical radius (vr).
def drawOval(centerX,centerY,hr,vr):
   radian = 0.0
   if hr < 1:
      hr = 1   
   if vr < 1:
      vr = 1        
   if hr > vr:
      step = pi / hr
   else:
      step = pi / vr
   startX = cos(radian) * hr + centerX
   startY = sin(radian) * vr + centerY
   x1 = startX
   y1 = startY
   while radian <= 2 * pi:
      radian = radian + step
      x2 = cos(radian) * hr + centerX
      y2 = sin(radian) * vr + centerY
      drawLine(x1,y1,x2,y2)
      x1 = x2
      y1 = y2
   drawLine(x1,y1,startX,startY)
      

# Fills an oval with center (centerX,centerY), 
# horizontal radius (hr) and vertical radius (vr).
def fillOval(centerX,centerY,hr,vr):
   begin_fill()
   drawOval(centerX,centerY,hr,vr)
   end_fill()
   #update()
     
  
# Draws a regular polygon with <numSides> sides that
# is inscribed in a circle with center (centerX,centerY)
# and radius (r).
def drawRegularPolygon(centerX,centerY,r,numSides):
   rotate = pi / 2
   if numSides < 2:
      numSides = 2
   if numSides % 2 == 0:
	   rotate = rotate + pi / numSides
   radian = 0
   count = 0
   step = 2 * pi / numSides
   halfSides = numSides // 2
   xStart = cos(radian - rotate) * r + centerX 
   yStart = sin(radian - rotate) * r + centerY
   x1 = xStart
   y1 = yStart
   while radian <= 2 * pi:
      radian = radian + step
      x2 = cos(radian - rotate) * r + centerX
      y2 = sin(radian - rotate) * r + centerY
      count = count + 1
      if numSides % 2 == 1:
         if count == halfSides:
            yTemp = y2
         elif count == halfSides+1: 
            y2 = yTemp   
      elif numSides % 4 == 0:
         if count == numSides // 2:
            yTemp1 = y2  
         elif count == numSides // 2 + 1:
            y2 = yTemp1       
         if count == 1:
            yTemp2 = y2  
         elif count == numSides:
            y2 = yTemp2      
      elif numSides % 4 == 2:                      
         if count == numSides // 2:
            yTemp1 = y2  
         elif count == numSides // 2 + 1:
            y2 = yTemp1       
         if count == 1:
            yTemp2 = y2  
         elif count == numSides:
            y2 = yTemp2                    
      drawLine(x1,y1,x2,y2)
      x1 = x2
      y1 = y2        
   drawLine(x2,y2,xStart,yStart)  
   

# Fill a regular polygon with <numSides> sides that
# is inscribed in a circle with center (centerX,centerY)
# and radius (r).
def fillRegularPolygon(centerX,centerY,r,numSides):   
   begin_fill()
   drawRegularPolygon(centerX,centerY,r,numSides)
   end_fill()
   #update()
         

# Draws an arbitrary polygon 
# Precondition: points is an array of integer values 
# whose length is an even number >= 6
def drawPolygon(points):   
   if len(points) < 6:
      update()
      sleep(1)
      print("Polygon Error in line",inspect.currentframe().f_back.f_back.f_lineno)
      print("When using drawPolygon/fillPolygon")
      print("you must have at least 6 int arguments.")
      exit()
   elif len(points) % 2 != 0:
      update()
      sleep(1)
      print("Polygon Error in line",inspect.currentframe().f_back.f_back.f_lineno)
      print("When using drawPolygon/fillPolygon")
      print("you must have an even # of int arguments.")
      exit()
   else:
      for p in range(0,len(points)-2,2):
         x1 = points[p]
         y1 = points[p+1]
         x2 = points[p+2]
         y2 = points[p+3]
         drawLine(x1,y1,x2,y2)
      drawLine(x2,y2,points[0],points[1])

 
# Fills an arbitrary polygon 
# Precondition: points is an array of integer values 
# whose length is an even number >= 6
def fillPolygon(points):   
   begin_fill() 
   drawPolygon(points)
   end_fill()
   #update()
   

# Draws an arc which is really a piece of an oval. 
# The first 4 arguments are identical to <drawOval>.
# The last 2 indicate the degree measure of where 
# the arc begins (start) and ends (finish).
# NOTE: 0 degrees is at the 12:00 position.
# ALSO: The arc is drawn clockwise.
def drawArc(centerX,centerY,hr,vr,start,finish=None):   
   if finish is None:
      finish = start
      start = vr
      vr = hr
   if (finish <= start):
      finish = finish + 360 
   newStart = (start-90) / 180 * pi
   newFinish = (finish-90) / 180 * pi
   radian = newStart
   if hr > vr:
      step = pi / hr
   else:
      step = pi / vr
   x1 = cos(radian) * hr + centerX
   y1 = sin(radian) * vr + centerY
   while radian <= newFinish:
      radian = radian + step
      x2 = cos(radian) * hr + centerX
      y2 = sin(radian) * vr + centerY
      drawLine(x1,y1,x2,y2)
      x1 = x2
      y1 = y2
   #update()       
      

# Fills an arc which is really a piece of a filled oval. 
# The first 4 arguments are identical to <fillOval>.
# The last 2 indicate the degree measure of where 
# the arc begins (start) and ends (finish).
# NOTE: 0 degrees is at the 12:00 position.
# ALSO: The arc is drawn clockwise.
def fillArc(centerX,centerY,hr,vr,start,finish=None):   
   if finish is None:
      finish = start
      start = vr
      vr = hr
   if (finish <= start):
      finish = finish + 360 
   newStart = (start-90) / 180 * pi
   newFinish = (finish-90) / 180 * pi
   x1 = cos(newStart) * hr + centerX
   y1 = sin(newStart) * vr + centerY
   x3 = cos(newFinish) * hr + centerX
   y3 = sin(newFinish) * vr + centerY 
   begin_fill()
   drawLine(centerX,centerY,x1,y1)
   radian = newStart
   if hr > vr:
      step = pi / hr
   else:
      step = pi / vr
   while radian <= newFinish:
      radian = radian + step
      x2 = cos(radian) * hr + centerX
      y2 = sin(radian) * vr + centerY
      drawLine(x1,y1,x2,y2)
      x1 = x2
      y1 = y2
   drawLine(x3,y3,centerX,centerY)
   end_fill()
   #update()
   

# Draws a "burst" of evenly spaced lines with radius (r)
# all radiating from that same center (centerX,centerY).
# The final argument (numLines) determines the number
# of evenly spaced lines.
def drawBurst(centerX,centerY,r,numLines):
   radian = 0.0
   if numLines < 2:
      numLines = 2
   step = 2 * pi / numLines
   rotate = pi / 2 
   while radian <= 2 * pi:
      x = cos(radian-rotate) * r + centerX
      y = sin(radian-rotate) * r + centerY
      drawLine(centerX,centerY,x,y)
      radian = radian + step    
      

# This is a "helping function" for
# <drawStar> and <fillStar> and is
# not meant to be called anywhere else.      
def getHalfRadius(radius, points):
   halfRadius = radius / 2
   if points == 3: 
      halfRadius = 140 * radius / 500
   elif points == 4: 
      halfRadius = 170 * radius / 400
   elif points == 5: 
      halfRadius = 191 * radius / 500
   elif points == 6: 
      halfRadius = 465 * radius / 800
   elif points == 7: 
      halfRadius = 179 * radius / 500
   elif points == 8: 
      halfRadius = 215 * radius / 400
   elif points == 9: 
      halfRadius = 173 * radius / 500
   elif points == 10: 
      halfRadius = 210 * radius / 400
   elif points < 50:
      if points % 2 == 1:
         halfRadius = (180-points) * radius / 500
      else:
         halfRadius = (222-points) * radius / 400
   else:
      halfRadius = radius / 2
   return halfRadius
      
      
# Draws a star with <numPoints> points that is
# inscribed in a circle with center (centerX,centerY)
# and radius (r).
def drawStar(centerX,centerY,r,numPoints):
   rotate = pi / 2
   count = 0
   radius = r
   halfRadius = getHalfRadius(r,numPoints) 
   last = 2 * numPoints
   radian = 0
   if numPoints < 2:
      numPoints = 2
   step = pi / numPoints
   xStart = int(cos(radian - rotate) * r + centerX) 
   yStart = int(sin(radian - rotate) * r + centerY)
   x1 = xStart
   y1 = yStart
   while radian <= 2 * pi:
      radian = radian + step
      if count % 2 == 1:
          radius = r      
      else:
          radius = halfRadius   
      count = count + 1      
      x2 = int(cos(radian - rotate) * radius + centerX)
      y2 = int(sin(radian - rotate) * radius + centerY)
      if 5 <= numPoints <= 51:
         kind = numPoints % 4 
         q = (numPoints - 3) // 2
         if kind == 1:
            if count == q:
               yTemp = y2
            elif count == q+1 or count == last-q-1 or count == last-q:
               y2 = yTemp        
         elif kind == 2:
            if count == q:
               yTemp1 = y2
            elif count == q+1 or count == last-q-1 or count == last-q:
               y2 = yTemp1  
            if count == q+3:
               yTemp2 = y2
            elif count == q+4 or count == last-q-4 or count == last-q-3:
               y2 = yTemp2              
         elif kind == 3:
            if count == q+2:
               yTemp = y2
            elif count == q+3 or count == last-q-3 or count == last-q-2:
               y2 = yTemp               
      drawLine(x1,y1,x2,y2)
      x1 = x2
      y1 = y2   
 
   drawLine(x2,y2,xStart,yStart)     
      
   
# Fills a star with <numPoints> points that is
# inscribed in a circle with center (centerX,centerY)
# and radius (r).
def fillStar(centerX,centerY,r,numPoints):   
   begin_fill()
   drawStar(centerX,centerY,r,numPoints)
   end_fill()
   #update()            

# Draws a spiral with center (centerX,centerY)
# that grows to a maximum radius of (maxRadius)
# The final argument (spacing) controls the
# spacing between each "loop" of the spiral. 
def drawSpiral(centerX, centerY, maxRadius, spacing):
   spiralInc = spacing / (2 * pi * 20) # Because of the 20 here...
   rotate = pi / 2
   spiralRadius = 0;
   radian = 0;
   x1 = centerX
   y1 = centerY
   while spiralRadius <= maxRadius:
      radian = radian + 0.05 # ...we need a 0.05 here because it is the inverse.
      x2 = cos(radian) * spiralRadius + centerX
      y2 = sin(radian) * spiralRadius + centerY
      drawLine(x1,y1,x2,y2)
      x1 = x2
      y1 = y2   
      spiralRadius += spiralInc;  
   #update() 
   

# Delays the output for a certain number of milli-seconds (mil)   
def delay(mil):
   update()
   sec = mil / 1000
   sleep(sec)           
            
            
# Converts a number from 0-15 to a single digit hexadecimal number
# This is a helper function for <decihex2>.  
def decihex1(dec):
   if dec == 15:
      return "F"
   elif dec == 14:
      return "E"   
   elif dec == 13:
      return "D"  
   elif dec == 12:
      return "C"  
   elif dec == 11:
      return "B"  
   elif dec == 10:
      return "A"  
   else:
      return str(dec)  
                
                                    
# Converts a number from 0-255 to a double digit hexadecimal number
# This is a helper function for <setRandomColor> and <setColor>.  
def decihex2(dec):
   quotient = dec // 16
   remainder = dec % 16
   return decihex1(quotient) + decihex1(remainder)
   

# Changes to a completely random color   
def setRandomColor():
   red = randint(0,255)
   green = randint(0,255)
   blue = randint(0,255)
   colorString = "#" + decihex2(red) + decihex2(green) + decihex2(blue)
   color(colorString)
   
   
# Changes the drawing color to a new color created by combining 
# different amounts of red, green and blue.
# Precondition: All 3 arguments are integers in the range [0..255] 
# NOTE: If only one argument is used, and it is a number, it will 
#       determine the color based on a preselected list.  
# ALSO: If only one argument is used, and it is a string, it will 
#       use that string as the color name.  
def setColor(red,green=None,blue=None):
   if blue is None:
      if type(red) is str:
         if red.lower() == "brown":
            color("#96640F") # proper brown
         elif red.lower() == "green":
            color("#00FF00") # proper green
         elif red.lower() == "dark green" or red.lower() == "darkgreen":
            color("#008000") # proper dark green      
         else:   
            color(red)
      elif red < 0:
         color("#FFFFFF")  # pure white
      elif red == 0:
         color("#000000")  # pitch black       
      else:   
         colors = ["gray","#FF0000","#00FF00","#0000FF","orange","cyan","magenta","yellow","purple","#96640F"]
         index = red % 10
         color(colors[index])
   else:         
      colorString = "#" + decihex2(red) + decihex2(green) + decihex2(blue)
      color(colorString)      


# Changes the background color to a new color created by combining 
# different amounts of red, green and blue.
# Precondition: All 3 arguments are integers in the range [0..255] 
# NOTE: If only one argument is used, and it is a number, it will 
#       determine the color based on a preselected list.  
# ALSO: If only one argument is used, and it is a string, it will 
#       use that string as the color name. 
def setBackground(red,green=None,blue=None):
   setColor(red,green,blue)
   fillRectangle(0,0,window_width(),window_height())    
   
   
# Displays a "heading" in the top 50 pixels of the graphics screen.
# The heading will include the Lab Assignment number (labNum) and
# the name of the student (name) centered at the top of the screen
# and separated from the rest of the output with a horizontal line.  
def drawHeading(name,labNum):
   penup()
   if type(labNum) is str:
      labNumString = labNum
   else:
      labNumString = str(labNum)
   s = "Lab "+labNumString+"  By: "+name
   x = (window_width() - len(s)*28) // 2
   color("black")
   drawString(s,x,52,"Courier New",28,"bold")
   drawLine(0,50,window_width(),50)    
      
      
# Determines if the "Turtle" coordinate (x,y) is inside the
# rectangle bounded by "Graphics" coordinates (x1,y1,x2,y2).
# Precondition: x1 <= x2 and y1 <= y2
def inside(x,y,x1,y1,x2,y2):
   x = actualX(x)
   y = actualY(y)
   return x1 <= x <= x2 and y1 <= y <= y2
             