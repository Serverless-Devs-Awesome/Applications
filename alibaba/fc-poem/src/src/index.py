import json, base64
import urllib.request
from PIL import Image, ImageDraw, ImageFont


class Response:
    def __init__(self, start_response, response):
        self.start = start_response
        self.response = response

    def __iter__(self):
        status = '200'
        response_headers = [('Content-type', 'text/html')]
        self.start(status, response_headers)
        yield self.response.encode("utf-8")


def getPoem(content):
    if not content:
        content = "我爱阿里"
    url = "http://1813774388953700.cn-hangzhou.fc.aliyuncs.com/2016-08-15/proxy/experience-activities/auto_poem/"
    data = urllib.request.urlopen(
        urllib.request.Request(
            url=url,
            data=json.dumps({
                "type": "3",
                "content": content
            }).encode("utf-8")
        )
    ).read()

    try:
        return json.loads(data.decode("utf-8"))["message"]
    except:
        return data.decode("utf-8")


def getPage():
    with open("index.html") as f:
        data = f.read()
    return data


def getPicture(text):
    font = ImageFont.truetype('font.ttf', 40)
    temp_base_pic = Image.open("love.jpg").convert("RGBA")
    draw = ImageDraw.Draw(temp_base_pic)
    wordList = text.split("。")
    for eve in range(0, len(wordList)):
        draw.text((300, (eve + 1) * 50 + 200), wordList[eve], (79, 79, 79), font=font)
    temp_base_pic.save("/tmp/test_output.png")
    with open("/tmp/test_output.png", "rb") as f:
        base64Data = str(base64.b64encode(f.read()), encoding='utf-8')
    return 'data:image/png;base64,' + base64Data


def handler(environ, start_response):
    path = environ['PATH_INFO'].replace("/api", "")

    if path == "/":
        return Response(start_response, getPage())
    else:
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except (ValueError):
            request_body_size = 0
        tempBody = environ['wsgi.input'].read(request_body_size).decode("utf-8")
        requestBody = json.loads(tempBody)

        if path == "/poem":
            return Response(start_response, getPoem(requestBody.get("content", "我爱阿里")))
        elif path == "/picture":
            return Response(start_response, getPicture(requestBody.get("content", "我爱你")))
