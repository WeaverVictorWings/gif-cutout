"""Smoke test: open every animation in the given folders, check nothing throws and the cutout is not empty.
Usage: python3 tests/smoke.py CLIPS_DIR [CLIPS_DIR ...]   (needs: pip install playwright pillow numpy; playwright install chromium)"""
import asyncio,glob,os,re,sys,pathlib,io,base64
import numpy as np
from PIL import Image
from playwright.async_api import async_playwright
URL=pathlib.Path(__file__).resolve().parent.parent.joinpath('index.html').as_uri()
EXT=('.gif','.png','.webp','.apng','.jpg','.jpeg')
async def setc(pg,id,v):
    await pg.evaluate("([id,v])=>{const e=document.getElementById(id);if(e.type==='checkbox')e.checked=v;else e.value=v;e.dispatchEvent(new Event('input',{bubbles:true}));e.dispatchEvent(new Event('change',{bubbles:true}))}",[id,v])
async def main(dirs):
    files=sorted(f for d in dirs for f in glob.glob(os.path.join(d,'*')) if f.lower().endswith(EXT))
    bad=0;rej=[]
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for f in files:
            pg=await (await b.new_context(viewport={'width':1280,'height':900})).new_page();errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
            try:
                await pg.goto(URL);await pg.wait_for_function('window.__gifTool');await pg.set_input_files('#file',f)
                try:
                    await pg.wait_for_function('window.__gifTool.G&&window.__gifTool.G.frames.length>0&&!/sample/.test(document.getElementById("info").textContent)',timeout=8000)
                except Exception:
                    toast=await pg.evaluate('(document.getElementById("toast")||{}).textContent||""')
                    if not errs and re.search('Unrecognised|无法识别|不是|Unsupported',toast):
                        print('REJ',os.path.basename(f),'(rejected with a message, no crash):',toast[:60]);rej.append(f);await pg.context.close();continue
                    raise
                n=await pg.evaluate('__gifTool.G.frames.length');res=[]
                for solid,main_ in ((False,False),(True,True)):
                    await setc(pg,'solid',solid);await setc(pg,'mainOnly',main_)
                    r=await pg.evaluate("(i)=>{const pr=__gifTool.getProcessed(i);let a=0;const d=pr.data;for(let k=3;k<d.length;k+=4)if(d[k]>128)a++;return a/(d.length/4)}",n//2)
                    res.append(round(r,3))
                tiny=await pg.evaluate('__gifTool.G.W*__gifTool.G.H<=16');ok=not errs and (res[0]>0 or tiny)
                print('OK ' if ok else 'BAD',os.path.basename(f),n,'frames opaque',res,errs[:1]);bad+=0 if ok else 1
            except Exception as e:
                print('BAD',os.path.basename(f),repr(e)[:120]);bad+=1
            await pg.context.close()
        await b.close()
    print(len(files),'files,',bad,'bad,',len(rej),'rejected (check these are really invalid files):',[os.path.basename(x) for x in rej]);sys.exit(1 if bad else 0)
asyncio.run(main(sys.argv[1:] or ['.']))
