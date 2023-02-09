from PIL import Image,ImageFont,ImageDraw
img_file =open('guests.txt')
names=img_file.readlines()
for i in names:
    inv=i[-1]
    img=Image.new('RGBA',(288,360),'white')
    image=Image.open('flowerr.png')
    image=image.resize((288,360))
    img.paste(image,(0,0))

    draw=ImageDraw.Draw(img)
    draw.text((8,250),'It would be  a pleasure to have the company of',fill='blue')
    draw.text((130,270),inv,fill='blue')
    draw.text((39,290),'at 11010 Memory Lane on April 1st',fill='blue')
    draw.rectangle((2,2,285,355),outline='yellow')
    img.save(f'{inv}invitation.png')
