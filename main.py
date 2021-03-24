import PIL
from PIL import Image
from tkinter.filedialog import *
import warnings

warnings.filterwarnings('ignore')

file_path = askopenfilenames()
img = PIL.Image.open(file_path)
myHeight, myWidth = img.size

img = img.resize((myHeight, myWidth), PIL.Image.ANTIALIAS)
save_path = asksaveasfilename()

img.save(save_path+"compressed.JPG")
