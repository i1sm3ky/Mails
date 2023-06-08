import random
from PIL import Image, ImageDraw, ImageFont
import os
import time

def CreateProfilePicture(Name):
    if Name:
        try:
            Split = Name.split(' ')
            Initials = '{}{}'.format(Split[0][0], Split[1][0])
        except:
            Initials = Name[0]

        Color_List = [
            (153, 102, 255),
            (000, 102, 255),
            (255, 000, 000),
            (255, 153, 000),
        ]
        
        TempColorList = Color_List
        
        BackgroundColor = random.choice(TempColorList)
        TempColorList.remove(BackgroundColor)
        TextColor = random.choice(TempColorList)
        BackgroundImage = Image.new('RGB', (288, 288), color=BackgroundColor)
        Font_Type = ImageFont.truetype(font='Segoe UI Bold.ttf', size=150)
        Draw = ImageDraw.Draw(BackgroundImage)
        Width, Height = Draw.textsize(Initials.upper(), Font_Type)
        Draw.text(((288 - Width)/2, 50), text=Initials.upper(),
                  fill=TextColor, font=Font_Type)

        BackgroundImage.save("Config/TempProfilePicture.png", "PNG")
        
        with open("Config/TempProfilePicture.png", "rb") as File:
            Data = File.read()
        os.remove("Config/TempProfilePicture.png")
        return Data
