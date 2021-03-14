import tkinter

root = tkinter.Tk()

# 透明度
root.wm_attributes("-alpha", 1)

# 设置为工具窗口，没有最大最小按钮
root.wm_attributes("-toolwindow", True)

# 永远置于顶层
root.wm_attributes("-topmost", True)

# 去除边框窗口，取出后无法鼠标拖动，需要自己监听鼠标事件
root.overrideredirect(True)

root.mainloop()
