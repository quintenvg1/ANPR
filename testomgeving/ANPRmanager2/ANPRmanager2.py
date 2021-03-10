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
            
            button1 = wx.Button(panel, label="bruh button")
            button1.Bind(wx.EVT_BUTTON, self.button1)
            
        def button1(self, event):
            print("bruh")
        #end-button1
    
    
app = wx.App()
frame2 = window1(parent=None, title="ANPRmanager2")
frame2.Show()
app.MainLoop()
