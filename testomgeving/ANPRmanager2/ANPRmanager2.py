import wx
import _thread as thread
import time
import datetime

nummerplaat = ""
naam = ""
startdatum = ""
einddatum = ""
currentDate = ""
pincode = 0000
x = 100
y = 50
def sleep(duration): # too lazy to type out time.sleep every time
    time.sleep(duration)
#end-sleep
class window1(wx.Frame):
        def __init__(self, *args, **kw): #runs automatically
            super(window1, self).__init__(parent=None, title='ANPR account manager', size=(720,480))
            panel = wx.Panel(self)
            
            #submit button
            submit = wx.Button(panel, label="voeg toe", pos=(2*x, 3*y))
            submit.Bind(wx.EVT_BUTTON, self.voegtoe)
            submit.SetBackgroundColour(wx.Colour(255,165,0))
            
            #input fields
            plate = wx.TextCtrl(panel, )
            

        def voegtoe(self, event):
            global nummerplaat
            global naam
            global startdatum
            global einddatum
            global pincode
            
            print("bruh")
        #end-button1
    
    
app = wx.App()
frame2 = window1(parent=None, title="ANPRmanager2")
frame2.Show()
app.MainLoop()
