from core import Handler, Request, Response, BytesIOToBytes, BytesToBuildImage
from core.lib.type import User
from .functions import *
from .download import download_avatar

package = "petpet"


class Info:
    def __init__(self, user: User, request: Request):
        self.qq = user.qq
        self.group = request.event.group.qq
        self.name = user.name
        self.gender = "unknown"

    async def init(self):
        self.img = BytesToBuildImage(await download_avatar(self.qq)).resize((640, 640)).convert("RGBA")
        return self


async def _get_one_image(request: Request):
    if request.event.quote.imageList:
        bytes_img = request.event.quote.imageList[0]
    elif request.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    return bytes_img


async def _get_two_image(request: Request):
    sender_img = BytesToBuildImage(await download_avatar(request.event.sender.qq))
    if len(request.event.imageList) >= 2:
        img_list = [
            BytesToBuildImage(request.event.imageList[0]),
            BytesToBuildImage(request.event.imageList[1])
        ]
    else:
        if request.event.imageList:
            img_list = [BytesToBuildImage(request.event.imageList[0])]
        elif request.event.atList:
            img_list = [BytesToBuildImage(await download_avatar(request.event.atList[0].qq))]
        else:
            img_list = [sender_img]
    return img_list, sender_img


@Handler.FrameToFrame
async def _universal(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = universal(BytesToBuildImage(bytes_img), [request.message])
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _petpet(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    arg = "圆" if "圆" in request.event.msg else "方"
    image = petpet(BytesToBuildImage(bytes_img), arg)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _kiss(request: Request) -> Response:
    img_list, sender_img = await _get_two_image(request)
    image = kiss(img_list, sender_img)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _rub(request: Request) -> Response:
    img_list, sender_img = await _get_two_image(request)
    image = rub(img_list, sender_img)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _play(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = play(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _pat(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = pat(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _rip(request: Request) -> Response:
    img_list = [BytesToBuildImage(await download_avatar(request.event.sender.qq))]

    if request.event.quote.imageList:
        img_list.append(request.event.quote.imageList[0])
    elif request.event.atList:
        img_list.append(await download_avatar(request.event.atList[0].qq))
    elif request.imageList:
        img_list.append(request.event.imageList[0])
    else:
        pass

    image = rip(img_list)

    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _throw(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = throw(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _crawl(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = crawl(BytesToBuildImage(bytes_img), request.event.msg.replace("爬", ""))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _support(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = support(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _always(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = always(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _loading(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = loading(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _turn(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = turn(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _littleangel(request: Request) -> Response:
    if request.event.atList:
        user = request.event.atList[0]
    else:
        user = request.event.sender

    image = littleangel(await Info(user, request).init(), request.message)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _dont_touch(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = dont_touch(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _alike(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = alike(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _roll(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = roll(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _play_game(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = play_game(BytesToBuildImage(bytes_img), request.message)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _worship(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = worship(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _eat(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = eat(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _bite(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = bite(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _police(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = police(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _police1(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = police1(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _ask(request: Request) -> Response:
    if request.event.atList:
        user = request.event.atList[0]
    else:
        user = request.event.sender

    image = ask(await Info(user, request).init(), request.message)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _prpr(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = prpr(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _twist(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = twist(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _wallpaper(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = wallpaper(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _china_flag(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = china_flag(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _make_friend(request: Request) -> Response:
    if request.event.atList:
        user = request.event.atList[0]
    else:
        user = request.event.sender

    image = make_friend(await Info(user, request).init(), request.message)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _back_to_work(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = back_to_work(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _perfect(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = perfect(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _follow(request: Request) -> Response:
    if request.event.atList:
        user = request.event.atList[0]
    else:
        user = request.event.sender

    image = follow(await Info(user, request).init(), request.message)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _my_friend(request: Request) -> Response:
    user = request.event.atList[0]

    image = my_friend(
        await Info(user, request).init(),
        await Info(request.event.sender, request).init(),
        "",
        request.message.split(" ")
    )
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _paint(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = paint(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _coupon(request: Request) -> Response:
    if request.event.atList:
        user = request.event.atList[0]
    else:
        user = request.event.sender

    image = coupon(await Info(user, request).init(), request.message)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _listen_music(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = listen_music(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _funny_mirror(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = funny_mirror(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _love_you(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = love_you(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _symmetric(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = symmetric(BytesToBuildImage(bytes_img), request.event.msg.replace("对称", ""))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _safe_sense(request: Request) -> Response:
    if request.event.atList:
        user = request.event.atList[0]
    else:
        user = request.event.sender

    image = safe_sense(await Info(user, request).init(), request.message)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _always_like(request: Request) -> Response:
    if request.event.atList:
        users = []
        for i in request.event.atList:
            users.append(await Info(i, request).init())
    else:
        users = [await Info(request.event.sender, request).init()]

    image = always_like(users, request.message)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _interview(request: Request) -> Response:
    sender_img = BytesToBuildImage(await download_avatar(request.event.sender.qq))

    if len(request.event.imageList) >= 2:
        img_list = [
            BytesToBuildImage(request.event.imageList[0]),
            BytesToBuildImage(request.event.imageList[1])
        ]
    else:
        if request.event.imageList:
            img_list = [BytesToBuildImage(request.event.imageList[0])]
        elif request.event.atList:
            img_list = [BytesToBuildImage(await download_avatar(request.event.atList[0].qq))]
        else:
            img_list = [sender_img]

    image = interview(img_list, request.message)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _punch(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = punch(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _cyan(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = cyan(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _pound(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = pound(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _thump(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = thump(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _need(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = need(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _cover_face(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = cover_face(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _cover_face(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = cover_face(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _knock(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = knock(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _knock(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = knock(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _garbage(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = garbage(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _whyatme(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = whyatme(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _decent_kiss(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = decent_kiss(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _jiujiu(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = jiujiu(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _suck(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = suck(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _hammer(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = hammer(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _tightly(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = tightly(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _distracted(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = distracted(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _anyasuki(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = anyasuki(BytesToBuildImage(bytes_img), request.message)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _thinkwhat(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = thinkwhat(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _keepaway(request: Request) -> Response:
    imageList = []
    for i in request.event.imageList:
        imageList.append(BytesToBuildImage(i))
    for i in request.event.atList:
        imageList.append(BytesToBuildImage(await download_avatar(i.qq)))

    if not imageList:
        imageList.append(BytesToBuildImage(await download_avatar(request.event.sender.qq)))

    image = keepaway(imageList, request.message)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _marriage(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = marriage(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _painter(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = painter(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _repeat(request: Request) -> Response:
    if request.event.atList:
        users = []
        for i in request.event.atList:
            users.append(await Info(i, request).init())
    else:
        users = [await Info(request.event.sender, request).init()]

    image = repeat(users, await Info(request.event.sender, request).init(), request.message)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _anti_kidnap(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = anti_kidnap(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _charpic(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = charpic(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _mywife(request: Request) -> Response:
    if request.event.atList:
        user = request.event.atList[0]
    else:
        user = request.event.sender

    image = mywife(await Info(user, request).init(), "", "")
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _walnutpad(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = walnutpad(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _teach(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = teach(BytesToBuildImage(bytes_img), request.message)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _addition(request: Request) -> Response:
    bytes_img = await _get_one_image(request)
    image = addition(BytesToBuildImage(bytes_img), request.message)
    return Response(image=BytesIOToBytes(image))
