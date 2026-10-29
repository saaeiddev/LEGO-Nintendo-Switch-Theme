#!/usr/bin/env python3
"""Build the official ZIP NXTheme format from generated artwork using NxThemeTool."""
from pathlib import Path
from PIL import Image
import json, os, subprocess, tempfile, shutil, zipfile, hashlib
root=Path(__file__).resolve().parents[1]
tool=os.environ.get('NXTHEME_TOOL')
if not tool: raise SystemExit('Set NXTHEME_TOOL to the NxThemeTool executable, or set DOTNET and NXTHEME_TOOL to the DLL.')
command=([os.environ['DOTNET'],tool] if os.environ.get('DOTNET') else [tool])
parts={'home':'home','lock':'lock','apps':'apps','user':'user','set':'settings','news':'apps','psl':'user'}
labels={'home':'Home','lock':'Lock','apps':'Games','user':'Profile','set':'Settings','news':'News','psl':'Player-Select'}
for d in ['artwork/backgrounds','themes','dist']: (root/d).mkdir(parents=True,exist_ok=True)
for target,source in parts.items():
    image=Image.open(root/'artwork/originals'/f'{source}.png').convert('RGB').resize((1280,720),Image.Resampling.LANCZOS)
    jpg=root/'artwork/backgrounds'/f'{target}.jpg'; image.save(jpg,quality=92,progressive=False,subsampling=0)
    with tempfile.TemporaryDirectory() as td:
        t=Path(td); shutil.copyfile(jpg,t/'image.jpg')
        (t/'info.json').write_text(json.dumps({'Version':17,'Target':target,'Author':'Amir Saeid Dehghan','ThemeName':f'LEGO — {labels[target]}','Id':f'lego2026{target}'},ensure_ascii=False),encoding='utf-8')
        out=root/'themes'/f'LEGO-{labels[target]}.nxtheme'
        for cmd in [['pack',str(t),str(out)],['validate',str(out)]]:
            r=subprocess.run(command+cmd,text=True,capture_output=True,check=True)
            print(target,*cmd[:1],r.stdout.strip())
            if 'Error:' in r.stdout or 'Errors:' in r.stdout or 'warning' in r.stdout.lower() and 'no warnings' not in r.stdout.lower(): raise SystemExit('Tool reported a validation issue')
        with zipfile.ZipFile(out) as z:
            assert not z.testzip() and set(z.namelist())=={'info.json','image.jpg'}
            assert json.loads(z.read('info.json'))['Target']==target
with zipfile.ZipFile(root/'dist/LEGO-Nintendo-Switch-Theme.zip','w',zipfile.ZIP_DEFLATED) as z:
    for target in parts: z.write(root/'themes'/f'LEGO-{labels[target]}.nxtheme',f'LEGO-{labels[target]}.nxtheme')
    z.write(root/'INSTALL.txt','INSTALL.txt')
with (root/'dist/SHA256SUMS.txt').open('w') as f:
    for p in sorted((root/'themes').glob('LEGO-*.nxtheme')):
        if 'EXPERIMENTAL' not in p.name: f.write(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n')
    p=root/'dist/LEGO-Nintendo-Switch-Theme.zip'; f.write(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n')
