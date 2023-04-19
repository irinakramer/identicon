# identicon


This program asks for user to input their user name
and returns an image representing the hash of their user name.

This is achieved by a series of type conversions which result in a 2D array
with RGB values for each element.
The image is generated based on this array.

============

### Details:
User input string is converted into a hash string.
Part of this hash string is used as a hex color, then it is converted into a unique RGB color.
Another part of the hash string is converted to a binary string and is used to 
build a 2d array of 1s and 0s, where 1s represent the colored tiles, and 0s - white tiles.
The 2d array is then modified to achieve symmetry along the y-axis, and is expanded so tiles are bigger. 
The image is then generated using PIL.
The image is a square of 5x5 colored and white tiles.
After being generated the image is displayed on the screen and is saved to disk.

Packages used: PIL, NumPy, Hashlib
