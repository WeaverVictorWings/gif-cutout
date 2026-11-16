"""Checks the export self-check: a good export raises no warning, a wrong frame count / size / delay is detected,
and an end-to-end export with a deliberately wrong encoder shows the warning. Usage: python3 tests/export_selfcheck.py CLIP.gif"""
import asyncio,sys,pathlib
from playwright.async_api import async_playwright
URL=pathlib.Path(__file__).resolve().parent.parent.joinpath('index.html').as_uri()+'?lang=zh-CN'
OBS="new MutationObserver(()=>{const t=document.getElementById('toast');if(t&&t.textContent)(window.__toasts=window.__toasts||[]).push(t.textContent)}).observe(document,{subtree:true,childList:true,characterData:true});"
async def main(clip):
    async with async_playwright() as p:
        b=await p.chromium.launch();ctx=await b.new_context(accept_downloads=True);pg=await ctx.new_page();errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.add_init_script(OBS);await pg.goto(URL);await pg.wait_for_function('window.__gifTool');await pg.set_input_files('#file',clip)
        await pg.wait_for_function('window.__gifTool.G&&!/sample/.test(document.getElementById("info").textContent)');await pg.wait_for_timeout(1500)
        r=await pg.evaluate("""async()=>{const T=__gifTool,list=T.exportList(),plan=T.makePlan();const good=await T.renderGIF(list,plan);
          return {good:good.note,frames:await T.verifyGif(good.blob,list.slice(1),plan),size:await T.verifyGif(good.blob,list,{...plan,W:plan.W+2}),delay:await T.verifyGif(good.blob,list.map(x=>({...x,ms:x.ms+500})),plan)}}""")
        ok=r['good']=='' and r['frames'] and r['size'] and r['delay'];print(r)
        await pg.evaluate("""async()=>{const T=__gifTool,list=T.exportList(),plan=T.makePlan();const short=await T.renderGIF(list.slice(2),plan);T.hook.enc=async()=>short.blob;}""")
        await pg.evaluate("window.__toasts=[]")
        async with pg.expect_download(timeout=60000) as dl: await pg.click('#goExport')
        await dl.value;await pg.wait_for_timeout(2500)
        w=[x for x in await pg.evaluate("window.__toasts") if '自检' in x];ok=ok and bool(w) and not errs
        print('end-to-end warning:',w,errs);await b.close();sys.exit(0 if ok else 1)
asyncio.run(main(sys.argv[1]))
