# Five Functions
# Jake Choi and Leo Zhi
# Nov 19, 2022
import cmpt120image as cmpt
import random as r


def recolorImage(img, color):
    # Determine if a pixel is white
    def isitwhite(pixel):
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]

        return r < 130 and g < 130 and b < 130

    #  Get dimensions of image
    height = len(img)
    width = len(img[0])

    # Make a copy of the original image
    coloredImage = cmpt.getBlackImage(width, height)

    # If pixel is not white, change its color
    for row in range(height):
        for column in range(width):
            if isitwhite(img[row][column]):
                coloredImage[row][column] = color

            else:
                coloredImage[row][column] = img[row][column]

    return coloredImage


def minify(img):
    wn = cmpt.getBlackImage(len(img), len(img[0]))

    # Returns a list of averages of R, G, or B values
    def averageRGB(img, rgb):
        avgRGB = []
        rowsOdd = []
        rowsEven = []
        valsOdd = []
        valsEven = []
        isEven = False

        # split image into odd/even rows
        for row in img:
            if isEven:
                rowsEven.append(row)
                isEven = False

            elif not isEven:
                rowsOdd.append(row)
                isEven = True

        # sum of consecutive rgb values, starting from last index in row
        for row in rowsOdd:
            for i in range(0, len(row), 2):
                sumTwoVal = row[i][rgb] + row[i + 1][rgb]
                valsOdd.append(sumTwoVal)

        for row in rowsEven:
            for i in range(0, len(row), 2):
                sumTwoVal = row[i][rgb] + row[i + 1][rgb]
                valsEven.append(sumTwoVal)

        # sum of rbg values based on index
        for i in range(len(valsOdd)):
            avgFourPix = (valsOdd[i] + valsEven[i]) / 4
            avgRGB.append(int(avgFourPix))

        return avgRGB

    # Return a list of values alternating RGB
    newImg = []
    for i in range(len(averageRGB(img, 0))):
        newImg.append([averageRGB(img, 0)[i], averageRGB(img, 1)[i], averageRGB(img, 2)[i]])

    # Group newImg into rows of 40 pixels
    newImg = [newImg[i:i + 40] for i in range(0, len(newImg), 40)]

    # delete first 2x2 while there still are more
    return newImg


def mirror(img):
    # Initialize the height and width
    height = len(img)
    width = len(img[0])

    # Make a copy of the original image
    mirroredImage = cmpt.getBlackImage(height, width)

    # mirror it
    for row in range(height):
        for column in range(width):
            # the new image is now mirrored by using negative sign
            mirroredImage[row][column] = img[row][-column]

    cmpt.showImage(mirroredImage)

    return mirroredImage


def drawItem(img, item, row, col):
    # save the original column value
    ogCol = col
    # construct tiny image inside
    for r in range(len(item)):
        for c in range(len(item[0])):
            img[row][col] = item[r][c]
            col += 1
        # Move to next row and reset column counter
        row += 1
        col = ogCol

    # Return canvas
    return img


def distributeItems(img, item, n):
    # Choose random row and column and draw items n times onto canvas
    for i in range(n):
        row = r.choice(range(len(img) - len(item)))
        col = r.choice(range(len(img[0]) - len(item[0])))
        distributed = drawItem(img, item, row, col)

    return distributed


# Defining Variables
canvas = cmpt.getWhiteImage(400, 300)
orange = cmpt.getImage('images/oranges.png')

# Calling Functions

# Call Recolored Image
# rec = recolorImage(orange, [100, 60, 0])
# cmpt.saveImage(rec, "res/orangeColored.png")

# Call Minified Image
# min = minify(orange)
# cmpt.saveImage(min, "res/orangeMinified.png")
# print(len(orange), 'x', len(orange[0]))
# print(len(min),'x', len(min[0]))

# Call Mirrored Image
# mir = mirror(orange)
# cmpt.saveImage(mir, "res/orangeMirrored.png")

# Call Draw Item
# draw = drawItem(canvas, orange, 100, 200)
# cmpt.saveImage(draw, "res/orangeDraw.png")

# Call Distribute Item
# dist = distributeItems(canvas, orange, 4)
# cmpt.saveImage(dist, "res/orangeDistributed.png")
