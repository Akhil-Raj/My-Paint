import cv2
import numpy as np


def nothing():
    pass


class _drawLine:
    def __init__(self):
        self.ix = 0; self.iy = 0; self.oldx = 0; self.oldy = 0; self.draw = False

    def draw(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.ix = x
            self.iy = y
            self.oldx = x
            self.oldy = y
            self.draw = True

        elif event == cv2.EVENT_MOUSEMOVE:
            if self.draw:
                cv2.rectangle(img, (self.ix, self.iy), (self.oldx, self.oldy), (255, 255, 255))
                cv2.rectangle(img, (self.ix, self.iy), (self.x, self.y), (b, g, r))
                self.oldx = x, self.oldy = y

        elif event == cv2.EVENT_LBUTTONUP:
            self.draw = False
            cv2.rectangle(img, (self.ix, self.iy), (self.oldx, self.oldy), (255, 255, 255))
            cv2.rectangle(img, (self.ix, self.iy), (self.x, self.y), (b, g, r))
            self.oldx = x, self.oldy = y

def myPaint2():
    cv2.namedWindow("myPaint")
    img = np.zeros((300, 1000, 3), np.uint8)
    img[:] = 255

    line = drawLine()
    #line.draw
    cv2.createTrackbar("Line(0:No, 1:Yes)", "myPaint", 0, 1, nothing)
    cv2.createTrackbar("Rectangle(0:No, 1:Yes)", "myPaint", 0, 1, nothing)
    cv2.createTrackbar("Polygon(0:No, 1:Yes)", "myPaint", 0, 1, nothing)
    cv2.createTrackbar("Circle(0:No, 1:Yes)", "myPaint", 0, 1, nothing)
    cv2.createTrackbar("Eraser(0:No, 1:Yes)", "myPaint", 0, 1, nothing)
    cv2.createTrackbar("R", "myPaint", 0, 255, nothing)
    cv2.createTrackbar("G", "myPaint", 0, 255, nothing)
    cv2.createTrackbar("B", "myPaint", 0, 255, nothing)

    while(1):
        #print(val)
        cv2.imshow("myPaint", img)

        r = cv2.getTrackbarPos("R", "myPaint")
        g = cv2.getTrackbarPos("G", "myPaint")
        b = cv2.getTrackbarPos("B", "myPaint")

        if cv2.getTrackbarPos("Line(0:No, 1:Yes)", "myPaint"):
            cv2.setMouseCallback("myPaint", line.draw)
        if cv2.waitKey(10) == 27:
                break

#global img, r, g, b
#def __init__(self):

def drawLine(event, x, y, flags, param):
    #print(b, g, r)
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        drawLine.ix = x
        drawLine.iy = y

    elif event == cv2.EVENT_LBUTTONUP:
        cv2.line(img, (drawLine.ix, drawLine.iy), (x, y), (b, g, r), thickness)


drawLine.ix = 0; drawLine.iy = 0;

def offTrackbars(trackbarNames, windowName):
    for i in trackbarNames:
        cv2.setTrackbarPos(i, windowName, 0)

def drawRect(event, x, y, flags, param):
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        drawRect.ix = x
        drawRect.iy = y

    elif event == cv2.EVENT_LBUTTONUP:
        cv2.rectangle(img, (drawRect.ix, drawRect.iy), (x, y), (b, g, r), thickness)


def drawCircle(event, x, y, flags, param):
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        drawCircle.ix = x
        drawCircle.iy = y

    elif event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img, (drawCircle.ix, drawCircle.iy), int(np.sqrt(np.sum([np.square(drawCircle.ix - x), np.square(drawCircle.iy - y)]))), (b, g, r), thickness)


def erase(event, x, y, flags, param):
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        erase.ix = x
        erase.iy = y
        erase.draw = True

    if event == cv2.EVENT_MOUSEMOVE:
        if erase.draw:
            cv2.circle(img, (x, y), thickness, (255, 255, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        erase.draw = False
        cv2.circle(img, (x, y), thickness, (255, 255, 255), -1)


drawRect.ix = 0; drawRect.iy = 0
b = 0; r = 0; g = 0
img = 0; thickness = 0;  # type: int # type: int

def myPaint():
    print(cv2.__version__)
    cv2.namedWindow("myPaint")
    global img, b, r, g, thickness
    img = np.zeros((300, 1000, 3), np.uint8)
    img[:] = 255
    trackbarNames = {"L" : "Line(0:No, Others: Thickness)", 'R' : "Rectangle(0:No, Others: Thickness)", "C" : "Circle(0:No, Others: Thickness)", "E" : "Eraser(0:No, Others: Thickness)"}

    #line = drawLine()
    #line.draw
    cv2.createTrackbar("Line(0:No, Others: Thickness)", "myPaint", 0, 20, nothing)
    cv2.createTrackbar("Rectangle(0:No, Others: Thickness)", "myPaint", 0, 20, nothing)
    cv2.createTrackbar("Circle(0:No, Others: Thickness)", "myPaint", 0, 20, nothing)
    cv2.createTrackbar("Eraser(0:No, Others: Thickness)", "myPaint", 0, 20, nothing)
    cv2.createTrackbar("R", "myPaint", 0, 255, nothing)
    cv2.createTrackbar("G", "myPaint", 0, 255, nothing)
    cv2.createTrackbar("B", "myPaint", 0, 255, nothing)
    prevL = False
    prevR = False
    prevC = False
    prevE = False
    while(1):
        cv2.imshow("myPaint", img)
        #print(val)
        #cv2.line(img, (0, 0), (100, 100), (0, 0, 0))
        r = cv2.getTrackbarPos("R", "myPaint")
        g = cv2.getTrackbarPos("G", "myPaint")
        b = cv2.getTrackbarPos("B", "myPaint")
        #cv2.setTrackbarPos(trackbarNames['L'], "myPaint", 1)
        lis = list(trackbarNames.values())
        #print(trackbarNames['L'])

        if cv2.getTrackbarPos(trackbarNames['L'], "myPaint"):
            #print(1)
            thickness = cv2.getTrackbarPos(trackbarNames['L'], "myPaint")
            #cv2.line(img, (100, 100), (200, 200), (0, 0, 0))
            cv2.setMouseCallback("myPaint", drawLine)
            if not prevL:
                prevL = True
                lis.remove(trackbarNames["L"])
                offTrackbars(lis, "myPaint")
        else:
            prevL = False


        if cv2.getTrackbarPos(trackbarNames['R'], "myPaint"):
            thickness = cv2.getTrackbarPos(trackbarNames['R'], "myPaint")
            cv2.setMouseCallback("myPaint", drawRect)
            if not prevR:
                prevR = True
                lis.remove(trackbarNames["R"])
                offTrackbars(lis, "myPaint")

        else:
            prevR = False

        if cv2.getTrackbarPos(trackbarNames['C'], "myPaint"):
            thickness = cv2.getTrackbarPos(trackbarNames['C'], "myPaint")
            cv2.setMouseCallback("myPaint", drawCircle)
            if not prevC:
                prevC = True
                lis.remove(trackbarNames["C"])
                offTrackbars(lis, "myPaint")
        else:
            prevC = False

        if cv2.getTrackbarPos(trackbarNames['E'], "myPaint"):
            thickness = cv2.getTrackbarPos(trackbarNames['E'], "myPaint")
            cv2.setMouseCallback("myPaint", erase)
            if not prevE:
                prevE = True
                lis.remove(trackbarNames["E"])
                offTrackbars(lis, "myPaint")
        else:
            prevE = False

        if cv2.waitKey(1) == 27:
            break


if __name__ == '__main__':
    myPaint()