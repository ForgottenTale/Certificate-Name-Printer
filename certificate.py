
import os 
import pandas as pd
from PIL import Image, ImageFont, ImageDraw

FONT_FILE = ImageFont.truetype(r'Poppins-Bold.ttf', 130)
FONT_COLOR = "#000000"
WIDTH, HEIGHT = 3508, 2480 """Specify the height and width of the certificate template"""

form = pd.read_excel("Enter the name of the excel sheet.xlsx")
name_list = form['Enter the name of the column'].to_list()


def make_cert(name):
    """function to generate certificate"""
    image_source = Image.open('Enter the name of the template.png')
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = draw.textsize(name, font=FONT_FILE)
    draw.text((WIDTH / 2 - name_width / 2, HEIGHT / 2 - name_height / 2 ), name, fill=FONT_COLOR, font=FONT_FILE)
    image_source.save("./out/"+str(name)+"/" + name +" 1"+ ".jpg")
    print('printing certificate of: ' + name)



for i in name_list:
   path = "./out/"
   os.chdir(path)
   newfolder = str(i)
   os.mkdir(i)
   os.chdir("../")
   make_cert(i)




