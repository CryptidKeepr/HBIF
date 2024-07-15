from pathlib import Path
import cv2


"""Parameter used to scale down the size of input image to make it eaier to detect larger faces. Example: 1.1 reduces image 10%."""
scaleFactorValue = 1.1

"""Parameter used to specify the number of neighboring rectangles that need to be identified for detection."""
minNeighborsValue =  5

"""Parameter that sets the minimum size of the object being detected."""
minSizeValue = (200, 200)

"""Color of the bounding box."""
bbBoxColor = (0, 250, 0)

"""Thickness of the bounding box."""
bbThickness = 4

"""Variable to store the original image path."""
primaryDir = 'og_images/'

"""Parameter for default image height."""
defaultHeight = 3456

"""Paramter for default image width."""
defaultWidth = 5184

"""Parameter for resized image height."""
resizeHeight = 512

"""Parameter for resized image width."""
resizeWidth = 512

"""Variable to find filepath."""
filepath = Path('image_cropper.py').parent.absolute()

"""Directroy for original images."""
og_image_dir = str(filepath.joinpath(filepath) / 'images' / 'og_images')

"""Directroy for cropped images."""
temp_dir = str(filepath.joinpath(filepath) / 'images'/ 'temp')

"""Directory for finsihed images."""
resized_image_dir = str(filepath.joinpath(filepath) / 'images'/ 'resized_images')

"""Variable for logo image directory."""
logo = 'images/assets/huntingdon_logo.png'

"""Variable for logo icon image directory."""
icon_logo = str(filepath.joinpath(filepath) / 'images' / 'assets' / 'huntingdon_logo_2.png')

"""Variable for college grey color."""
hunt_grey = '#696b68'

"""Variable for college red color."""
hunt_red = '#e61433'

"""Variable for college white color."""
hunt_white = '#ffffff'

"""Variable for font."""
custom_font = 'Title Wave'
#
# """Variable for font location."""
# font_path = str(filepath.joinpath(filepath) / 'images '/ 'assets'/ stored_font)
#
# """Variable for custom font."""
# custom_font = FontProperties(fname=font_path)
