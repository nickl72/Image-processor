from tkinter import *
from tkinter import filedialog
from ascii_image_converter import convert2ascii

scale = int(input('<p style="display: none">Scale down image by:</p>\n'))
contrast = int(input('<p style="display: none">Increase contrast by (integers only):</p>\n'))

# sets up tkinter window
root = Tk()
# loads file from gui
root.filename = filedialog.askopenfilename()

# runs conversion
convert2ascii(root.filename, scale, contrast, True)
# print(root.filename)
