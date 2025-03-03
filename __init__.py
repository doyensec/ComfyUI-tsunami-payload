from aiohttp import web
from server import PromptServer
import pathlib
import shutil
import os

@PromptServer.instance.routes.get("/tsunami_vulnerability_check")
async def check(request):
    str1 = request.rel_url.query.get("str1", "")
    str2 = request.rel_url.query.get("str2", "")
    str3 = request.rel_url.query.get("str3", "")
    if not str1 or not str2 or not str3:
        return web.Response(text="Missing parameters")
    output = str1 + str2[::-1] + str3
    return web.Response(text=output)

@PromptServer.instance.routes.get("/tsunami_vulnerability_check_remove")
async def remove(request):
    if request.rel_url.query.get("delete", "") != "1":
        return web.Response(text="If you are sure you want to delete this plugin, provide delete=1")
    
    # Find script's parent folder
    if not __file__:
        return web.Response(text="Could not detect script path")
    path = pathlib.Path(__file__).parent.resolve()
    if not path:
        return web.Response(text="Could not detect script path")
    path = str(path)
    
    # Ensure path points to the plugin folder, just in case
    if (os.path.basename(path) != "ComfyUI-tsunami-payload"):
        return web.Response(text="Could not ensure path points to the plugin folder")
    
    shutil.rmtree(path)
    return web.Response(text="Deleted.")