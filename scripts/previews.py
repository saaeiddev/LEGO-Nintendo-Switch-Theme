from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
r=Path(__file__).resolve().parents[1]
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
f=lambda n:ImageFont.truetype(font,n); b=lambda n:ImageFont.truetype(bold,n)
for target,title in [('home','HOME'),('lock','LOCK SCREEN'),('apps','GAME LIBRARY'),('user','USER PROFILE'),('set','SYSTEM SETTINGS')]:
    screen=Image.open(r/'artwork/backgrounds'/f'{target}.jpg').convert('RGBA'); d=ImageDraw.Draw(screen,'RGBA')
    d.rectangle((0,0,1280,77),fill=(0,8,25,100));d.text((45,22),'●  LEGO',font=b(25),fill='white');d.text((1110,22),'12:45  ▰',font=f(22),fill='white')
    if target=='home':
        for i in range(5):
            x=80+i*175;d.rounded_rectangle((x,250,x+150,400),radius=12,fill=(12+i*14,30+i*10,54+i*14,220),outline=(255,255,255,200),width=3);d.text((x+20,305),['PLAY','BUILD','EXPLORE','RACE','CREATE'][i],font=b(18),fill='white')
        d.text((85,435),'SELECT A GAME',font=b(20),fill='white')
    elif target=='lock':
        d.text((80,205),'12:45',font=b(74),fill='white');d.text((83,300),'Press a button to continue',font=f(28),fill='white')
    elif target=='apps':
        d.text((65,105),'All Software',font=b(32),fill='white')
        for i in range(8):
            x=70+(i%4)*170;y=185+(i//4)*170;d.rounded_rectangle((x,y,x+140,y+140),radius=10,fill=(25+i*10,47+i*4,70+i*5,220),outline=(255,255,255,180),width=2);d.text((x+20,y+60),'GAME',font=b(18),fill='white')
    elif target=='user':
        d.ellipse((60,120,155,215),fill=(245,191,0,255));d.text((180,140),'Player',font=b(37),fill='white')
        for i,word in enumerate(['Profile','Friend List','User Settings']):d.text((65,285+i*63),word,font=f(25),fill='white')
    else:
        d.text((60,110),'System Settings',font=b(34),fill='white')
        for i,word in enumerate(['Airplane Mode','Screen Brightness','Themes','System']):
            y=185+i*70;d.rounded_rectangle((55,y,525,y+55),radius=8,fill=(0,10,35,150));d.text((75,y+12),word,font=f(24),fill='white')
    d.text((45,670),'CONCEPTUAL MOCKUP  •  NOT A CONSOLE SCREENSHOT',font=b(13),fill=(255,255,255,205))
    canvas=Image.new('RGB',(1600,1000),(8,16,30));c=ImageDraw.Draw(canvas);c.rounded_rectangle((65,90,1535,900),50,fill=(17,20,26));c.rounded_rectangle((78,105,190,885),45,fill=(200,26,34));c.rounded_rectangle((1410,105,1522,885),45,fill=(15,91,155));canvas.paste(screen.convert('RGB'),(160,135));c.text((160,925),f'LEGO  /  {title}',font=b(24),fill=(240,244,255));c.text((1100,930),'CONCEPT PREVIEW',font=f(17),fill=(140,154,174));canvas.save(r/'previews'/f'{target}-concept.jpg',quality=90,subsampling=0)
