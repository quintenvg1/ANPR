#!/ust/bin/python3
# program to run the guis
import wx
import database_handler
import time

global dbmanager #kinda want to access the controller from every function
dbmanager = database_handler.Databasecontroller #define the manager to be a database controller

loggedin = False
x = 25
y = 25

def printhello():
    print("hello")

class window1(wx.Frame): #
    def __init__(self, *args, **kw):
        super(window1, self).__init__(parent=None, title='ANPR main', size=(480,320)) #super is usefull to run the class anyway, and call the methods and variables from another program
        panel = wx.Panel(self)
        
        label1 = wx.StaticText(panel, pos=(7 * x, 1 * y), label="status")
        text1 = wx.TextCtrl(panel, pos=(12 *  x, 2 * y), value="text")
        text1.Bind(wx.EVT_TEXT, self.updateText)
        
        btn1 = wx.Button(panel,  pos=(7 * x, 2 * y ) ,label="emergency")
        btn1.Bind(wx.EVT_BUTTON, self.emergency)
        

        self.Show()
    def emergency(self, event):
        print("emergency active opening the gates")
    #end-emergency
    
    def updateText(self, event):
        text = event.GetString()
        print(text)
    #end-updateText
        
#end-window1

#variables die nodig zijn voor het programma en globaal accesable moeten zijn
name = ""
password = ""
plaat = ""
nieuweplaat = ""
nieuwpaswoord = ""
nieuwenaam = ""
class window2(wx.Frame): #anpr manager
    def __init__(self, *args, **kw): #runs automatically
        super(window2, self).__init__(parent=None, title='ANPR account manager', size=(480,320))
        panel = wx.Panel(self)
        
        #nametag
        text_ctrl1 = wx.TextCtrl(panel, pos=(5, 5), value="naam")
        text_ctrl1.Bind(wx.EVT_TEXT, self.nametext)
        
        #passwordtag
        text_ctrl2 = wx.TextCtrl(panel, pos=(5, 50), value="paswoord")
        text_ctrl2.Bind(wx.EVT_TEXT, self.passwordtext)
        
        #license plate tag
        text_ctrl3 = wx.TextCtrl(panel, pos=(5, 100), value="plaat")
        text_ctrl3.Bind(wx.EVT_TEXT, self.platetext)
        
        text_ctrl5 = wx.TextCtrl(panel, pos=(200, 5), size=(100, 35), value="nieuwe plaat")
        text_ctrl5.Bind(wx.EVT_TEXT, self.newplatetext)
        
        text_ctrl6 = wx.TextCtrl(panel, pos=(200, 50), size=(100, 35), value="nieuwe naam")
        text_ctrl6.Bind(wx.EVT_TEXT, self.nieuwenaamtext)
        
        text_ctrl7 = wx.TextCtrl(panel, pos=(200, 100), size=(100, 35),value="nieuwe paswoord")
        text_ctrl7.Bind(wx.EVT_TEXT, self.nieuwpaswoord)
        
        #
        text_ctrl4 = wx.TextCtrl(panel, pos=(5, 150), size=(250, 75), value="program log, currently not functional")
        
        st = wx.StaticText(panel, label="userid:", pos=(305, 215))
        uid = wx.StaticText(panel, label="1", pos=(350, 215))
        #loginbutton
        my_btn = wx.Button(panel, label='login', pos=(100, 5))
        my_btn.Bind(wx.EVT_BUTTON, self.login)
        my_btn1 = wx.Button(panel, label='update',size=(100, 35) ,pos=(305, 5))
        my_btn1.Bind(wx.EVT_BUTTON, self.update)
        my_btn1_1 = wx.Button(panel, label='new account', size=(100, 35) ,pos=(305, 50))
        my_btn1_1.Bind(wx.EVT_BUTTON, self.create_account)
        my_btn2 = wx.Button(panel, label="logout", pos=(100, 50))
        my_btn2.Bind(wx.EVT_BUTTON, self.logout)
        my_btn3 = wx.Button(panel, label="delete account", pos=(300,150))
        my_btn3.SetBackgroundColour(wx.Colour(240, 0, 0))
        my_btn3.Bind(wx.EVT_BUTTON, self.delete_account)
        help_button = wx.Button(panel, pos=(305, 100), size=(100, 35), label='help')
        help_button.SetBackgroundColour(wx.Colour(100,100,240))
        version_icon = wx.StaticText(panel, pos=(305, 180), label="version 0.0.1a")
        connection_status = wx.StaticText(panel, pos=(305, 200), label="connected")
        #show the window
        self.Show()
    
    #text handling
    def nametext(self, event):
        global name
        name = event.GetString()
        print(name)
    #end-nametext
    
    def nieuwenaamtext(self, event):
        global nieuwenaam
        nieuwenaam = event.GetString()
        print(nieuwenaam)
        
    #end-nieuwenaamtext
    def passwordtext(self, event):
        global password
        password = event.GetString()
        print(password)
    #end-passwordtext
    
    def nieuwpaswoord(self, event):
        global nieuwpaswoord
        nieuwpaswoord = event.GetString()
        print(nieuwpaswoord)
    
    def platetext(self, event):
        global plaat
        plaat = event.GetString()
        print(plaat)
    #end-platetext
    
    def newplatetext(self, event):
        global nieuweplaat
        nieuweplaat = event.GetString()
        print(nieuweplaat)
    #end-newplatetext
    
    def help(self, event):
        wx.MessageBox("Als u problemen onderindt met het programma of u zit vast contacteer dan uw systeembeheerder, als u uw wachtwoord of login bent vergeten, laat dit dan weten aan uw systeembeheerder")
    #end-help
        
    def login(self, event):
        user = ""
        global loggedin #because global...?
        global name
        global password
        print(name)
        print(password)
        #query the database on username and 
        print("attempting login")
        #loggedin = True
        time.sleep(1) #login delay, vertraag bruteforce attacks door telkens 1 seconde te wachten
        user = dbmanager.getuserfromcredentials(name, password)
        if(user != ""): #check if some user came back
            loggedin = True # the uses is logged in now
            wx.MessageBox("u bent ingelogd")
        else:
            wx.MessageBox("dit account werd niet gevonden, controlleer uw wachtwoord of maak een account.")
        print(user)
    #end-login
    
    def update(self, event):
        global loggedin #because global...?
        #query the database to update where username is correct
        #naam, paswoord, nieuwenaam ,nieuwpaswoord, nieuweplaat
        global name
        global password
        global plaat
        global nieuwenaam
        global nieuweplaat
        global nieuwpaswoord
        if(loggedin):
            dbmanager.updateuser(name, password, nieuwenaam, nieuwpaswoord, nieuweplaat)
            print("updated")
        else:
            wx.MessageBox("you have to login first")
    #end-update
    
    def logout(self, event):
        global loggedin
        wx.MessageBox("U bent nu uitgelogd.")
        loggedin = False
    #endlogout
    
    def delete_account(self, event):
        global name
        global password
        dbmanager.deleteuser(name, password)
        wx.MessageBox("uw account werd verwijderd de naam was" + "' "+name+"'")
    #end-delete_account
    
    def create_account(self, event): #not ready just yet
        global nieuwenaam
        global nieuwpaswoord
        global nieuweplaat
        dbmanager.createuser(nieuwenaam, nieuwpaswoord, nieuweplaat)
        wx.MessageBox("account werd aangemaakt noteer deze gegevens: naam " + "'"+ nieuwenaam +"' met paswoord "+" '"+nieuwpaswoord+"' " + "als u uw gegevens verliest kan u mogelijk geen aanpassingen meer maken")
    #end-create_account
#end-window2

if __name__ == '__main__':
    app = wx.App()
    frame = window1()
    frame2 = window2()
    app.MainLoop()
#end-if