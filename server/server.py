from sanic import Sanic, Request, Websocket
from sanic.response import text, json

app = Sanic("MyHelloWorldApp")


@app.get("/")
async def hello_world(request: Request, ws: Websocket):
    return text("Hello, world.")


@app.websocket("/feed")
async def feed(request: Request, ws: Websocket):
    async for msg in ws:
        await ws.send(msg)


if __name__ == "__main__":
    app.run(port=3000)


# #!/usr/bin/env python
# from pywhisper import main as whisper
# from gpt import translate as gpt
# import sys

# model = "small"
# args = sys.argv[1:]
# func = args[0]
# url = args[1]

# print('Func:', str(func), " Lang: ", str(url))

# if func == "transcribe":
#     link = url
#     result = whisper(link, model)
#     print(result)
