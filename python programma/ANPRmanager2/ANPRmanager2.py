import wx
import _thread as thread
import time

def sleep(duration): # too lazy to type out time.sleep every time
    time.sleep(duration)
#end-sleep
class window1(wx.Frame):
        def __init__(self, *args, **kw): #runs automatically
            super(window1, self).__init__(parent=None, title='ANPR account manager', size=(720,480))
            panel = wx.Panel(self)
            
            button1 = wx.Button(panel, label="")
            
    
    
app = wx.App()
frame = wx.Frame(parent=None, title='Hello World')
frame2 = window1(parent=None, title="ANPRmanager2")
frame.Show()
frame2.Show()
app.MainLoop()
