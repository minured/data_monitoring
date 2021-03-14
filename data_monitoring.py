from DragWindow import DragWindow
import tkinter as tk
import requests

url = "https://xmtwx.crm.189.cn/WX_CUST_WEBSERVICE/wapSelf/wapSelfAction.do?action=packageUseChange_channel&values=O7of008yBL6pJ5oYN5Jnu15CW/YvKHhXV0tbrSUGZPZA_a6Vi6U60thmA_aA_aBA_aUzDKQNFxBruA_aAdLYCzgRppWsd/cFQBv9arxeqn0jgo7hSW5MXP3eYJYHA_awK/rCTAdoBe0ETb6XkM2NSPw="
count = 1
timer_interval = 1

# timer刷新 但是退出有问题
# def delay_run():
#     global count
#     while True:
#         DX_text.set(str(count))
#         time.sleep(1)
#         count += 1
#
# t = Timer(timer_interval, delay_run)
# t.start()

FPS = 120000


def test():
    global count
    root.update()
    DX_text.set(str(count))
    count += 1
    root.after(FPS, test)


def get_data():
    root.update()
    try:
        res = requests.get(url).json()
    except:
        DX_text.set("获取流量失败")
        return

    # 字典使用get，key不存在会返回None，不发生keyerror
    DX_used = res['detail_data'][2].get('used')

    # 每天0点的时候，通用流量一开始不存在
    try:
        TY_rest = res['detail_data'][3].get('balace')
    except:
        TY_rest = "0"
    DX_text.set(DX_used)
    TY_text.set(TY_rest)
    root.after(FPS, get_data)


root = DragWindow()
root.set_window_size(90, 45)
root.set_display_postion(500, 400)

bg = "white"

DX_text = tk.StringVar()
TY_text = tk.StringVar()
DX_text.set("查询中")

DX_label = tk.Label(root, textvariable=DX_text, bg=bg).pack(anchor="center")
TY_label = tk.Label(root, textvariable=TY_text, bg=bg).pack(anchor="center")

# TODO 背景透明度 与 字体透明度 分开设置

# TODO 以后要做成异步的，否则要求请之后才显示

# 右键与菜单
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Dva爱你")
menu.add_separator()
menu.add_command(label="退出", command=root.quit)


def on_right_click(event):
    menu.post(event.x_root, event.y_root)


root.bind('<ButtonPress-3>', on_right_click)
root.after(0, get_data)
root.mainloop()

# async def get_data():
#     async with aiohttp.request("GET", url) as r:
#         response = await r.text()
#         print(response)
#
# tasks = [get_data()]
#
# event_loop = asyncio.get_event_loop()
# results = event_loop.run_until_complete(asyncio.gather(*tasks))
# event_loop.close()
