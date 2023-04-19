import hashlib
import numpy as np
from PIL import Image, ImageColor

## IDENTICON PROGRAM ##
# This program asks for user to input their user name
# and returns an image representing the hash of their user name.
# This is achieved by a series of type conversions which result in a 2D array
# with RGB values for each element.
# The image is generated based on this array.


# FUNCTONS
# Prepare user input
def prep(str):
    return str.lower().replace(" ", "")[:20]


# Convert first 6 chars of hash to RGB tuple
def to_rgb(hash):
    return ImageColor.getcolor('#' + hash[:6], "RGB")


# Convert hash to binary and return 15 chars from it
def to_binlist15(hash):
    bstr = format(int(hash[6:], 16), '0>42b')

    return list(bstr[:15])


# Convert to list of ints
def to_intlist(blist):
    return [int(x) for x in blist]
    

# Build 2D array
def to_matrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]


# Make list simmetrical by adding elements to right side
def to_mirror(lst):
    mir = lst
    
    for i in range(len(lst)):
        mir[i].append(lst[i][1])
        mir[i].append(lst[i][0])

    return mir

    
# Repeat array values to simulate larger tiles
def expand(lst, n):
    expanded = np.array(lst)
    expanded = np.repeat(lst, n, axis=1)
    expanded = np.repeat(expanded, n, axis=0)

    return expanded.tolist()


# Build pixels array with RGB color for '1' and RBG white for '0'
def to_pixelsarr(lst):
    colors = lst
    
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == 1:
                colors[i][j] = rgb_color
            else:
                colors[i][j] = white_color
                
    # Convert the pixels into an array using numpy
    array = np.array(colors, dtype=np.uint8)
    
    return array


# Use PIL to create an image from the new array of pixels and save it
def generate_img(arr):
    img = Image.fromarray(arr)
    img.show()
    img.save(user_input + ".png")


def generate_rgb_array(hash):
    # Convert hash to binary with 15chars
    blist = to_binlist15(hash)
  
    # convert to list of ints
    ilist = to_intlist(blist)

    # create 2D list: (3 x 5) = 15 total pixels
    ilist2d = to_matrix(ilist, 3)
    
    # Add a mirror part to each row (3 + 2), so the end result array is (5 x5)
    mlist = to_mirror(ilist2d)

    # Expand list for larger tiles to accomodate 20 pixels each
    explist = expand(mlist, 20)

    # Build pixels array
    array = to_pixelsarr(explist)

    return array


def show_message():
    img_name = user_input + ".png"
    print("Your identicon icon was generated and saved as", img_name)

    
def generate_identicon(hash):
    arr = generate_rgb_array(hash)
    generate_img(arr)
    show_message()


    
## PROGRAM
print("Hello, welcome to identicon generator!")

user_input = prep(input("Enter your username: "))
hash_object = hashlib.sha1(user_input.encode('utf-8')).hexdigest()
rgb_color = to_rgb(hash_object)
white_color = (255, 255, 255)

generate_identicon(hash_object)

