#!/usr/bin/env python3
"""Create the NXThemes 3 ZIP-format HOME package from the project artwork."""
import json, zipfile, pathlib
from PIL import Image
root=pathlib.Path(__file__).resolve().parents[1]
img=root/'artwork/lego-home.jpg'
with Image.open(img) as im:
    assert im.size == (1280,720) and im.format == 'JPEG'
    assert not im.info.get('progressive'), 'progressive JPEG is unsupported'
manifest={'Version':17,'Target':'home','Author':'Amir Saeid Dehghan','ThemeName':'LEGO City — HOME (experimental)','Id':'legoHome01'}
out=root/'themes/LEGO-HOME-EXPERIMENTAL.nxtheme'
out.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
    z.writestr('info.json',json.dumps(manifest,ensure_ascii=False))
    z.write(img,'image.jpg')
with zipfile.ZipFile(out) as z:
    assert z.testzip() is None and set(z.namelist())=={'info.json','image.jpg'}
print(out)
