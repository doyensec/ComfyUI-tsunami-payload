from aiohttp import web
from server import PromptServer

@PromptServer.instance.routes.get("/tsunami_vulnerability_check")
async def run_poc(request):
    str1 = request.rel_url.query["str1"]
    str2 = request.rel_url.query["str2"]
    str3 = request.rel_url.query["str3"]
    output = str1 + str2[::-1] + str3
    return web.Response(text=output)