from PIL import Image
from numpy import asarray
from ascii_map import ascii_arr

def convert2ascii(path, scale = 1, contrast = 1, html = False):
    image = Image.open(path).convert('L') # Converts image to greyscale
    width = int(image.size[0]/scale) 
    height = int(image.size[1]/scale)
    data = asarray(image.resize((width,height))).copy() # scales image
    image.resize((width, height)).show()
    
    # Outputs html templating if called out
    if html:
        print('''
            <style> p {font-size: 8px; font-family: monospace; zoom:25%;}</style>
            <p>
        ''')

    # prints appropriate ascii char for each pixel
    for band in data:
        for pix in band:
            print(ascii_arr[int(pix/8/contrast)*2*contrast], end='')
        if html:
            print('</br>', end='')
        else: 
            print('\n', end='')
    
    if html:
        print('</p></body></html>')

