import wx
import _thread as thread
import time
import datetime
import databasemanager2

dbm = databasemanager2.Database_handler
nummerplaat = ""
naam = ""
startdatum = ""
einddatum = ""
currentDate = ""
pincode = 0000
locatie = "gratiekapel"
locaties = {"gratiekapel", "agora", "middelheim"}
x = 100
y = 50
now = datetime.datetime.now()
date = str(now.now())[0:7]
date += "-"
print(date)

def sleep(duration): # too lazy to type out time.sleep every time
    time.sleep(duration)
#end-sleep
class window1(wx.Frame):
        def __init__(self, *args, **kw): #runs automatically
            super(window1, self).__init__(parent=None, title='ANPR account manager', size=(720,480))
            panel = wx.Panel(self)
            
            #submit button
            submit = wx.Button(panel, label="voeg toe", pos=(5, 5*y))
            submit.Bind(wx.EVT_BUTTON, self.voegtoe)
            submit.SetBackgroundColour(wx.Colour(0,165,0))
            
            #delete button
            deleteinfo = wx.StaticText(panel, label="1 selecteer locatie, 2 geef nummerplaat of naam in, 3 druk op delete", pos=(x, 7*y))
            delete = wx.Button(panel, label="delete", pos=(5, 7*y))
            delete.Bind(wx.EVT_BUTTON, self.delete)
            delete.SetBackgroundColour(wx.Colour(255,0,0))
            
            #textfield plaat
            example = wx.StaticText(panel, label="1-123-ABC", pos=(2*x, 5))
            plate = wx.TextCtrl(panel, value="nummerplaat", pos=(5,5), size=(100,25))
            plate.Bind(wx.EVT_TEXT, self.plaatText)
            
            #texfield naam
            name = wx.TextCtrl(panel, value="naam", pos=(5, y), size=(100,25))
            name.Bind(wx.EVT_TEXT, self.naamtext)
            
            #textfield pincode
            example1 = wx.StaticText(panel, pos=(2*x, 2*y) ,label="XXXX, 0 op plaats 1 wordt niet weergegeven")
            codefield = wx.TextCtrl(panel, value="pincode", pos=(5, 2*y), size=(100,25))
            codefield.Bind(wx.EVT_TEXT, self.pincodenummer)
            
            #textfield startdatum
            label = wx.StaticText(panel, pos=(2*x, 4*y), label="yyyy-mm-dd")
            startdate = wx.TextCtrl(panel, value=str(date), pos=(5, 3*y), size=(100,25))
            startdate.Bind(wx.EVT_TEXT, self.startDatumtext)
            
            #textfield eindDatum
            label1 = wx.StaticText(panel, label='yyyy-mm-dd', pos=(2*x, 3*y))
            enddate = wx.TextCtrl(panel, value=str(date), pos=(5, 4*y), size=(100,25))
            enddate.Bind(wx.EVT_TEXT, self.eindDatumtext)
            
            #location selector
            option1 = wx.RadioButton(panel, name="gratiekapel" , label="gratiekapel", pos=(5*x, 5))
            option1.Bind(wx.EVT_RADIOBUTTON, self.locationselect)
            option2 = wx.RadioButton(panel, name="agora", label="agora", pos=(5*x, y))
            option2.Bind(wx.EVT_RADIOBUTTON, self.locationselect)
            option3 = wx.RadioButton(panel, name="middelheim" , label="middelheim", pos=(5*x, 2*y))
            option3.Bind(wx.EVT_RADIOBUTTON, self.locationselect)
            
            #wx.TextEntryDialog(None, "dawg").ShowModal()
        #end-Gui-build
        
        def plaatText(self, event):
            global nummerplaat
            nummerplaat = event.GetString()
        #end-plaatText
            
        def naamtext(self, event):
            global naam
            naam = event.GetString()
        #endnaam
        
        def startDatumtext(self, event):
            global startdatum
            startdatum = event.GetString()
        #end-startdatum
        
        def eindDatumtext(self, event):
            global einddatum
            einddatum = event.GetString()
        #end-eindDatumtext
        
        def pincodenummer(self, event):
            global pincode
            pincode = int(event.GetString())
        #end-pincode
        
        def locationselect(self, event):
            #find a way to extract a string somewhere
            global locatie
            option = event.GetEventObject()
            locatie = option.GetLabel()
            print(locatie)
        #def-locationselect
        
        def voegtoe(self, event):
            #def add_user(locatie, naam, nummerplaat, startdatum, einddatum, pincode):
            time.sleep(0.5)
            global nummerplaat
            global naam
            global startdatum
            global einddatum
            global pincode
            global locatie # selecteer de locatie van de gebruiker
            #global dbm
            try:
                dbm.add_user(locatie, naam, nummerplaat, startdatum, einddatum, pincode)
                wx.MessageBox("nummerplaat in de database gezet voor " + naam + " met als plaat " + nummerplaat)
            except:
                wx.MessageBox("error, hebt u alle gegevens ingegeven?")
        #end-voegtoe
        
        def delete(self, event): # remains untested
            global locatie
            global naam
            global nummerplaat
            dbm.remove_user(locatie, naam, nummerplaat)
        #end-delete
    
    
app = wx.App()
frame2 = window1(parent=None, title="ANPRmanager2")
frame2.Show()
app.MainLoop()
