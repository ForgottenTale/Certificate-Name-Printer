""" # Python code to generate certificates from a list of names
    # Author : ijas <ijas.dev>
    # Date : 23 June 2020
"""
# import os 
import pandas as pd
from PIL import Image, ImageFont, ImageDraw

FONT_FILE = ImageFont.truetype(r'Poppins-Bold.ttf', 130)
FONT_COLOR = "#000000"
WIDTH, HEIGHT = 3508, 2480

form = pd.read_excel("Certificate Names list.xlsx")
name_list = form['Quiz'].to_list()


def make_cert(name):
    """function to generate certificate"""
    image_source = Image.open('Treasure Hunt Certificate.png')
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = draw.textsize(name, font=FONT_FILE)
    draw.text((WIDTH / 2 - name_width / 2, HEIGHT / 2 - name_height / 2 + 20), name, fill=FONT_COLOR, font=FONT_FILE)
    image_source.save("./out/"+str(name)+"/" + name +" 1"+ ".jpg")
    print('printing certificate of: ' + name)



for i in name_list:
#    path = "./out/"
#    os.chdir(path)
#    newfolder = str(i)
#    os.mkdir(newfolder)
#    os.chdir("../")
   make_cert("Albin Kuruvilla")



# Content Wrting Certificate
# Quiz Certificate
# Resume Building Certificate
# Treasure Hunt Certificate

# Treasure Hunt	
# Content	
# Resume	
# Quiz
