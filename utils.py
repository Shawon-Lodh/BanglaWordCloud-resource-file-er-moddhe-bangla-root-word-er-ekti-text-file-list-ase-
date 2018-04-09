import codecs
from os import path
import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from quadtree import *

def get_ind_points(img, width, height, x0, y0, w, h):
    #print("from (" + str(x0) + ", " + str(y0) + ") to (" + str(x0+w) + ", " + str(y0+h) + ")")
    points = []
    pixel_values = list(img.getdata())
    if img.mode == 'RGB':
        channels = 3
    elif img.mode == 'L':
        channels = 1
    else:
        print("Unknown mode: %s" % img.mode)
        return None
    pixel_values = np.array(pixel_values).reshape((height, width, channels))
    cnt = 0;
    # print(len(pixel_values))
    # print(len(pixel_values[0]))
    for i in range(y0, y0+h+1):
        for j in range(x0, x0+w+1):
            # print(i, j)
            if pixel_values[i][j][0] != 255 or pixel_values[i][j][1] != 255 or pixel_values[i][j][2] != 255:
                cnt += 1
                points.append(Point(j, i))
    # print("not white pixel: " + str(cnt))
    return points
def get_points(img, width, height):
    points = []
    pixel_values = list(img.getdata())
    if img.mode == 'RGB':
        channels = 3
    elif img.mode == 'L':
        channels = 1
    else:
        print("Unknown mode: %s" % img.mode)
        return None
    pixel_values = np.array(pixel_values).reshape((height, width, channels))
    cnt = 0;
    # print(len(pixel_values))
    # print(len(pixel_values[0]))
    for i in range(len(pixel_values)):
        for j in range(len(pixel_values[0])):
            #print(i, j)
            if pixel_values[i][j][0] != 255 or pixel_values[i][j][1] != 255 or pixel_values[i][j][2] != 255:
                cnt += 1
                points.append(Point(j, i))
    #print("not white pixel: " + str(cnt))
    return points

def get_font_size(freq, minfreq, maxfreq, fontmin, fontmax):
    sz = fontmin if freq == minfreq else (freq / maxfreq) * (fontmax - fontmin) + fontmin
    #print(int(round(sz)))
    #sz = 40
    return int(round(sz))

def draw_text(wordList):
    imagename = 'testtest.jpg'
    imageWidth = 800
    imageHeight = 600
    img = Image.new('RGB', (imageWidth, imageHeight), color='white')
    img.save(imagename)
    img = Image.open(imagename)

    points = get_points(img, imageWidth, imageHeight)

    minfreq = wordList[len(wordList)-1][1]
    maxfreq = wordList[0][1]
    fontmin = 12
    fontmax = 50
    for word, freq in wordList[:25]: #[:25 limiting wordlist, else  it takes too time.]
        #print(len(points))
        fontsize = get_font_size(freq, minfreq, maxfreq, fontmin, fontmax)
        #print(fontsize)
        points = place(word, fontsize, img, imageWidth, imageHeight, points)
        #points = get_points(img, imageWidth, imageHeight)
        print("drawing " + str(word))
        #break
    # fig = plt.figure(figsize=(8, 8))
    # plt.title("Quadtree")
    # #ax = fig.add_subplot(111)
    # x = [point.x for point in points]
    # y = [point.y for point in points]
    # plt.plot(x, y, 'r.')
    # plt.axis([0, imageWidth, imageHeight, 0])
    # plt.show()

def place(word, fontsize, img, width, height, points):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("C:\Windows\Fonts\Siyamrupali.ttf", size=fontsize, encoding="utf-8")
    w, h = font.getsize(word)

    #check if we get enough space
    row = height // 2
    col = width // 2
    cnt = 0
    c = 0;
    r = 0;
    #print(row, col)
    if ispoints_in_region(col, row, w, h, points) == False:
        draw.text((col, row), word, 'red', font=font)
        img.save(img.filename)
        #print(len(get_ind_points(img, width, height, col, row, w, h)))
        points.extend(get_ind_points(img, width, height, col, row, w, h))
        return points
    cnt += 1
    while cnt < height * width:
        #going right
        c += 1
        if row >= 0:
            for i in range(col + 1, col + c + 1):
                if i < width:
                    #print(row, i)
                    if ispoints_in_region(i, row, w, h, points) == False:
                        draw.text((i, row), word, 'red', font=font)
                        img.save(img.filename)
                        #print(len(get_ind_points(img, width, height, i, row, w, h)))
                        points.extend(get_ind_points(img, width, height, i, row, w, h))
                        return points
                    cnt += 1
        col = col + c
        #print("cnt1: " + str(cnt))
        if cnt >= height * width:
            break
        #going down
        r += 1
        if col < width:
            for i in range(row + 1, row + r + 1):
                if i < height:
                    #print(i, col)
                    if ispoints_in_region(col, i, w, h, points) == False:
                        draw.text((col, i), word, 'red', font=font)
                        img.save(img.filename)
                        #print(len(get_ind_points(img, width, height, col, i, w, h)))
                        points.extend(get_ind_points(img, width, height, col, i, w, h))
                        return points
                    cnt += 1
        row = row + r
        #print("cnt2: " + str(cnt))
        if cnt >= height * width:
            break
        #going left
        c += 1
        if row < height:
            for i in range(col - 1, col - c - 1, -1):
                if i >= 0:
                    #print(row, i)
                    if ispoints_in_region(i, row, w, h, points) == False:
                        draw.text((i, row), word, 'red', font=font)
                        img.save(img.filename)
                        #print(len(get_ind_points(img, width, height, i, row, w, h)))
                        points.extend(get_ind_points(img, width, height, i, row, w, h))
                        return points
                    cnt += 1
        col = col - c
        #print("cnt3: " + str(cnt))
        if cnt >= height * width:
            break
        #going up
        r += 1
        if col >= 0:
            for i in range(row - 1, row - r - 1, -1):
                if i >= 0:
                    #print(i, col)
                    if ispoints_in_region(col, i, w, h, points) == False:
                        draw.text((col, i), word, 'red', font=font)
                        img.save(img.filename)
                        #print(len(get_ind_points(img, width, height, col, i, w, h)))
                        points.extend(get_ind_points(img, width, height, col, i, w, h))
                        return points
                    cnt += 1
        row = row - r
        #print("cnt4: " + str(cnt))

    # draw.text(((width-w)/2,(height-h)/2), word, 'red', font=font)
    # img.save(img.filename)

# def points_in_region(x0, y0, w, h, points):
#     return len(contains(x0, y0, w, h, points))

def ispoints_in_region(x, y, w, h, points):
    for point in points:
        if point.x >= x and point.x <= x + w and point.y >= y and point.y <= y + h:
            return True
    return False

#wordList = [('মহান', 132), ('মা', 105), ('(স)', 105), ('আল্লাহ', 96), ('আল্লাহর', 76)]
#draw_text(wordList)